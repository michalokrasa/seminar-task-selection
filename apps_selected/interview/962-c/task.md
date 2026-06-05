# CF 962/C

## Problem Description
You are given a positive integer $n$, written without leading zeroes (for example, the number 04 is incorrect). 

In one operation you can delete any digit of the given integer so that the result remains a positive integer without leading zeros.

Determine the minimum number of operations that you need to consistently apply to the given integer $n$ to make from it the square of some positive integer or report that it is impossible.

An integer $x$ is the square of some positive integer if and only if $x=y^2$ for some positive integer $y$.


-----Input-----

The first line contains a single integer $n$ ($1 \le n \le 2 \cdot 10^{9}$). The number is given without leading zeroes.


-----Output-----

If it is impossible to make the square of some positive integer from $n$, print -1. In the other case, print the minimal number of operations required to do it.


-----Examples-----
Input
8314

Output
2

Input
625

Output
0

Input
333

Output
-1



-----Note-----

In the first example we should delete from $8314$ the digits $3$ and $4$. After that $8314$ become equals to $81$, which is the square of the integer $9$.

In the second example the given $625$ is the square of the integer $25$, so you should not delete anything. 

In the third example it is impossible to make the square from $333$, so the answer is -1.

## Contest Information
- **URL**: https://codeforces.com/problemset/problem/962/C
- **Difficulty**: interview
- **Tags**: brute force, implementation, math
- **Contest ID**: 962
- **Problem Index**: C
- **Number of Tests**: 70
- **Number of Solutions**: 22

## Task
Solve this competitive programming problem. Write your Python solution to `/app/solution.py`.

Your solution must:
1. Read input from standard input (stdin)
2. Write output to standard output (stdout)
3. Handle all the given constraints and edge cases
4. Be saved to `/app/solution.py`

## Test Cases
The solution will be validated against multiple test cases.
