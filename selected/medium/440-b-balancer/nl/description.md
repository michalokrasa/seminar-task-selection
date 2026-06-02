# Balancer

## Goal

Find the minimum number of adjacent moves to equalize the number of matches across all matchboxes.

## Rules

- `n` matchboxes lie in a line, each containing some matches.
- The total number of matches is divisible by `n`; every box must end up with `total / n` matches.
- A single **move** transfers one match from a box to one of its **adjacent** neighbours.
- Minimise the total number of moves.

## Input / Output

- **Input**: first line `n` (1 ≤ n ≤ 50000); second line `n` space-separated non-negative integers (match counts, sum divisible by `n`).
- **Output**: a single integer — the minimum number of moves.
