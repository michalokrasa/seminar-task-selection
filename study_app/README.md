# Study App

A step-by-step wizard for running the NL-vs-Gherkin prompt-writing study. Tracks
per-participant progress and timing, enforces sequential completion of steps,
and counterbalances task/modality assignment across participants.

## Study flow

The consent form, baseline questionnaire, and post-study survey are **no
longer part of the app** — they're sent directly to participants via email
(see `emails/study-invitation.md` and `emails/post-study.md`). Only the
task-writing portion of the study happens in-app:

1. **Onboarding**
   1. Welcome screen (custom step; overview of the remaining steps, full-screen + autosave notes)
   2. Gherkin introduction (custom step)
   3. Prompt-writing guidelines + examples (custom step)
   4. "Ready to start" info screen (next step is Task 1; contact email for questions)
2. **Study**
   1. Task 1A — prompt-writing (custom step, NL or Gherkin per assignment)
   2. Task 1B — prompt-writing (custom step, the other modality for the same task)
   3. Task 2A — prompt-writing (custom step, NL or Gherkin per assignment)
   4. Task 2B — prompt-writing (custom step, the other modality for the same task)
3. **Confirmation**
   1. Recap screen confirming all four specifications were submitted, with the option to
      go back and edit any answer, or click "Finish" to end the study

Participants can move **back and forth** between any previously-reached
step (via the "← Back" / "Next →" nav in `Wizard.jsx`) to review or update
their answers before finishing — completion of a step is never required to
revisit it, only to move past the current frontier step.

Each participant accesses the app via a link containing their ID as a path
segment: `https://<site>/p001`. All state is keyed by this `pid`. If a
participant visits the site with no ID in the URL, they're shown a prompt to
enter it (which then updates the URL via `pushState`, so subsequent reloads
resume from the path). The old `?pid=p001` query-string form is still
accepted as a fallback.

Once a participant's `pid` is resolved, `Wizard.jsx` also mirrors the
currently viewed step into the path as `/<pid>/<step-id>` (e.g.
`/p001/task:1:...`, or `/p001/done` once finished) via `replaceState`. This
is purely a display convenience for bookmarking/sharing/debugging — the
actual progress is always re-derived from `/api/progress` on load, never
read back out of the URL.

### Autosave

While writing a prompt in a task step, the draft is autosaved every 30
seconds (in addition to the manual "Save draft" button and on submit), so
no input is lost if the participant closes the tab or their connection
drops. Autosaved drafts update the same `draft` row for that
participant/step in the `progress` sheet in place (via
`upsertDraftRow` in `netlify/functions/utils/sheets.mjs`) rather than
appending a new row every 30s.

## Architecture

```
Browser (Vite + React SPA)
  ├─ GET  /api/assignment?pid=X   → Netlify Function → reads "assignments" sheet
  ├─ GET  /api/progress?pid=X     → Netlify Function → reads "progress" sheet
  └─ POST /api/step-complete      → Netlify Function → appends/updates row in "progress" sheet
```

- **Frontend**: Vite + React, single-page wizard (no routing library — one
  component renders whichever step is "current" for the participant).
- **Backend**: Netlify Functions (Node, `netlify/functions/*.mjs`) — thin,
  stateless handlers, no persistent server.
- **Datastore**: a single Google Sheet, accessed via the Sheets API with a
  service-account credential. Chosen over a dedicated DB because the
  embedded Google Forms already write natively to Sheets — this keeps all
  study data (forms + custom steps) in one place for analysis.
- **Hosting**: Netlify free tier (static site + functions), zero cost at
  this study's scale.

### Why this stack (see prior design discussion)

- Google Forms alone can't enforce sequential gating or per-participant
  counterbalanced ordering — hence a thin custom app owns flow control for
  the task-writing portion, while consent/baseline/post-study Forms are
  sent directly via email since they don't need any of that gating logic.
- Netlify Functions + Sheets API avoids running/maintaining a database for a
  small-N pilot study.

## Data model (Google Sheet tabs)

| Tab                | Columns                                                                                                                                                                                 | Written by                                                                                                                                  |
| ------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| `assignments`      | `participant_id, task_1_slug, task_1_first_modality, task_1_second_modality, task_2_slug, task_2_first_modality, task_2_second_modality, condition_group, task_1_bucket, task_2_bucket` | Uploaded once, offline, from `scripts/generate_assignments.py` output                                                                       |
| `progress`         | `participant_id, step_id, status, timestamp, payload`                                                                                                                                   | Written live by `/api/step-complete` (`status` ∈ `started` / `draft` / `completed`); `draft` rows are updated in place, others are appended |
| (native form tabs) | Whatever each Google Form auto-creates                                                                                                                                                  | Google Forms, on submit                                                                                                                     |

`step_id` for task steps encodes the concrete assignment, e.g.
`task:1:730-h:gherkin`, so progress rows are self-describing without needing
a join against `assignments`.

## Counterbalancing

`scripts/generate_assignments.py` reads the approved task pool from
`../apps_selected_approved/{introductory,interview,competition}/` (12 tasks:
4 per difficulty) and produces a CSV to upload into the `assignments` tab.

Two balance guarantees, for any participant count `N`:

- **Task usage** — participants are grouped into rounds of
  `pool_size // 2` (6, for 12 tasks). Within a round, tasks are paired via a
  shuffled perfect matching, so every task is used **exactly once per
  round**. A fresh matching (different seed) is generated per round, so
  repeated rounds don't reuse identical pairs.
