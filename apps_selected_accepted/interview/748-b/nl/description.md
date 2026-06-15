# Keyboard Key Swap

## Goal

Determine if it's possible to swap pairs of keys on a keyboard to transform a mistyped string into a favorite pattern string. If possible, list the pairs of keys to swap.

## Rules

- Each key can either be in its correct position or swapped with exactly one other key.
- Each key can be involved in at most one swap.
- If it's impossible to achieve the transformation with swaps, return `-1`.

## Input / Output

- **Input**: Two strings `s` and `t` of equal length (up to 1000 characters), consisting only of lowercase English letters.
- **Output**: If transformation is impossible, output `-1`. Otherwise, output the number of swaps `k` followed by `k` lines of two space-separated letters representing the keys to swap. Each letter must appear in at most one swap.
