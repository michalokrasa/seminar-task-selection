Feature: Calculate the midpoint time of a contest

  As a competitive programmer
  I want to calculate the midpoint time of a contest
  So that I can know the exact middle time during the contest

  Rule: Input and Output format
    Given the start and end time of a contest in hh:mm format
    Then the output should be the midpoint time in hh:mm format
    And the output should be exactly two digits for hours and minutes, separated by a colon

  Scenario: Contest lasts exactly one hour
    Given the contest starts at "10:00"
    And the contest ends at "11:00"
    When I calculate the midpoint
    Then the midpoint time should be "10:30"

  Scenario: Contest lasts only two minutes
    Given the contest starts at "11:10"
    And the contest ends at "11:12"
    When I calculate the midpoint
    Then the midpoint time should be "11:11"

  Scenario: Contest spans over two hours
    Given the contest starts at "01:02"
    And the contest ends at "03:02"
    When I calculate the midpoint
    Then the midpoint time should be "02:02"

  Scenario: Contest starts and ends at the same hour
    Given the contest starts at "14:20"
    And the contest ends at "14:40"
    When I calculate the midpoint
    Then the midpoint time should be "14:30"

  Scenario: Contest starts late in the day
    Given the contest starts at "23:00"
    And the contest ends at "23:30"
    When I calculate the midpoint
    Then the midpoint time should be "23:15"

  Scenario Outline: Calculate midpoint for various contest times
    Given the contest starts at "<start_time>"
    And the contest ends at "<end_time>"
    When I calculate the midpoint
    Then the midpoint time should be "<midpoint_time>"

    Examples:
      | start_time | end_time | midpoint_time |
      | 10:00      | 11:00    | 10:30         |
      | 11:10      | 11:12    | 11:11         |
      | 01:02      | 03:02    | 02:02         |
      | 14:20      | 14:40    | 14:30         |
      | 23:00      | 23:30    | 23:15         |
