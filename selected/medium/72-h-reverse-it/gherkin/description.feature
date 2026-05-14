Feature: Integer reversal
  As a number reverser
  I want to reverse the digits of an integer
  So that Hormizd's tester can verify GNU's program

  Rule: Input / Output format
    The program reads a single integer from stdin (may have leading zeros or a negative sign).
    The program prints the reversed integer to stdout with no leading zeros.

  Rule: Sign and leading zeros
    If the number is negative, the reversed result is also negative.
    Leading zeros in the input are stripped before reversing.
    Leading zeros produced by reversal are stripped from the output.

  Scenario: Positive number with no leading zeros reverses normally
    Given the input is "23"
    When the number is reversed
    Then the output is "32"

  Scenario: Negative number reverses its digits and keeps the minus sign
    Given the input is "-032"
    When the number is reversed
    Then the output is "-23"

  Scenario: Input with leading zeros strips them before reversing
    Given the input is "01234560"
    When the number is reversed
    Then the output is "654321"

  Scenario: Trailing zeros in input become leading zeros and are stripped
    Given the input is "100"
    When the number is reversed
    Then the output is "1"

  Scenario Outline: Reversal for various inputs
    Given the input is "<input>"
    When the number is reversed
    Then the output is "<output>"

    Examples:
      | input    | output  |
      | 23       | 32      |
      | -032     | -23     |
      | 01234560 | 654321  |
      | 100      | 1       |
      | -0010    | -1      |
