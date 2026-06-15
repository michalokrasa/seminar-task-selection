# CF 622/B

## Problem Description
You are given the current time in 24-hour format hh:mm. Find and print the time after a minutes.

Note that you should find only the time after a minutes, see the examples to clarify the problem statement.

You can read more about 24-hour format here https://en.wikipedia.org/wiki/24-hour_clock.


-----Input-----

The first line contains the current time in the format hh:mm (0 ≤ hh < 24, 0 ≤ mm < 60). The hours and the minutes are given with two digits (the hours or the minutes less than 10 are given with the leading zeroes).

The second line contains integer a (0 ≤ a ≤ 10^4) — the number of the minutes passed.


-----Output-----

The only line should contain the time after a minutes in the format described in the input. Note that you should print exactly two digits for the hours and the minutes (add leading zeroes to the numbers if needed).

See the examples to check the input/output format.


-----Examples-----
Input
23:59
10

Output
00:09

Input
20:20
121

Output
22:21

Input
10:10
0

Output
10:10

## Contest Information
- **URL**: https://codeforces.com/problemset/problem/622/B
- **Difficulty**: interview
- **Tags**: implementation
- **Contest ID**: 622
- **Problem Index**: B
- **Number of Tests**: 59
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
