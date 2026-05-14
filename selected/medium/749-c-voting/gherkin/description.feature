Feature: Voting outcome simulation
  As a vote predictor
  I want to simulate the optimal voting strategy for both factions
  So that the winning fraction can be determined

  Rule: Input / Output format
    The program reads n from stdin, then a string of n characters ('D' or 'R').
    The program prints a single character: 'D' or 'R'.

  Rule: Voting procedure
    Employees vote in order 1..n, repeating rounds until only one eligible voter remains.
    Each voter optimally eliminates one opponent (any opponent — even one who has already voted).
    The last remaining voter's fraction wins.

  Scenario: All depublicans win trivially
    Given the voter sequence is "DD"
    When the vote is simulated
    Then the winner is "D"

  Scenario: Depublicans win with majority and optimal play
    Given the voter sequence is "DDRRR"
    When the vote is simulated
    Then the winner is "D"

  Scenario: Remocrats win when they have more voters
    Given the voter sequence is "DDRRRR"
    When the vote is simulated
    Then the winner is "R"

  Scenario: Single voter wins immediately
    Given the voter sequence is "R"
    When the vote is simulated
    Then the winner is "R"

  Scenario Outline: Voting outcome for various sequences
    Given the voter sequence is "<sequence>"
    When the vote is simulated
    Then the winner is "<winner>"

    Examples:
      | sequence | winner |
      | DDRRR    | D      |
      | DDRRRR   | R      |
      | D        | D      |
      | R        | R      |
      | DRDR     | D      |
