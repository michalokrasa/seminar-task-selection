Feature: Strange sort feasibility check
  As a sequence sorter
  I want to determine if a sequence can be sorted using adjacent swaps in pairs
  So that AquaMoon knows whether the desired ordering is achievable

  Rule: Input / Output format
    The program reads t test cases from stdin.
    Each test case has n on the first line, then n integers on the second line.
    For each test case the program prints "YES" or "NO" to stdout.

  Scenario: Already sorted sequence is always achievable
    Given the sequence is 1 2 3 4
    When the feasibility is checked
    Then the result is "YES"

  Scenario: Sequence sortable by swapping even-indexed pairs
    Given the sequence is 4 3 2 5
    When the feasibility is checked
    Then the result is "YES"

  Scenario: Sequence with equal elements at even positions is sortable
    Given the sequence is 3 3 2 2
    When the feasibility is checked
    Then the result is "YES"

  Scenario: Sequence requiring an odd number of swaps is not achievable
    Given the sequence is 1 2 3 5 4
    When the feasibility is checked
    Then the result is "NO"

  Scenario Outline: Feasibility check for various sequences
    Given the sequence is <sequence>
    When the feasibility is checked
    Then the result is "<result>"

    Examples:
      | sequence  | result |
      | 4 3 2 5   | YES    |
      | 3 3 2 2   | YES    |
      | 1 2 3 5 4 | NO     |
