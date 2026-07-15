import React from 'react';

export default function ConfirmationStep({ onFinish }) {
  return (
    <div>
      <h2>All four specifications submitted 🎉</h2>
      <p>
        Your specifications for both tasks (Gherkin and natural-language versions)
        have been submitted successfully. You're about to finish the study.
      </p>
      <p className="hint">
        Use the <strong>← Back</strong> button above if you'd like to review
        or update any of your answers before finishing. Otherwise, click{' '}
        <strong>Finish</strong> below to complete the study.
      </p>
      <div style={{ textAlign: 'right', marginTop: '1rem' }}>
        <button className="primary" onClick={onFinish}>
          Finish →
        </button>
      </div>
    </div>
  );
}
