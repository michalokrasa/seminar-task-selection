Feature: Determine the winner of the dice game between Mishka and Chris
  As a referee
  I want to determine the winner of the dice game
  So that Mishka and Chris know who won or if it's a draw

  Rule: Input and output format
    - The input starts with an integer n (1 ≤ n ≤ 100), the number of rounds.
    - Each of the next n lines contains two integers m_i and c_i (1 ≤ m_i, c_i ≤ 6).
    - Output "Mishka" if Mishka wins more rounds, "Chris" if Chris wins more rounds, or "Friendship is magic!^^" if they win an equal number of rounds.

  Scenario: Mishka wins the game
    Given the number of rounds is 3
    And the rounds are:
      | Mishka | Chris |
      | 3      | 5     |
      | 2      | 1     |
      | 4      | 2     |
    When the game is evaluated
    Then the result should be "Mishka"

  Scenario: The game is a draw
    Given the number of rounds is 2
    And the rounds are:
      | Mishka | Chris |
      | 6      | 1     |
      | 1      | 6     |
    When the game is evaluated
    Then the result should be "Friendship is magic!^^"

  Scenario: Chris wins the game
    Given the number of rounds is 3
    And the rounds are:
      | Mishka | Chris |
      | 1      | 5     |
      | 3      | 3     |
      | 2      | 2     |
    When the game is evaluated
    Then the result should be "Chris"

  Scenario: All rounds are draws
    Given the number of rounds is 3
    And the rounds are:
      | Mishka | Chris |
      | 2      | 2     |
      | 4      | 4     |
      | 6      | 6     |
    When the game is evaluated
    Then the result should be "Friendship is magic!^^"

  Scenario: Mishka wins all rounds
    Given the number of rounds is 4
    And the rounds are:
      | Mishka | Chris |
      | 6      | 5     |
      | 5      | 4     |
      | 4      | 3     |
      | 3      | 2     |
    When the game is evaluated
    Then the result should be "Mishka"

  Scenario Outline: Evaluate different game outcomes
    Given the number of rounds is <rounds>
    And the rounds are:
      | Mishka | Chris |
      | <m1>   | <c1>  |
      | <m2>   | <c2>  |
      | <m3>   | <c3>  |
    When the game is evaluated
    Then the result should be "<result>"

    Examples:
      | rounds | m1 | c1 | m2 | c2 | m3 | c3 | result                  |
      | 3      | 3  | 5  | 2  | 1  | 4  | 2  | Mishka                  |
      | 2      | 6  | 1  | 1  | 6  | 0  | 0  | Friendship is magic!^^  |
      | 3      | 1  | 5  | 3  | 3  | 2  | 2  | Chris                   |
      | 3      | 2  | 2  | 4  | 4  | 6  | 6  | Friendship is magic!^^  |
