# Dice Game Result

## Goal

Determine the winner of a dice game between Mishka and Chris, or declare a draw if they win an equal number of rounds.

## Rules

- The game consists of `n` rounds.
- In each round, both players roll a die with values from 1 to 6.
- The player with the higher roll wins the round.
- If both rolls are equal, the round is a draw.
- The player who wins the most rounds wins the game.
- If both players win the same number of rounds, the game is a draw.

## Input / Output

- **Input**: 
  - The first line contains an integer `n` (1 ≤ n ≤ 100), the number of rounds.
  - The next `n` lines each contain two integers `m_i` and `c_i` (1 ≤ m_i, c_i ≤ 6), representing the dice rolls of Mishka and Chris in the `i-th` round.
- **Output**: 
  - Print "Mishka" if Mishka wins the game.
  - Print "Chris" if Chris wins the game.
  - Print "Friendship is magic!^^" if the game is a draw.
