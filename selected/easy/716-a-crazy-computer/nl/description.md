# Crazy Computer

## Goal

Count how many words remain on the screen after a user finishes typing, given that the screen clears automatically after a period of inactivity.

## Rules

- The computer has a timeout parameter `c` (seconds).
- Words are typed at given timestamps. They accumulate on the screen as long as consecutive timestamps are no more than `c` seconds apart.
- If the gap between two consecutive words exceeds `c` seconds, the screen clears before the new word is added.
- At the end, only the words from the last unbroken streak remain on screen.

## Input / Output

- **Input**: first line contains `n` (number of words) and `c` (timeout in seconds); second line contains `n` strictly increasing timestamps.
- **Output**: a single integer — the number of words visible on screen after the last word is typed.
