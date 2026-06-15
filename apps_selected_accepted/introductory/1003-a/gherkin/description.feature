Feature: Distribute coins into pockets

  As a competitive programmer
  I want to determine the minimum number of pockets needed
  So that no two coins with the same value are in the same pocket

  Rule: Input and Output format
    - Input consists of an integer n (1 ≤ n ≤ 100) representing the number of coins.
    - Followed by n integers a_i (1 ≤ a_i ≤ 100) representing the values of the coins.
    - Output a single integer representing the minimum number of pockets required.

  Scenario: Single coin
    Given the number of coins is 1
    And the coin values are "100"
    When I calculate the minimum number of pockets
    Then the result should be 1

  Scenario: All coins have unique values
    Given the number of coins is 4
    And the coin values are "1 2 3 4"
    When I calculate the minimum number of pockets
    Then the result should be 1

  Scenario: Multiple coins with the same value
    Given the number of coins is 6
    And the coin values are "1 2 4 3 3 2"
    When I calculate the minimum number of pockets
    Then the result should be 2

  Scenario: All coins have the same value
    Given the number of coins is 5
    And the coin values are "7 7 7 7 7"
    When I calculate the minimum number of pockets
    Then the result should be 5

  Scenario: Two different values with multiple occurrences
    Given the number of coins is 8
    And the coin values are "5 5 5 6 6 6 6 5"
    When I calculate the minimum number of pockets
    Then the result should be 4

  Scenario Outline: Various distributions of coin values
    Given the number of coins is <n>
    And the coin values are "<coin_values>"
    When I calculate the minimum number of pockets
    Then the result should be <pockets>

    Examples:
      | n | coin_values       | pockets |
      | 6 | "1 2 4 3 3 2"     | 2       |
      | 1 | "100"             | 1       |
      | 3 | "10 10 10"        | 3       |
      | 5 | "1 2 2 3 3"       | 2       |
