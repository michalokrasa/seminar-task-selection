import { StreamLanguage, HighlightStyle, syntaxHighlighting } from '@codemirror/language';
import { tags as t } from '@lezer/highlight';

// Minimal Gherkin tokenizer: keywords, tags, comments, strings, doc strings,
// data-table pipes and <placeholder> variables.
const KEYWORD_RE = /^(Feature|Background|Rule|Scenario Outline|Scenario|Examples)(?=\s*:)/;
const STEP_RE = /^(Given|When|Then|And|But|\*)\b/;

export const gherkinLanguage = StreamLanguage.define({
  startState() {
    return { inDocString: false };
  },
  token(stream, state) {
    if (state.inDocString) {
      if (stream.match(/^"""/)) {
        state.inDocString = false;
        return 'string';
      }
      stream.skipToEnd();
      return 'string';
    }

    if (stream.eatSpace()) return null;

    if (stream.match(/^#.*/)) return 'comment';

    if (stream.match(/^"""/)) {
      state.inDocString = true;
      return 'string';
    }

    if (stream.match(/^"[^"]*"/)) return 'string';

    if (stream.match(/^@[\w-]+/)) return 'tagName';

    if (stream.match(/^<[^<>]+>/)) return 'variableName';

    if (stream.match(KEYWORD_RE)) return 'keyword';

    if (stream.match(STEP_RE)) return 'keyword';

    if (stream.match(/^\|/)) return 'operator';

    if (stream.match(/^\d+(\.\d+)?/)) return 'number';

    stream.next();
    return null;
  },
});

export const gherkinHighlightStyle = HighlightStyle.define([
  { tag: t.comment, color: '#94a3b8', fontStyle: 'italic' },
  { tag: t.keyword, color: '#2563eb', fontWeight: 'bold' },
  { tag: t.string, color: '#059669' },
  { tag: t.tagName, color: '#9333ea' },
  { tag: t.variableName, color: '#d97706' },
  { tag: t.operator, color: '#64748b' },
  { tag: t.number, color: '#dc2626' },
]);

export const gherkinHighlighting = syntaxHighlighting(gherkinHighlightStyle);
