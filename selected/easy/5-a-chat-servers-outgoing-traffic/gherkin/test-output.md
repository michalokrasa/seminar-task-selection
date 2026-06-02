# easy/5-a-chat-servers-outgoing-traffic

**Status:** PASS

## stdout

```
============================= test session starts ==============================
platform linux -- Python 3.10.18, pytest-7.4.4, pluggy-1.6.0
PyQt5 5.15.10 -- Qt runtime 5.15.17 -- Qt compiled 5.15.2
rootdir: /tmp/tmpsh79r9_j
configfile: pytest.ini
plugins: Faker-25.1.0, anyio-4.9.0, cov-5.0.0, mock-3.12.0, qt-4.3.1
collected 1 item

tmp764dvfp7.py::test_code_contest_solution 
============================================================
Test 1/10
============================================================
Input:
+Mike
Mike:hello
+Kate
+Dmitry
-Dmitry
Kate:hi
-Kate


Expected Output:
9


Actual Output from /app/solution.py:
9

✓ Test 1 PASSED - Output matches expected!

============================================================
Test 2/10
============================================================
Input:
+Mike
-Mike
+Mike
Mike:Hi   I am here
-Mike
+Kate
-Kate


Expected Output:
14


Actual Output from /app/solution.py:
14

✓ Test 2 PASSED - Output matches expected!

============================================================
Test 3/10
============================================================
Input:
+adabacaba
-adabacaba
+aca
aca:caba
-aca
+bacaba
-bacaba
+aba
-aba
+bad


Expected Output:
4


Actual Output from /app/solution.py:
4

✓ Test 3 PASSED - Output matches expected!

============================================================
Test 4/10
============================================================
Input:
+cab
+abac
-abac
+baca


Expected Output:
0


Actual Output from /app/solution.py:
0

✓ Test 4 PASSED - Output matches expected!

============================================================
Test 5/10
============================================================
Input:
+8UjgAJ
8UjgAJ:02hR7UBc1tqqfL
-8UjgAJ
+zdi
-zdi


Expected Output:
14


Actual Output from /app/solution.py:
14

✓ Test 5 PASSED - Output matches expected!

============================================================
Test 6/10
============================================================
Input:
+acabadab
+caba0aba


Expected Output:
0


Actual Output from /app/solution.py:
0

✓ Test 6 PASSED - Output matches expected!

============================================================
Test 7/10
============================================================
Input:
+Dmitry
+Mike
Dmitry:All letters will be used
Dmitry:qwertyuiopasdfghjklzxcvbnm QWERTYUIOPASDFGHJKLZXCVBNM
Dmitry:And digits too
Dmitry:1234567890 0987654321
-Dmitry


Expected Output:
224


Actual Output from /app/solution.py:
224

✓ Test 7 PASSED - Output matches expected!

============================================================
Test 8/10
============================================================
Input:
+Dmitry
+Mike
+Kate
Dmitry:


Expected Output:
0


Actual Output from /app/solution.py:
0

✓ Test 8 PASSED - Output matches expected!

============================================================
Test 9/10
============================================================
Input:
+badabac
badabac:abacabad
-badabac
+0ab
-0ab
+dabacab
-dabacab
+a0ab
-a0ab
+0abaca
-0abaca
+dabac
-dabac
+abaca
-abaca
+bacabada
-bacabada
+aca
-aca
+abadabaca
-abadabaca
+acaba
-acaba
+abacabadab
-abacabadab


Expected Output:
8


Actual Output from /app/solution.py:
8

✓ Test 9 PASSED - Output matches expected!

============================================================
Test 10/10
============================================================
Input:
+qlHEc2AuYy
qlHEc2AuYy:YYRwD0 edNZgpE nGfOguRWnMYpTpGUVM aXDKGXo1Gv1tHL9
qlHEc2AuYy:yvh3GsPcImqrvoUcBNQcP6ezwpU0 xAVltaKZp94VKiNao
qlHEc2AuYy:zuCO6Opey L  eu7lTwysaSk00zjpv zrDfbt8l  hpHfu
+pErDMxgVgh
qlHEc2AuYy:I1FLis  mmQbZtd8Ui7y 1vcax6yZBMhVRdD6Ahlq7MNCw
qlHEc2AuYy:lz MFUNJZhlqBYckHUDlNhLiEkmecRh1o0t7alXBvCRVEFVx
pErDMxgVgh:jCyMbu1dkuEj5TzbBOjyUhpfC50cL8R900Je3R KxRgAI dT
qlHEc2AuYy:62b47eabo2hf vSUD7KioN ZHki6WB6gh3u GKv5rgwyfF
pErDMxgVgh:zD5 9 ympl4wR gy7a7eAGAn5xVdGP9FbL6hRCZAR6O4pT6zb


Expected Output:
615


Actual Output from /app/solution.py:
615

✓ Test 10 PASSED - Output matches expected!

✓ All 10 tests passed!
PASSED

============================== 1 passed in 1.95s ===============================
```
