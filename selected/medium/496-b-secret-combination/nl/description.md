# Secret Combination

## Goal

Find the smallest number displayable on a combination lock by pressing two buttons in any order and any number of times.

## Rules

- **Button 1**: adds 1 to every digit simultaneously; digit `9` wraps around to `0`.
- **Button 2**: shifts all digits one position to the right; the last digit becomes the first.
- The lock opens when the display shows the **lexicographically smallest** number reachable (leading zeros are kept; comparison ignores leading zeros).
- Strategy: for each of the 10 possible "add" amounts (0–9), compute the rotated string that is smallest; then pick the globally smallest across all 10 choices.

## Input / Output

- **Input**: first line is `n` (number of digits, 1 ≤ n ≤ 1000); second line is a string of `n` digits.
- **Output**: a single string of `n` digits — the smallest reachable state of the display.
