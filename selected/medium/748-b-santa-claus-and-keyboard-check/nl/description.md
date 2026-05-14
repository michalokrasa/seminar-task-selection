# Santa Claus and Keyboard Check

## Goal

Given Santa's intended pattern `s` and the string `t` he actually typed, determine which pairs of keys were swapped on the keyboard, or report that no consistent swap set exists.

## Rules

- Each key is either in its correct position or swapped with exactly one other key; no key appears in more than one swap pair.
- For every position `i`, the mapping `s[i] → t[i]` must be consistent: the same character in `s` always maps to the same character in `t` and vice versa.
- A character may map to itself (key is in the correct place).
- If `s[i] → t[i]` but also `s[j] → t[k]` where `t[i] = s[j]` but `t[j] ≠ s[i]`, there is a contradiction → print `-1`.
- If a consistent bijective mapping exists, print the number of swapped pairs `k`, then `k` lines each containing the two letters in the pair.

## Input / Output

- **Input**: two strings `s` and `t` on separate lines (length 1–1000, lowercase letters).
- **Output**: `-1` if impossible; otherwise `k` followed by `k` lines of swap pairs.
