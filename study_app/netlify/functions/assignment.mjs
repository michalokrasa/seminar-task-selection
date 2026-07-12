import { getSheetRows } from './utils/sheets.mjs';

export const handler = async (event) => {
  const pid = event.queryStringParameters?.pid;
  if (!pid) {
    return { statusCode: 400, body: JSON.stringify({ error: 'Missing pid parameter' }) };
  }

  try {
    const rows = await getSheetRows('assignments', 'A2:F');
    // Expected headers: participant_id, task_1_slug, task_1_modality, task_2_slug, task_2_modality, condition_group
    const match = rows.find((r) => r[0] === pid);
    if (!match) {
      return { statusCode: 404, body: JSON.stringify({ error: 'Participant not found' }) };
    }

    const assignment = {
      participant_id: match[0],
      task_1_slug: match[1],
      task_1_modality: match[2],
      task_2_slug: match[3],
      task_2_modality: match[4],
      condition_group: match[5] || '',
    };

    return { statusCode: 200, body: JSON.stringify({ assignment }) };
  } catch (err) {
    return { statusCode: 500, body: JSON.stringify({ error: err.message }) };
  }
};
