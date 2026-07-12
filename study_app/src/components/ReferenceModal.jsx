import React, { useState } from 'react';
import { marked } from '../lib/markdown.js';
import introMd from '../content/onboarding-intro.md?raw';
import guidelinesMd from '../content/prompt-guidelines.md?raw';

const TABS = [
  { key: 'intro', label: 'Gherkin intro', content: introMd },
  { key: 'guidelines', label: 'Prompt guidelines', content: guidelinesMd },
];

export default function ReferenceModal({ onClose }) {
  const [activeTab, setActiveTab] = useState(TABS[0].key);
  const active = TABS.find((t) => t.key === activeTab);

  return (
    <div className="modal-overlay" onClick={onClose}>
      <div className="modal-content" onClick={(e) => e.stopPropagation()}>
        <div className="modal-header">
          <div className="modal-tabs">
            {TABS.map((tab) => (
              <button
                key={tab.key}
                className={`modal-tab ${tab.key === activeTab ? 'active' : ''}`}
                onClick={() => setActiveTab(tab.key)}
              >
                {tab.label}
              </button>
            ))}
          </div>
          <button className="modal-close" onClick={onClose} aria-label="Close">
            ✕
          </button>
        </div>
        <div className="modal-body" dangerouslySetInnerHTML={{ __html: marked.parse(active.content) }} />
      </div>
    </div>
  );
}
