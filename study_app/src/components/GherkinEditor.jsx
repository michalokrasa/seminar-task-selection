import React, { useEffect, useRef } from 'react';
import { EditorView, basicSetup } from 'codemirror';
import { EditorState } from '@codemirror/state';
import { keymap } from '@codemirror/view';
import { indentWithTab } from '@codemirror/commands';
import { gherkinLanguage, gherkinHighlighting } from '../lib/gherkinLanguage.js';

export default function GherkinEditor({ value, onChange, placeholder }) {
  const containerRef = useRef(null);
  const viewRef = useRef(null);
  const onChangeRef = useRef(onChange);
  onChangeRef.current = onChange;
  const isEmpty = !value;

  useEffect(() => {
    const state = EditorState.create({
      doc: value || '',
      extensions: [
        basicSetup,
        keymap.of([indentWithTab]),
        gherkinLanguage,
        gherkinHighlighting,
        EditorView.lineWrapping,
        EditorView.updateListener.of((update) => {
          if (update.docChanged) {
            onChangeRef.current(update.state.doc.toString());
          }
        }),
        EditorView.theme({
          '&': {
            fontSize: '0.95rem',
            border: '1px solid #cbd5e1',
            borderRadius: '8px',
          },
          '.cm-content': {
            fontFamily:
              'ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace',
            minHeight: '200px',
          },
          '.cm-scroller': {
            minHeight: '200px',
          },
          '&.cm-focused': {
            outline: 'none',
            borderColor: '#2563eb',
          },
        }),
      ],
    });

    const view = new EditorView({
      state,
      parent: containerRef.current,
    });
    viewRef.current = view;

    return () => {
      view.destroy();
      viewRef.current = null;
    };
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  // Keep the editor in sync if `value` is reset externally (e.g. step change).
  useEffect(() => {
    const view = viewRef.current;
    if (!view) return;
    const current = view.state.doc.toString();
    if (value !== current) {
      view.dispatch({
        changes: { from: 0, to: current.length, insert: value || '' },
      });
    }
  }, [value]);

  return (
    <div className="gherkin-editor">
      {isEmpty && <div className="gherkin-editor-placeholder">{placeholder}</div>}
      <div ref={containerRef} />
    </div>
  );
}
