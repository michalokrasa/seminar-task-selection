# CF 883/H

## Problem Description
Kolya has a string s of length n consisting of lowercase and uppercase Latin letters and digits.

He wants to rearrange the symbols in s and cut it into the minimum number of parts so that each part is a palindrome and all parts have the same lengths. A palindrome is a string which reads the same backward as forward, such as madam or racecar.

Your task is to help Kolya and determine the minimum number of palindromes of equal lengths to cut s into, if it is allowed to rearrange letters in s before cuttings.


-----Input-----

The first line contains an integer n (1 ≤ n ≤ 4·10^5) — the length of string s.

The second line contains a string s of length n consisting of lowercase and uppercase Latin letters and digits.


-----Output-----

Print to the first line an integer k — minimum number of palindromes into which you can cut a given string.

Print to the second line k strings — the palindromes themselves. Separate them by a space. You are allowed to print palindromes in arbitrary order. All of them should have the same length.


-----Examples-----
Input
6
aabaac

Output
2
aba aca 
Input
8
0rTrT022

Output
1
02TrrT20 
Input
2
aA

Output
2
a A

## Contest Information
- **URL**: https://codeforces.com/problemset/problem/883/H
- **Difficulty**: competition
- **Tags**: brute force, implementation, strings
- **Contest ID**: 883
- **Problem Index**: H
- **Number of Tests**: 27
- **Number of Solutions**: 14

## Task
Solve this competitive programming problem. Write your Python solution to `/app/solution.py`.

Your solution must:
1. Read input from standard input (stdin)
2. Write output to standard output (stdout)
3. Handle all the given constraints and edge cases
4. Be saved to `/app/solution.py`

## Test Cases
The solution will be validated against multiple test cases.
