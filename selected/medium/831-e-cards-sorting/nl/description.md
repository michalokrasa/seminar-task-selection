# Cards Sorting

## Goal

Count the total number of times Vasily takes the top card from the deck during a specific sorting procedure.

## Rules

- Vasily always knows the current minimum value in the deck.
- He repeatedly picks up the top card:
  - If its value equals the current minimum, the card is **removed** from the deck.
  - Otherwise, the card is placed at the **bottom** of the deck.
- When all cards with the current minimum value have been removed, the minimum updates to the next smallest value.
- The process ends when the deck is empty.
- Count every pick (both removals and re-queuing).

## Input / Output

- **Input**: first line is `n` (1 ≤ n ≤ 100 000); second line is `n` space-separated integers (1 ≤ a_i ≤ 100 000).
- **Output**: a single integer — the total number of top-card picks.
