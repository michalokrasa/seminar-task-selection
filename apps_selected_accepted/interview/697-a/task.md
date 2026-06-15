# CF 697/A

## Problem Description
Ted has a pineapple. This pineapple is able to bark like a bulldog! At time t (in seconds) it barks for the first time. Then every s seconds after it, it barks twice with 1 second interval. Thus it barks at times t, t + s, t + s + 1, t + 2s, t + 2s + 1, etc.

 [Image] 

Barney woke up in the morning and wants to eat the pineapple, but he can't eat it when it's barking. Barney plans to eat it at time x (in seconds), so he asked you to tell him if it's gonna bark at that time.


-----Input-----

The first and only line of input contains three integers t, s and x (0 ≤ t, x ≤ 10^9, 2 ≤ s ≤ 10^9) — the time the pineapple barks for the first time, the pineapple barking interval, and the time Barney wants to eat the pineapple respectively.


-----Output-----

Print a single "YES" (without quotes) if the pineapple will bark at time x or a single "NO" (without quotes) otherwise in the only line of output.


-----Examples-----
Input
3 10 4

Output
NO

Input
3 10 3

Output
YES

Input
3 8 51

Output
YES

Input
3 8 52

Output
YES



-----Note-----

In the first and the second sample cases pineapple will bark at moments 3, 13, 14, ..., so it won't bark at the moment 4 and will bark at the moment 3.

In the third and fourth sample cases pineapple will bark at moments 3, 11, 12, 19, 20, 27, 28, 35, 36, 43, 44, 51, 52, 59, ..., so it will bark at both moments 51 and 52.

## Contest Information
- **URL**: https://codeforces.com/problemset/problem/697/A
- **Difficulty**: interview
- **Tags**: implementation, math
- **Contest ID**: 697
- **Problem Index**: A
- **Number of Tests**: 95
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
