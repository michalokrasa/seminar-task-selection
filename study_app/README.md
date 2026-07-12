# Study App

A step-by-step wizard for running the NL-vs-Gherkin prompt-writing study. Tracks
per-participant progress and timing, enforces sequential completion of steps,
and counterbalances task/modality assignment across participants.

## Study flow

1. **Pre-study**
   1. Consent form (embedded Google Form)
   2. Baseline questionnaire (embedded Google Form)
2. **Onboarding**
   1. Gherkin introduction (custom step)
   2. Prompt-writing guidelines + examples (custom step)
   3. "Ready to start" info screen (next step is Task 1; contact email for questions)
3. **Study**
   1. Task 1 — prompt-writing (custom step, NL or Gherkin per assignment)
   2. Task 2 — prompt-writing (custom step, opposite modality of Task 1)
4. **Post-study**
   1. Post-experiment survey (embedded Google Form)

Each participant accesses the app via a link containing their ID as a path
segment: `https://<site>/p001`. All state is keyed by this `pid`. If a
participant visits the site with no ID in the URL, they're shown a prompt to
enter it (which then updates the URL via `pushState`, so subsequent reloads
resume from the path). The old `?pid=p001` query-string form is still
accepted as a fallback.

Once a participant's `pid` is resolved, `Wizard.jsx` also mirrors the current
step into the path as `/<pid>/<step-id>` (e.g. `/p001/pre:consent`, or
`/p001/done` once finished) via `replaceState`. This is purely a display
convenience for bookmarking/sharing/debugging — the actual current step is
always re-derived from `/api/progress` on load, never read back out of the
URL.

## Architecture

```
Browser (Vite + React SPA)
  ├─ GET  /api/assignment?pid=X   → Netlify Function → reads "assignments" sheet
  ├─ GET  /api/progress?pid=X     → Netlify Function → reads "progress" sheet
  ├─ POST /api/step-complete      → Netlify Function → appends row to "progress" sheet
  └─ <iframe src="https://docs.google.com/forms/...">  (for form-type steps)
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
  counterbalanced ordering — hence a thin custom app owns flow control while
  Forms are embedded only for the parts where they add nothing extra
  (consent, Likert scales).
- Netlify Functions + Sheets API avoids running/maintaining a database for a
  small-N pilot study.

## Data model (Google Sheet tabs)

| Tab                | Columns                                                                                                                     | Written by                                                                           |
| ------------------ | --------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------ |
| `assignments`      | `participant_id, task_1_slug, task_1_modality, task_2_slug, task_2_modality, condition_group, task_1_bucket, task_2_bucket` | Uploaded once, offline, from `scripts/generate_assignments.py` output                |
| `progress`         | `participant_id, step_id, status, timestamp, payload`                                                                       | Appended live by `/api/step-complete` (`status` ∈ `started` / `draft` / `completed`) |
| (native form tabs) | Whatever each Google Form auto-creates                                                                                      | Google Forms, on submit                                                              |

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
│   ├── Wizard.jsx             ← step engine: resolves current step, fetches/records progress
│   ├── ProgressBar.jsx        ← visual step indicator
│   ├── FormStep.jsx           ← embeds a Google Form iframe + "Continue" button
│   ├── Onboarding.jsx         ← static Gherkin intro / guidelines content
│   └── TaskStep.jsx           ← prompt-writing textarea for a study task
├── config/steps.js            ← master step-ID list + Google Form URLs + modality labels
├── hooks/useParticipant.js    ← resolves `pid` from the URL, fetches assignment
└── data/descriptions.json     ← generated by scripts/build_descriptions.py (gitignored)
```

### Step engine

`MASTER_STEP_IDS` in `src/config/steps.js` defines the fixed step order.
`task:1` / `task:2` placeholders are expanded at runtime in `Wizard.jsx`
using the participant's `assignment` (from `/api/assignment`) into concrete
step IDs like `task:1:730-h:gherkin`.

On each render, `Wizard.jsx`:

1. Fetches `completedStepIds` for the participant from `/api/progress`.
2. Finds the first step not yet completed → that's the current step.
3. On mount of a step, records a `started` event (idempotent-ish; best
   effort, not deduplicated).
4. On "Continue"/"Submit", records a `completed` event and advances.

This means **closing and reopening the link resumes exactly where the
participant left off** — state lives in the Sheet, not in browser storage.

### Google Form steps

Cross-origin iframes can't notify the parent page when a Form is submitted,
so `FormStep.jsx` uses a self-report pattern: the form is embedded, and a
separate "Continue →" button (with instructions to submit the form first)
records completion. This is a known limitation — see the note in prior
design discussion about the Apps Script webhook alternative if exact
Form-submission timestamps become necessary.

## Backend structure

```
netlify/functions/
├── utils/sheets.mjs      ← thin Sheets API client (JWT service-account auth)
├── assignment.mjs        ← GET  /api/assignment?pid=X
├── progress.mjs          ← GET/POST /api/progress?pid=X (also usable for polling)
└── step-complete.mjs     ← POST /api/step-complete {pid, stepId, status, payload}
```

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

- `src/config/steps.js` `FORM_URLS` still contain placeholder `REPLACE`
  Google Form URLs — swap in real form links once created.
- Reconcile `selected/` vs `apps_selected_approved/` as the single source of
  truth for task descriptions and assignment slugs.
- `FormStep.jsx` completion is self-reported; consider the Apps
  Script `onFormSubmit` webhook if exact submission timestamps matter.
