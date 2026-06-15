Feature: Minimize the sum of numbers on remaining cards

  As a player,
  I want to discard cards with the same number
  So that I can minimize the sum of numbers on the remaining cards.

  Rule: Input and Output format
    Given five integers representing the numbers on the cards.
    The output should be the minimum possible sum of numbers on the remaining cards after discarding at most two or three cards with the same number.

  Scenario: Discard two cards with the same number
    Given the cards 7, 3, 7, 3, 20
    When I discard two cards with the number 7
    Then the minimum sum of remaining cards should be 26

  Scenario: No cards to discard
    Given the cards 7, 9, 3, 1, 8
    When I cannot discard any cards
    Then the minimum sum of remaining cards should be 28

  Scenario: Discard three cards with the same number
    Given the cards 10, 10, 10, 10, 10
    When I discard three cards with the number 10
    Then the minimum sum of remaining cards should be 20

  Scenario: Discard two cards with a different number
    Given the cards 5, 5, 5, 2, 2
    When I discard two cards with the number 5
    Then the minimum sum of remaining cards should be 9

  Scenario: Discard three cards with a different number
    Given the cards 4, 4, 4, 6, 6
    When I discard three cards with the number 4
    Then the minimum sum of remaining cards should be 12

  Scenario Outline: Calculate minimum sum for various card combinations
    Given the cards <t1>, <t2>, <t3>, <t4>, <t5>
    When I calculate the minimum sum after discarding
    Then the minimum sum of remaining cards should be <result>

    Examples:
      | t1 | t2 | t3 | t4 | t5 | result |
      | 7  | 3  | 7  | 3  | 20 | 26     |
      | 7  | 9  | 3  | 1  | 8  | 28     |
      | 10 | 10 | 10 | 10 | 10 | 20     |
      | 5  | 5  | 5  | 2  | 2  | 9      |
      | 4  | 4  | 4  | 6  | 6  | 12     |
