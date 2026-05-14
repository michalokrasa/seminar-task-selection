# 31_B. Sysadmin Bob

## Problem Description
Email address in Berland is a string of the form A@B, where A and B are arbitrary strings consisting of small Latin letters. 

Bob is a system administrator in «Bersoft» company. He keeps a list of email addresses of the company's staff. This list is as a large string, where all addresses are written in arbitrary order, separated by commas. The same address can be written more than once.

Suddenly, because of unknown reasons, all commas in Bob's list disappeared. Now Bob has a string, where all addresses are written one after another without any separators, and there is impossible to determine, where the boundaries between addresses are. Unfortunately, on the same day his chief asked him to bring the initial list of addresses. Now Bob wants to disjoin addresses in some valid way. Help him to do that.

Input

The first line contains the list of addresses without separators. The length of this string is between 1 and 200, inclusive. The string consists only from small Latin letters and characters «@».

Output

If there is no list of the valid (according to the Berland rules) email addresses such that after removing all commas it coincides with the given string, output No solution. In the other case, output the list. The same address can be written in this list more than once. If there are several solutions, output any of them.

Examples

Input

a@aa@a


Output

a@a,a@a


Input

a@a@a


Output

No solution


Input

@aa@a


Output

No solution

## Contest Information
- **Contest ID**: 31
- **Problem Index**: B
- **Points**: 1000.0
- **Rating**: 1500
- **Tags**: greedy, implementation, strings
- **Time Limit**: {'seconds': 0, 'nanos': 500000000} seconds
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