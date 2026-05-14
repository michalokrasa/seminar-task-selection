# Football Championship

## Goal

Given the results of 5 out of 6 group-stage games (BERLAND's last game is unknown), find the score `X:Y` (`X > Y`) for BERLAND's final game such that BERLAND finishes in 1st or 2nd place, minimising `X − Y` (and then minimising `Y`). If no winning score achieves this, print `IMPOSSIBLE`.

## Rules

- The group has 4 teams; each pair plays once (6 games total).
- **Points**: win = 3, draw = 1, loss = 0.
- **Tiebreaker order** (when points are equal):
  1. Goal difference (scored − conceded), higher is better.
  2. Total goals scored, higher is better.
  3. Team name lexicographic order, smaller name ranks higher.
- BERLAND must win the last game (`X > Y`).
- Choose the score with the **minimum margin** `X − Y`; if still tied, choose the **minimum `Y`**.
- The result score can be arbitrarily large (e.g., `10:0`).
- If BERLAND cannot place in the top 2 with any winning score, output `IMPOSSIBLE`.

## Input / Output

- **Input**: 5 lines, each of the form `team1 team2 goals1:goals2` (team names up to 20 uppercase letters; goals 0–9).
- **Output**: `X:Y` or `IMPOSSIBLE`.
