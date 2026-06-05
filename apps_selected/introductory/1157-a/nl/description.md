# Reachable Numbers

## Goal

Determine how many distinct numbers can be reached from a given number `n` by repeatedly applying a specific transformation function.

## Rules

- Define a function `f(x)`:
  - Increment `x` by 1.
  - Remove all trailing zeros from the result.
- A number `y` is considered reachable from `n` if `y` can be obtained by applying `f` to `n` zero or more times.
- The task is to count all distinct numbers that can be reached from `n` using the function `f`.

## Input / Output

- **Input**: A single integer `n` where \(1 \leq n \leq 10^9\).
- **Output**: A single integer representing the number of distinct numbers reachable from `n`.
