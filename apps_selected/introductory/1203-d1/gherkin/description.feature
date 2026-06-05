Feature: Maximum Substring Removal for Subsequence Preservation
  As a competitive programmer
  I want to determine the maximum length of a substring that can be removed from a string
  So that a given subsequence is still preserved in the modified string

  Rule: Input and Output Format
    Given a string s and a string t
    - s consists of at least 1 and at most 200 lowercase Latin letters
    - t consists of at least 1 and at most 200 lowercase Latin letters
    - t is guaranteed to be a subsequence of s
    The output should be a single integer representing the maximum length of the substring that can be removed from s while keeping t as a subsequence

  Scenario: Removing maximum substring when t is a prefix of s
    Given s is "bbaba"
    And t is "bb"
    When I calculate the maximum removable substring length
    Then the result should be 3

  Scenario: Removing maximum substring when t is interleaved in s
    Given s is "baaba"
    And t is "ab"
    When I calculate the maximum removable substring length
    Then the result should be 2

  Scenario: No removal possible when s equals t
    Given s is "abcde"
    And t is "abcde"
    When I calculate the maximum removable substring length
    Then the result should be 0

  Scenario: Removing maximum substring with non-contiguous t in s
    Given s is "asdfasdf"
    And t is "fasd"
    When I calculate the maximum removable substring length
    Then the result should be 3

  Scenario: Removing maximum substring when t is at the end of s
    Given s is "abcdefg"
    And t is "efg"
    When I calculate the maximum removable substring length
    Then the result should be 4

  Scenario Outline: Maximum removable substring length for various s and t
    Given s is "<s>"
    And t is "<t>"
    When I calculate the maximum removable substring length
    Then the result should be <result>

    Examples:
      | s         | t    | result |
      | bbaba     | bb   | 3      |
      | baaba     | ab   | 2      |
      | abcde     | abcde| 0      |
      | asdfasdf  | fasd | 3      |
      | abcdefg   | efg  | 4      |
