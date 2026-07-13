import React, { useEffect, useRef, useState } from 'react';
import { marked } from '../lib/markdown.js';
import GherkinEditor from './GherkinEditor.jsx';

const AUTOSAVE_INTERVAL_MS = 30000;

export default function TaskStep({
  pid,
  stepIndex,
  taskSlug,
  modality,
  description,
  initialDraft,
  onContinue,
  onSaveDraft,
}) {
  const [draft, setDraft] = useState(initialDraft || '');
  const [saving, setSaving] = useState(false);
  const [saved, setSaved] = useState(false);

  const label = modality === 'gherkin' ? 'Gherkin' : 'Natural-language';

  // Keep a ref to the latest draft/task info so the autosave interval below
  // always saves the freshest value without needing to be re-created on
  // every keystroke.
  const latestRef = useRef({ draft, taskSlug, modality, onSaveDraft });
  useEffect(() => {
    latestRef.current = { draft, taskSlug, modality, onSaveDraft };
  }, [draft, taskSlug, modality, onSaveDraft]);

  async function saveDraft(text) {
    setSaving(true);
    await onSaveDraft({ taskSlug, modality, prompt: text });
    setSaved(true);
    setSaving(false);
  }

  // Autosave: every 30s, persist the current draft so no input is lost even
  // if the participant never clicks "Save draft" manually.
  useEffect(() => {
    const id = setInterval(() => {
      const { draft: latestDraft, taskSlug: ts, modality: m, onSaveDraft: save } = latestRef.current;
      save({ taskSlug: ts, modality: m, prompt: latestDraft });
      setSaved(true);
    }, AUTOSAVE_INTERVAL_MS);
    return () => clearInterval(id);
  }, []);

  async function handleSave() {
    await saveDraft(draft);
  }

  async function handleSubmit() {
    if (!draft.trim()) {
      if (!confirm('Your prompt is empty. Continue anyway?')) return;
    }
    const payload = { taskSlug, modality, prompt: draft };
    await handleSave();
    setDraft('');
    setSaved(false);
    onContinue(payload);
  }

  return (
    <div>
      <h2 style={{ marginBottom: '0.4rem' }}>Task {stepIndex - 3}</h2>
      <p style={{ margin: '0 0 1.5rem', fontSize: '1.05rem', fontWeight: 600, lineHeight: 1.5 }}>
        Read the problem description below carefully, then write a prompt
        that you would give to an LLM so that it can solve this problem for
        you. Your prompt must be written in{' '}
        <strong>{label.toLowerCase()}</strong> format.
      </p>
      <div className="task-layout">
        <div className="task-description">
          <div dangerouslySetInnerHTML={{ __html: marked.parse(description || '') }} />
        </div>
        <div className="task-editor">
          {modality === 'gherkin' ? (
            <GherkinEditor
              value={draft}
              onChange={(next) => {
                setDraft(next);
                setSaved(false);
              }}
              placeholder={`Write your ${label.toLowerCase()} prompt here...`}
            />
          ) : (
            <textarea
              className="task-textarea"
              value={draft}
              onChange={(e) => {
                setDraft(e.target.value);
                setSaved(false);
              }}
              placeholder={`Write your ${label.toLowerCase()} prompt here...`}
            />
          )}
        </div>
      </div>
      <div className="task-footer">
        <button className="secondary" onClick={handleSave} disabled={saving}>
          {saving ? 'Saving...' : saved ? 'Saved ✓' : 'Save draft'}
        </button>
        <p className="hint" style={{ margin: 0 }}>
          Autosave is on — your prompt is saved automatically every 30 seconds.
        </p>
        <button className="primary" onClick={handleSubmit}>
          Submit and continue →
        </button>
      </div>
    </div>
  );
}
