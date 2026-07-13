import { google } from 'googleapis';

const SHEET_ID = process.env.STUDY_SHEET_ID;
const CLIENT_EMAIL = process.env.STUDY_SERVICE_ACCOUNT_EMAIL;
const PRIVATE_KEY = process.env.STUDY_SERVICE_ACCOUNT_KEY?.replace(/\\n/g, '\n');

function getSheetsClient() {
  if (!SHEET_ID || !CLIENT_EMAIL || !PRIVATE_KEY) {
    throw new Error(
      'Missing required env vars: STUDY_SHEET_ID, STUDY_SERVICE_ACCOUNT_EMAIL, STUDY_SERVICE_ACCOUNT_KEY'
    );
  }
  const auth = new google.auth.JWT(CLIENT_EMAIL, null, PRIVATE_KEY, [
    'https://www.googleapis.com/auth/spreadsheets',
  ]);
  return google.sheets({ version: 'v4', auth });
}

export async function getSheetRows(tab, range) {
  const sheets = getSheetsClient();
  const res = await sheets.spreadsheets.values.get({
    spreadsheetId: SHEET_ID,
    range: `${tab}!${range}`,
  });
  return res.data.values || [];
}

export async function appendRow(tab, values) {
  const sheets = getSheetsClient();
  await sheets.spreadsheets.values.append({
    spreadsheetId: SHEET_ID,
    range: `${tab}!A1`,
    valueInputOption: 'USER_ENTERED',
    insertDataOption: 'INSERT_ROWS',
    resource: { values: [values] },
  });
}

// Autosave writes a `draft` row roughly every 30s. Rather than appending a
// brand-new row every time (which would flood the sheet with near-duplicate
// history), find the existing draft row for this participant/step and
// overwrite it in place. Falls back to appending if no existing row is
// found (e.g. the first save for this step).
export async function upsertDraftRow(tab, pid, stepId, values) {
  const sheets = getSheetsClient();
  const res = await sheets.spreadsheets.values.get({
    spreadsheetId: SHEET_ID,
    range: `${tab}!A2:E`,
  });
  const rows = res.data.values || [];
  const rowIndex = rows.findIndex((r) => r[0] === pid && r[1] === stepId && r[2] === 'draft');

  if (rowIndex === -1) {
    await appendRow(tab, values);
    return;
  }

  const sheetRowNumber = rowIndex + 2; // +2 accounts for the header row + 1-index
  await sheets.spreadsheets.values.update({
    spreadsheetId: SHEET_ID,
    range: `${tab}!A${sheetRowNumber}:E${sheetRowNumber}`,
    valueInputOption: 'USER_ENTERED',
    resource: { values: [values] },
  });
}

export { SHEET_ID };
