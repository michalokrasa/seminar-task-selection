Feature: Test file renaming script generator
  As a contest archive organiser
  I want to generate the minimum number of move commands to rename test files
  So that examples come first and regular tests follow, numbered 1..n

  Rule: Input / Output format
    The program reads n from stdin, then n lines each with a filename and type (1=example, 0=regular).
    The program prints the minimum number of move commands, then the commands themselves.

  Rule: Renaming target
    After all moves: examples are named "1", "2", ..., "e" (e = total examples).
    Regular tests are named "e+1", "e+2", ..., "n".
    A "move A B" overwrites B if it exists and removes A.
    The script must be valid: it must never read a file that has been moved away.

  Scenario: One example already in place, others need renaming
    Given the files are:
      | name   | type |
      | 01     | 0    |
      | 2      | 1    |
      | 2extra | 0    |
      | 3      | 1    |
      | 99     | 0    |
    When the minimum move script is generated
    Then the number of moves is 4

  Scenario: Swap required — temporary name must be used
    Given the files are:
      | name | type |
      | 1    | 0    |
      | 2    | 1    |
    When the minimum move script is generated
    Then the number of moves is 3

  Scenario: Mixed names requiring careful ordering
    Given the files are:
      | name  | type |
      | 1     | 0    |
      | 11    | 1    |
      | 111   | 0    |
      | 1111  | 1    |
      | 11111 | 0    |
    When the minimum move script is generated
    Then the number of moves is 5

  Scenario Outline: Minimum move count for various file sets
    Given a file set leading to <moves> move commands
    When the minimum move script is generated
    Then the number of moves is <moves>

    Examples:
      | moves |
      | 4     |
      | 3     |
      | 5     |
