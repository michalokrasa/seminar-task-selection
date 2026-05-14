# Reverse It!

## Goal

Reverse the digits of a (potentially very large) integer, stripping leading zeros from both the input and the output.

## Rules

- If the number is **negative**, preserve the minus sign; reverse only the digit string.
- Leading zeros in the **input** are stripped before reversing (e.g., `032` is treated as `32`).
- Leading zeros in the **output** (produced by reversing trailing zeros) are stripped (e.g., reversing `100` gives `1`).
- The number can be up to 10^1000 in absolute value (up to ~10 000 characters).

## Input / Output

- **Input**: a single integer on one line, possibly with a leading minus sign and/or leading zeros.
- **Output**: the reversed integer with no leading zeros (and the minus sign if the input was negative).
