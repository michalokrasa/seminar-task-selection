# CF 977/B

## Problem Description

Two-gram is an ordered pair (i.e. string of length two) of capital Latin letters. For example, "AZ", "AA", "ZA" — three distinct two-grams.

You are given a string $s$ consisting of $n$ capital Latin letters. Your task is to find any two-gram contained in the given string as a substring (i.e. two consecutive characters of the string) maximal number of times. For example, for string $s$ = "BBAABBBA" the answer is two-gram "BB", which is contained in $s$ three times. In other words, find any most frequent two-gram.

Note that occurrences of the two-gram can overlap with each other.

### Input

The first line of the input contains integer number $n$ ($2 \le n \le 100$) — the length of string $s$. The second line of the input contains the string $s$ consisting of $n$ capital Latin letters.

### Output

Print the only line containing exactly two capital Latin letters — any two-gram contained in the given string $s$ as a substring (i.e. two consecutive characters of the string) maximal number of times.

### Examples

Input

```
7
ABACABA
```

Output

```
AB
```

---

Input

```
5
ZZZAA
```

Output

```
ZZ
```

### Note

In the first example "BA" is also valid answer.

In the second example the only two-gram "ZZ" can be printed because it contained in the string "ZZZAA" two times.

## Contest Information

- **URL**: https://codeforces.com/problemset/problem/977/B
- **Difficulty**: introductory
- **Tags**: implementation, strings
- **Contest ID**: 977
- **Problem Index**: B
- **Number of Tests**: 22
- **Number of Solutions**: 1

## Task

Solve this competitive programming problem. Write your Python solution to `/app/solution.py`.

Your solution must:

1. Read input from standard input (stdin)
2. Write output to standard output (stdout)
3. Handle all the given constraints and edge cases
4. Be saved to `/app/solution.py`

## Test Cases

The solution will be validated against multiple test cases.
