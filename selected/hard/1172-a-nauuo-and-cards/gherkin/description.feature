Feature: Minimum card operations to sort the pile
  As Nauuo
  I want to arrange numbered cards into sorted order in the pile
  So that I minimise the total number of draw-and-play operations

  Rule: Input / Output format
    The program reads n, then two lines of n integers each (hand and pile). 0 represents an empty card.
    The program prints a single integer — the minimum number of operations.

  Background:
    Given each numbered card 1..n appears exactly once across hand and pile

  Scenario: Pile has a correct prefix — only a few operations needed
    Given n is 3
    And the hand contains [0, 2, 0]
    And the pile contains [3, 0, 1]
    When the minimum operations are computed
    Then the output is 2

  Scenario: Pile must be rebuilt because first card is out of place
    Given n is 3
    And the hand contains [0, 2, 0]
    And the pile contains [1, 0, 3]
    When the minimum operations are computed
    Then the output is 4

  Scenario Outline: Various card arrangements
    Given n is <n>
    And the hand contains <hand>
    And the pile contains <pile>
    When the minimum operations are computed
    Then the output is <ops>

    Examples:
      | n  | hand                   | pile                    | ops |
      | 3  | 0 2 0                  | 3 0 1                   | 2   |
      | 3  | 0 2 0                  | 1 0 3                   | 4   |
      | 11 | 0 0 0 5 0 0 0 4 0 0 11 | 9 2 6 0 8 1 7 0 3 0 10  | 18  |
