# 1512_A. Spy Detected!

## Problem Description
You are given an array a consisting of n (n ≥ 3) positive integers. It is known that in this array, all the numbers except one are the same (for example, in the array [4, 11, 4, 4] all numbers except one are equal to 4).

Print the index of the element that does not equal others. The numbers in the array are numbered from one.

Input

The first line contains a single integer t (1 ≤ t ≤ 100). Then t test cases follow.

The first line of each test case contains a single integer n (3 ≤ n ≤ 100) — the length of the array a.

The second line of each test case contains n integers a_1, a_2, …, a_n (1 ≤ a_i ≤ 100).

It is guaranteed that all the numbers except one in the a array are the same.

Output

For each test case, output a single integer — the index of the element that is not equal to others.

Example

Input


4
4
11 13 11 11
5
1 4 4 4 4
10
3 3 3 3 10 3 3 3 3 3
3
20 20 10


Output


2
1
5
3

## Contest Information
- **Contest ID**: 1512
- **Problem Index**: A
- **Points**: 0.0
- **Rating**: 800
- **Tags**: brute force, implementation
- **Time Limit**: {'seconds': 2, 'nanos': 0} seconds
- **Memory Limit**: 256000000 bytes

## Task
Solve this competitive programming problem. Write your Python solution to `/app/solution.py`.

Your solution must:
1. Read input from standard input (stdin)
2. Write output to standard output (stdout)
3. Handle all the given constraints and edge cases
4. Be saved to `/app/solution.py`

## Test Cases
The solution will be validated against multiple test cases.