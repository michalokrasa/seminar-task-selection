# Filename Pattern Matching

## Goal

Determine if there exists a pattern using '?' that matches exactly the specified files to be deleted and none of the others.

## Rules

- A pattern matches a filename if they have the same length and all characters match, except '?' which can match any single character.
- The pattern must match all files to be deleted and none of the files that should not be deleted.

## Input / Output

- **Input**: 
  - First line: two integers `n` and `m` (1 ≤ m ≤ n ≤ 100) representing the total number of files and the number of files to be deleted.
  - Next `n` lines: each line contains a filename consisting of lowercase English letters, digits, and dots ('.'). Each filename is unique and has a length of at most 100.
  - Last line: `m` distinct integers in ascending order, indicating the indices of files to be deleted.

- **Output**: 
  - If a pattern exists, print "Yes" followed by the pattern on the next line.
  - If no such pattern exists, print "No".
