# CF 765/B

## Problem Description

Kostya likes Codeforces contests very much. However, he is very disappointed that his solutions are frequently hacked. That's why he decided to obfuscate (intentionally make less readable) his code before upcoming contest.

To obfuscate the code, Kostya first looks at the first variable name used in his program and replaces all its occurrences with a single symbol a, then he looks at the second variable name that has not been replaced yet, and replaces all its occurrences with b, and so on. Kostya is well-mannered, so he doesn't use any one-letter names before obfuscation. Moreover, there are at most 26 unique identifiers in his programs.

You are given a list of identifiers of some program with removed spaces and line breaks. Check if this program can be a result of Kostya's obfuscation.

### Input

In the only line of input there is a string S of lowercase English letters (1 ≤ |S| ≤ 500) — the identifiers of a program with removed whitespace characters.

### Output

If this program can be a result of Kostya's obfuscation, print "YES" (without quotes), otherwise print "NO".

### Examples

Input

```
abacaba
```

Output

```
YES
```

---

Input

```
jinotega
```

Output

```
NO
```

### Note

In the first sample case, one possible list of identifiers would be "number string number character number string number". Here how Kostya would obfuscate the program:

replace all occurences of number with a, the result would be "a string a character a string a",

replace all occurences of string with b, the result would be "a b a character a b a",

replace all occurences of character with c, the result would be "a b a c a b a",

all identifiers have been replaced, thus the obfuscation is finished.

## Contest Information

- **URL**: https://codeforces.com/problemset/problem/765/B
- **Difficulty**: competition
- **Tags**: greedy, implementation, strings
- **Contest ID**: 765
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
