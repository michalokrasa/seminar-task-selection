Feature: Excessive electric shock counter
  As a letter deduction tracker
  I want to count shocks received after the secret letter became uniquely determined
  So that Valentin knows how many shocks he could have avoided

  Rule: Input / Output format
    The program reads n from stdin, then n action lines.
    Each action is ". word" (no shock), "! word" (shocked), or "? letter" (guess).
    The program prints a single integer — the number of excessive shocks.

  Rule: Shock types
    A ". word" action means the secret letter is NOT in that word — eliminates those letters as candidates.
    A "! word" action means the secret letter IS in that word — keeps only letters in that word as candidates.
    A "? letter" action is an incorrect guess (except the last one which is correct) — eliminates that letter.
    A shock is "excessive" if it occurs (from "!" or incorrect "?") after the candidate set has size 1.

  Scenario: Letter uniquely determined after two actions, one excessive shock follows
    Given the actions are:
      | action |
      | ! abc  |
      | . ad   |
      | . b    |
      | ! cd   |
      | ? c    |
    When excessive shocks are counted
    Then the count is 1

  Scenario: No excessive shocks when letter is only determined at the final guess
    Given the actions are:
      | action         |
      | ! ababahalamaha |
      | ? a            |
      | ? b            |
      | ? a            |
      | ? b            |
      | ? a            |
      | ? h            |
    When excessive shocks are counted
    Then the count is 0

  Scenario Outline: Excessive shock count for various action sequences
    Given the number of actions is <n> and the sequence leads to <count> excessive shocks
    When excessive shocks are counted
    Then the count is <count>

    Examples:
      | n | count |
      | 5 | 1     |
      | 8 | 2     |
      | 7 | 0     |
