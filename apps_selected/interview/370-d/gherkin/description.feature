Feature: Determine the smallest possible square frame on a broken monitor

  As a player,
  I want to identify the smallest square frame that can encompass all white pixels on a broken monitor,
  So that I can automate the process of finding the frame for the game.

  Rule: Input and Output Format
    Given the monitor resolution as two integers n and m (1 ≤ n, m ≤ 2000)
    And n lines each containing m characters representing the monitor state
    Where '.' represents a black pixel and 'w' represents a white pixel
    Then output the monitor screen with the frame represented by '+'
    And unchanged white pixels represented by 'w'
    If no valid frame exists, output -1

  Scenario: Frame exists with multiple white pixels
    Given the monitor resolution "4 8"
    And the monitor state:
      """
      ..w..w..
      ........
      ........
      ..w..w..
      """
    When I determine the smallest frame
    Then the output should be:
      """
      ..w++w..
      ..+..+..
      ..+..+..
      ..w++w..
      """

  Scenario: Frame exists with a single white pixel
    Given the monitor resolution "5 6"
    And the monitor state:
      """
      ......
      .w....
      ......
      ..w...
      ......
      """
    When I determine the smallest frame
    Then the output should be:
      """
      ......
      +w+...
      +.+...
      ++w...
      ......
      """

  Scenario: Frame does not exist
    Given the monitor resolution "2 4"
    And the monitor state:
      """
      ....
      .w..
      """
    When I determine the smallest frame
    Then the output should be:
      """
      ....
      .w..
      """

  Scenario: No valid frame can encompass all white pixels
    Given the monitor resolution "2 6"
    And the monitor state:
      """
      w..w.w
      ...w..
      """
    When I determine the smallest frame
    Then the output should be "-1"

  Scenario Outline: Various frame configurations
    Given the monitor resolution "<resolution>"
    And the monitor state:
      """
      <state>
      """
    When I determine the smallest frame
    Then the output should be:
      """
      <output>
      """

    Examples:
      | resolution | state                  | output                  |
      | "4 8"      | "..w..w..\n........\n........\n..w..w.." | "..w++w..\n..+..+..\n..+..+..\n..w++w.." |
      | "5 6"      | "......\n.w....\n......\n..w...\n......" | "......\n+w+...\n+.+...\n++w...\n......" |
      | "2 4"      | "....\n.w.."          | "....\n.w.."            |
      | "2 6"      | "w..w.w\n...w.."      | "-1"                    |
