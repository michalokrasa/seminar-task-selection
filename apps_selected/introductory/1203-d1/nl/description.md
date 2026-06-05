# Maximum Removable Substring Length

## Goal

Determine the maximum length of a contiguous substring that can be removed from string `s` such that string `t` remains a subsequence of the modified `s`.

## Rules

- A subsequence is derived by deleting some characters of a string without changing the order of the remaining characters.
- You can remove a contiguous substring from `s` to maximize its length while ensuring `t` is still a subsequence of the resulting string.

## Input / Output

- **Input**: 
  - A string `s` (1 to 200 lowercase Latin letters).
  - A string `t` (1 to 200 lowercase Latin letters), guaranteed to be a subsequence of `s`.
- **Output**: 
  - An integer representing the maximum length of the substring that can be removed from `s` while keeping `t` as a subsequence.
