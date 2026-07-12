import React, { useEffect, useRef, useState } from 'react';
import { MASTER_STEP_IDS, FORM_URLS } from '../config/steps.js';
import descriptions from '../data/descriptions.json';
import ProgressBar from './ProgressBar.jsx';
import FormStep from './FormStep.jsx';
import Onboarding from './Onboarding.jsx';
import TaskStep from './TaskStep.jsx';
import ReferenceModal from './ReferenceModal.jsx';

async function fetchProgress(pid) {
  const res = await fetch(`/api/progress?pid=${encodeURIComponent(pid)}`);
  const data = await res.json();
  if (!res.ok) throw new Error(data.error || 'Failed to load progress');
  return {
    completedStepIds: data.completedStepIds || [],
    startedStepIds: data.startedStepIds || [],
    drafts: data.drafts || {},
  };
}

async function recordStep(pid, stepId, status, payload = {}) {
  const res = await fetch('/api/step-complete', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ pid, stepId, status, payload }),
  });
  const data = await res.json();
  if (!res.ok) throw new Error(data.error || 'Failed to record step');
  return data;
}

export default function Wizard({ pid, assignment, loading, error }) {
  const [completedStepIds, setCompletedStepIds] = useState([]);
  const [drafts, setDrafts] = useState({});
  const [stepLoading, setStepLoading] = useState(true);
  const [stepError, setStepError] = useState(null);
  const [showReference, setShowReference] = useState(false);
  const startedStepIdsRef = useRef(new Set());

  // Build concrete steps using the participant assignment.
  const steps = React.useMemo(() => {
    if (!assignment) return [];
    return MASTER_STEP_IDS.map((id) => {
      if (id === 'task:1') {
        return {
          id: `task:1:${assignment.task_1_slug}:${assignment.task_1_modality}`,
          kind: 'task',
          taskSlug: assignment.task_1_slug,
          modality: assignment.task_1_modality,
        };
      }
      if (id === 'task:2') {
        return {
          id: `task:2:${assignment.task_2_slug}:${assignment.task_2_modality}`,
          kind: 'task',
          taskSlug: assignment.task_2_slug,
          modality: assignment.task_2_modality,
        };
      }
      return { id, kind: 'form' };
    });
  }, [assignment]);

  const currentIndex = React.useMemo(() => {
    if (steps.length === 0) return 0;
    let i = 0;
    while (i < steps.length && completedStepIds.includes(steps[i].id)) i += 1;
    return Math.min(i, steps.length - 1);
  }, [completedStepIds, steps]);

  const isDone = React.useMemo(
    () => steps.length > 0 && completedStepIds.includes(steps[steps.length - 1].id),
    [completedStepIds, steps]
  );

  useEffect(() => {
    if (!pid) return;
    setStepLoading(true);
    fetchProgress(pid)
      .then(({ completedStepIds: completed, startedStepIds: started, drafts: loadedDrafts }) => {
        started.forEach((id) => startedStepIdsRef.current.add(id));
        setCompletedStepIds(completed);
        setDrafts(loadedDrafts);
      })
      .catch((err) => setStepError(err.message))
      .finally(() => setStepLoading(false));
  }, [pid]);

  // Mirror the current step into the URL (/<pid>/<step-id>) so it's
  // shareable/bookmarkable and visible in the address bar. This is purely a
  // reflection of server-derived progress, not a navigation source of truth
  // — reloading always re-resolves the step from /api/progress.
  useEffect(() => {
    if (!pid || steps.length === 0) return;
    const segment = isDone ? 'done' : steps[currentIndex]?.id;
    if (!segment) return;
    const target = `/${encodeURIComponent(pid)}/${segment}`;
    if (window.location.pathname !== target) {
      window.history.replaceState({}, '', target);
    }
  }, [pid, steps, currentIndex, isDone]);

  useEffect(() => {
    if (stepLoading) return;
    if (!steps[currentIndex]) return;
    const id = steps[currentIndex].id;
    if (completedStepIds.includes(id)) return;
    if (startedStepIdsRef.current.has(id)) return;
    startedStepIdsRef.current.add(id);
    recordStep(pid, id, 'started').catch(() => {
      startedStepIdsRef.current.delete(id);
    });
  }, [currentIndex, steps, pid, completedStepIds, stepLoading]);

  async function handleComplete(payload) {
    const current = steps[currentIndex];
    if (!current) return;
    try {
      await recordStep(pid, current.id, 'completed', payload);
      setCompletedStepIds((prev) => (prev.includes(current.id) ? prev : [...prev, current.id]));
    } catch (err) {
      setStepError(err.message);
    }
  }

  async function handleSaveDraft(payload) {
    const id = steps[currentIndex].id;
    await recordStep(pid, id, 'draft', payload);
    setDrafts((prev) => ({ ...prev, [id]: payload }));
  }

  if (loading || stepLoading) return <p>Loading study...</p>;
  if (error) return <div className="error">{error}</div>;
  if (stepError) return <div className="error">{stepError}</div>;
  if (!assignment) return <div className="error">No assignment found for participant ID.</div>;

  const current = steps[currentIndex];
  const completedSet = new Set(completedStepIds);
  const canShowReference = completedSet.has('onboarding:guidelines');

  if (isDone) {
    return (
      <div className="card">
        <h2>Study complete</h2>
        <p>Thank you for participating. You may close this window now.</p>
        <p>If you have any questions, you can contact me at <a href="mailto:michal.okrasa@unine.ch">michal.okrasa@unine.ch</a></p>
      </div>
    );
  }

  return (
    <div>
      <ProgressBar
        total={steps.length}
        current={currentIndex}
        completed={completedSet}
      />
      {canShowReference && (
        <button className="reference-link" onClick={() => setShowReference(true)}>
          📖 View training materials
        </button>
      )}
      <StepContent
        pid={pid}
        step={current}
        stepIndex={currentIndex}
        draft={drafts[current.id]?.prompt || ''}
        onComplete={handleComplete}
        onSaveDraft={handleSaveDraft}
      />
      {showReference && <ReferenceModal onClose={() => setShowReference(false)} />}
    </div>
  );
}

function StepContent({ pid, step, stepIndex, draft, onComplete, onSaveDraft }) {
  if (step.kind === 'task') {
    return (
      <TaskStep
        key={step.id}
        pid={pid}
        stepIndex={stepIndex}
        taskSlug={step.taskSlug}
        modality={step.modality}
        description={getTaskDescription(step.taskSlug)}
        initialDraft={draft}
        onContinue={onComplete}
        onSaveDraft={onSaveDraft}
      />
    );
  }

  switch (step.id) {
    case 'pre:consent':
      return <FormStep pid={pid} title="Consent Form" formUrl={FORM_URLS['pre:consent']} onContinue={onComplete} />;
    case 'pre:baseline':
      return <FormStep pid={pid} title="Baseline Questionnaire" formUrl={FORM_URLS['pre:baseline']} onContinue={onComplete} />;
    case 'onboarding:intro':
      return <Onboarding type="intro" onContinue={onComplete} />;
    case 'onboarding:guidelines':
      return <Onboarding type="guidelines" onContinue={onComplete} />;
    case 'check:comprehension':
      return <Onboarding type="ready" onContinue={onComplete} />;
    case 'post:feedback':
      return <FormStep pid={pid} title="Post-Study Survey" formUrl={FORM_URLS['post:feedback']} onContinue={onComplete} />;
    default:
      return <div className="error">Unknown step: {step.id}</div>;
  }
}

function getTaskDescription(taskSlug) {
  return descriptions[taskSlug] || `(Description for ${taskSlug} is not available.)`;
}
