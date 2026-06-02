# medium/1106-b-lunar-new-year-and-food-ordering

**Status:** PASS

## stdout

```
============================= test session starts ==============================
platform linux -- Python 3.10.18, pytest-7.4.4, pluggy-1.6.0
PyQt5 5.15.10 -- Qt runtime 5.15.17 -- Qt compiled 5.15.2
rootdir: /tmp/tmp5qpxgi6s
configfile: pytest.ini
plugins: Faker-25.1.0, anyio-4.9.0, cov-5.0.0, mock-3.12.0, qt-4.3.1
collected 1 item

tmpq17s_2lj.py::test_code_contest_solution 
============================================================
Test 1/10
============================================================
Input:
6 6
6 6 6 6 6 6
6 66 666 6666 66666 666666
1 6
2 13
3 6
4 11
5 6
6 6


Expected Output:
36
11058
99996
4333326
0
0


Actual Output from /app/solution.py:
36
11058
99996
4333326
0
0

✓ Test 1 PASSED - Output matches expected!

============================================================
Test 2/10
============================================================
Input:
8 5
8 6 2 1 4 5 7 5
6 3 3 2 6 2 3 2
2 8
1 4
4 7
3 4
6 10


Expected Output:
22
24
14
10
39


Actual Output from /app/solution.py:
22
24
14
10
39

✓ Test 2 PASSED - Output matches expected!

============================================================
Test 3/10
============================================================
Input:
6 6
6 6 6 6 6 6
6 66 666 6666 66666 666666
1 6
2 6
3 6
4 6
5 6
6 66


Expected Output:
36
396
3996
39996
399996
0


Actual Output from /app/solution.py:
36
396
3996
39996
399996
0

✓ Test 3 PASSED - Output matches expected!

============================================================
Test 4/10
============================================================
Input:
1 1
10000000
284517
1 10000000


Expected Output:
2845170000000


Actual Output from /app/solution.py:
2845170000000

✓ Test 4 PASSED - Output matches expected!

============================================================
Test 5/10
============================================================
Input:
1 1
1
642400
1 1


Expected Output:
642400


Actual Output from /app/solution.py:
642400

✓ Test 5 PASSED - Output matches expected!

============================================================
Test 6/10
============================================================
Input:
1 1
6577865
227563
1 5978566


Expected Output:
1360500414658


Actual Output from /app/solution.py:
1360500414658

✓ Test 6 PASSED - Output matches expected!

============================================================
Test 7/10
============================================================
Input:
5 6
26 75 98 33 53
382051 563872 378058 483440 203755
5 56
3 9
5 38
5 6
2 24
2 2


Expected Output:
11933189
3402522
14366204
2268348
13532928
1127744


Actual Output from /app/solution.py:
11933189
3402522
14366204
2268348
13532928
1127744

✓ Test 7 PASSED - Output matches expected!

============================================================
Test 8/10
============================================================
Input:
10 15
132 138 38 75 14 115 129 68 119 118
728344 513371 120930 757031 137753 453796 348671 185533 966778 521678
4 58
1 8
8 22
3 98
2 111
6 158
2 82
1 170
1 26
1 4
4 76
10 106
5 100
4 116
7 62


Expected Output:
43907798
5826752
4081726
15058400
56984181
67179393
33037922
108948627
13563628
2086712
43648529
96247068
0
0
0


Actual Output from /app/solution.py:
43907798
5826752
4081726
15058400
56984181
67179393
33037922
108948627
13563628
2086712
43648529
96247068
0
0
0

✓ Test 8 PASSED - Output matches expected!

============================================================
Test 9/10
============================================================
Input:
1 1
1
558976
1 1


Expected Output:
558976


Actual Output from /app/solution.py:
558976

✓ Test 9 PASSED - Output matches expected!

============================================================
Test 10/10
============================================================
Input:
1 1
411017
129875
1 8160563


Expected Output:
0


Actual Output from /app/solution.py:
0

✓ Test 10 PASSED - Output matches expected!

✓ All 10 tests passed!
PASSED

============================== 1 passed in 2.08s ===============================
```
