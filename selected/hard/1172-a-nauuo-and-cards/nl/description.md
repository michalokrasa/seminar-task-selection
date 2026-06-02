# Nauuo and Cards

## Goal

Find the minimum number of operations to arrange the pile so that cards 1, 2, …, n appear in increasing order from top to bottom.

## Rules

- There are `2n` cards: `n` numbered cards (1–n) and `n` empty cards (represented as 0).
- `n` cards are in Nauuo's **hand**; the remaining `n` form a **pile** ordered top to bottom.
- Each numbered card appears exactly once (either in hand or pile).
- In one **operation**: choose any card from hand → place it at the **bottom** of the pile → draw the **top** card from the pile into hand.
- The goal state is a pile of [1, 2, 3, …, n] (top to bottom).
- Find the minimum number of operations to reach the goal.

## Input / Output

- **Input**: first line `n`; second line — `n` integers (hand); third line — `n` integers (pile, top to bottom). `0` = empty card.
- **Output**: a single integer — the minimum number of operations.
