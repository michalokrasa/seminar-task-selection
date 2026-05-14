# Ants

## Goal

Simulate an ant colony diffusion process on a 2D integer lattice and answer queries about the final ant count at specific junctions.

## Rules

- Initially, `n` ants are all at junction `(0, 0)`.
- Each minute, every junction `(x, y)` that contains **≥ 4 ants** fires simultaneously: exactly 4 ants leave, one going to each of `(x+1, y)`, `(x−1, y)`, `(x, y+1)`, `(x, y−1)`.
- The process repeats until no junction has ≥ 4 ants (guaranteed to terminate for given input range).
- Ants from different junctions do not interact.
- For each query junction, output the number of ants there once the process has stopped.

## Input / Output

- **Input**: first line contains `n` (0 ≤ n ≤ 30 000) and `t` (1 ≤ t ≤ 50 000); each of the next `t` lines contains integers `xi yi` (−10^9 ≤ xi, yi ≤ 10^9).
- **Output**: `t` integers, one per line — the ant count at each queried junction.
