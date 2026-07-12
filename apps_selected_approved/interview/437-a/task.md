# CF 437/A

## Problem Description

Once upon a time a child got a test consisting of multiple-choice questions as homework. A multiple-choice question consists of four choices: A, B, C and D. Each choice has a description, and the child should find out the only one that is correct.

Fortunately the child knows how to solve such complicated test. The child will follow the algorithm:

If there is some choice whose description is at least twice shorter than all other descriptions, or at least twice longer than all other descriptions, then the child thinks the choice is great. If there is exactly one great choice then the child chooses it. Otherwise the child chooses C (the child thinks it is the luckiest choice).

You are given a multiple-choice questions, can you predict child's choice?

### Input

The first line starts with "A." (without quotes), then follows the description of choice A. The next three lines contain the descriptions of the other choices in the same format. They are given in order: B, C, D. Please note, that the description goes after prefix "X.", so the prefix must not be counted in description's length.

Each description is non-empty and consists of at most 100 characters. Each character can be either uppercase English letter or lowercase English letter, or "\_".

### Output

Print a single line with the child's choice: "A", "B", "C" or "D" (without quotes).

### Examples

Input

```
A.VFleaKing_is_the_author_of_this_problem
B.Picks_is_the_author_of_this_problem
C.Picking_is_the_author_of_this_problem
D.Ftiasch_is_cute
```

Output

```
D
```

---

Input

```
A.ab
B.abcde
C.ab
D.abc
```

Output

```
C
```

---

Input

```
A.c
B.cc
C.c
D.c
```

Output

```
B
```

### Note

In the first sample, the first choice has length 39, the second one has length 35, the third one has length 37, and the last one has length 15. The choice D (length 15) is twice shorter than all other choices, so it is great choice. There is no other great choices so the child will choose D.

In the second sample, no choice is great, so the child will choose the luckiest choice C.

In the third sample, the choice B (length 2) is twice longer than all other choices, so it is great choice. There is no other great choices so the child will choose B.

## Contest Information

- **URL**: https://codeforces.com/problemset/problem/437/A
- **Difficulty**: interview
- **Tags**: implementation
- **Contest ID**: 437
- **Problem Index**: A
- **Number of Tests**: 35
- **Number of Solutions**: 25

## Task

Solve this competitive programming problem. Write your Python solution to `/app/solution.py`.

Your solution must:

1. Read input from standard input (stdin)
2. Write output to standard output (stdout)
3. Handle all the given constraints and edge cases
4. Be saved to `/app/solution.py`

## Test Cases

The solution will be validated against multiple test cases.
