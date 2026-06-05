Feature: Construct a palindromic matrix from given integers

  As a competitive programmer
  I want to construct a square matrix from given integers
  So that the matrix is palindromic and uses all integers exactly once

  Rule: Input and Output format
    - Input consists of an integer n (1 ≤ n ≤ 20) and n^2 integers (1 ≤ a_i ≤ 1000).
    - Output "YES" followed by the n x n matrix if possible, otherwise "NO".

  Scenario: Single element matrix
    Given n is 1
    And the integers are 10
    When constructing the matrix
    Then the output should be "YES"
    And the matrix should be:
      | 10 |

  Scenario: Simple 3x3 palindromic matrix
    Given n is 3
    And the integers are 1, 1, 1, 1, 1, 3, 3, 3, 3
    When constructing the matrix
    Then the output should be "YES"
    And the matrix should be:
      | 1 3 1 |
      | 3 1 3 |
      | 1 3 1 |

  Scenario: Impossible 4x4 matrix
    Given n is 4
    And the integers are 1, 2, 1, 9, 8, 4, 3, 8, 8, 3, 4, 8, 9, 2, 1, 1
    When constructing the matrix
    Then the output should be "NO"

  Scenario: Simple 4x4 palindromic matrix
    Given n is 4
    And the integers are 1, 8, 8, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 8, 8, 1
    When constructing the matrix
    Then the output should be "YES"
    And the matrix should be:
      | 1 2 2 1 |
      | 8 2 2 8 |
      | 8 2 2 8 |
      | 1 2 2 1 |

  Scenario: Edge case with maximum n
    Given n is 20
    And the integers are all 1s
    When constructing the matrix
    Then the output should be "YES"
    And the matrix should be a 20x20 matrix filled with 1s

  Scenario Outline: Constructing palindromic matrices
    Given n is <n>
    And the integers are <integers>
    When constructing the matrix
    Then the output should be <output>
    And the matrix should be <matrix>

    Examples:
      | n | integers                                      | output | matrix                                                                 |
      | 2 | 1, 1, 2, 2                                    | YES    | 1 2, 2 1                                                               |
      | 3 | 1, 1, 1, 1, 1, 3, 3, 3, 3                     | YES    | 1 3 1, 3 1 3, 1 3 1                                                   |
      | 4 | 1, 8, 8, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 8, 8, 1| YES    | 1 2 2 1, 8 2 2 8, 8 2 2 8, 1 2 2 1                                     |
      | 4 | 1, 2, 1, 9, 8, 4, 3, 8, 8, 3, 4, 8, 9, 2, 1, 1| NO     |                                                                       |
