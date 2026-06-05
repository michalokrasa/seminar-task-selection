# CF 960/A

## Problem Description
A has a string consisting of some number of lowercase English letters 'a'. He gives it to his friend B who appends some number of letters 'b' to the end of this string. Since both A and B like the characters 'a' and 'b', they have made sure that at this point, at least one 'a' and one 'b' exist in the string.

B now gives this string to C and he appends some number of letters 'c' to the end of the string. However, since C is a good friend of A and B, the number of letters 'c' he appends is equal to the number of 'a' or to the number of 'b' in the string. It is also possible that the number of letters 'c' equals both to the number of letters 'a' and to the number of letters 'b' at the same time.

You have a string in your hands, and you want to check if it is possible to obtain the string in this way or not. If it is possible to obtain the string, print "YES", otherwise print "NO" (without the quotes).


-----Input-----

The first and only line consists of a string $S$ ($ 1 \le |S| \le 5\,000 $). It is guaranteed that the string will only consist of the lowercase English letters 'a', 'b', 'c'.


-----Output-----

Print "YES" or "NO", according to the condition.


-----Examples-----
Input
aaabccc

Output
YES

Input
bbacc

Output
NO

Input
aabc

Output
YES



-----Note-----

Consider first example: the number of 'c' is equal to the number of 'a'. 

Consider second example: although the number of 'c' is equal to the number of the 'b', the order is not correct.

Consider third example: the number of 'c' is equal to the number of 'b'.

## Contest Information
- **URL**: https://codeforces.com/problemset/problem/960/A
- **Difficulty**: competition
- **Tags**: implementation
- **Contest ID**: 960
- **Problem Index**: A
- **Number of Tests**: 42
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
