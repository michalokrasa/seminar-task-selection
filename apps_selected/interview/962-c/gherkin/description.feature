Feature: Determine the minimum number of deletions to make a number a perfect square

  As a competitive programmer
  I want to determine the minimum number of deletions needed to transform a given integer into a perfect square
  So that I can solve the problem efficiently and correctly

  Rule: Input and Output format
    - The input is a single integer n (1 ≤ n ≤ 2 * 10^9) without leading zeroes.
    - The output is the minimal number of deletions required to make n a perfect square, or -1 if impossible.

  Scenario: Number is already a perfect square
    Given the number 625
    When I determine the minimum deletions
    Then the result should be 0

  Scenario: Number can be transformed into a perfect square by deleting some digits
    Given the number 8314
    When I determine the minimum deletions
    Then the result should be 2

  Scenario: Number cannot be transformed into a perfect square
    Given the number 333
    When I determine the minimum deletions
    Then the result should be -1

  Scenario: Single digit number that is a perfect square
    Given the number 4
    When I determine the minimum deletions
    Then the result should be 0

  Scenario: Large number that cannot be transformed into a perfect square
    Given the number 987654321
    When I determine the minimum deletions
    Then the result should be -1

  Scenario Outline: Transforming numbers into perfect squares
    Given the number <number>
    When I determine the minimum deletions
    Then the result should be <result>

    Examples:
      | number | result |
      | 144    | 0      |
      | 100    | 0      |
      | 123456 | -1     |
      | 49     | 0      |
