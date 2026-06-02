Feature: Count successful robot movement commands
  As a robot controller
  I want to determine which commands the robot successfully fulfils
  So that I can evaluate how many targets were reached

  Rule: Input / Output format
    The program reads t test cases from stdin.
    Each test case has n commands with time t_i and target x_i in increasing time order.
    The program prints one integer per test case — the count of successful commands.

  Background:
    Given the robot starts at position 0 at time 0
    And the robot moves at speed 1 unit per second
    And the robot ignores new commands while already moving toward a target

  Scenario: Only the last command is successful (described in problem statement)
    Given the commands are:
      | time | target |
      | 1    | 5      |
      | 3    | 0      |
      | 6    | 4      |
    When the successful commands are counted
    Then the output is 1

  Scenario: An ignored command is still successful if robot passes through target
    Given the commands are:
      | time | target |
      | 1    | 5      |
      | 2    | 4      |
      | 10   | -5     |
    When the successful commands are counted
    Then the output is 2

  Scenario: No command is successful
    Given the commands are:
      | time | target |
      | 2    | -5     |
      | 3    | 1      |
      | 4    | 1      |
      | 5    | 1      |
      | 6    | 1      |
    When the successful commands are counted
    Then the output is 0

  Scenario Outline: Sample test cases from problem statement
    Given the commands produce <successful> successful outcomes
    Then the output is <successful>

    Examples:
      | successful |
      | 1          |
      | 2          |
      | 0          |
      | 2          |
      | 1          |
      | 1          |
      | 0          |
      | 2          |
