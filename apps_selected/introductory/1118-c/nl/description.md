# Palindromic Matrix

## Goal

Determine if it's possible to arrange given integers into a square matrix that is palindromic, and if so, provide one such arrangement.

## Rules

- A matrix is palindromic if it remains unchanged when rows and columns are reversed.
- Use each integer exactly once in the matrix.
- If multiple solutions exist, any valid solution is acceptable.

## Input / Output

- **Input**: 
  - An integer `n` (1 ≤ n ≤ 20), the size of the matrix.
  - A list of `n^2` integers (1 ≤ each integer ≤ 1000) to fill the matrix.
- **Output**: 
  - Print "YES" followed by the `n x n` matrix if a palindromic arrangement is possible.
  - Print "NO" if no such arrangement can be made.
