# hard/72-b-ini-file

**Status:** PASS

## stdout

```
============================= test session starts ==============================
platform linux -- Python 3.10.18, pytest-7.4.4, pluggy-1.6.0
PyQt5 5.15.10 -- Qt runtime 5.15.17 -- Qt compiled 5.15.2
rootdir: /tmp/tmpgz_jngdx
configfile: pytest.ini
plugins: Faker-25.1.0, anyio-4.9.0, cov-5.0.0, mock-3.12.0, qt-4.3.1
collected 1 item

tmp9gg5s1eo.py::test_code_contest_solution 
============================================================
Test 1/1
============================================================
Input:
11
a= 1
b=a
a = 2
 ; comment
[z]
1=2
[y]
2=3
[z]
2=1
[w]


Expected Output:
a=2
b=a
[w]
[y]
2=3
[z]
1=2
2=1


Actual Output from /app/solution.py:
a=2
b=a
[w]
[y]
2=3
[z]
1=2
2=1

✓ Test 1 PASSED - Output matches expected!

✓ All 1 tests passed!
PASSED

============================== 1 passed in 0.44s ===============================
```
