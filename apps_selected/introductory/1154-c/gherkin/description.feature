Feature: Determine the maximum number of days the cat can eat without additional food purchases

  As a cat owner,
  I want to determine the optimal starting day for a trip
  So that my cat can eat for the maximum number of days without needing additional food.

  Rule: Input and Output Format
    Given three integers a, b, and c representing the number of daily rations of fish food, rabbit stew, and chicken stakes respectively.
    The output should be a single integer representing the maximum number of days the cat can eat without additional food purchases.

  Scenario: Minimum rations for each type of food
    Given the rations are 1 fish food, 1 rabbit stew, and 1 chicken stake
    When I calculate the maximum days
    Then the result should be 3

  Scenario: Equal rations for each type of food
    Given the rations are 3 fish food, 2 rabbit stew, and 2 chicken stakes
    When I calculate the maximum days
    Then the result should be 7

  Scenario: Excessive rabbit stew
    Given the rations are 1 fish food, 100 rabbit stew, and 1 chicken stake
    When I calculate the maximum days
    Then the result should be 3

  Scenario: Large number of rations
    Given the rations are 30 fish food, 20 rabbit stew, and 10 chicken stakes
    When I calculate the maximum days
    Then the result should be 39

  Scenario: Only one type of food available
    Given the rations are 0 fish food, 0 rabbit stew, and 10 chicken stakes
    When I calculate the maximum days
    Then the result should be 2

  Scenario Outline: Various combinations of rations
    Given the rations are <a> fish food, <b> rabbit stew, and <c> chicken stakes
    When I calculate the maximum days
    Then the result should be <result>

    Examples:
      | a  | b  | c  | result |
      | 2  | 1  | 1  | 4      |
      | 3  | 2  | 2  | 7      |
      | 1  | 100| 1  | 3      |
      | 30 | 20 | 10 | 39     |
