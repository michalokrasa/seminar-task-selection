Feature: Mishka's Problem Solving

  As a competitive programmer
  I want to determine the maximum number of problems Mishka can solve
  So that I can understand Mishka's problem-solving capability based on his skill level

  Rule: Input and Output Format
    - Input consists of two integers n and k, followed by a list of n integers representing problem difficulties.
    - Output is a single integer representing the maximum number of problems Mishka can solve.

  Scenario: Mishka solves problems from both ends
    Given n is 8 and k is 4
    And the problem difficulties are [4, 2, 3, 1, 5, 1, 6, 4]
    When Mishka solves problems
    Then the maximum number of problems he can solve is 5

  Scenario: Mishka cannot solve any problem
    Given n is 5 and k is 2
    And the problem difficulties are [3, 1, 2, 1, 3]
    When Mishka solves problems
    Then the maximum number of problems he can solve is 0

  Scenario: Mishka solves all problems
    Given n is 5 and k is 100
    And the problem difficulties are [12, 34, 55, 43, 21]
    When Mishka solves problems
    Then the maximum number of problems he can solve is 5

  Scenario: Mishka solves problems from one end only
    Given n is 6 and k is 3
    And the problem difficulties are [1, 2, 3, 4, 5, 6]
    When Mishka solves problems
    Then the maximum number of problems he can solve is 3

  Scenario: Mishka solves problems with mixed difficulties
    Given n is 7 and k is 5
    And the problem difficulties are [5, 4, 6, 3, 2, 7, 1]
    When Mishka solves problems
    Then the maximum number of problems he can solve is 4

  Scenario Outline: Mishka's problem-solving scenarios
    Given n is <n> and k is <k>
    And the problem difficulties are <difficulties>
    When Mishka solves problems
    Then the maximum number of problems he can solve is <solved>

    Examples:
      | n | k  | difficulties               | solved |
      | 8 | 4  | [4, 2, 3, 1, 5, 1, 6, 4]   | 5      |
      | 5 | 2  | [3, 1, 2, 1, 3]            | 0      |
      | 5 | 100| [12, 34, 55, 43, 21]       | 5      |
      | 6 | 3  | [1, 2, 3, 4, 5, 6]         | 3      |
