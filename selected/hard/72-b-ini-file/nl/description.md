# INI File

## Goal

Reformat a given INI file by sorting sections and keys, deduplicating keys, and removing comments and extra whitespace.

## Rules

- **Comments**: any line whose first non-space character is `;` is discarded entirely.
- **Section headers**: lines of the form `[section]` (with optional surrounding spaces). Spaces around the brackets and inside are stripped.
- **Key-value pairs**: lines of the form `key = value` (with optional spaces around `key` and `value`). Spaces are stripped from both.
- Key-value lines before the first section header belong to a "global" (no-section) namespace printed first.
- If the same key appears multiple times in the same section, keep only the **last** occurrence.
- **Output order**:
  1. Global key-value pairs, sorted lexicographically by key.
  2. Each section in lexicographic order of section name, preceded by `[section]`.
  3. Within each section, key-value pairs sorted lexicographically by key.
- Empty sections (no surviving key-value pairs) are still printed with their header.
- No blank lines in output.

## Input / Output

- **Input**: first line is `n` (1 ≤ n ≤ 510); the next `n` lines form the INI file.
- **Output**: the reformatted INI file.
