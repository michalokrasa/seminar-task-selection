# medium/831-e-cards-sorting

**Status:** PASS

## stdout

```
============================= test session starts ==============================
platform linux -- Python 3.10.18, pytest-7.4.4, pluggy-1.6.0
PyQt5 5.15.10 -- Qt runtime 5.15.17 -- Qt compiled 5.15.2
rootdir: /tmp/tmph8zhbkfj
configfile: pytest.ini
plugins: Faker-25.1.0, anyio-4.9.0, cov-5.0.0, mock-3.12.0, qt-4.3.1
collected 1 item

tmpysmx7eol.py::test_code_contest_solution 
============================================================
Test 1/9
============================================================
Input:
4
6 3 1 2


Expected Output:
7


Actual Output from /app/solution.py:
7

✓ Test 1 PASSED - Output matches expected!

============================================================
Test 2/9
============================================================
Input:
1
1000


Expected Output:
1


Actual Output from /app/solution.py:
1

✓ Test 2 PASSED - Output matches expected!

============================================================
Test 3/9
============================================================
Input:
7
3 3 3 3 3 3 3


Expected Output:
7


Actual Output from /app/solution.py:
7

✓ Test 3 PASSED - Output matches expected!

============================================================
Test 4/9
============================================================
Input:
87
12 2 2 10 12 1 5 9 15 2 4 7 7 14 8 10 1 6 7 6 13 15 10 6 2 11 13 1 15 14 8 8 4 7 11 12 3 15 9 2 13 1 7 11 2 1 13 11 8 14 2 2 12 7 13 4 13 3 13 3 11 1 7 13 15 8 12 4 12 4 1 4 9 3 13 12 10 15 14 10 7 7 7 2 7 6 10


Expected Output:
580


Actual Output from /app/solution.py:
580

✓ Test 4 PASSED - Output matches expected!

============================================================
Test 5/9
============================================================
Input:
20
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1


Expected Output:
20


Actual Output from /app/solution.py:
20

✓ Test 5 PASSED - Output matches expected!

============================================================
Test 6/9
============================================================
Input:
30
6283 14661 69188 39640 41261 48019 86266 70517 4592 69008 20602 33339 29980 96844 76008 96294 27120 22671 5243 742 33692 18068 29056 48033 1223 82728 99765 38350 36425 10671


Expected Output:
235


Actual Output from /app/solution.py:
235

✓ Test 6 PASSED - Output matches expected!

============================================================
Test 7/9
============================================================
Input:
100
9 9 72 55 14 8 55 58 35 67 3 18 73 92 41 49 15 60 18 66 9 26 97 47 43 88 71 97 19 34 48 96 79 53 8 24 69 49 12 23 77 12 21 88 66 9 29 13 61 69 54 77 41 13 4 68 37 74 7 6 29 76 55 72 89 4 78 27 29 82 18 83 12 4 32 69 89 85 66 13 92 54 38 5 26 56 17 55 29 4 17 39 29 94 3 67 85 98 21 14


Expected Output:
1805


Actual Output from /app/solution.py:
1805

✓ Test 7 PASSED - Output matches expected!

============================================================
Test 8/9
============================================================
Input:
64
826 142 89 337 897 891 1004 704 281 644 910 852 147 193 289 384 625 695 416 944 162 939 164 1047 359 114 499 99 713 300 268 316 256 404 852 496 373 322 716 202 689 857 936 806 556 153 137 863 1047 678 564 474 282 135 610 176 855 360 814 144 77 112 354 154


Expected Output:
1042


Actual Output from /app/solution.py:
1042

✓ Test 8 PASSED - Output matches expected!

============================================================
Test 9/9
============================================================
Input:
10
4 3 4 3 3 3 4 4 4 3


Expected Output:
15


Actual Output from /app/solution.py:
15

✓ Test 9 PASSED - Output matches expected!

✓ All 9 tests passed!
PASSED

============================== 1 passed in 1.68s ===============================
```
