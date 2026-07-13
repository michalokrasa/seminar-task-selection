import { appendRow, upsertDraftRow } from './utils/sheets.mjs';

export const handler = async (event) => {
  if (event.httpMethod !== 'POST') {
    return { statusCode: 405, body: JSON.stringify({ error: 'Method not allowed' }) };
  }

  try {
    const { pid, stepId, status, payload } = JSON.parse(event.body || '{}');
    if (!pid || !stepId || !status) {
      return { statusCode: 400, body: JSON.stringify({ error: 'Missing pid, stepId, or status' }) };
    }

    const row = [pid, stepId, status, new Date().toISOString(), JSON.stringify(payload || {})];

    // Drafts are autosaved every 30s; update the same record in place
    // instead of appending a new row each time.
    if (status === 'draft') {
      await upsertDraftRow('progress', pid, stepId, row);
    } else {
      await appendRow('progress', row);
    }

    return { statusCode: 200, body: JSON.stringify({ ok: true }) };
  } catch (err) {
    return { statusCode: 500, body: JSON.stringify({ error: err.message }) };
  }
};
