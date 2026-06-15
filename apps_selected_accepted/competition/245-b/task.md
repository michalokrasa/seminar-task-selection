# CF 245/B

## Problem Description
Vasya is an active Internet user. One day he came across an Internet resource he liked, so he wrote its address in the notebook. We know that the address of the written resource has format: <protocol>://<domain>.ru[/<context>] 

where:  <protocol> can equal either "http" (without the quotes) or "ftp" (without the quotes),  <domain> is a non-empty string, consisting of lowercase English letters,  the /<context> part may not be present. If it is present, then <context> is a non-empty string, consisting of lowercase English letters. 

If string <context> isn't present in the address, then the additional character "/" isn't written. Thus, the address has either two characters "/" (the ones that go before the domain), or three (an extra one in front of the context).

When the boy came home, he found out that the address he wrote in his notebook had no punctuation marks. Vasya must have been in a lot of hurry and didn't write characters ":", "/", ".".

Help Vasya to restore the possible address of the recorded Internet resource.


-----Input-----

The first line contains a non-empty string that Vasya wrote out in his notebook. This line consists of lowercase English letters only. 

It is guaranteed that the given string contains at most 50 letters. It is guaranteed that the given string can be obtained from some correct Internet resource address, described above.


-----Output-----

Print a single line — the address of the Internet resource that Vasya liked. If there are several addresses that meet the problem limitations, you are allowed to print any of them.


-----Examples-----
Input
httpsunrux

Output
http://sun.ru/x

Input
ftphttprururu

Output
ftp://http.ru/ruru



-----Note-----

In the second sample there are two more possible answers: "ftp://httpruru.ru" and "ftp://httpru.ru/ru".

## Contest Information
- **URL**: https://codeforces.com/problemset/problem/245/B
- **Difficulty**: competition
- **Tags**: implementation, strings
- **Contest ID**: 245
- **Problem Index**: B
- **Number of Tests**: 20
- **Number of Solutions**: 17

## Task
Solve this competitive programming problem. Write your Python solution to `/app/solution.py`.

Your solution must:
1. Read input from standard input (stdin)
2. Write output to standard output (stdout)
3. Handle all the given constraints and edge cases
4. Be saved to `/app/solution.py`

## Test Cases
The solution will be validated against multiple test cases.
