# competition/722-a

**Status:** FAIL (exit code 1)

## stdout

```
============================= test session starts ==============================
platform linux -- Python 3.10.18, pytest-7.4.4, pluggy-1.6.0
PyQt5 5.15.10 -- Qt runtime 5.15.17 -- Qt compiled 5.15.2
rootdir: /tmp/tmpajl94_52
configfile: pytest.ini
plugins: Faker-25.1.0, anyio-4.9.0, cov-5.0.0, mock-3.12.0, qt-4.3.1
collected 52 items

tmp3mcw_d4j.py::test_case[case0] PASSED
tmp3mcw_d4j.py::test_case[case1] PASSED
tmp3mcw_d4j.py::test_case[case2] PASSED
tmp3mcw_d4j.py::test_case[case3] PASSED
tmp3mcw_d4j.py::test_case[case4] PASSED
tmp3mcw_d4j.py::test_case[case5] PASSED
tmp3mcw_d4j.py::test_case[case6] PASSED
tmp3mcw_d4j.py::test_case[case7] PASSED
tmp3mcw_d4j.py::test_case[case8] PASSED
tmp3mcw_d4j.py::test_case[case9] PASSED
tmp3mcw_d4j.py::test_case[case10] PASSED
tmp3mcw_d4j.py::test_case[case11] PASSED
tmp3mcw_d4j.py::test_case[case12] PASSED
tmp3mcw_d4j.py::test_case[case13] PASSED
tmp3mcw_d4j.py::test_case[case14] PASSED
tmp3mcw_d4j.py::test_case[case15] PASSED
tmp3mcw_d4j.py::test_case[case16] PASSED
tmp3mcw_d4j.py::test_case[case17] PASSED
tmp3mcw_d4j.py::test_case[case18] PASSED
tmp3mcw_d4j.py::test_case[case19] PASSED
tmp3mcw_d4j.py::test_case[case20] PASSED
tmp3mcw_d4j.py::test_case[case21] FAILED
tmp3mcw_d4j.py::test_case[case22] PASSED
tmp3mcw_d4j.py::test_case[case23] PASSED
tmp3mcw_d4j.py::test_case[case24] PASSED
tmp3mcw_d4j.py::test_case[case25] PASSED
tmp3mcw_d4j.py::test_case[case26] PASSED
tmp3mcw_d4j.py::test_case[case27] PASSED
tmp3mcw_d4j.py::test_case[case28] PASSED
tmp3mcw_d4j.py::test_case[case29] FAILED
tmp3mcw_d4j.py::test_case[case30] PASSED
tmp3mcw_d4j.py::test_case[case31] PASSED
tmp3mcw_d4j.py::test_case[case32] PASSED
tmp3mcw_d4j.py::test_case[case33] PASSED
tmp3mcw_d4j.py::test_case[case34] PASSED
tmp3mcw_d4j.py::test_case[case35] PASSED
tmp3mcw_d4j.py::test_case[case36] PASSED
tmp3mcw_d4j.py::test_case[case37] PASSED
tmp3mcw_d4j.py::test_case[case38] PASSED
tmp3mcw_d4j.py::test_case[case39] PASSED
tmp3mcw_d4j.py::test_case[case40] PASSED
tmp3mcw_d4j.py::test_case[case41] PASSED
tmp3mcw_d4j.py::test_case[case42] FAILED
tmp3mcw_d4j.py::test_case[case43] PASSED
tmp3mcw_d4j.py::test_case[case44] PASSED
tmp3mcw_d4j.py::test_case[case45] PASSED
tmp3mcw_d4j.py::test_case[case46] PASSED
tmp3mcw_d4j.py::test_case[case47] PASSED
tmp3mcw_d4j.py::test_case[case48] PASSED
tmp3mcw_d4j.py::test_case[case49] PASSED
tmp3mcw_d4j.py::test_case[case50] PASSED
tmp3mcw_d4j.py::test_case[case51] FAILED

=================================== FAILURES ===================================
______________________________ test_case[case21] _______________________________

i = 21, inp = '12\n90:32\n', expected = '10:32\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='12\n90:32\n'
E         expected='10:32'
E         got='01:32'
E       assert '01:32' == '10:32'
E         - 10:32
E         ?  -
E         + 01:32
E         ? +

tmp3mcw_d4j.py:27: AssertionError
______________________________ test_case[case29] _______________________________

i = 29, inp = '12\n40:11\n', expected = '10:11\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='12\n40:11\n'
E         expected='10:11'
E         got='01:11'
E       assert '01:11' == '10:11'
E         - 10:11
E         ?  -
E         + 01:11
E         ? +

tmp3mcw_d4j.py:27: AssertionError
______________________________ test_case[case42] _______________________________

i = 42, inp = '12\n20:00\n', expected = '10:00\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='12\n20:00\n'
E         expected='10:00'
E         got='01:00'
E       assert '01:00' == '10:00'
E         - 10:00
E         ?  -
E         + 01:00
E         ? +

tmp3mcw_d4j.py:27: AssertionError
______________________________ test_case[case51] _______________________________

i = 51, inp = '12\n20:20\n', expected = '10:20\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='12\n20:20\n'
E         expected='10:20'
E         got='01:20'
E       assert '01:20' == '10:20'
E         - 10:20
E         ?  -
E         + 01:20
E         ? +

tmp3mcw_d4j.py:27: AssertionError
=========================== short test summary info ============================
FAILED tmp3mcw_d4j.py::test_case[case21] - AssertionError: input='12\n90:32\n'
FAILED tmp3mcw_d4j.py::test_case[case29] - AssertionError: input='12\n40:11\n'
FAILED tmp3mcw_d4j.py::test_case[case42] - AssertionError: input='12\n20:00\n'
FAILED tmp3mcw_d4j.py::test_case[case51] - AssertionError: input='12\n20:20\n'
========================= 4 failed, 48 passed in 9.28s =========================
```
