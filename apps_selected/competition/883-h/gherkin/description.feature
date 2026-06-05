Feature: Rearrange and partition string into palindromes

  As a competitive programmer
  I want to rearrange a string and partition it into the minimum number of palindromes of equal length
  So that I can solve the problem efficiently and correctly

  Rule: Input and Output format
    - Input consists of an integer n (1 ≤ n ≤ 400,000) and a string s of length n.
    - Output should be an integer k and k palindromes of equal length.

  Scenario: Simple case with two palindromes
    Given the string "aabaac"
    When I rearrange and partition the string
    Then the minimum number of palindromes is 2
    And the palindromes are "aba" and "aca"

  Scenario: Single palindrome from rearrangement
    Given the string "0rTrT022"
    When I rearrange and partition the string
    Then the minimum number of palindromes is 1
    And the palindrome is "02TrrT20"

  Scenario: Case with distinct characters
    Given the string "aA"
    When I rearrange and partition the string
    Then the minimum number of palindromes is 2
    And the palindromes are "a" and "A"

  Scenario: All characters are the same
    Given the string "aaaa"
    When I rearrange and partition the string
    Then the minimum number of palindromes is 1
    And the palindrome is "aaaa"

  Scenario: Mixed case with digits and letters
    Given the string "1a2b2a1"
    When I rearrange and partition the string
    Then the minimum number of palindromes is 1
    And the palindrome is "1a2b2a1"

  Scenario Outline: Various input cases
    Given the string "<input_string>"
    When I rearrange and partition the string
    Then the minimum number of palindromes is <expected_k>
    And the palindromes are <expected_palindromes>

    Examples:
      | input_string | expected_k | expected_palindromes  |
      | "aabaac"     | 2          | "aba aca"             |
      | "0rTrT022"   | 1          | "02TrrT20"            |
      | "aA"         | 2          | "a A"                 |
      | "aaaa"       | 1          | "aaaa"                |
      | "1a2b2a1"    | 1          | "1a2b2a1"             |
