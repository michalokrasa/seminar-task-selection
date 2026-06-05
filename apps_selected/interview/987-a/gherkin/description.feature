Feature: Determine absent Infinity Gems based on observed colors

  As a competitive programmer
  I want to determine which Infinity Gems are absent based on the colors I observe
  So that I can output the names of the missing Gems

  Rule: Input and Output format
    - Input consists of an integer n (0 ≤ n ≤ 6) followed by n lines of distinct colors.
    - Colors are: purple, green, blue, orange, red, yellow.
    - Output the number of absent Gems followed by their names, each on a new line.
    - Gem names are: Power, Time, Space, Soul, Reality, Mind.

  Scenario: No Gems observed
    Given no colors are observed
    When I determine the absent Gems
    Then the output should be:
      """
      6
      Power
      Time
      Space
      Soul
      Reality
      Mind
      """

  Scenario: All Gems observed
    Given all colors are observed: purple, green, blue, orange, red, yellow
    When I determine the absent Gems
    Then the output should be:
      """
      0
      """

  Scenario: Some Gems observed
    Given the colors observed are: red, purple, yellow, orange
    When I determine the absent Gems
    Then the output should be:
      """
      2
      Space
      Time
      """

  Scenario: One Gem observed
    Given the color observed is: blue
    When I determine the absent Gems
    Then the output should be:
      """
      5
      Power
      Time
      Soul
      Reality
      Mind
      """

  Scenario: Five Gems observed
    Given the colors observed are: purple, green, blue, orange, red
    When I determine the absent Gems
    Then the output should be:
      """
      1
      Mind
      """

  Scenario Outline: Determine absent Gems from observed colors
    Given the colors observed are: <colors>
    When I determine the absent Gems
    Then the output should be:
      """
      <absent_count>
      <absent_gems>
      """

    Examples:
      | colors                      | absent_count | absent_gems                  |
      | ""                          | 6            | Power, Time, Space, Soul, Reality, Mind |
      | "purple, green, blue, orange, red, yellow" | 0 | "" |
      | "red, purple, yellow, orange" | 2          | Space, Time                 |
      | "blue"                       | 5            | Power, Time, Soul, Reality, Mind |
      | "purple, green, blue, orange, red" | 1     | Mind                        |
