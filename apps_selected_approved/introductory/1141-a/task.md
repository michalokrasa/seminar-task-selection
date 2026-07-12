# CF 1141/A

## Problem Description

Polycarp plays "Game 23". Initially he has a number $n$ and his goal is to transform it to $m$. In one move, he can multiply $n$ by $2$ or multiply $n$ by $3$. He can perform any number of moves.

Print the number of moves needed to transform $n$ to $m$. Print -1 if it is impossible to do so.

It is easy to prove that any way to transform $n$ to $m$ contains the same number of moves (i.e. number of moves doesn't depend on the way of transformation).

### Input

The only line of the input contains two integers $n$ and $m$ ($1 \le n \le m \le 5\cdot10^8$).

### Output

Print the number of moves to transform $n$ to $m$, or -1 if there is no solution.

### Examples

Input

```
120 51840
```

Output

```
7
```

---

Input

```
42 42
```

Output

```
0
```

---

Input

```
48 72
```

Output

```
-1
```

### Note

In the first example, the possible sequence of moves is: $120 \rightarrow 240 \rightarrow 720 \rightarrow 1440 \rightarrow 4320 \rightarrow 12960 \rightarrow 25920 \rightarrow 51840.$ The are $7$ steps in total.

In the second example, no moves are needed. Thus, the answer is $0$.

In the third example, it is impossible to transform $48$ to $72$.

## Contest Information

- **URL**: https://codeforces.com/problemset/problem/1141/A
- **Difficulty**: introductory
- **Tags**: implementation, math
- **Contest ID**: 1141
- **Problem Index**: A
- **Number of Tests**: 77
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
