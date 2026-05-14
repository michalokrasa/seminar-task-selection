# Nauuo and Votes

## Goal

Determine the outcome of a comment vote given a fixed number of upvotes, downvotes, and undecided voters.

## Rules

- There are `x` confirmed upvoters, `y` confirmed downvoters, and `z` voters whose choice is unknown.
- The result is `"+"` if upvotes strictly outnumber downvotes.
- The result is `"-"` if downvotes strictly outnumber upvotes.
- The result is `"0"` if upvotes and downvotes are equal.
- If different assignments of the `z` unknown voters lead to different outcomes, the result is `"?"` (uncertain).

## Input / Output

- **Input**: three integers `x y z` on a single line (0 ≤ x, y, z ≤ 100).
- **Output**: one of `+`, `-`, `0`, or `?`.
