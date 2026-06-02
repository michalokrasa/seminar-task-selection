Feature: Detect the unique element in an array
  As a spy hunter
  I want to identify the one element that differs from all others
  So that I can pinpoint the spy

  Rule: Input / Output format
    The program reads t test cases from stdin.
    For each test case: first line is n, second line contains n space-separated integers.
    The program prints the 1-based index of the unique element for each test case.

  Scenario: Unique element is in the middle
    Given the array is [11, 13, 11, 11]
    When the unique element is found
    Then the output is 2

  Scenario: Unique element is first
    Given the array is [1, 4, 4, 4, 4]
    When the unique element is found
    Then the output is 1

  Scenario: Unique element is last
    Given the array is [20, 20, 10]
    When the unique element is found
    Then the output is 3

  Scenario: Unique element is in a large array
    Given the array is [3, 3, 3, 3, 10, 3, 3, 3, 3, 3]
    When the unique element is found
    Then the output is 5

  Scenario Outline: Multiple test cases
    Given the array is <array>
    When the unique element is found
    Then the output is <index>

    Examples:
      | array                        | index |
      | 11 13 11 11                  | 2     |
      | 1 4 4 4 4                    | 1     |
      | 3 3 3 3 10 3 3 3 3 3         | 5     |
      | 20 20 10                     | 3     |
