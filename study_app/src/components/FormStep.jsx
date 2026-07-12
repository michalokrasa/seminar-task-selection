import React from 'react';

export default function FormStep({ pid, title, formUrl, onContinue }) {
  // Substitute the participant ID into the form's pre-fill entry param.
  // FORM_URLS entries contain a PID_PLACEHOLDER token in place of the real
  // entry.<ID> value (see config/steps.js for how to obtain the entry ID).
  const url = formUrl.includes('REPLACE')
    ? formUrl
    : formUrl.replace('PID_PLACEHOLDER', encodeURIComponent(pid));

  return (
    <div>
      <h2>{title}</h2>
      <p className="hint">
        Submit the form below, then click <strong>Continue</strong> to proceed.
      </p>
      <iframe
        className="form-iframe"
        src={url}
        title={title}
        allowFullScreen
      />
      <div style={{ marginTop: '1rem', textAlign: 'right' }}>
        <button className="primary" onClick={() => onContinue()}>
          Continue →
        </button>
      </div>
    </div>
  );
}
