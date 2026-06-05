# Statue Rearrangement on Islands

## Goal

Determine if it is possible to rearrange statues on a cycle of islands to match a desired order using adjacent moves.

## Rules

- Islands are connected in a cycle, allowing movement between adjacent islands.
- Each island has a pedestal, and all but one island initially have a statue.
- Statues can be moved to an adjacent island with an empty pedestal.
- The goal is to rearrange the statues to match a specified desired order.

## Input / Output

- **Input**: 
  - An integer `n` (2 ≤ n ≤ 200,000) representing the number of islands.
  - A list of `n` integers `a_i` (0 ≤ a_i ≤ n - 1) where `a_i = 0` indicates an empty pedestal.
  - A list of `n` integers `b_i` (0 ≤ b_i ≤ n - 1) where `b_i = 0` indicates the desired empty pedestal.
- **Output**: 
  - Print "YES" if the statues can be rearranged to match the desired order, otherwise print "NO".
