Feature: Determine the pairs of keys that could be swapped to fix the keyboard

  As a competitive programmer
  I want to determine which pairs of keys could be swapped to restore the correct order of keys
  So that Santa can type his favorite pattern correctly

  Rule: Input consists of two strings s and t of the same length, containing only lowercase English letters.
        Output should be the number of pairs of keys to swap, followed by the pairs themselves, or -1 if impossible.

  Scenario: No swaps needed
    Given the favorite pattern "hastalavistababy"
    And the typed string "hastalavistababy"
    When determining the swaps
    Then the output should be "0"

  Scenario: Multiple swaps needed
    Given the favorite pattern "helloworld"
    And the typed string "ehoolwlroz"
    When determining the swaps
    Then the output should be "3"
    And the swaps should include "h e"
    And the swaps should include "l o"
    And the swaps should include "d z"

  Scenario: Impossible to fix with swaps
    Given the favorite pattern "merrychristmas"
    And the typed string "christmasmerry"
    When determining the swaps
    Then the output should be "-1"

  Scenario: Single swap needed
    Given the favorite pattern "abc"
    And the typed string "bac"
    When determining the swaps
    Then the output should be "1"
    And the swaps should include "a b"

  Scenario: All characters swapped in pairs
    Given the favorite pattern "abcd"
    And the typed string "badc"
    When determining the swaps
    Then the output should be "2"
    And the swaps should include "a b"
    And the swaps should include "c d"

  Scenario Outline: Various swap scenarios
    Given the favorite pattern "<pattern>"
    And the typed string "<typed>"
    When determining the swaps
    Then the output should be "<output>"

    Examples:
      | pattern         | typed           | output |
      | helloworld      | ehoolwlroz      | 3      |
      | hastalavistababy| hastalavistababy| 0      |
      | merrychristmas  | christmasmerry  | -1     |
      | abc             | bac             | 1      |
