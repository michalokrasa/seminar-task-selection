import React, { useState } from 'react';

export default function PidPrompt({ onSubmit }) {
  const [value, setValue] = useState('');

  function handleSubmit(e) {
    e.preventDefault();
    onSubmit(value);
  }

  return (
    <form onSubmit={handleSubmit}>
      <h2>Enter your participant ID</h2>
      <p className="hint">
        Use the ID provided to you in the study invitation link.
      </p>
      <input
        type="text"
        value={value}
        onChange={(e) => setValue(e.target.value)}
        placeholder="e.g. p001"
        autoFocus
      />
      <div style={{ marginTop: '1rem' }}>
        <button type="submit" className="primary" disabled={!value.trim()}>
          Continue
        </button>
      </div>
    </form>
  );
}
