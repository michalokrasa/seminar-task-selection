# AquaMoon and Strange Sort

## Goal

Determine whether a sequence of numbers can be sorted into non-decreasing order using only the allowed swap operation, with all friends ending up facing right.

## Rules

- Each operation swaps two adjacent friends and flips both their directions.
- All friends start facing right; all must face right after all operations.
- Because each swap flips directions, every element must be moved an **even** number of times in total to restore all directions to right.
- The key insight: elements at odd-indexed positions (0-indexed: 0, 2, 4, …) can only exchange with each other, and similarly for even-indexed positions. Therefore the sorted order of elements at even positions must match their relative order in the original sequence, and likewise for odd positions.
- Print `YES` if such a sequence of operations exists, `NO` otherwise.

## Input / Output

- **Input**: first line is `t` (number of test cases); for each test case, first line is `n`, second line is `n` space-separated integers.
- **Output**: for each test case, print `YES` or `NO`.
