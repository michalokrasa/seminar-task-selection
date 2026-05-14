Feature: Bill and wallet size compatibility check
  As a bill tracker
  I want to check whether all earned bills fit into a given wallet
  So that Polycarp knows if he needs a bigger wallet

  Rule: Input / Output format
    The program reads an integer n from stdin, then n query lines.
    A query "+ x y" adds a bill of size x × y.
    A query "? h w" asks whether every bill so far fits into wallet h × w.
    For each "?" query the program prints "YES" or "NO" to stdout.

  Background:
    Given no bills have been earned yet

  Scenario: A single bill fits into a wallet when rotated
    Given a bill of size 3 × 2 has been earned
    When checking wallet 2 × 3
    Then the result is "YES"

  Scenario: A bill does not fit into a wallet that is too small
    Given a bill of size 3 × 2 has been earned
    When checking wallet 1 × 20
    Then the result is "NO"

  Scenario: Two bills both fit because they can overlap
    Given a bill of size 3 × 2 has been earned
    And a bill of size 2 × 3 has been earned
    When checking wallet 3 × 3
    Then the result is "YES"

  Scenario: A later-added bill makes a previously-passing wallet invalid
    Given a bill of size 3 × 2 has been earned
    And a bill of size 2 × 3 has been earned
    And a bill of size 1 × 5 has been earned
    When checking wallet 1 × 5
    Then the result is "NO"

  Scenario Outline: Full query session
    Given the following queries are processed:
      | query   |
      | + 3 2   |
      | + 2 3   |
      | ? 1 20  |
      | ? 3 3   |
      | ? 2 3   |
      | + 1 5   |
      | ? 10 10 |
      | ? 1 5   |
    Then the answers to "?" queries are:
      | answer |
      | NO     |
      | YES    |
      | YES    |
      | YES    |
      | NO     |

    Examples:
      | ignored |
      | -       |
