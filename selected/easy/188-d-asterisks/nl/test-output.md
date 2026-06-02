# easy/188-d-asterisks

**Status:** PASS

## stdout

```
============================= test session starts ==============================
platform linux -- Python 3.10.18, pytest-7.4.4, pluggy-1.6.0
PyQt5 5.15.10 -- Qt runtime 5.15.17 -- Qt compiled 5.15.2
rootdir: /tmp/tmpyqt_bgzv
configfile: pytest.ini
plugins: Faker-25.1.0, anyio-4.9.0, cov-5.0.0, mock-3.12.0, qt-4.3.1
collected 1 item

tmpmjr9o7qi.py::test_code_contest_solution 
============================================================
Test 1/2
============================================================
Input:
3


Expected Output:
*
**
***


Actual Output from /app/solution.py:
*
**
***

✓ Test 1 PASSED - Output matches expected!

============================================================
Test 2/2
============================================================
Input:
6


Expected Output:
*
**
***
****
*****
******


Actual Output from /app/solution.py:
*
**
***
****
*****
******

✓ Test 2 PASSED - Output matches expected!

✓ All 2 tests passed!
PASSED

============================== 1 passed in 0.49s ===============================
```
