Feature: Determine if the pineapple will bark at a given time

  As a competitive programmer
  I want to determine if the pineapple will bark at a specific time
  So that Barney can decide if he can eat the pineapple without interruption

  Rule: Input and Output format
    Given three integers t, s, and x
    - t is the time the pineapple barks for the first time
    - s is the interval in seconds after which the pineapple barks twice
    - x is the time Barney wants to eat the pineapple
    Output "YES" if the pineapple will bark at time x, otherwise "NO"

  Scenario: Pineapple barks at the first time
    Given t is 3, s is 10, and x is 3
    When checking if the pineapple barks at time x
    Then the output should be "YES"

  Scenario: Pineapple does not bark at a non-barking time
    Given t is 3, s is 10, and x is 4
    When checking if the pineapple barks at time x
    Then the output should be "NO"

  Scenario: Pineapple barks at a subsequent barking time
    Given t is 3, s is 8, and x is 51
    When checking if the pineapple barks at time x
    Then the output should be "YES"

  Scenario: Pineapple barks at the second of a pair of barks
    Given t is 3, s is 8, and x is 52
    When checking if the pineapple barks at time x
    Then the output should be "YES"

  Scenario: Pineapple does not bark at a time before the first bark
    Given t is 5, s is 7, and x is 2
    When checking if the pineapple barks at time x
    Then the output should be "NO"

  Scenario Outline: Check various times for barking
    Given t is <t>, s is <s>, and x is <x>
    When checking if the pineapple barks at time x
    Then the output should be "<output>"

    Examples:
      | t | s | x  | output |
      | 3 | 10 | 3  | YES    |
      | 3 | 10 | 4  | NO     |
      | 3 | 8  | 51 | YES    |
      | 3 | 8  | 52 | YES    |
      | 5 | 7  | 2  | NO     |
