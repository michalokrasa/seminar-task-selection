import React, { useState } from 'react';
import { marked } from '../lib/markdown.js';
import descriptions from '../data/descriptions.json';

const slugs = Object.keys(descriptions);

export default function DescriptionPreview() {
  const [index, setIndex] = useState(0);

  if (slugs.length === 0) {
    return <div className="error">No descriptions found in descriptions.json.</div>;
  }

  const slug = slugs[index];
  const description = descriptions[slug];

  function goPrev() {
    setIndex((i) => Math.max(0, i - 1));
  }

  function goNext() {
    setIndex((i) => Math.min(slugs.length - 1, i + 1));
  }

  function handleKeyDown(e) {
    if (e.key === 'ArrowLeft') goPrev();
    if (e.key === 'ArrowRight') goNext();
  }

  return (
    <div onKeyDown={handleKeyDown} tabIndex={0}>
      <h2>Description preview ({index + 1} / {slugs.length})</h2>
      <p className="hint">
        Problem: <strong>{slug}</strong>
      </p>
      <div
        style={{
          background: '#f8fafc',
          padding: '1rem',
          borderRadius: '8px',
          marginBottom: '1rem',
          border: '1px solid #e2e8f0',
        }}
      >
        <div dangerouslySetInnerHTML={{ __html: marked.parse(description || '') }} />
      </div>
      <div style={{ display: 'flex', justifyContent: 'space-between', marginTop: '1rem' }}>
        <button className="secondary" onClick={goPrev} disabled={index === 0}>
          ← Previous
        </button>
        <select value={slug} onChange={(e) => setIndex(slugs.indexOf(e.target.value))}>
          {slugs.map((s) => (
            <option key={s} value={s}>
              {s}
            </option>
          ))}
        </select>
        <button className="primary" onClick={goNext} disabled={index === slugs.length - 1}>
          Next →
        </button>
      </div>
    </div>
  );
}
