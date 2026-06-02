# easy/716-a-crazy-computer

**Status:** PASS

## stdout

```
============================= test session starts ==============================
platform linux -- Python 3.10.18, pytest-7.4.4, pluggy-1.6.0
PyQt5 5.15.10 -- Qt runtime 5.15.17 -- Qt compiled 5.15.2
rootdir: /tmp/tmpclzgdxfx
configfile: pytest.ini
plugins: Faker-25.1.0, anyio-4.9.0, cov-5.0.0, mock-3.12.0, qt-4.3.1
collected 1 item

tmp4m8xnpwa.py::test_code_contest_solution 
============================================================
Test 1/10
============================================================
Input:
6 1
1 3 5 7 9 10


Expected Output:
2


Actual Output from /app/solution.py:
2

✓ Test 1 PASSED - Output matches expected!

============================================================
Test 2/10
============================================================
Input:
6 5
1 3 8 14 19 20


Expected Output:
3


Actual Output from /app/solution.py:
3

✓ Test 2 PASSED - Output matches expected!

============================================================
Test 3/10
============================================================
Input:
2 1000000000
1 1000000000


Expected Output:
2


Actual Output from /app/solution.py:
2

✓ Test 3 PASSED - Output matches expected!

============================================================
Test 4/10
============================================================
Input:
2 1
1 100


Expected Output:
1


Actual Output from /app/solution.py:
1

✓ Test 4 PASSED - Output matches expected!

============================================================
Test 5/10
============================================================
Input:
5 5
1 7 12 13 14


Expected Output:
4


Actual Output from /app/solution.py:
4

✓ Test 5 PASSED - Output matches expected!

============================================================
Test 6/10
============================================================
Input:
3 5
1 10 20


Expected Output:
1


Actual Output from /app/solution.py:
1

✓ Test 6 PASSED - Output matches expected!

============================================================
Test 7/10
============================================================
Input:
1 1
1000000000


Expected Output:
1


Actual Output from /app/solution.py:
1

✓ Test 7 PASSED - Output matches expected!

============================================================
Test 8/10
============================================================
Input:
2 1
1 2


Expected Output:
2


Actual Output from /app/solution.py:
2

✓ Test 8 PASSED - Output matches expected!

============================================================
Test 9/10
============================================================
Input:
3 1
1 2 10


Expected Output:
1


Actual Output from /app/solution.py:
1

✓ Test 9 PASSED - Output matches expected!

============================================================
Test 10/10
============================================================
Input:
3 10
1 2 3


Expected Output:
3


Actual Output from /app/solution.py:
3

✓ Test 10 PASSED - Output matches expected!

✓ All 10 tests passed!
PASSED

============================== 1 passed in 1.79s ===============================
```
