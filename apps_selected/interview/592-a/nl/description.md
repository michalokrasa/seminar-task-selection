# PawnChess Winner

## Goal

Determine which player wins the game of PawnChess given the initial board configuration, assuming both players play optimally.

## Rules

- The game is played on an 8x8 board with white ('W') and black ('B') pawns.
- Player A (white) wins by moving a white pawn to the first row.
- Player B (black) wins by moving a black pawn to the eighth row.
- Player A moves first, followed by Player B, alternating turns.
- A pawn can only move to an adjacent empty cell in its respective direction (up for white, down for black).
- The game guarantees a winner, as there will always be available moves for both players.

## Input / Output

- **Input**: 
  - 8 lines, each containing 8 characters ('.', 'B', 'W') representing the board.
  - No white pawns on the first row and no black pawns on the last row.
- **Output**: 
  - A single character 'A' if Player A wins, or 'B' if Player B wins.
