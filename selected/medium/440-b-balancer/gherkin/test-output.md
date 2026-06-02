# medium/440-b-balancer

**Status:** PASS

## stdout

```
============================= test session starts ==============================
platform linux -- Python 3.10.18, pytest-7.4.4, pluggy-1.6.0
PyQt5 5.15.10 -- Qt runtime 5.15.17 -- Qt compiled 5.15.2
rootdir: /tmp/tmp9xy4o0_w
configfile: pytest.ini
plugins: Faker-25.1.0, anyio-4.9.0, cov-5.0.0, mock-3.12.0, qt-4.3.1
collected 1 item

tmpcjuat41a.py::test_code_contest_solution 
============================================================
Test 1/10
============================================================
Input:
6
1 6 2 5 3 7


Expected Output:
12


Actual Output from /app/solution.py:
12

✓ Test 1 PASSED - Output matches expected!

============================================================
Test 2/10
============================================================
Input:
20
1 1 1 1 1 1 1 1 1 1 999999999 999999999 999999999 999999999 999999999 999999999 999999999 999999999 999999999 999999999


Expected Output:
49999999900


Actual Output from /app/solution.py:
49999999900

✓ Test 2 PASSED - Output matches expected!

============================================================
Test 3/10
============================================================
Input:
20
1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 2 2 2 2 2 2 2 2 2 2


Expected Output:
49999999900


Actual Output from /app/solution.py:
49999999900

✓ Test 3 PASSED - Output matches expected!

============================================================
Test 4/10
============================================================
Input:
2
0 1000000000


Expected Output:
500000000


Actual Output from /app/solution.py:
500000000

✓ Test 4 PASSED - Output matches expected!

============================================================
Test 5/10
============================================================
Input:
4
0 0 0 0


Expected Output:
0


Actual Output from /app/solution.py:
0

✓ Test 5 PASSED - Output matches expected!

============================================================
Test 6/10
============================================================
Input:
6
0 0 0 6 6 6


Expected Output:
27


Actual Output from /app/solution.py:
27

✓ Test 6 PASSED - Output matches expected!

============================================================
Test 7/10
============================================================
Input:
6
6 6 6 0 0 0


Expected Output:
27


Actual Output from /app/solution.py:
27

✓ Test 7 PASSED - Output matches expected!

============================================================
Test 8/10
============================================================
Input:
2
20180000 0


Expected Output:
10090000


Actual Output from /app/solution.py:
10090000

✓ Test 8 PASSED - Output matches expected!

============================================================
Test 9/10
============================================================
Input:
5
0 0 0 0 0


Expected Output:
0


Actual Output from /app/solution.py:
0

✓ Test 9 PASSED - Output matches expected!

============================================================
Test 10/10
============================================================
Input:
1
0


Expected Output:
0


Actual Output from /app/solution.py:
0

✓ Test 10 PASSED - Output matches expected!

✓ All 10 tests passed!
PASSED

============================== 1 passed in 1.91s ===============================
```
