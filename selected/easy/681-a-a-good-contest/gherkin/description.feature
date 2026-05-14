Feature: Good contest performance check
  As a contest participant
  I want to know whether I had a good performance
  So that I can track my progress toward a red handle

  Rule: Input / Output format
    The program reads from stdin: first line is an integer n (1 ≤ n ≤ 100), then n lines each with "<handle> <before> <after>".
    The program prints a single word to stdout: "YES" or "NO".

  Scenario: Anton outscored a red-handle participant whose rating increased — good performance
    Given Anton outscored the following participants:
      | handle     | before | after |
      | Burunduk1  | 2526   | 2537  |
      | BudAlNik   | 2084   | 2214  |
      | subscriber | 2833   | 2749  |
    When the contest result is evaluated
    Then the performance is "YES"

  Scenario: No outscored participant is both red and gained rating — not a good performance
    Given Anton outscored the following participants:
      | handle      | before | after |
      | Applejack   | 2400   | 2400  |
      | Fluttershy  | 2390   | 2431  |
      | Pinkie_Pie  | -2500  | -2450 |
    When the contest result is evaluated
    Then the performance is "NO"

  Scenario: Outscored participant had red handle but rating did not increase
    Given Anton outscored the following participants:
      | handle    | before | after |
      | Redguy    | 2400   | 2400  |
    When the contest result is evaluated
    Then the performance is "NO"

  Scenario: Outscored participant had rating increase but handle was not red
    Given Anton outscored the following participants:
      | handle  | before | after |
      | Newbie  | 1200   | 1300  |
    When the contest result is evaluated
    Then the performance is "NO"

  Scenario: Outscored participant had red handle and rating increased
    Given Anton outscored the following participants:
      | handle   | before | after |
      | Legend   | 2500   | 2600  |
    When the contest result is evaluated
    Then the performance is "YES"
