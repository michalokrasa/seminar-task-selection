import { appendRow } from './utils/sheets.mjs';

export const handler = async (event) => {
  if (event.httpMethod !== 'POST') {
    return { statusCode: 405, body: JSON.stringify({ error: 'Method not allowed' }) };
  }

  try {
    const { pid, stepId, status, payload } = JSON.parse(event.body || '{}');
    if (!pid || !stepId || !status) {
      return { statusCode: 400, body: JSON.stringify({ error: 'Missing pid, stepId, or status' }) };
    }

    await appendRow('progress', [
      pid,
      stepId,
      status,
      new Date().toISOString(),
      JSON.stringify(payload || {}),
    ]);

    return { statusCode: 200, body: JSON.stringify({ ok: true }) };
  } catch (err) {
    return { statusCode: 500, body: JSON.stringify({ error: err.message }) };
  }
};
