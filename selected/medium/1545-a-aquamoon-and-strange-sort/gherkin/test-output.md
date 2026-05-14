# medium/1545-a-aquamoon-and-strange-sort

**Status:** PASS

## stdout

```
============================= test session starts ==============================
platform linux -- Python 3.10.18, pytest-7.4.4, pluggy-1.6.0
PyQt5 5.15.10 -- Qt runtime 5.15.17 -- Qt compiled 5.15.2
rootdir: /tmp/tmpzeg1bzyl
configfile: pytest.ini
plugins: Faker-25.1.0, anyio-4.9.0, cov-5.0.0, mock-3.12.0, qt-4.3.1
collected 1 item

tmpj2tyqw26.py::test_code_contest_solution 
============================================================
Test 1/10
============================================================
Input:
3
4
4 3 2 5
4
3 3 2 2
5
1 2 3 5 4


Expected Output:
YES
YES
NO


Actual Output from /app/solution.py:
YES
YES
NO

✓ Test 1 PASSED - Output matches expected!

============================================================
Test 2/10
============================================================
Input:
1
10
9 4 2 8 2 4 2 4 1 9


Expected Output:
NO


Actual Output from /app/solution.py:
NO

✓ Test 2 PASSED - Output matches expected!

============================================================
Test 3/10
============================================================
Input:
1
42
1 1 1 9 4 7 1 5 7 3 1 9 10 10 8 1 10 3 7 6 7 4 10 9 9 9 6 3 4 6 4 4 8 6 2 2 2 5 8 10 7 10


Expected Output:
NO


Actual Output from /app/solution.py:
NO

✓ Test 3 PASSED - Output matches expected!

============================================================
Test 4/10
============================================================
Input:
1
7
3 8 5 8 5 8 5


Expected Output:
NO


Actual Output from /app/solution.py:
NO

✓ Test 4 PASSED - Output matches expected!

============================================================
Test 5/10
============================================================
Input:
1
64
8 7 7 2 4 9 3 7 9 4 7 10 6 7 6 4 9 9 10 2 2 2 10 3 8 9 3 1 5 10 6 5 7 4 3 5 7 10 7 5 8 4 5 7 10 7 10 8 2 3 8 10 1 3 8 3 9 2 9 2 5 10 5 5


Expected Output:
NO


Actual Output from /app/solution.py:
NO

✓ Test 5 PASSED - Output matches expected!

============================================================
Test 6/10
============================================================
Input:
1
10
4 1 4 1 4 1 2 1 2 2


Expected Output:
NO


Actual Output from /app/solution.py:
NO

✓ Test 6 PASSED - Output matches expected!

============================================================
Test 7/10
============================================================
Input:
2
8
1 2 1 2 1 2 1 2
8
1 1 1000 1000 2000 2000 2000 2000


Expected Output:
NO
YES


Actual Output from /app/solution.py:
NO
YES

✓ Test 7 PASSED - Output matches expected!

============================================================
Test 8/10
============================================================
Input:
2
9
2 1 100 100 100 100 100 101 101
4
1 2 101 100


Expected Output:
NO
NO


Actual Output from /app/solution.py:
NO
NO

✓ Test 8 PASSED - Output matches expected!

============================================================
Test 9/10
============================================================
Input:
2
6
2 1 2 1 2 1
7
2 1 2 2 1 2 1


Expected Output:
NO
YES


Actual Output from /app/solution.py:
NO
YES

✓ Test 9 PASSED - Output matches expected!

============================================================
Test 10/10
============================================================
Input:
1
2
4 3


Expected Output:
NO


Actual Output from /app/solution.py:
NO

✓ Test 10 PASSED - Output matches expected!

✓ All 10 tests passed!
PASSED

============================== 1 passed in 1.76s ===============================
```
