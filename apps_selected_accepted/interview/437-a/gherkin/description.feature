Feature: Predict child's choice in a multiple-choice question

  As a competitive programmer
  I want to determine the child's choice based on the description lengths
  So that I can predict the answer the child will choose

  Rule: Input and Output format
    - Input consists of four lines, each starting with a letter (A, B, C, D) followed by a period and a description.
    - Descriptions are non-empty and consist of at most 100 characters.
    - Output is a single letter ("A", "B", "C", or "D") representing the child's choice.

  Scenario: Single great choice due to shortest description
    Given the descriptions:
      | A | VFleaKing_is_the_author_of_this_problem |
      | B | Picks_is_the_author_of_this_problem     |
      | C | Picking_is_the_author_of_this_problem   |
      | D | Ftiasch_is_cute                         |
    When the child's choice is determined
    Then the output should be "D"

  Scenario: No great choice, default to C
    Given the descriptions:
      | A | ab   |
      | B | abcde|
      | C | ab   |
      | D | abc  |
    When the child's choice is determined
    Then the output should be "C"

  Scenario: Single great choice due to longest description
    Given the descriptions:
      | A | c  |
      | B | cc |
      | C | c  |
      | D | c  |
    When the child's choice is determined
    Then the output should be "B"

  Scenario: All descriptions are the same length
    Given the descriptions:
      | A | abc |
      | B | def |
      | C | ghi |
      | D | jkl |
    When the child's choice is determined
    Then the output should be "C"

  Scenario: Two great choices, default to C
    Given the descriptions:
      | A | a  |
      | B | bb |
      | C | c  |
      | D | dd |
    When the child's choice is determined
    Then the output should be "C"

  Scenario Outline: Determine child's choice based on description lengths
    Given the descriptions:
      | A | <descA> |
      | B | <descB> |
      | C | <descC> |
      | D | <descD> |
    When the child's choice is determined
    Then the output should be "<choice>"

    Examples:
      | descA | descB | descC | descD | choice |
      | ab    | abcde | ab    | abc   | C      |
      | c     | cc    | c     | c     | B      |
      | a     | b     | c     | d     | C      |
      | short | long  | short | short | B      |
