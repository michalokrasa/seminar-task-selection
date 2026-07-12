import React, { useState } from 'react';
import { marked } from '../lib/markdown.js';
import GherkinEditor from './GherkinEditor.jsx';

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

  async function handleSave() {
    setSaving(true);
    await onSaveDraft({ taskSlug, modality, prompt: draft });
    setSaved(true);
    setSaving(false);
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
      <h2 style={{ marginBottom: '0.2rem' }}>Task {stepIndex - 4} — {label} prompt</h2>
      <p className="hint" style={{ margin: '0 0 0.4rem' }}>
        Problem: <strong>{taskSlug}</strong>
      </p>
      <p style={{ margin: '0 0 0.5rem' }}>
        Below is the problem description for this task. Read it carefully,
        then write a prompt that you would give to an LLM so that it can
        solve this problem for you. Your prompt must be written in{' '}
        <strong>{label.toLowerCase()}</strong> format.
      </p>
      <div style={{ display: 'flex', gap: '0.75rem', marginBottom: '0.5rem' }}>
        <div
          style={{
            flex: 1,
            background: '#f8fafc',
            padding: '1rem',
            borderRadius: '8px',
            border: '1px solid #e2e8f0',
            overflowY: 'auto',
            maxHeight: '90vh',
          }}
        >
          <div dangerouslySetInnerHTML={{ __html: marked.parse(description || '') }} />
        </div>
        <div style={{ flex: 1, display: 'flex', flexDirection: 'column' }}>
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
              style={{ flex: 1, minHeight: '90vh', resize: 'vertical' }}
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
      <div style={{ display: 'flex', justifyContent: 'space-between', marginTop: '1rem' }}>
        <button className="secondary" onClick={handleSave} disabled={saving}>
          {saving ? 'Saving...' : saved ? 'Saved ✓' : 'Save draft'}
        </button>
        <button className="primary" onClick={handleSubmit}>
          Submit and continue →
        </button>
      </div>
    </div>
  );
}
