# Sysadmin Bob

## Goal

Given a string formed by concatenating valid email addresses (with all commas removed), reconstruct any valid comma-separated list of email addresses that could have produced it, or report that no solution exists.

## Rules

- A valid email address has the form `A@B` where `A` and `B` are non-empty strings of lowercase Latin letters.
- The input string contains only lowercase Latin letters and `@` characters.
- Each `@` in the input must belong to exactly one email address (as its separator).
- Both the local part (before `@`) and the domain part (after `@`) of every address must be non-empty.
- If multiple valid decompositions exist, output any one of them.
- If no valid decomposition exists, output `No solution`.

## Input / Output

- **Input**: a single string of length 1–200 consisting of lowercase letters and `@`.
- **Output**: a comma-separated list of valid email addresses, or `No solution`.
