Feature: Validate string formation from 'a', 'b', and 'c'

  As a competitive programmer
  I want to verify if a given string can be formed by appending 'b's and 'c's to 'a's
  So that I can determine if the string meets the problem's conditions

  Rule: Input and Output format
    - The input is a single string S consisting of only 'a', 'b', and 'c'.
    - The output is "YES" if the string can be formed according to the rules, otherwise "NO".

  Scenario: Valid string with equal 'a' and 'c'
    Given the string "aaabccc"
    When I check the string formation
    Then the result should be "YES"

  Scenario: Invalid string due to incorrect order
    Given the string "bbacc"
    When I check the string formation
    Then the result should be "NO"

  Scenario: Valid string with equal 'b' and 'c'
    Given the string "aabc"
    When I check the string formation
    Then the result should be "YES"

  Scenario: Invalid string with missing 'a'
    Given the string "bcc"
    When I check the string formation
    Then the result should be "NO"

  Scenario: Valid string with equal 'a', 'b', and 'c'
    Given the string "abc"
    When I check the string formation
    Then the result should be "YES"

  Scenario Outline: Check various string formations
    Given the string "<input>"
    When I check the string formation
    Then the result should be "<output>"

    Examples:
      | input    | output |
      | aaabccc  | YES    |
      | bbacc    | NO     |
      | aabc     | YES    |
      | abc      | YES    |
      | aabbcc   | YES    |
