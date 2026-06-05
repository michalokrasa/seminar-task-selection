Feature: Count reachable numbers from a given number using function f(x)

  As a competitive programmer
  I want to determine how many distinct numbers are reachable from a given number n using the function f(x)
  So that I can solve the problem efficiently and correctly

  Rule: Input and Output format
    - Input: A single integer n (1 ≤ n ≤ 10^9)
    - Output: A single integer representing the number of distinct numbers reachable from n

  Scenario: Reachable numbers from a number with no trailing zeros
    Given the number 7
    When I apply the function f(x) repeatedly
    Then I should get 9 distinct reachable numbers

  Scenario: Reachable numbers from a number with trailing zeros
    Given the number 1098
    When I apply the function f(x) repeatedly
    Then I should get 20 distinct reachable numbers

  Scenario: Reachable numbers from a number that is a power of 10
    Given the number 10
    When I apply the function f(x) repeatedly
    Then I should get 19 distinct reachable numbers

  Scenario: Reachable numbers from a single-digit number
    Given the number 9
    When I apply the function f(x) repeatedly
    Then I should get 9 distinct reachable numbers

  Scenario: Reachable numbers from a large number
    Given the number 1000000000
    When I apply the function f(x) repeatedly
    Then I should get 10 distinct reachable numbers

  Scenario Outline: Reachable numbers from various inputs
    Given the number <input>
    When I apply the function f(x) repeatedly
    Then I should get <output> distinct reachable numbers

    Examples:
      | input       | output |
      | 1098        | 20     |
      | 10          | 19     |
      | 9           | 9      |
      | 10099       | 101    |
