# 1101_E. Polycarp's New Job

## Problem Description
Polycarp has recently got himself a new job. He now earns so much that his old wallet can't even store all the money he has.

Berland bills somehow come in lots of different sizes. However, all of them are shaped as rectangles (possibly squares). All wallets are also produced in form of rectangles (possibly squares).

A bill x × y fits into some wallet h × w if either x ≤ h and y ≤ w or y ≤ h and x ≤ w. Bills can overlap with each other in a wallet and an infinite amount of bills can fit into a wallet. That implies that all the bills Polycarp currently have fit into a wallet if every single one of them fits into it independently of the others.

Now you are asked to perform the queries of two types:

  1. +~x~y — Polycarp earns a bill of size x × y; 
  2. ?~h~w — Polycarp wants to check if all the bills he has earned to this moment fit into a wallet of size h × w. 



It is guaranteed that there is at least one query of type 1 before the first query of type 2 and that there is at least one query of type 2 in the input data.

For each query of type 2 print "YES" if all the bills he has earned to this moment fit into a wallet of given size. Print "NO" otherwise.

Input

The first line contains a single integer n (2 ≤ n ≤ 5 ⋅ 10^5) — the number of queries.

Each of the next n lines contains a query of one of these two types:

  1. +~x~y (1 ≤ x, y ≤ 10^9) — Polycarp earns a bill of size x × y; 
  2. ?~h~w (1 ≤ h, w ≤ 10^9) — Polycarp wants to check if all the bills he has earned to this moment fit into a wallet of size h × w. 



It is guaranteed that there is at least one query of type 1 before the first query of type 2 and that there is at least one query of type 2 in the input data.

Output

For each query of type 2 print "YES" if all the bills he has earned to this moment fit into a wallet of given size. Print "NO" otherwise.

Example

Input


9
+ 3 2
+ 2 3
? 1 20
? 3 3
? 2 3
+ 1 5
? 10 10
? 1 5
+ 1 1


Output


NO
YES
YES
YES
NO

Note

The queries of type 2 of the example:

  1. Neither bill fits; 
  2. Both bills fit (just checking that you got that bills can overlap); 
  3. Both bills fit (both bills are actually the same); 
  4. All bills fit (too much of free space in a wallet is not a problem); 
  5. Only bill 1 × 5 fit (all the others don't, thus it's "NO"). 

## Contest Information
- **Contest ID**: 1101
- **Problem Index**: E
- **Points**: 0.0
- **Rating**: 1500
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