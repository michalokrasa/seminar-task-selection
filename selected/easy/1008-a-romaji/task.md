# 1008_A. Romaji

## Problem Description
Vitya has just started learning Berlanese language. It is known that Berlanese uses the Latin alphabet. Vowel letters are "a", "o", "u", "i", and "e". Other letters are consonant.

In Berlanese, there has to be a vowel after every consonant, but there can be any letter after any vowel. The only exception is a consonant "n"; after this letter, there can be any letter (not only a vowel) or there can be no letter at all. For example, the words "harakiri", "yupie", "man", and "nbo" are Berlanese while the words "horse", "king", "my", and "nz" are not.

Help Vitya find out if a word s is Berlanese.

Input

The first line of the input contains the string s consisting of |s| (1≤ |s|≤ 100) lowercase Latin letters.

Output

Print "YES" (without quotes) if there is a vowel after every consonant except "n", otherwise print "NO".

You can print each letter in any case (upper or lower).

Examples

Input

sumimasen


Output

YES


Input

ninja


Output

YES


Input

codeforces


Output

NO

Note

In the first and second samples, a vowel goes after each consonant except "n", so the word is Berlanese.

In the third sample, the consonant "c" goes after the consonant "r", and the consonant "s" stands on the end, so the word is not Berlanese.

## Contest Information
- **Contest ID**: 1008
- **Problem Index**: A
- **Points**: 500.0
- **Rating**: 900
- **Tags**: implementation, strings
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