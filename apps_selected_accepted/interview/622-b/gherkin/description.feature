Feature: Calculate time after a given number of minutes

  As a user
  I want to calculate the time after a given number of minutes from a starting time in 24-hour format
  So that I can determine the future time accurately

  Rule: Input and Output Format
    - The input consists of a starting time in the format hh:mm (0 ≤ hh < 24, 0 ≤ mm < 60).
    - The input also includes an integer a (0 ≤ a ≤ 10^4) representing the number of minutes to add.
    - The output should be the time after a minutes in the same format hh:mm with leading zeroes if necessary.

  Scenario: Adding minutes that result in a new day
    Given the current time is "23:59"
    And the minutes to add is 10
    When I calculate the new time
    Then the result should be "00:09"

  Scenario: Adding minutes within the same day
    Given the current time is "20:20"
    And the minutes to add is 121
    When I calculate the new time
    Then the result should be "22:21"

  Scenario: Adding zero minutes
    Given the current time is "10:10"
    And the minutes to add is 0
    When I calculate the new time
    Then the result should be "10:10"

  Scenario: Adding minutes that result in exactly the next hour
    Given the current time is "13:45"
    And the minutes to add is 15
    When I calculate the new time
    Then the result should be "14:00"

  Scenario: Adding a large number of minutes
    Given the current time is "01:00"
    And the minutes to add is 1440
    When I calculate the new time
    Then the result should be "01:00"

  Scenario Outline: Calculate new time after adding minutes
    Given the current time is "<current_time>"
    And the minutes to add is <minutes_to_add>
    When I calculate the new time
    Then the result should be "<expected_time>"

    Examples:
      | current_time | minutes_to_add | expected_time |
      | "23:59"      | 10             | "00:09"       |
      | "20:20"      | 121            | "22:21"       |
      | "10:10"      | 0              | "10:10"       |
      | "13:45"      | 15             | "14:00"       |
      | "01:00"      | 1440           | "01:00"       |
