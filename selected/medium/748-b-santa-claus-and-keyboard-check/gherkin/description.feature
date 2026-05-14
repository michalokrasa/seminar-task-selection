Feature: Keyboard key swap detection
  As a keyboard repair assistant
  I want to identify which pairs of keys were swapped
  So that Santa can restore his keyboard to the correct layout

  Rule: Input / Output format
    The program reads two strings s and t from stdin (same length, lowercase letters only).
    If a valid swap set exists, the program prints k (number of swaps) then k lines each with two letters.
    If no valid swap set exists, the program prints -1.

  Scenario: No keys are swapped — strings are identical
    Given the intended pattern is "hastalavistababy"
    And the typed string is "hastalavistababy"
    When the swap pairs are determined
    Then the number of swaps is 0

  Scenario: Three pairs of keys were swapped
    Given the intended pattern is "helloworld"
    And the typed string is "ehoolwlroz"
    When the swap pairs are determined
    Then the number of swaps is 3
    And the swap pairs include "h e"
    And the swap pairs include "l o"
    And the swap pairs include "d z"

  Scenario: No consistent swap mapping exists
    Given the intended pattern is "merrychristmas"
    And the typed string is "christmasmerry"
    When the swap pairs are determined
    Then the result is -1

  Scenario: A letter maps to two different letters — no solution
    Given the intended pattern is "ab"
    And the typed string is "ba"
    When the swap pairs are determined
    Then the number of swaps is 1

  Scenario Outline: Swap detection for various inputs
    Given the intended pattern is "<s>"
    And the typed string is "<t>"
    When the swap pairs are determined
    Then the result is "<result>"

    Examples:
      | s                | t                | result |
      | helloworld       | ehoolwlroz       | 3      |
      | hastalavistababy | hastalavistababy | 0      |
      | merrychristmas   | christmasmerry   | -1     |
