Feature: Football championship score finder
  As a championship analyst
  I want to find the minimum winning score for BERLAND in its final game
  So that BERLAND advances to the next stage

  Rule: Input / Output format
    The program reads 5 lines from stdin, each describing a completed game as "team1 team2 goals1:goals2".
    The program prints "X:Y" (minimum winning score for BERLAND) or "IMPOSSIBLE".

  Rule: Ranking criteria (in order)
    1. Total points (win=3, draw=1, loss=0) — higher is better.
    2. Goal difference (scored minus conceded) — higher is better.
    3. Total goals scored — higher is better.
    4. Team name in lexicographical order — smaller name ranks higher.
    BERLAND must finish 1st or 2nd in the group after its final game (a win, X > Y).
    Among valid scores, choose the one with smallest X−Y; break ties by smallest Y.

  Scenario: BERLAND needs a large margin to overcome a goal deficit
    Given the completed games are:
      | game                    |
      | AERLAND DERLAND 2:1     |
      | DERLAND CERLAND 0:3     |
      | CERLAND AERLAND 0:1     |
      | AERLAND BERLAND 2:0     |
      | DERLAND BERLAND 4:0     |
    When the minimum winning score is found
    Then the output is "6:0"

  Scenario: BERLAND cannot reach top-2 regardless of score
    Given the completed games are:
      | game                    |
      | AERLAND DERLAND 2:2     |
      | DERLAND CERLAND 2:3     |
      | CERLAND AERLAND 1:3     |
      | AERLAND BERLAND 2:1     |
      | DERLAND BERLAND 4:1     |
    When the minimum winning score is found
    Then the output is "IMPOSSIBLE"

  Scenario Outline: Championship outcome for various game results
    Given the five completed game results lead to <outcome>
    When the minimum winning score is found
    Then the output is "<outcome>"

    Examples:
      | outcome     |
      | 6:0         |
      | IMPOSSIBLE  |
