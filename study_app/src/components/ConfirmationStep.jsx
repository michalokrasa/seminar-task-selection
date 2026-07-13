import React from 'react';

export default function ConfirmationStep({ onFinish }) {
  return (
    <div>
      <h2>Both tasks submitted 🎉</h2>
      <p>
        Your prompts for Task 1 and Task 2 have both been submitted
        successfully. You're about to finish the study.
      </p>
      <p className="hint">
        Use the <strong>← Back</strong> button above if you'd like to review
        or update either of your answers before finishing. Otherwise, click{' '}
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
