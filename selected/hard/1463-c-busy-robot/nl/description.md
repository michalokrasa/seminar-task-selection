# Busy Robot

## Goal

Count how many movement commands the robot "successfully" fulfils.

## Rules

- The robot starts at position 0 at time 0, moving at speed 1 unit/second along a number line.
- Commands arrive in chronological order; command `i` says "go to point `x_i` at time `t_i`".
- When the robot is **idle** (has reached its current target) and a command arrives, it starts moving toward `x_i`.
- When the robot is **already moving**, any new command is **ignored**.
- Command `i` is **successful** if the robot is at position `x_i` at any time in the interval `[t_i, t_{i+1}]` (with `t_{n+1} = +∞`). An ignored command can still be successful.
- Count the total number of successful commands.

## Input / Output

- **Input**: first line `t` (1 ≤ t ≤ 1000, test cases); each test case starts with `n`, followed by `n` lines of `t_i x_i` in increasing order of `t_i`.
- **Output**: for each test case, a single integer — the count of successful commands.
