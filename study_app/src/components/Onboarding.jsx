import React from 'react';
import { marked } from '../lib/markdown.js';
import introMd from '../content/onboarding-intro.md?raw';
import guidelinesMd from '../content/prompt-guidelines.md?raw';
import readyMd from '../content/ready-for-task.md?raw';

const CONTENT_BY_TYPE = {
  intro: introMd,
  guidelines: guidelinesMd,
  ready: readyMd,
};

export default function Onboarding({ type, onContinue }) {
  const content = CONTENT_BY_TYPE[type] || guidelinesMd;
  return (
    <div>
      <div dangerouslySetInnerHTML={{ __html: marked.parse(content) }} />
      <div style={{ textAlign: 'right', marginTop: '1rem' }}>
        <button className="primary" onClick={() => onContinue()}>Continue →</button>
      </div>
    </div>
  );
}
