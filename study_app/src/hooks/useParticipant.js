import { useEffect, useState } from 'react';

function getPidFromUrl() {
  // Path shape is /<pid> or /<pid>/<step-id>; pid is always the first segment.
  const path = window.location.pathname.replace(/^\/+|\/+$/g, '');
  const [pidSegment] = path.split('/');
  if (pidSegment === 'preview') return '';
  if (pidSegment) return decodeURIComponent(pidSegment);
  // Back-compat with the old ?pid=YOUR_ID links.
  const params = new URLSearchParams(window.location.search);
  return params.get('pid') || '';
}

export function useParticipant() {
  const [pid, setPidState] = useState(getPidFromUrl());
  const [assignment, setAssignment] = useState(null);
  const [loading, setLoading] = useState(!!getPidFromUrl());
  const [error, setError] = useState(null);

  function setPid(newPid) {
    const clean = newPid.trim();
    if (!clean) return;
    window.history.pushState({}, '', `/${encodeURIComponent(clean)}`);
    setPidState(clean);
  }

  useEffect(() => {
    if (!pid) {
      setLoading(false);
      setError(null);
      return;
    }

    setLoading(true);
    setError(null);

    async function load() {
      try {
        const res = await fetch(`/api/assignment?pid=${encodeURIComponent(pid)}`);
        const data = await res.json();
        if (!res.ok) throw new Error(data.error || 'Failed to load assignment');
        setAssignment(data.assignment);
      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    }
    load();
  }, [pid]);

  return { pid, setPid, assignment, loading, error };
}
