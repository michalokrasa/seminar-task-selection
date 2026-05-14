Feature: Shortest unique phone number substring finder
  As a phone book search engine
  I want to find the shortest digit sequence that uniquely identifies each contact
  So that Polycarp can look up any contact with the fewest keystrokes

  Rule: Input / Output format
    The program reads n from stdin, then n 9-digit phone numbers (one per line).
    The program prints n lines, each containing the shortest unique identifying substring for the corresponding number.

  Rule: Uniqueness
    A sequence uniquely identifies a number if it is a substring of that number
    and is NOT a substring of any other number in the contacts.
    If multiple shortest sequences exist, any one may be printed.

  Scenario: All numbers share no common substrings — single digit suffices
    Given the contacts are:
      | number    |
      | 123456789 |
      | 100000000 |
      | 100123456 |
    When the shortest unique substrings are found
    Then the result for 123456789 is "9"
    And the result for 100000000 is "000"
    And the result for 100123456 is "01"

  Scenario: Two numbers share many digits — longer substring needed
    Given the contacts are:
      | number    |
      | 123456789 |
      | 193456789 |
      | 134567819 |
      | 934567891 |
    When the shortest unique substrings are found
    Then the result for 123456789 has length 2
    And the result for 193456789 has length 3
    And the result for 134567819 has length 2
    And the result for 934567891 has length 2

  Scenario Outline: Unique substring lengths for a small contact list
    Given the contacts are <numbers>
    When the shortest unique substrings are found
    Then each result uniquely identifies its number

    Examples:
      | numbers                               |
      | 123456789, 100000000, 100123456       |
      | 123456789, 193456789, 134567819, 934567891 |
