# Shockers

## Goal

Count the number of electric shocks Valentin received **after** the secret letter could have been uniquely identified — i.e., the number of excessive shocks.

## Rules

- The jury has chosen one secret letter from the alphabet.
- Actions are processed in order:
  - **`. word`**: Valentin said `word` and was NOT shocked → the secret letter is **not** in `word`; remove all letters in `word` from the candidate set.
  - **`! word`**: Valentin said `word` and WAS shocked → the secret letter IS in `word`; keep only letters that are in `word` (intersect candidates with `word`'s letters).
  - **`? letter`**: Valentin guessed `letter`; if this is not the last action it is an incorrect guess → remove `letter` from the candidate set. This action itself counts as a shock if it occurs after the letter was uniquely determined.
- The letter is **uniquely determined** from the moment the candidate set shrinks to exactly 1 letter.
- Count every shock (from `!` actions and incorrect `?` actions) that occurs **strictly after** the point of unique determination.

## Input / Output

- **Input**: first line is `n` (1 ≤ n ≤ 10^5); each of the next `n` lines is an action string.
- **Output**: a single integer — the number of excessive electric shocks.
