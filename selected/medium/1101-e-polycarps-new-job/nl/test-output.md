# medium/1101-e-polycarps-new-job

**Status:** PASS

## stdout

```
============================= test session starts ==============================
platform linux -- Python 3.10.18, pytest-7.4.4, pluggy-1.6.0
PyQt5 5.15.10 -- Qt runtime 5.15.17 -- Qt compiled 5.15.2
rootdir: /tmp/tmp76g451_i
configfile: pytest.ini
plugins: Faker-25.1.0, anyio-4.9.0, cov-5.0.0, mock-3.12.0, qt-4.3.1
collected 1 item

tmp9rmt1af8.py::test_code_contest_solution 
============================================================
Test 1/8
============================================================
Input:
9
+ 3 2
+ 2 3
? 1 20
? 3 3
? 2 3
+ 1 5
? 10 10
? 1 5
+ 1 1


Expected Output:
NO
YES
YES
YES
NO


Actual Output from /app/solution.py:
NO
YES
YES
YES
NO

✓ Test 1 PASSED - Output matches expected!

============================================================
Test 2/8
============================================================
Input:
10
+ 47 81
? 18 64
? 49 81
? 87 56
? 31 45
? 22 8
? 16 46
? 13 41
? 30 3
? 62 53


Expected Output:
NO
YES
YES
NO
NO
NO
NO
NO
NO


Actual Output from /app/solution.py:
NO
YES
YES
NO
NO
NO
NO
NO
NO

✓ Test 2 PASSED - Output matches expected!

============================================================
Test 3/8
============================================================
Input:
3
+ 1 5
+ 1 3
? 1 4


Expected Output:
NO


Actual Output from /app/solution.py:
NO

✓ Test 3 PASSED - Output matches expected!

============================================================
Test 4/8
============================================================
Input:
5
+ 9 6
? 4 7
? 10 1
? 5 6
? 5 5


Expected Output:
NO
NO
NO
NO


Actual Output from /app/solution.py:
NO
NO
NO
NO

✓ Test 4 PASSED - Output matches expected!

============================================================
Test 5/8
============================================================
Input:
69
+ 1 2
+ 1 2
+ 1 2
+ 1 2
+ 1 2
+ 1 2
+ 1 2
+ 1 2
+ 1 2
+ 1 2
+ 1 2
+ 1 2
+ 1 2
+ 1 2
+ 1 2
+ 1 2
+ 1 2
+ 1 2
+ 1 2
+ 1 2
+ 1 2
+ 1 2
+ 1 2
+ 1 2
+ 1 2
+ 1 2
+ 1 2
+ 1 2
+ 1 2
+ 1 2
+ 1 2
+ 1 2
+ 1 2
+ 1 2
+ 1 2
+ 1 2
+ 1 2
+ 1 2
+ 1 2
+ 1 2
+ 1 2
+ 1 2
+ 1 2
+ 1 2
+ 1 2
+ 1 2
+ 1 2
+ 1 2
+ 1 2
+ 1 2
+ 1 2
+ 1 2
+ 1 2
+ 1 2
+ 1 2
+ 1 2
+ 1 2
+ 1 2
+ 1 2
+ 1 2
+ 1 2
+ 1 2
+ 1 2
+ 1 2
+ 1 2
+ 1 2
+ 1 2
+ 1 2
? 1 2


Expected Output:
YES


Actual Output from /app/solution.py:
YES

✓ Test 5 PASSED - Output matches expected!

============================================================
Test 6/8
============================================================
Input:
10
+ 29 48
+ 88 49
+ 85 91
+ 63 62
+ 29 20
+ 8 35
+ 11 77
+ 49 21
+ 23 77
? 58 16


Expected Output:
NO


Actual Output from /app/solution.py:
NO

✓ Test 6 PASSED - Output matches expected!

============================================================
Test 7/8
============================================================
Input:
2
+ 2 2
? 2 2


Expected Output:
YES


Actual Output from /app/solution.py:
YES

✓ Test 7 PASSED - Output matches expected!

============================================================
Test 8/8
============================================================
Input:
5
+ 1 7
+ 6 7
+ 8 3
? 10 10
+ 5 4


Expected Output:
YES


Actual Output from /app/solution.py:
YES

✓ Test 8 PASSED - Output matches expected!

✓ All 8 tests passed!
PASSED

============================== 1 passed in 1.45s ===============================
```
