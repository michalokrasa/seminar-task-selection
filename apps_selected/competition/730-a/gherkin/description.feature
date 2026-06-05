Feature: Equalize friends' ratings for Toda 2 championship

  As a group of friends wanting to participate in a Toda 2 championship,
  I want to equalize our ratings by losing matches strategically,
  So that we can form a team with the highest possible equal rating.

  Rule: Input and Output Format
    - Input consists of an integer n (2 ≤ n ≤ 100) representing the number of friends.
    - Followed by n non-negative integers representing the initial ratings of each friend.
    - Output a single integer R, the final equal rating for all friends.
    - Output an integer t, the number of matches played.
    - Followed by t lines, each containing n characters '0' or '1', indicating which friends play in each match.
    - Each match must have between 2 and 5 friends playing.

  Scenario: All friends have the same initial rating
    Given the number of friends is 3
    And their initial ratings are 1, 1, 1
    When they play matches to equalize ratings
    Then the final rating should be 1
    And the number of matches should be 0

  Scenario: Two friends with different ratings
    Given the number of friends is 2
    And their initial ratings are 1, 2
    When they play matches to equalize ratings
    Then the final rating should be 0
    And the number of matches should be 2
    And the match configurations should be:
      | 11 |
      | 11 |

  Scenario: Multiple friends with varying ratings
    Given the number of friends is 5
    And their initial ratings are 4, 5, 1, 7, 4
    When they play matches to equalize ratings
    Then the final rating should be 1
    And the number of matches should be 8
    And the match configurations should be:
      | 01010 |
      | 00011 |
      | 01010 |
      | 10010 |
      | 00011 |
      | 11000 |
      | 00011 |
      | 11000 |

  Scenario: Minimum number of friends with zero ratings
    Given the number of friends is 2
    And their initial ratings are 0, 0
    When they play matches to equalize ratings
    Then the final rating should be 0
    And the number of matches should be 0

  Scenario: Maximum number of friends with mixed ratings
    Given the number of friends is 100
    And their initial ratings are a mix of values between 0 and 100
    When they play matches to equalize ratings
    Then the final rating should be determined
    And the number of matches should be calculated
    And each match should have between 2 and 5 friends playing

  Scenario Outline: Various initial ratings
    Given the number of friends is <n>
    And their initial ratings are <ratings>
    When they play matches to equalize ratings
    Then the final rating should be <final_rating>
    And the number of matches should be <num_matches>
    And the match configurations should be:
      | <match_configurations> |

    Examples:
      | n  | ratings     | final_rating | num_matches | match_configurations       |
      | 2  | 1, 2        | 0            | 2           | 11, 11                     |
      | 3  | 1, 1, 1     | 1            | 0           |                           |
      | 5  | 4, 5, 1, 7, 4 | 1          | 8           | 01010, 00011, 01010, 10010, 00011, 11000, 00011, 11000 |
      | 4  | 3, 3, 3, 3  | 3            | 0           |                           |
