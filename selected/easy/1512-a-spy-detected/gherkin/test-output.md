# easy/1512-a-spy-detected

**Status:** PASS

## stdout

```
============================= test session starts ==============================
platform linux -- Python 3.10.18, pytest-7.4.4, pluggy-1.6.0
PyQt5 5.15.10 -- Qt runtime 5.15.17 -- Qt compiled 5.15.2
rootdir: /tmp/tmpnu488ioh
configfile: pytest.ini
plugins: Faker-25.1.0, anyio-4.9.0, cov-5.0.0, mock-3.12.0, qt-4.3.1
collected 1 item

tmpga5m32w6.py::test_code_contest_solution 
============================================================
Test 1/5
============================================================
Input:
4
4
11 13 11 11
5
1 4 4 4 4
10
3 3 3 3 10 3 3 3 3 3
3
20 20 10


Expected Output:

2
1
5
3


Actual Output from /app/solution.py:
2
1
5
3

✓ Test 1 PASSED - Output matches expected!

============================================================
Test 2/5
============================================================
Input:
2
3
5 6 6
3
7 7 6


Expected Output:
1
3


Actual Output from /app/solution.py:
1
3

✓ Test 2 PASSED - Output matches expected!

============================================================
Test 3/5
============================================================
Input:
2
3
4 6 6
3
7 7 6


Expected Output:
1
3


Actual Output from /app/solution.py:
1
3

✓ Test 3 PASSED - Output matches expected!

============================================================
Test 4/5
============================================================
Input:
2
3
4 6 6
3
6 7 6


Expected Output:
1
2


Actual Output from /app/solution.py:
1
2

✓ Test 4 PASSED - Output matches expected!

============================================================
Test 5/5
============================================================
Input:
4
4
11 20 11 11
5
1 4 4 4 4
10
3 3 3 3 10 3 3 3 3 3
3
20 20 10


Expected Output:
2
1
5
3


Actual Output from /app/solution.py:
2
1
5
3

✓ Test 5 PASSED - Output matches expected!

✓ All 5 tests passed!
PASSED

============================== 1 passed in 1.10s ===============================
```
