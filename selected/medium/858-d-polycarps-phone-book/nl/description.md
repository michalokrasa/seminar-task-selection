# Polycarp's Phone Book

## Goal

For each phone number in Polycarp's contacts, find the **shortest** substring of digits such that entering it into the search returns only that number (i.e., the substring does not appear in any other contact).

## Rules

- Every phone number is a distinct 9-digit integer starting with a non-zero digit.
- A search query matches a number if the query string is a **substring** of that number.
- For each number, find the shortest non-empty substring that is not a substring of any other number.
- If multiple such shortest substrings exist, output any one of them.

## Input / Output

- **Input**: first line is `n` (1 ≤ n ≤ 70 000); each of the next `n` lines is a 9-digit phone number.
- **Output**: `n` lines, the `i`-th containing the shortest unique-identifying substring for the `i`-th number.
