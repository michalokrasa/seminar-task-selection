Feature: Determine potential leaders in a chat meeting

  As the assistant director,
  I want to identify potential leaders from a chat meeting log,
  So that the director can talk to the team leader.

  Rule: Input and Output Format
    - Input consists of two integers n and m, followed by m messages.
    - Each message is either "+ id" or "- id".
    - Output the number of potential leaders and their IDs in increasing order.
    - If no leader can be identified, output "0".

  Scenario: All participants can be leaders
    Given the number of participants is 5
    And the number of messages is 4
    And the messages are:
      | + 1 |
      | + 2 |
      | - 2 |
      | - 1 |
    Then the number of potential leaders is 4
    And the potential leaders are 1, 3, 4, 5

  Scenario: Only one participant can be a leader
    Given the number of participants is 3
    And the number of messages is 2
    And the messages are:
      | + 1 |
      | - 2 |
    Then the number of potential leaders is 1
    And the potential leader is 3

  Scenario: No participant can be a leader
    Given the number of participants is 2
    And the number of messages is 4
    And the messages are:
      | + 1 |
      | - 1 |
      | + 2 |
      | - 2 |
    Then the number of potential leaders is 0

  Scenario: Some participants can be leaders
    Given the number of participants is 5
    And the number of messages is 6
    And the messages are:
      | + 1 |
      | - 1 |
      | - 3 |
      | + 3 |
      | + 4 |
      | - 4 |
    Then the number of potential leaders is 3
    And the potential leaders are 2, 3, 5

  Scenario: No participant can be a leader with interleaved log
    Given the number of participants is 2
    And the number of messages is 4
    And the messages are:
      | + 1 |
      | - 2 |
      | + 2 |
      | - 1 |
    Then the number of potential leaders is 0

  Scenario Outline: Determine potential leaders from various logs
    Given the number of participants is <n>
    And the number of messages is <m>
    And the messages are:
      | <message1> |
      | <message2> |
      | <message3> |
      | <message4> |
    Then the number of potential leaders is <k>
    And the potential leaders are <leaders>

    Examples:
      | n | m | message1 | message2 | message3 | message4 | k | leaders  |
      | 5 | 4 | + 1      | + 2      | - 2      | - 1      | 4 | 1, 3, 4, 5 |
      | 3 | 2 | + 1      | - 2      |          |          | 1 | 3        |
      | 2 | 4 | + 1      | - 1      | + 2      | - 2      | 0 |          |
      | 5 | 6 | + 1      | - 1      | - 3      | + 3      | 3 | 2, 3, 5  |
