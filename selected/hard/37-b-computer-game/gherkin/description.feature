Feature: Boss battle scroll usage optimiser
  As a game strategy assistant
  I want to determine the minimum time to defeat the boss using spell scrolls
  So that Petya knows the optimal scroll usage sequence

  Rule: Input / Output format
    The program reads N, max, reg from stdin, then N lines each with powi and dmgi.
    If the boss can be defeated, print YES, then the time and scroll count, then each scroll's use time and index.
    If the boss cannot be defeated, print NO.

  Rule: Battle mechanics
    Each second: boss takes damage from all active spells, then regenerates reg HP (capped at max).
    The boss is defeated if HP ≤ 0 at end of a second.
    A scroll i can only be used when boss HP ≤ powi% of max.
    Scroll use happens after the regeneration step; at most one scroll per second.
    Once used, a scroll inflicts dmgi damage per second permanently.
    The first scroll can be used at second 0 (before any damage/regen cycle).

  Scenario: Damage never exceeds regeneration — boss cannot be defeated
    Given the boss has max HP 10 and regeneration 3
    And the scrolls are:
      | pow | dmg |
      | 100 | 3   |
      | 99  | 1   |
    When the optimal strategy is found
    Then the result is "NO"

  Scenario: Scrolls used optimally allow defeating the boss
    Given the boss has max HP 100 and regeneration 10
    And the scrolls are:
      | pow | dmg |
      | 100 | 11  |
      | 90  | 9   |
    When the optimal strategy is found
    Then the result is "YES"
    And the boss is defeated at second 19
    And 2 scrolls are used

  Scenario Outline: Battle outcome for various configurations
    Given N scrolls and boss parameters leading to <result>
    When the optimal strategy is found
    Then the result is "<result>"

    Examples:
      | result |
      | NO     |
      | YES    |
