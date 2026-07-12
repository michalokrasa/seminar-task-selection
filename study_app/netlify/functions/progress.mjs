import { getSheetRows, appendRow } from './utils/sheets.mjs';

export const handler = async (event) => {
  const pid = event.queryStringParameters?.pid;
  if (!pid) {
    return { statusCode: 400, body: JSON.stringify({ error: 'Missing pid parameter' }) };
  }

  if (event.httpMethod === 'GET') {
    try {
      const rows = await getSheetRows('progress', 'A2:E');
      // Expected headers: participant_id, step_id, status, timestamp
      const completed = rows
        .filter((r) => r[0] === pid && r[2] === 'completed')
        .map((r) => r[1]);
      const started = [...new Set(
        rows.filter((r) => r[0] === pid && r[2] === 'started').map((r) => r[1])
      )];
      const drafts = {};
      rows.forEach((r) => {
        if (r[0] === pid && r[2] === 'draft') {
          try {
            drafts[r[1]] = JSON.parse(r[4] || '{}');
          } catch {
            drafts[r[1]] = {};
          }
        }
      });
      return {
        statusCode: 200,
        body: JSON.stringify({ completedStepIds: completed, startedStepIds: started, drafts }),
      };
    } catch (err) {
      return { statusCode: 500, body: JSON.stringify({ error: err.message }) };
    }
  }

  if (event.httpMethod === 'POST') {
    try {
      const body = JSON.parse(event.body || '{}');
      const { stepId, status, payload } = body;
      await appendRow('progress', [pid, stepId, status, new Date().toISOString(), JSON.stringify(payload || {})]);
      return { statusCode: 200, body: JSON.stringify({ ok: true }) };
    } catch (err) {
      return { statusCode: 500, body: JSON.stringify({ error: err.message }) };
    }
  }

  return { statusCode: 405, body: JSON.stringify({ error: 'Method not allowed' }) };
};
