Feature: Ant colony diffusion simulation
  As an ant colony simulator
  I want to determine the final distribution of ants on a 2D lattice
  So that scientists can answer queries about specific junctions

  Rule: Input / Output format
    The program reads n (initial ants at origin) and t (number of queries) from stdin.
    Each of the next t lines contains coordinates xi yi of a query junction.
    The program prints t integers — the number of ants at each queried junction when diffusion stops.

  Rule: Diffusion process
    Each minute, every junction with ≥ 4 ants fires: 4 ants leave, one to each of the 4 neighbours.
    The process repeats until no junction has ≥ 4 ants.
    Ants never interfere; the process is guaranteed to terminate.

  Scenario: Single ant — no movement occurs
    Given there are 1 ants at the origin
    When the diffusion stops
    And the query is junction (0, 0)
    Then the answer is 1

  Scenario: Single ant — neighbouring junctions are empty
    Given there are 1 ants at the origin
    When the diffusion stops
    And the query is junction (0, 1)
    Then the answer is 0

  Scenario: 6 ants — one firing event scatters 4 ants, 2 remain at origin
    Given there are 6 ants at the origin
    When the diffusion stops
    And the query is junction (0, 0)
    Then the answer is 2

  Scenario: 6 ants — adjacent junctions each receive 1 ant
    Given there are 6 ants at the origin
    When the diffusion stops
    And the query is junction (0, 1)
    Then the answer is 1

  Scenario: Far-away junction is always empty
    Given there are 6 ants at the origin
    When the diffusion stops
    And the query is junction (0, 2)
    Then the answer is 0

  Scenario Outline: Ant count at queried junctions after diffusion
    Given there are <n> ants at the origin
    When the diffusion stops
    And the query is junction (<x>, <y>)
    Then the answer is <count>

    Examples:
      | n | x | y  | count |
      | 1 | 0 | 1  | 0     |
      | 1 | 0 | 0  | 1     |
      | 6 | 0 | -2 | 0     |
      | 6 | 0 | -1 | 1     |
      | 6 | 0 | 0  | 2     |
      | 6 | 0 | 1  | 1     |
      | 6 | 0 | 2  | 0     |
