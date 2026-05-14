# Suffix Three — Language Detector

## Goal

Identify the language of a sentence by checking which suffix it ends with.

## Rules

- If the sentence ends with `"po"` → the language is **FILIPINO**.
- If the sentence ends with `"desu"` or `"masu"` → the language is **JAPANESE**.
- If the sentence ends with `"mnida"` → the language is **KOREAN**.
- Spaces in sentences are represented as underscores (`_`).
- It is guaranteed that every input sentence ends with exactly one of the four suffixes above.

## Input / Output

- **Input**: first line is an integer `t` (number of test cases); each of the next `t` lines is a sentence string.
- **Output**: for each sentence, one line containing `FILIPINO`, `JAPANESE`, or `KOREAN`.
