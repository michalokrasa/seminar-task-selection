# medium/858-d-polycarps-phone-book

**Status:** PASS

## stdout

```
============================= test session starts ==============================
platform linux -- Python 3.10.18, pytest-7.4.4, pluggy-1.6.0
PyQt5 5.15.10 -- Qt runtime 5.15.17 -- Qt compiled 5.15.2
rootdir: /tmp/tmpxzbq1wy0
configfile: pytest.ini
plugins: Faker-25.1.0, anyio-4.9.0, cov-5.0.0, mock-3.12.0, qt-4.3.1
collected 1 item

tmph0v4y_2z.py::test_code_contest_solution 
============================================================
Test 1/10
============================================================
Input:
3
123456789
100000000
100123456


Expected Output:
7
000
01


Actual Output from /app/solution.py:
7
000
01

✓ Test 1 PASSED - Output matches expected!

============================================================
Test 2/10
============================================================
Input:
4
123456789
193456789
134567819
934567891


Expected Output:
2
193
13
91


Actual Output from /app/solution.py:
2
193
13
91

✓ Test 2 PASSED - Output matches expected!

============================================================
Test 3/10
============================================================
Input:
3
638631659
929648227
848163730


Expected Output:
5
2
0


Actual Output from /app/solution.py:
5
2
0

✓ Test 3 PASSED - Output matches expected!

============================================================
Test 4/10
============================================================
Input:
5
567323818
353474649
468171032
989223926
685081078


Expected Output:
56
35
17
98
85


Actual Output from /app/solution.py:
56
35
17
98
85

✓ Test 4 PASSED - Output matches expected!

============================================================
Test 5/10
============================================================
Input:
5
774610315
325796798
989859836
707706423
310546337


Expected Output:
74
32
89
70
05


Actual Output from /app/solution.py:
74
32
89
70
05

✓ Test 5 PASSED - Output matches expected!

============================================================
Test 6/10
============================================================
Input:
10
181033039
210698534
971006898
391227170
323096464
560766866
377374442
654389922
544146403
779261493


Expected Output:
18
21
97
91
32
56
37
65
41
79


Actual Output from /app/solution.py:
18
21
97
91
32
56
37
65
41
79

✓ Test 6 PASSED - Output matches expected!

============================================================
Test 7/10
============================================================
Input:
10
506504092
561611075
265260859
557114891
838578824
985006846
456984731
856424964
658005674
666280709


Expected Output:
04
61
26
55
83
68
45
64
58
66


Actual Output from /app/solution.py:
04
61
26
55
83
68
45
64
58
66

✓ Test 7 PASSED - Output matches expected!

============================================================
Test 8/10
============================================================
Input:
5
139127034
452751056
193432721
894001929
426470953


Expected Output:
13
45
93
8
42


Actual Output from /app/solution.py:
13
45
93
8
42

✓ Test 8 PASSED - Output matches expected!

============================================================
Test 9/10
============================================================
Input:
10
197120216
680990683
319631438
442393410
888300189
170777450
164487872
487350759
651751346
652859411


Expected Output:
97
68
31
42
88
70
64
73
51
52


Actual Output from /app/solution.py:
97
68
31
42
88
70
64
73
51
52

✓ Test 9 PASSED - Output matches expected!

============================================================
Test 10/10
============================================================
Input:
4
898855826
343430636
210120107
467957087


Expected Output:
89
3
1
46


Actual Output from /app/solution.py:
89
3
1
46

✓ Test 10 PASSED - Output matches expected!

✓ All 10 tests passed!
PASSED

============================== 1 passed in 1.85s ===============================
```
