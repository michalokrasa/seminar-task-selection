Feature: Correct broken clock time display

  As a user with a broken clock
  I want to correct the time displayed on the clock
  So that it shows a valid time in either 12-hour or 24-hour format with minimal changes

  Rule: Input and output format
    Given the input format is an integer (12 or 24) followed by a time in HH:MM format
    Then the output should be a valid time in the same format with minimal digit changes

  Scenario: Valid 24-hour time
    Given the clock format is 24-hour
    And the time displayed is "17:30"
    When I correct the time
    Then the output should be "17:30"

  Scenario: Invalid 12-hour time with hour correction
    Given the clock format is 12-hour
    And the time displayed is "17:30"
    When I correct the time
    Then the output should be "07:30"

  Scenario: Invalid 24-hour time with full correction
    Given the clock format is 24-hour
    And the time displayed is "99:99"
    When I correct the time
    Then the output should be "09:09"

  Scenario: Invalid 12-hour time with minute correction
    Given the clock format is 12-hour
    And the time displayed is "12:60"
    When I correct the time
    Then the output should be "12:00"

  Scenario: Invalid 24-hour time with minimal changes
    Given the clock format is 24-hour
    And the time displayed is "25:61"
    When I correct the time
    Then the output should be "05:01"

  Scenario Outline: Correcting broken clock time
    Given the clock format is <format>
    And the time displayed is "<time>"
    When I correct the time
    Then the output should be "<corrected_time>"

    Examples:
      | format | time  | corrected_time |
      | 24     | 17:30 | 17:30          |
      | 12     | 17:30 | 07:30          |
      | 24     | 99:99 | 09:09          |
      | 12     | 12:60 | 12:00          |
