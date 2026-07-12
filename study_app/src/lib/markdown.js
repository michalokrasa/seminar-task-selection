import { Marked } from 'marked';
import { markedHighlight } from 'marked-highlight';
import markedKatex from 'marked-katex-extension';
import hljs from 'highlight.js/lib/core';
import gherkin from 'highlight.js/lib/languages/gherkin';
import 'highlight.js/styles/github.css';
import 'katex/dist/katex.min.css';

// highlight.js's bundled gherkin grammar predates Gherkin 6 and is missing
// the `Rule` keyword — extend it rather than patching the package.
function gherkinWithRule(hljsInstance) {
  const definition = gherkin(hljsInstance);
  definition.keywords += ' Rule';
  return definition;
}
hljs.registerLanguage('gherkin', gherkinWithRule);

function escapeHtml(str) {
  return str
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;');
}

export const marked = new Marked(
  markedHighlight({
    langPrefix: 'hljs language-',
    highlight(code, lang) {
      if (lang && hljs.getLanguage(lang)) {
        return hljs.highlight(code, { language: lang }).value;
      }
      return escapeHtml(code);
    },
  }),
  markedKatex({
    throwOnError: false,
    nonStandard: true,
  })
);