- **Modality order** — the nl-first vs gherkin-first split across all `N`
  participants is exactly `N//2` vs `N - N//2` (off by at most one),
  computed independently of task-pair assignment so the two factors aren't
  confounded.

```bash
python3 scripts/generate_assignments.py 6          # 6 participants, one full round
python3 scripts/generate_assignments.py p001 p002  # explicit participant IDs
```

Upload the CSV into the `assignments` tab (Google Sheets: paste + "Split
text to columns", or File → Import for reliability — see project notes).

## Task descriptions

`scripts/build_descriptions.py` reads every task's `nl/description.md` and
`gherkin/description.feature` from `../selected/<bucket>/<slug>/` and embeds
them into `src/data/descriptions.json` at build/dev time, so the frontend
can render the correct description for each participant's assigned
task + modality without any runtime fetch.

This runs automatically as part of `npm run dev` / `npm run build`.

> Note: `build_descriptions.py` currently sources from `selected/`, while
> `generate_assignments.py` sources from `apps_selected_approved/`. Make
> sure both directories contain the same task slugs referenced in your
> assignments, or update one script to match the other.

## Frontend structure

```
src/
├── App.jsx                    ← mounts the wizard
├── components/
│   ├── Wizard.jsx             ← step engine: resolves current/viewed step, fetches/records progress, back/forth nav
│   ├── ProgressBar.jsx        ← visual step indicator
│   ├── Onboarding.jsx         ← static Gherkin intro / guidelines content
│   ├── ConfirmationStep.jsx   ← recap screen before finishing the study
│   └── TaskStep.jsx           ← prompt-writing editor for a study task, with autosave
├── config/steps.js            ← master step-ID list + modality labels
├── hooks/useParticipant.js    ← resolves `pid` from the URL, fetches assignment
└── data/descriptions.json     ← generated by scripts/build_descriptions.py (gitignored)
```

### Step engine

`MASTER_STEP_IDS` in `src/config/steps.js` defines the fixed step order.
`task:1:first`, `task:1:second`, `task:2:first`, and `task:2:second` placeholders
are expanded at runtime in `Wizard.jsx` using the participant's `assignment`
(from `/api/assignment`) into concrete step IDs like `task:1:730-h:gherkin`.

On each render, `Wizard.jsx`:

1. Fetches `completedStepIds` for the participant from `/api/progress`.
2. Computes `frontierIndex` — the first step not yet completed — which
   gates how far forward the participant can navigate.
3. Tracks a separate `viewIndex` for the step currently displayed, which
   can move freely between `0` and `frontierIndex` via the "← Back" /
   "Next →" nav, letting participants review or edit previously completed
   steps without losing their place.
4. On mount of a step, records a `started` event (idempotent-ish; best
   effort, not deduplicated).
5. On "Continue"/"Submit", records a `completed` event and advances
   `viewIndex` by one.

This means **closing and reopening the link resumes exactly where the
participant left off** — state lives in the Sheet, not in browser storage.

### Email-based forms

The consent form, baseline questionnaire, and post-study survey are sent
directly to participants via email rather than embedded in the app (see
`emails/study-invitation.md` and `emails/post-study.md`) — cross-origin
iframes can't notify the parent page when a Google Form is submitted, and
these forms don't need the app's sequential-gating logic anyway.

## Backend structure

```
netlify/functions/
├── utils/sheets.mjs      ← thin Sheets API client (JWT service-account auth)
├── assignment.mjs        ← GET  /api/assignment?pid=X
├── progress.mjs          ← GET/POST /api/progress?pid=X (also usable for polling)
└── step-complete.mjs     ← POST /api/step-complete {pid, stepId, status, payload}
```

## Email templates

```
emails/
├── study-invitation.md   ← sent at study start: consent + baseline forms, study link
└── post-study.md         ← sent after both tasks are done: post-study survey
```

Both templates use `{{PLACEHOLDER}}` tokens (participant name/ID, form URLs,
study link) to fill in per send, and remind participants to use a full-size
screen (not a phone/tablet) for the best experience.

Required environment variables (set in Netlify site settings, or a local
`.env` for `netlify dev`):

| Variable                      | Description                                                       |
| ----------------------------- | ----------------------------------------------------------------- |
| `STUDY_SHEET_ID`              | The Google Sheet's ID (from its URL)                              |
| `STUDY_SERVICE_ACCOUNT_EMAIL` | Service account email with Editor access to the Sheet             |
| `STUDY_SERVICE_ACCOUNT_KEY`   | Service account private key (PEM, with literal `\n` for newlines) |

## Local development

```bash
npm install
npm install --prefix netlify/functions
npx netlify dev
```

Serves the frontend + functions together at `http://localhost:8888`.
Visit `http://localhost:8888/p001` (participant ID must exist in the
`assignments` tab), or just `http://localhost:8888/` to be prompted for one.

## Deployment

Deploy via Netlify (static build + functions), see `netlify.toml` for build
config (`npm run build`, publish `dist/`, functions in
`netlify/functions/`).

## Known TODOs

- Fill in the real Google Form URLs and study link in `emails/*.md` before
  sending them out.
- Reconcile `selected/` vs `apps_selected_approved/` as the single source of
  truth for task descriptions and assignment slugs.
