# Polycarp's New Job

## Goal

Process a sequence of bill-earning and wallet-check queries. For each check query, determine whether every bill earned so far fits into the specified wallet.

## Rules

- A bill `x × y` fits into wallet `h × w` if either (`x ≤ h` and `y ≤ w`) or (`y ≤ h` and `x ≤ w`). Bills can be rotated but not folded.
- Bills may overlap inside a wallet; infinitely many bills can fit simultaneously.
- All bills must fit independently — each one is checked against the wallet on its own.
- Query type `+ x y` adds a new bill of size `x × y` to the collection.
- Query type `? h w` checks if all currently collected bills fit into wallet `h × w`.

## Input / Output

- **Input**: first line is `n` (number of queries); each of the next `n` lines is either `+ x y` or `? h w`.
- **Output**: for each `?` query, print `YES` or `NO` on its own line.
