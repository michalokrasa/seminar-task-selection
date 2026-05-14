Feature: Card deck sort operation counter
  As a card sorter
  I want to count how many times Vasily picks up the top card
  So that the total effort of sorting the deck can be measured

  Rule: Input / Output format
    The program reads n from stdin, then a sequence of n integers.
    The program prints a single integer — the total number of top-card picks.

  Rule: Sorting procedure
    Vasily repeatedly takes the top card.
    If its value equals the current minimum, the card is removed.
    Otherwise, the card is placed at the bottom of the deck.
    This continues until the deck is empty.

  Scenario: Deck with one card requires exactly one pick
    Given the deck from top to bottom is 1000
    When Vasily sorts the deck
    Then the total number of picks is 1

  Scenario: All cards equal — each is picked and removed in sequence
    Given the deck from top to bottom is 3 3 3 3 3 3 3
    When Vasily sorts the deck
    Then the total number of picks is 7

  Scenario: Deck requires cycling to reach minimum values
    Given the deck from top to bottom is 6 3 1 2
    When Vasily sorts the deck
    Then the total number of picks is 7

  Scenario Outline: Pick count for various decks
    Given the deck from top to bottom is <deck>
    When Vasily sorts the deck
    Then the total number of picks is <count>

    Examples:
      | deck          | count |
      | 6 3 1 2       | 7     |
      | 1000          | 1     |
      | 3 3 3 3 3 3 3 | 7     |
