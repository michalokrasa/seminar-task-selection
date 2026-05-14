Feature: INI file formatter
  As an INI file processor
  I want to reformat a given INI file according to strict ordering and deduplication rules
  So that the output is canonical and clean

  Rule: Input / Output format
    The program reads n from stdin, then n lines of an INI file.
    The program prints the reformatted INI file to stdout.

  Rule: Formatting rules
    Comment lines (first non-space character is ";") are discarded.
    Key-value lines have the form "key=value" (spaces around key and value are stripped).
    Section lines have the form "[section]" (spaces around brackets are stripped).
    Key-value lines before any section header belong to the global (no-section) namespace.
    Sections are printed in lexicographic order of section name.
    Within each section (and globally), key-value pairs are printed in lexicographic order by key.
    If a key appears more than once in the same section, only the last occurrence is kept.
    Empty sections (with no key-value pairs) are still printed with their header.

  Scenario: Global key-value pairs are deduplicated, last value wins
    Given the INI file contains:
      | line   |
      | a= 1   |
      | b=a    |
      | a = 2  |
    When the file is formatted
    Then the output contains "a=2" before "b=a"

  Scenario: Sections are printed in lexicographic order
    Given the INI file contains sections z, y, and w
    When the file is formatted
    Then sections appear in order: w, y, z

  Scenario: Comments are removed from output
    Given the INI file contains a line " ; this is a comment"
    When the file is formatted
    Then no comment lines appear in the output

  Scenario: Empty section is still printed
    Given the INI file contains "[w]" with no key-value pairs under it
    When the file is formatted
    Then "[w]" appears in the output

  Scenario Outline: Full formatting of a sample INI file
    Given the INI file has 11 lines as in the first example
    When the file is formatted
    Then the output matches:
      | line  |
      | a=2   |
      | b=a   |
      | [w]   |
      | [y]   |
      | 2=3   |
      | [z]   |
      | 1=2   |
      | 2=1   |

    Examples:
      | ignored |
      | -       |
