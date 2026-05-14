Feature: Chat server outgoing traffic calculation
  As a chat server
  I want to track how many bytes I send
  So that Polycarp can measure total outgoing traffic

  Rule: Input / Output format
    The program reads up to 100 commands from stdin, one per line.
    Each command is either "+<name>" (add), "-<name>" (remove), or "<sender>:<message>" (send).
    The program prints a single integer to stdout — the total bytes of outgoing traffic.

  Background:
    Given the chat room is empty
    And the total traffic counter is 0

  Scenario: Sending a message adds traffic proportional to participants and message length
    Given "Mike" has joined the chat
    When "Mike" sends the message "hello"
    Then the traffic increases by 5 bytes
    And the total traffic is 5 bytes

  Scenario: Add and Remove commands produce no traffic
    Given "Mike" has joined the chat
    When "Kate" joins the chat
    And "Kate" leaves the chat
    Then the total traffic is 0 bytes

  Scenario: Message is delivered to all current participants including the sender
    Given "Mike" has joined the chat
    And "Kate" has joined the chat
    And "Dmitry" has joined the chat
    When "Mike" sends the message "hi"
    Then the traffic increases by 6 bytes
    And the total traffic is 6 bytes

  Scenario Outline: Full session traffic calculation
    Given the following commands are processed:
      | command       |
      | +Mike         |
      | Mike:hello    |
      | +Kate         |
      | +Dmitry       |
      | -Dmitry       |
      | Kate:hi       |
      | -Kate         |
    Then the total outgoing traffic is <total> bytes

    Examples:
      | total |
      | 9     |
