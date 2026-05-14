Feature: Vote outcome determination
  As a comment platform
  I want to determine the result of a vote
  So that users know whether a comment is positively or negatively received

  Rule: Input / Output format
    The program reads a single line from stdin containing three integers x, y, z (0 ≤ x, y, z ≤ 100).
    The program prints a single character to stdout: "+" , "-", "0", or "?".

  Scenario: More confirmed upvotes than downvotes with no unknowns yields plus
    Given there are 2 confirmed upvotes
    And there are 0 confirmed downvotes
    And there are 0 unknown votes
    When the vote result is calculated
    Then the outcome is "+"

  Scenario: More confirmed downvotes than upvotes with no unknowns yields minus
    Given there are 3 confirmed upvotes
    And there are 7 confirmed downvotes
    And there are 0 unknown votes
    When the vote result is calculated
    Then the outcome is "-"

  Scenario: Equal confirmed votes with no unknowns yields zero
    Given there are 1 confirmed upvotes
    And there are 1 confirmed downvotes
    And there are 0 unknown votes
    When the vote result is calculated
    Then the outcome is "0"

  Scenario: Unknown votes cannot change the outcome — result is still certain
    Given there are 2 confirmed upvotes
    And there are 0 confirmed downvotes
    And there are 1 unknown votes
    When the vote result is calculated
    Then the outcome is "+"

  Scenario: Unknown votes can swing the result — outcome is uncertain
    Given there are 0 confirmed upvotes
    And there are 0 confirmed downvotes
    And there are 1 unknown votes
    When the vote result is calculated
    Then the outcome is "?"

  Scenario Outline: Vote outcome for various inputs
    Given there are <x> confirmed upvotes
    And there are <y> confirmed downvotes
    And there are <z> unknown votes
    When the vote result is calculated
    Then the outcome is "<result>"

    Examples:
      | x | y | z | result |
      | 3 | 7 | 0 | -      |
      | 2 | 0 | 1 | +      |
      | 1 | 1 | 0 | 0      |
      | 0 | 0 | 1 | ?      |
