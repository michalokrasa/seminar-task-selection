Feature: Equalize matchboxes with minimum adjacent moves
  As a puzzle solver
  I want to redistribute matches between adjacent boxes
  So that every box holds the same count using as few moves as possible

  Rule: Input / Output format
    The program reads n from stdin, then n non-negative integers on the next line.
    The total is guaranteed to be divisible by n.
    The program prints a single integer — the minimum number of moves.

  Scenario: Already balanced — zero moves needed
    Given n is 3 and the boxes contain [2, 2, 2]
    When the minimum moves are calculated
    Then the output is 0

  Scenario: Two boxes need one transfer
    Given n is 2 and the boxes contain [1, 3]
    When the minimum moves are calculated
    Then the output is 1

  Scenario: Sample from problem statement
    Given n is 6 and the boxes contain [1, 6, 2, 5, 3, 7]
    When the minimum moves are calculated
    Then the output is 12

  Scenario: All matches in last box — must pass through every adjacent pair
    Given n is 4 and the boxes contain [0, 0, 0, 4]
    When the minimum moves are calculated
    Then the output is 6

  Scenario Outline: Various configurations
    Given n is <n> and the boxes contain <boxes>
    When the minimum moves are calculated
    Then the output is <moves>

    Examples:
      | n | boxes       | moves |
      | 6 | 1 6 2 5 3 7 | 12    |
      | 2 | 1 3         | 1     |
      | 3 | 2 2 2       | 0     |
      | 4 | 0 0 0 4     | 6     |
