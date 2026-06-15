Feature: Determine if a pattern can match specific files for deletion

  As a programmer
  I want to determine if a pattern can be created to match specific files for deletion
  So that I can delete only the desired files using a single command

  Rule: Input and Output format
    Given the number of total files and files to be deleted
    And a list of filenames
    And a list of indices of files to be deleted
    When a pattern can be created to match only the files to be deleted
    Then output "Yes" followed by the pattern
    Otherwise, output "No"

  Scenario: Simple match with question mark
    Given the input:
      | 3 2 |
      | ab  |
      | ac  |
      | cd  |
      | 1 2 |
    Then the output should be:
      | Yes |
      | a?  |

  Scenario: Pattern with multiple question marks
    Given the input:
      | 5 3   |
      | test  |
      | tezt  |
      | test. |
      | .est  |
      | tes.  |
      | 1 4 5 |
    Then the output should be:
      | Yes  |
      | ?es? |

  Scenario: No possible pattern
    Given the input:
      | 4 4 |
      | a   |
      | b   |
      | c   |
      | dd  |
      | 1 2 3 4 |
    Then the output should be:
      | No |

  Scenario: Pattern with dots and question marks
    Given the input:
      | 6 3 |
      | .svn |
      | .git |
      | .... |
      | ...  |
      | ..   |
      | .    |
      | 1 2 3 |
    Then the output should be:
      | Yes  |
      | .??? |

  Scenario: All files match the same pattern
    Given the input:
      | 3 3 |
      | abc |
      | abc |
      | abc |
      | 1 2 3 |
    Then the output should be:
      | Yes |
      | abc |

  Scenario Outline: Determine pattern for file deletion
    Given the input:
      | <n> <m> |
      | <file1> |
      | <file2> |
      | <file3> |
      | <file4> |
      | <file5> |
      | <indices> |
    Then the output should be:
      | <result> |
      | <pattern> |

    Examples:
      | n  | m | file1 | file2 | file3 | file4 | file5 | indices | result | pattern |
      | 3  | 2 | ab    | ac    | cd    |       |       | 1 2     | Yes    | a?      |
      | 5  | 3 | test  | tezt  | test. | .est  | tes.  | 1 4 5   | Yes    | ?es?    |
      | 4  | 4 | a     | b     | c     | dd    |       | 1 2 3 4 | No     |         |
      | 6  | 3 | .svn  | .git  | ....  | ...   | ..    | 1 2 3   | Yes    | .???    |
