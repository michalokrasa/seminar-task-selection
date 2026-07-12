Feature: Transform number n to m using Game 23 rules

  As a competitive programmer
  I want to determine the number of moves needed to transform a number n to m
  So that I can solve the problem using the rules of multiplying by 2 or 3

  Rule: Input and Output format
    - Input consists of two integers n and m (1 ≤ n ≤ m ≤ 5 * 10^8)
    - Output the number of moves required to transform n to m
    - Output -1 if it is impossible to transform n to m

  Scenario: Transforming n to m with multiple moves
    Given n is 120 and m is 51840
    When I calculate the number of moves
    Then the result should be 7

  Scenario: No transformation needed
    Given n is 42 and m is 42
    When I calculate the number of moves
    Then the result should be 0

  Scenario: Impossible transformation
    Given n is 48 and m is 72
    When I calculate the number of moves
    Then the result should be -1

  Scenario: Large numbers with possible transformation
    Given n is 1 and m is 6
    When I calculate the number of moves
    Then the result should be 2

  Scenario: Large numbers with impossible transformation
    Given n is 5 and m is 100
    When I calculate the number of moves
    Then the result should be -1

  Scenario Outline: Various transformations from n to m
    Given n is <n> and m is <m>
    When I calculate the number of moves
    Then the result should be <result>

    Examples:
      | n   | m    | result |
      | 120 | 51840| 7      |
      | 42  | 42   | 0      |
      | 48  | 72   | -1     |
      | 1   | 6    | 2      |
      | 5   | 100  | -1     |
