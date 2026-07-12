# Game 23 Transformation

## Goal

Determine the minimum number of moves required to transform a number `n` into a number `m` by multiplying by 2 or 3, or determine if it is impossible.

## Rules

- You can multiply the number `n` by 2 or by 3 in each move.
- The transformation must result in exactly `m` starting from `n`.
- If it is impossible to transform `n` to `m` using the allowed operations, return -1.

## Input / Output

- **Input**: A single line containing two integers `n` and `m` where \(1 \leq n \leq m \leq 5 \times 10^8\).
- **Output**: A single integer representing the number of moves required to transform `n` to `m`, or -1 if it is not possible.
