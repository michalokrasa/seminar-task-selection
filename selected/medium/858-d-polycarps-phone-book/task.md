# 858_D. Polycarp's phone book

## Problem Description
There are n phone numbers in Polycarp's contacts on his phone. Each number is a 9-digit integer, starting with a digit different from 0. All the numbers are distinct.

There is the latest version of Berdroid OS installed on Polycarp's phone. If some number is entered, is shows up all the numbers in the contacts for which there is a substring equal to the entered sequence of digits. For example, is there are three phone numbers in Polycarp's contacts: 123456789, 100000000 and 100123456, then:

  * if he enters 00 two numbers will show up: 100000000 and 100123456, 
  * if he enters 123 two numbers will show up 123456789 and 100123456, 
  * if he enters 01 there will be only one number 100123456. 



For each of the phone numbers in Polycarp's contacts, find the minimum in length sequence of digits such that if Polycarp enters this sequence, Berdroid shows this only phone number.

Input

The first line contains single integer n (1 ≤ n ≤ 70000) — the total number of phone contacts in Polycarp's contacts.

The phone numbers follow, one in each line. Each number is a positive 9-digit integer starting with a digit from 1 to 9. All the numbers are distinct.

Output

Print exactly n lines: the i-th of them should contain the shortest non-empty sequence of digits, such that if Polycarp enters it, the Berdroid OS shows up only the i-th number from the contacts. If there are several such sequences, print any of them.

Examples

Input

3
123456789
100000000
100123456


Output

9
000
01


Input

4
123456789
193456789
134567819
934567891


Output

2
193
81
91

## Contest Information
- **Contest ID**: 858
- **Problem Index**: D
- **Points**: 2000.0
- **Rating**: 1600
- **Tags**: data structures, implementation, sortings
- **Time Limit**: {'seconds': 4, 'nanos': 0} seconds
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