Feature: Validate Kostya's Obfuscation

  As a competitive programmer
  I want to determine if a given string can be the result of Kostya's obfuscation
  So that I can verify the correctness of the obfuscation process

  Rule: Input and Output Format
    - Input is a single string S of lowercase English letters (1 ≤ |S| ≤ 500).
    - Output "YES" if the string can be a result of Kostya's obfuscation, otherwise "NO".

  Scenario: Simple valid obfuscation
    Given the input string "abacaba"
    When I check if it can be a result of Kostya's obfuscation
    Then the output should be "YES"

  Scenario: Simple invalid obfuscation
    Given the input string "jinotega"
    When I check if it can be a result of Kostya's obfuscation
    Then the output should be "NO"

  Scenario: Single character string
    Given the input string "a"
    When I check if it can be a result of Kostya's obfuscation
    Then the output should be "YES"

  Scenario: All unique characters in sequence
    Given the input string "abcdefghijklmnopqrstuvwxyz"
    When I check if it can be a result of Kostya's obfuscation
    Then the output should be "YES"

  Scenario: Repeated characters in non-sequential order
    Given the input string "aabbcc"
    When I check if it can be a result of Kostya's obfuscation
    Then the output should be "YES"

  Scenario Outline: Various input strings
    Given the input string "<input_string>"
    When I check if it can be a result of Kostya's obfuscation
    Then the output should be "<expected_output>"

    Examples:
      | input_string       | expected_output |
      | abacaba            | YES             |
      | jinotega           | NO              |
      | a                  | YES             |
      | abcdefghijklmnopqrstuvwxyz | YES     |
      | aabbcc             | YES             |
