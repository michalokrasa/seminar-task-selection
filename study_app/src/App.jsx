import React from 'react';
import Wizard from './components/Wizard.jsx';
import PidPrompt from './components/PidPrompt.jsx';
import DescriptionPreview from './components/DescriptionPreview.jsx';
import { useParticipant } from './hooks/useParticipant.js';

function App() {
  const { pid, setPid, assignment, loading, error } = useParticipant();
  const isPreview = window.location.pathname.replace(/^\/+|\/+$/g, '') === 'preview';

  return (
    <div className="container">
      <div className="card">
        {isPreview ? (
          <DescriptionPreview />
        ) : !pid ? (
          <PidPrompt onSubmit={setPid} />
        ) : (
          <Wizard pid={pid} assignment={assignment} loading={loading} error={error} />
        )}
      </div>
    </div>
  );
}

export default App;
