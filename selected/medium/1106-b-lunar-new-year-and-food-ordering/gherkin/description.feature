Feature: Restaurant food ordering with cheapest-available fallback
  As a restaurant
  I want to serve each customer as many dishes as possible at minimum extra cost
  So that customers receive their order or the cheapest available alternative

  Rule: Input / Output format
    The program reads n and m, then two arrays of length n (quantities and costs), then m orders (type, count) from stdin.
    The program prints m lines, each being the total cost for that customer.

  Scenario: Customer is served exactly what they ordered
    Given food kind 1 has 4 dishes at cost 6
    When a customer orders 4 dishes of kind 1
    Then the customer is charged 24

  Scenario: Preferred food is out of stock — fallback to cheapest available
    Given food kind 2 has 0 dishes remaining
    And food kind 4 has 1 dish at cost 2
    When a customer orders 1 dish of kind 2
    Then the customer is served 1 dish of kind 4 and charged 2

  Scenario: Among equally cheap alternatives the smallest index is chosen
    Given food kind 2 is out of stock
    And food kind 4 has stock at cost 2
    And food kind 6 has stock at cost 2
    When a customer orders 1 dish of kind 2
    Then the customer is served from kind 4 (smaller index among equally cheap kinds)

  Scenario: No food remains — customer leaves angrily and pays nothing
    Given all food kinds have 0 dishes remaining
    When a customer orders any number of dishes
    Then the customer is charged 0

  Scenario Outline: Full session with 5 customers
    Given 8 food kinds with quantities [8,6,2,1,4,5,7,5] and costs [6,3,3,2,6,2,3,2]
    When the following orders are processed in sequence:
      | customer | type | dishes |
      | 1        | 2    | 8      |
      | 2        | 1    | 4      |
      | 3        | 4    | 7      |
      | 4        | 3    | 4      |
      | 5        | 6    | 10     |
    Then the costs for customers 1 through 5 are <costs>

    Examples:
      | costs          |
      | 22,24,14,10,39 |
