# Voting

## Goal

Simulate an optimal voting process between two factions (depublicans `D` and remocrats `R`) and determine which faction wins.

## Rules

- Employees vote in order from 1 to n, then the round repeats; employees who have been eliminated are skipped.
- Each eligible employee optimally removes one opponent (any opponent from the other fraction, in any position) to maximise their fraction's chance of winning.
- The process ends when only one eligible voter remains; that voter's fraction wins.
- Optimal strategy: each voter eliminates the nearest upcoming opponent who would otherwise eliminate them first.

## Input / Output

- **Input**: first line is `n` (1 ≤ n ≤ 200 000); second line is a string of `n` characters, each `D` or `R`.
- **Output**: `D` if depublicans win, `R` if remocrats win.
