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

export { SHEET_ID };
