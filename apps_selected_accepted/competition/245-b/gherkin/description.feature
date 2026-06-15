Feature: Restore Internet Resource Address
  As a user who has written down a web address without punctuation,
  I want to restore the address to its correct format,
  So that I can access the Internet resource correctly.

  Rule: Input and Output Format
    - The input is a non-empty string of lowercase English letters.
    - The output should be a valid web address in the format: <protocol>://<domain>.ru[/<context>].
    - <protocol> is either "http" or "ftp".
    - <domain> is a non-empty string of lowercase English letters.
    - <context> is optional and, if present, is a non-empty string of lowercase English letters.

  Scenario: Basic http address with context
    Given the input "httpsunrux"
    When the address is restored
    Then the output should be "http://sun.ru/x"

  Scenario: Basic ftp address with context
    Given the input "ftphttprururu"
    When the address is restored
    Then the output should be "ftp://http.ru/ruru"

  Scenario: Address with no context
    Given the input "httpdomainru"
    When the address is restored
    Then the output should be "http://domain.ru"

  Scenario: Address with minimal domain and context
    Given the input "ftpaxruy"
    When the address is restored
    Then the output should be "ftp://a.ru/xruy"

  Scenario: Address with multiple valid outputs
    Given the input "ftphttprururu"
    When the address is restored
    Then the output should be one of "ftp://http.ru/ruru", "ftp://httpruru.ru", "ftp://httpru.ru/ru"

  Scenario Outline: Restore address from input
    Given the input "<input>"
    When the address is restored
    Then the output should be "<output>"

    Examples:
      | input          | output              |
      | httpsunrux     | http://sun.ru/x     |
      | ftphttprururu  | ftp://http.ru/ruru  |
      | httpdomainru   | http://domain.ru    |
      | ftpaxruy       | ftp://a.ru/xruy     |
