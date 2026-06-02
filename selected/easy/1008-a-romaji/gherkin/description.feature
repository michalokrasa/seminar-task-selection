Feature: Berlanese word validation
  As a language learner
  I want to check if a word follows Berlanese phonetic rules
  So that I can write correct Berlanese words

  Rule: Input / Output format
    The program reads a single lowercase Latin string s (1 ≤ |s| ≤ 100) from stdin.
    The program prints "YES" if every consonant except "n" is followed by a vowel, otherwise "NO".

  Background:
    Given the vowels are "a", "o", "u", "i", "e"

  Scenario: Word where every non-n consonant is followed by a vowel
    Given the word is "harakiri"
    When the word is checked for Berlanese validity
    Then the output is "YES"

  Scenario: Word ending with consonant "n" is valid
    Given the word is "man"
    When the word is checked for Berlanese validity
    Then the output is "YES"

  Scenario: Word where "n" precedes a non-vowel is valid
    Given the word is "nbo"
    When the word is checked for Berlanese validity
    Then the output is "YES"

  Scenario: Word where a non-n consonant is not followed by a vowel
    Given the word is "codeforces"
    When the word is checked for Berlanese validity
    Then the output is "NO"

  Scenario: Word ending with a non-n consonant is invalid
    Given the word is "horse"
    When the word is checked for Berlanese validity
    Then the output is "NO"

  Scenario Outline: Various Berlanese validity checks
    Given the word is "<word>"
    When the word is checked for Berlanese validity
    Then the output is "<result>"

    Examples:
      | word      | result |
      | sumimasen | YES    |
      | ninja     | YES    |
      | codeforces| NO     |
      | king      | NO     |
      | nbo       | YES    |
