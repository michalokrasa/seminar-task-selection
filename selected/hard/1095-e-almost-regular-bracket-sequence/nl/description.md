# Almost Regular Bracket Sequence

## Goal

Count the number of positions in a bracket sequence such that flipping the bracket at that position (changing `(` to `)` or vice versa) makes the entire sequence a **regular** bracket sequence.

## Rules

- A **regular** bracket sequence has equal numbers of `(` and `)`, and every prefix has at least as many `(` as `)`.
- For the result to be non-zero, `n` must be even; if `n` is odd, the answer is always `0`.
- After a flip at position `i`, check whether the new sequence is regular.
- Flipping `(` to `)` decreases the total `(` count by 1 and increases `)` by 1 (net balance change: −2).
- Flipping `)` to `(` increases `(` by 1 and decreases `)` by 1 (net balance change: +2).
- Use prefix-sum arrays to efficiently check validity for each candidate position.

## Input / Output

- **Input**: first line is `n` (1 ≤ n ≤ 10^6); second line is a string of `n` brackets.
- **Output**: a single integer — the number of positions where a flip yields a regular sequence.
