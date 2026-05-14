# 1095_E. Almost Regular Bracket Sequence

## Problem Description
You are given a bracket sequence s consisting of n opening '(' and closing ')' brackets.

A regular bracket sequence is a bracket sequence that can be transformed into a correct arithmetic expression by inserting characters '1' and '+' between the original characters of the sequence. For example, bracket sequences "()()", "(())" are regular (the resulting expressions are: "(1)+(1)", "((1+1)+1)"), and ")(" and "(" are not.

You can change the type of some bracket s_i. It means that if s_i =  ')' then you can change it to '(' and vice versa.

Your task is to calculate the number of positions i such that if you change the type of the i-th bracket, then the resulting bracket sequence becomes regular.

Input

The first line of the input contains one integer n (1 ≤ n ≤ 10^6) — the length of the bracket sequence.

The second line of the input contains the string s consisting of n opening '(' and closing ')' brackets.

Output

Print one integer — the number of positions i such that if you change the type of the i-th bracket, then the resulting bracket sequence becomes regular.

Examples

Input


6
(((())


Output


3


Input


6
()()()


Output


0


Input


1
)


Output


0


Input


8
)))(((((


Output


0

## Contest Information
- **Contest ID**: 1095
- **Problem Index**: E
- **Points**: 0.0
- **Rating**: 1900
- **Tags**: implementation
- **Time Limit**: {'seconds': 3, 'nanos': 0} seconds
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