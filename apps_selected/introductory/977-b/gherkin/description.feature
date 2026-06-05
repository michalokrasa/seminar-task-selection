Feature: Find the most frequent two-gram in a string

  As a competitive programmer
  I want to determine the most frequently occurring two-gram in a given string
  So that I can solve the problem efficiently and correctly

  Rule: Input and Output format
    - The input consists of an integer n (2 ≤ n ≤ 100) followed by a string s of length n.
    - The output should be a two-gram (a string of two consecutive characters) that appears most frequently in s.

  Scenario: Simple case with distinct two-grams
    Given the input:
      """
      7
      ABACABA
      """
    When the program is executed
    Then the output should be "AB"

  Scenario: Case with overlapping two-grams
    Given the input:
      """
      5
      ZZZAA
      """
    When the program is executed
    Then the output should be "ZZ"

  Scenario: Case with multiple valid answers
    Given the input:
      """
      6
      AABBCC
      """
    When the program is executed
    Then the output should be "AA" or "BB" or "CC"

  Scenario: Case with all identical characters
    Given the input:
      """
      4
      AAAA
      """
    When the program is executed
    Then the output should be "AA"

  Scenario: Case with minimum length string
    Given the input:
      """
      2
      XY
      """
    When the program is executed
    Then the output should be "XY"

  Scenario Outline: Various input cases
    Given the input:
      """
      <n>
      <string>
      """
    When the program is executed
    Then the output should be "<two-gram>"

    Examples:
      | n  | string  | two-gram |
      | 7  | ABACABA | AB       |
      | 5  | ZZZAA   | ZZ       |
      | 6  | AABBCC  | AA       |
      | 4  | AAAA    | AA       |
      | 2  | XY      | XY       |
