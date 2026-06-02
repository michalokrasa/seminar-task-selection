Feature: Asterisk triangle pattern
  As a programmer
  I want to print a triangular asterisk pattern
  So that line i contains exactly i asterisks

  Rule: Input / Output format
    The program reads a single integer n (1 ≤ n ≤ 50) from stdin.
    The program prints n lines, where line i (1-indexed) contains i asterisk characters.

  Scenario: Single row
    Given the input n is 1
    When the pattern is printed
    Then the output is:
      """
      *
      """

  Scenario: Three rows
    Given the input n is 3
    When the pattern is printed
    Then the output is:
      """
      *
      **
      ***
      """

  Scenario: Six rows
    Given the input n is 6
    When the pattern is printed
    Then the output is:
      """
      *
      **
      ***
      ****
      *****
      ******
      """

  Scenario Outline: Various values of n produce the correct number of lines and last-line length
    Given the input n is <n>
    When the pattern is printed
    Then the output has exactly <n> lines
    And the last line contains exactly <n> asterisks

    Examples:
      | n  |
      | 1  |
      | 3  |
      | 6  |
      | 50 |
