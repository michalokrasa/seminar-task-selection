# Card Game Outcome

## Goal

Determine the winner of a card game between Conan and Agasa, assuming both play optimally.

## Rules

- Players take turns removing cards, starting with Conan.
- On each turn, a player removes one card and all cards with numbers strictly less than the chosen card.
- A player loses if they cannot make a move because no cards are left.

## Input / Output

- **Input**: 
  - An integer `n` (1 ≤ n ≤ 100,000) representing the number of cards.
  - A list of `n` integers `a_1, a_2, ..., a_n` (1 ≤ a_i ≤ 100,000) representing the numbers on the cards.
- **Output**: 
  - Print "Conan" if Conan wins, otherwise print "Agasa".
