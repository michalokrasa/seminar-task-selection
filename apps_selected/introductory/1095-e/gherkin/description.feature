Feature: Determine positions to change for a regular bracket sequence

  As a competitive programmer
  I want to determine the number of positions in a bracket sequence that can be changed to make it regular
  So that I can solve the problem of transforming a bracket sequence into a regular one

  Rule: Input and Output format
    - The input consists of an integer n and a string s of length n.
    - The output is a single integer representing the number of positions that can be changed to make the sequence regular.

  Scenario: Simple unbalanced sequence
    Given the bracket sequence "(((()"
    When I calculate the number of changeable positions
    Then the result should be 3

  Scenario: Already regular sequence
    Given the bracket sequence "()()()"
    When I calculate the number of changeable positions
    Then the result should be 0

  Scenario: Single bracket
    Given the bracket sequence ")"
    When I calculate the number of changeable positions
    Then the result should be 0

  Scenario: Complex unbalanced sequence
    Given the bracket sequence ")))(((((("
    When I calculate the number of changeable positions
    Then the result should be 0

  Scenario: Balanced but incorrect sequence
    Given the bracket sequence "(()))("
    When I calculate the number of changeable positions
    Then the result should be 2

  Scenario Outline: Various bracket sequences
    Given the bracket sequence "<sequence>"
    When I calculate the number of changeable positions
    Then the result should be <result>

    Examples:
      | sequence   | result |
      | "(((()"    | 3      |
      | "()()()"   | 0      |
      | ")"        | 0      |
      | ")))((((((" | 0      |
      | "(()))("   | 2      |
