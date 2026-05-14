Feature: Combination lock minimum number finder
  As a combination lock solver
  I want to find the smallest number reachable by adding and rotating
  So that the lock can be opened

  Rule: Input / Output format
    The program reads an integer n and then a string of n digits from stdin.
    The program prints a string of n digits — the smallest reachable number.

  Rule: Operations
    Button 1 adds 1 to every digit simultaneously (digit 9 wraps to 0).
    Button 2 rotates all digits one position to the right (last digit moves to first).
    Leading zeros are kept in the output (all n digits are always printed).
    The goal is the lexicographically smallest number (ignoring leading zeros for comparison).

  Scenario: Adding shifts all digits to their minimum rotation candidate
    Given the display shows "579"
    When the minimum number is found
    Then the display shows "024"

  Scenario: Rotating reveals a smaller arrangement
    Given the display shows "2014"
    When the minimum number is found
    Then the display shows "0142"

  Scenario: Single digit always becomes 0
    Given the display shows "7"
    When the minimum number is found
    Then the display shows "0"

  Scenario Outline: Minimum display state for various inputs
    Given the display shows "<input>"
    When the minimum number is found
    Then the display shows "<output>"

    Examples:
      | input | output |
      | 579   | 024    |
      | 2014  | 0142   |
      | 0000  | 0000   |
      | 9     | 0      |
