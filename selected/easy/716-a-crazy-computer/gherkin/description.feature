Feature: Crazy computer word retention
  As a user typing on a crazy computer
  I want to know how many words remain on the screen
  So that I can track what has not been erased by the timeout

  Rule: Input / Output format
    The program reads from stdin: first line contains integers n and c; second line contains n space-separated timestamps.
    The program prints a single integer to stdout — the number of words remaining on screen.

  Background:
    Given the screen starts empty

  Scenario: Words typed within the timeout window all stay on screen
    Given the timeout is 5 seconds
    And words are typed at seconds 1, 3
    When the user finishes typing
    Then 2 words remain on the screen

  Scenario: A gap larger than the timeout clears the screen
    Given the timeout is 5 seconds
    And words are typed at seconds 1, 7
    When the user finishes typing
    Then 1 word remains on the screen

  Scenario: Only the last unbroken streak is visible
    Given the timeout is 5 seconds
    And words are typed at seconds 1, 3, 8, 14, 19, 20
    When the user finishes typing
    Then 3 words remain on the screen

  Scenario: Every word except the last is separated by more than the timeout
    Given the timeout is 1 second
    And words are typed at seconds 1, 3, 5, 7, 9, 10
    When the user finishes typing
    Then 2 words remain on the screen

  Scenario Outline: Word retention for various timeout and timestamp sequences
    Given the timeout is <c> seconds
    And words are typed at seconds <timestamps>
    When the user finishes typing
    Then <remaining> words remain on the screen

    Examples:
      | c | timestamps              | remaining |
      | 5 | 1, 3, 8, 14, 19, 20    | 3         |
      | 1 | 1, 3, 5, 7, 9, 10      | 2         |
