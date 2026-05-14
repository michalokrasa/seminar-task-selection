# medium/749-c-voting

**Status:** PASS

## stdout

```
============================= test session starts ==============================
platform linux -- Python 3.10.18, pytest-7.4.4, pluggy-1.6.0
PyQt5 5.15.10 -- Qt runtime 5.15.17 -- Qt compiled 5.15.2
rootdir: /tmp/tmpfzhtsi4d
configfile: pytest.ini
plugins: Faker-25.1.0, anyio-4.9.0, cov-5.0.0, mock-3.12.0, qt-4.3.1
collected 1 item

tmpp9_l90ka.py::test_code_contest_solution 
============================================================
Test 1/10
============================================================
Input:
5
DDRRR


Expected Output:
D


Actual Output from /app/solution.py:
D

✓ Test 1 PASSED - Output matches expected!

============================================================
Test 2/10
============================================================
Input:
6
DDRRRR


Expected Output:
R


Actual Output from /app/solution.py:
R

✓ Test 2 PASSED - Output matches expected!

============================================================
Test 3/10
============================================================
Input:
1
R


Expected Output:
R


Actual Output from /app/solution.py:
R

✓ Test 3 PASSED - Output matches expected!

============================================================
Test 4/10
============================================================
Input:
7
DDRRRRD


Expected Output:
R


Actual Output from /app/solution.py:
R

✓ Test 4 PASSED - Output matches expected!

============================================================
Test 5/10
============================================================
Input:
6
RDDRDR


Expected Output:
D


Actual Output from /app/solution.py:
D

✓ Test 5 PASSED - Output matches expected!

============================================================
Test 6/10
============================================================
Input:
21
DDDDRRRRRDRDRDRDRDRDR


Expected Output:
R


Actual Output from /app/solution.py:
R

✓ Test 6 PASSED - Output matches expected!

============================================================
Test 7/10
============================================================
Input:
7
RRRDDDD


Expected Output:
R


Actual Output from /app/solution.py:
R

✓ Test 7 PASSED - Output matches expected!

============================================================
Test 8/10
============================================================
Input:
7
DDRRRDR


Expected Output:
R


Actual Output from /app/solution.py:
R

✓ Test 8 PASSED - Output matches expected!

============================================================
Test 9/10
============================================================
Input:
100
RRDRRDDDDDDDRDRRRDRDRDDDRDDDRDDRDRRDRRRDRRDRRRRRRRDRRRRRRDDDRRDDRRRDRRRDDRRDRRDDDDDRRDRDDRDDRRRDRRDD


Expected Output:
R


Actual Output from /app/solution.py:
R

✓ Test 9 PASSED - Output matches expected!

============================================================
Test 10/10
============================================================
Input:
8
RDDRDRRD


Expected Output:
R


Actual Output from /app/solution.py:
R

✓ Test 10 PASSED - Output matches expected!

✓ All 10 tests passed!
PASSED

============================== 1 passed in 1.94s ===============================
```
