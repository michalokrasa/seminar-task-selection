Feature: Statue Rearrangement on Islands

  As an islander,
  I want to rearrange the statues on the islands in a desired order,
  So that the statues are placed according to the new configuration.

  Rule: Input and Output Format
    Given n islands in a cycle with n-1 statues and 1 empty pedestal,
    When provided with the current and desired statue configurations,
    Then determine if the desired configuration can be achieved.

  Scenario: Simple rearrangement with 3 islands
    Given the number of islands is 3
    And the current configuration is "1 0 2"
    And the desired configuration is "2 0 1"
    Then the output should be "YES"

  Scenario: Direct swap with 2 islands
    Given the number of islands is 2
    And the current configuration is "1 0"
    And the desired configuration is "0 1"
    Then the output should be "YES"

  Scenario: Impossible rearrangement with 4 islands
    Given the number of islands is 4
    And the current configuration is "1 2 3 0"
    And the desired configuration is "0 3 2 1"
    Then the output should be "NO"

  Scenario: Already in desired order with 5 islands
    Given the number of islands is 5
    And the current configuration is "0 1 2 3 4"
    And the desired configuration is "0 1 2 3 4"
    Then the output should be "YES"

  Scenario: Complex rearrangement with 6 islands
    Given the number of islands is 6
    And the current configuration is "1 2 0 3 4 5"
    And the desired configuration is "1 0 2 3 4 5"
    Then the output should be "YES"

  Scenario Outline: Various configurations
    Given the number of islands is <n>
    And the current configuration is "<current>"
    And the desired configuration is "<desired>"
    Then the output should be "<output>"

    Examples:
      | n | current     | desired     | output |
      | 3 | 1 0 2       | 2 0 1       | YES    |
      | 2 | 1 0         | 0 1         | YES    |
      | 4 | 1 2 3 0     | 0 3 2 1     | NO     |
      | 5 | 0 1 2 3 4   | 0 1 2 3 4   | YES    |
      | 6 | 1 2 0 3 4 5 | 1 0 2 3 4 5 | YES    |
