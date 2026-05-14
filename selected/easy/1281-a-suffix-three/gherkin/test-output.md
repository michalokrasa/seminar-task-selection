# easy/1281-a-suffix-three

**Status:** PASS

## stdout

```
============================= test session starts ==============================
platform linux -- Python 3.10.18, pytest-7.4.4, pluggy-1.6.0
PyQt5 5.15.10 -- Qt runtime 5.15.17 -- Qt compiled 5.15.2
rootdir: /tmp/tmpyes1yyof
configfile: pytest.ini
plugins: Faker-25.1.0, anyio-4.9.0, cov-5.0.0, mock-3.12.0, qt-4.3.1
collected 1 item

tmpxsv7yxyg.py::test_code_contest_solution 
============================================================
Test 1/5
============================================================
Input:
8
kamusta_po
genki_desu
ohayou_gozaimasu
annyeong_hashimnida
hajime_no_ippo
bensamu_no_sentou_houhou_ga_okama_kenpo
ang_halaman_doon_ay_sarisari_singkamasu
si_roy_mustang_ay_namamasu


Expected Output:
FILIPINO
JAPANESE
JAPANESE
KOREAN
FILIPINO
FILIPINO
JAPANESE
JAPANESE


Actual Output from /app/solution.py:
FILIPINO
JAPANESE
JAPANESE
KOREAN
FILIPINO
FILIPINO
JAPANESE
JAPANESE

✓ Test 1 PASSED - Output matches expected!

============================================================
Test 2/5
============================================================
Input:
30
opo
p_po
popo
desu
po
udesu
podesu
desupo
sddesu
mumasu
mmnida
mmasu
masu
desu_po
pomnida
masumasu
pppo
mnida
masu_po
desu_masu
a_masu
po_po
masupo
masu_masu
mnidamasu
pomasu
mnida_po
mnida_desu
nakupo
po_masu


Expected Output:
FILIPINO
FILIPINO
FILIPINO
JAPANESE
FILIPINO
JAPANESE
JAPANESE
FILIPINO
JAPANESE
JAPANESE
KOREAN
JAPANESE
JAPANESE
FILIPINO
KOREAN
JAPANESE
FILIPINO
KOREAN
FILIPINO
JAPANESE
JAPANESE
FILIPINO
FILIPINO
JAPANESE
JAPANESE
JAPANESE
FILIPINO
JAPANESE
FILIPINO
JAPANESE


Actual Output from /app/solution.py:
FILIPINO
FILIPINO
FILIPINO
JAPANESE
FILIPINO
JAPANESE
JAPANESE
FILIPINO
JAPANESE
JAPANESE
KOREAN
JAPANESE
JAPANESE
FILIPINO
KOREAN
JAPANESE
FILIPINO
KOREAN
FILIPINO
JAPANESE
JAPANESE
FILIPINO
FILIPINO
JAPANESE
JAPANESE
JAPANESE
FILIPINO
JAPANESE
FILIPINO
JAPANESE

✓ Test 2 PASSED - Output matches expected!

============================================================
Test 3/5
============================================================
Input:
30
po
ppo
op_po
mnida
masu
desu
popo
msmasu
pomasu
po_po
usedpo
masu_po
opmasu
opo
ua_masu
op_masu
mnidapo
dmnida
opdesu
adinmpo
podesu
nakupo
oppo
mmasu
p_po
adinm_po
used_po
usedmasu
m_umasu
o_ppo


Expected Output:
FILIPINO
FILIPINO
FILIPINO
KOREAN
JAPANESE
JAPANESE
FILIPINO
JAPANESE
JAPANESE
FILIPINO
FILIPINO
FILIPINO
JAPANESE
FILIPINO
JAPANESE
JAPANESE
FILIPINO
KOREAN
JAPANESE
FILIPINO
JAPANESE
FILIPINO
FILIPINO
JAPANESE
FILIPINO
FILIPINO
FILIPINO
JAPANESE
JAPANESE
FILIPINO


Actual Output from /app/solution.py:
FILIPINO
FILIPINO
FILIPINO
KOREAN
JAPANESE
JAPANESE
FILIPINO
JAPANESE
JAPANESE
FILIPINO
FILIPINO
FILIPINO
JAPANESE
FILIPINO
JAPANESE
JAPANESE
FILIPINO
KOREAN
JAPANESE
FILIPINO
JAPANESE
FILIPINO
FILIPINO
JAPANESE
FILIPINO
FILIPINO
FILIPINO
JAPANESE
JAPANESE
FILIPINO

✓ Test 3 PASSED - Output matches expected!

============================================================
Test 4/5
============================================================
Input:
30
mnidamnida
opmnida
adinm_masu
usam_masu
useddesu
adinmmasu
mnida_po
dnmnida
masumnida
usam_po
mnidadesu
used_masu
mnida_mnida
adinm_mnida
usammasu
masu_desu
usammnida
genki_desu
mm_mnida
adinmmnida
op_mnida
adinm_desu
used_desu
usam_desu
adinmdesu
saranghamnida
desu_desu
tang_na_moo_po
used_mnida
usam_mnida


Expected Output:
KOREAN
KOREAN
JAPANESE
JAPANESE
JAPANESE
JAPANESE
FILIPINO
KOREAN
KOREAN
FILIPINO
JAPANESE
JAPANESE
KOREAN
KOREAN
JAPANESE
JAPANESE
KOREAN
JAPANESE
KOREAN
KOREAN
KOREAN
JAPANESE
JAPANESE
JAPANESE
JAPANESE
KOREAN
JAPANESE
FILIPINO
KOREAN
KOREAN


Actual Output from /app/solution.py:
KOREAN
KOREAN
JAPANESE
JAPANESE
JAPANESE
JAPANESE
FILIPINO
KOREAN
KOREAN
FILIPINO
JAPANESE
JAPANESE
KOREAN
KOREAN
JAPANESE
JAPANESE
KOREAN
JAPANESE
KOREAN
KOREAN
KOREAN
JAPANESE
JAPANESE
JAPANESE
JAPANESE
KOREAN
JAPANESE
FILIPINO
KOREAN
KOREAN

✓ Test 4 PASSED - Output matches expected!

============================================================
Test 5/5
============================================================
Input:
30
imamnida
usamdesu
pomnida
desudesu
op_desu
desumnida
po_desu
po_mnida
a_mnida
desu_po
mnidamasu
masupo
desumasu
udesu
desupo
e_desu
po_masu
uudesu
usedmnida
usampo
masu_masu
mnida_masu
kamusta_po
masudesu
u_masu
ds_desu
u_edesu
desu_masu
masumasu
masu_mnida


Expected Output:
KOREAN
JAPANESE
KOREAN
JAPANESE
JAPANESE
KOREAN
JAPANESE
KOREAN
KOREAN
FILIPINO
JAPANESE
FILIPINO
JAPANESE
JAPANESE
FILIPINO
JAPANESE
JAPANESE
JAPANESE
KOREAN
FILIPINO
JAPANESE
JAPANESE
FILIPINO
JAPANESE
JAPANESE
JAPANESE
JAPANESE
JAPANESE
JAPANESE
KOREAN


Actual Output from /app/solution.py:
KOREAN
JAPANESE
KOREAN
JAPANESE
JAPANESE
KOREAN
JAPANESE
KOREAN
KOREAN
FILIPINO
JAPANESE
FILIPINO
JAPANESE
JAPANESE
FILIPINO
JAPANESE
JAPANESE
JAPANESE
KOREAN
FILIPINO
JAPANESE
JAPANESE
FILIPINO
JAPANESE
JAPANESE
JAPANESE
JAPANESE
JAPANESE
JAPANESE
KOREAN

✓ Test 5 PASSED - Output matches expected!

✓ All 5 tests passed!
PASSED

============================== 1 passed in 1.00s ===============================
```
