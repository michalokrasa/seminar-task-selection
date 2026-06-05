Feature: Determine the winner of the card game between Conan and Agasa
  As a player of the card game
  I want to determine the winner based on the optimal play strategy
  So that I can predict the outcome of the game

  Rule: Input and Output format
    Given the number of cards n (1 ≤ n ≤ 100000)
    And a list of integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 100000) representing the numbers on the cards
    When the game is played optimally
    Then output "Conan" if Conan wins, otherwise output "Agasa"

  Scenario: Conan wins by removing all cards in one move
    Given the number of cards is 3
    And the cards are [4, 5, 7]
    When the game is played
    Then the output should be "Conan"

  Scenario: Agasa wins because cards are identical
    Given the number of cards is 2
    And the cards are [1, 1]
    When the game is played
    Then the output should be "Agasa"

  Scenario: Conan wins with distinct cards
    Given the number of cards is 4
    And the cards are [2, 3, 5, 6]
    When the game is played
    Then the output should be "Conan"

  Scenario: Agasa wins with multiple identical cards
    Given the number of cards is 5
    And the cards are [3, 3, 3, 3, 3]
    When the game is played
    Then the output should be "Agasa"

  Scenario: Conan wins with a single card
    Given the number of cards is 1
    And the cards are [10]
    When the game is played
    Then the output should be "Conan"

  Scenario Outline: Determine winner based on card configuration
    Given the number of cards is <n>
    And the cards are <cards>
    When the game is played
    Then the output should be <winner>

    Examples:
      | n | cards       | winner |
      | 3 | [4, 5, 7]   | Conan  |
      | 2 | [1, 1]      | Agasa  |
      | 4 | [2, 3, 5, 6]| Conan  |
      | 5 | [3, 3, 3, 3, 3] | Agasa |
