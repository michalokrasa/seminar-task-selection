Feature: Almost regular bracket sequence position counter
  As a bracket sequence analyser
  I want to count positions where flipping one bracket makes the sequence regular
  So that the number of such positions is reported

  Rule: Input / Output format
    The program reads n from stdin, then a string of n '(' and ')' characters.
    The program prints a single integer — the count of valid flip positions.

  Rule: Regular bracket sequence
    A bracket sequence is regular if it is balanced (equal opening and closing brackets)
    and every prefix has at least as many opening brackets as closing brackets.
    Flipping position i means changing '(' to ')' or ')' to '('.

  Scenario: Already regular sequence has no valid flip positions
    Given the bracket sequence is "()()()"
    And its length is 6
    When the flip positions are counted
    Then the count is 0

  Scenario: Too many unmatched openers — three positions fix the sequence
    Given the bracket sequence is "(((())"
    And its length is 6
    When the flip positions are counted
    Then the count is 3

  Scenario: Single closing bracket cannot be made regular by one flip
    Given the bracket sequence is ")"
    And its length is 1
    When the flip positions are counted
    Then the count is 0

  Scenario: Heavily unbalanced sequence has no single-flip fix
    Given the bracket sequence is ")))((((("
    And its length is 8
    When the flip positions are counted
    Then the count is 0

  Scenario Outline: Flip position count for various sequences
    Given the bracket sequence is "<sequence>"
    And its length is <n>
    When the flip positions are counted
    Then the count is <count>

    Examples:
      | n | sequence | count |
      | 6 | (((())   | 3     |
      | 6 | ()()()   | 0     |
      | 1 | )        | 0     |
      | 8 | )))(((((  | 0     |
