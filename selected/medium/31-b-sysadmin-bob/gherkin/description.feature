Feature: Email address list reconstruction
  As an email list parser
  I want to split a comma-free concatenation of email addresses back into valid addresses
  So that Bob can restore his contacts list

  Rule: Input / Output format
    The program reads a single string from stdin consisting of lowercase letters and "@" characters.
    The program prints a comma-separated list of valid email addresses, or "No solution".

  Rule: Email format
    A valid email address has the form A@B where A and B are non-empty strings of lowercase Latin letters.

  Scenario: Single "@" splits into one valid address
    Given the input string is "a@b"
    When the addresses are reconstructed
    Then the output is "a@b"

  Scenario: Two "@" signs with sufficient surrounding letters splits into two addresses
    Given the input string is "a@aa@a"
    When the addresses are reconstructed
    Then the output is "a@a,a@a"

  Scenario: Two "@" signs but no way to assign non-empty parts yields no solution
    Given the input string is "a@a@a"
    When the addresses are reconstructed
    Then the output is "No solution"

  Scenario: Leading "@" with no local part yields no solution
    Given the input string is "@aa@a"
    When the addresses are reconstructed
    Then the output is "No solution"

  Scenario Outline: Reconstruction for various inputs
    Given the input string is "<input>"
    When the addresses are reconstructed
    Then the output is "<output>"

    Examples:
      | input   | output       |
      | a@aa@a  | a@a,a@a      |
      | a@a@a   | No solution  |
      | @aa@a   | No solution  |
