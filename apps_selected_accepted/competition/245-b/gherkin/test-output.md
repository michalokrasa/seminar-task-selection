# competition/245-b

**Status:** FAIL (exit code 1)

## stdout

```
============================= test session starts ==============================
platform linux -- Python 3.10.18, pytest-7.4.4, pluggy-1.6.0
PyQt5 5.15.10 -- Qt runtime 5.15.17 -- Qt compiled 5.15.2
rootdir: /tmp/tmphmlbbox4
configfile: pytest.ini
plugins: Faker-25.1.0, anyio-4.9.0, cov-5.0.0, mock-3.12.0, qt-4.3.1
collected 20 items

tmp63m62z98.py::test_case[case0] PASSED
tmp63m62z98.py::test_case[case1] PASSED
tmp63m62z98.py::test_case[case2] PASSED
tmp63m62z98.py::test_case[case3] PASSED
tmp63m62z98.py::test_case[case4] PASSED
tmp63m62z98.py::test_case[case5] FAILED
tmp63m62z98.py::test_case[case6] PASSED
tmp63m62z98.py::test_case[case7] PASSED
tmp63m62z98.py::test_case[case8] FAILED
tmp63m62z98.py::test_case[case9] PASSED
tmp63m62z98.py::test_case[case10] PASSED
tmp63m62z98.py::test_case[case11] PASSED
tmp63m62z98.py::test_case[case12] PASSED
tmp63m62z98.py::test_case[case13] PASSED
tmp63m62z98.py::test_case[case14] FAILED
tmp63m62z98.py::test_case[case15] PASSED
tmp63m62z98.py::test_case[case16] PASSED
tmp63m62z98.py::test_case[case17] PASSED
tmp63m62z98.py::test_case[case18] PASSED
tmp63m62z98.py::test_case[case19] PASSED

=================================== FAILURES ===================================
_______________________________ test_case[case5] _______________________________

i = 5, inp = 'httpruhhphhhpuhruruhhpruhhphruhhru\n'
expected = 'http://ruhhphhhpuh.ru/ruhhpruhhphruhhru\n'

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
E       AssertionError: input='httpruhhphhhpuhruruhhpruhhphruhhru\n'
E         expected='http://ruhhphhhpuh.ru/ruhhpruhhphruhhru'
E         got='http://.ru/hhphhhpuhruruhhpruhhphruhhru'
E       assert 'http://.ru/h...pruhhphruhhru' == 'http://ruhhp...pruhhphruhhru'
E         - http://ruhhphhhpuh.ru/ruhhpruhhphruhhru
E         ?                   -  -
E         + http://.ru/hhphhhpuhruruhhpruhhphruhhru
E         ?        +  +

tmp63m62z98.py:27: AssertionError
_______________________________ test_case[case8] _______________________________

i = 8, inp = 'httpruhttttpruhttprupruhttpruhtturuhttphtruuru\n'
expected = 'http://ruhttttp.ru/httprupruhttpruhtturuhttphtruuru\n'

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
E       AssertionError: input='httpruhttttpruhttprupruhttpruhtturuhttphtruuru\n'
E         expected='http://ruhttttp.ru/httprupruhttpruhtturuhttphtruuru'
E         got='http://.ru/httttpruhttprupruhttpruhtturuhttphtruuru'
E       assert 'http://.ru/h...ruhttphtruuru' == 'http://ruhtt...ruhttphtruuru'
E         - http://ruhttttp.ru/httprupruhttpruhtturuhttphtruuru
E         ?                -  -
E         + http://.ru/httttpruhttprupruhttpruhtturuhttphtruuru
E         ?        +  +

tmp63m62z98.py:27: AssertionError
______________________________ test_case[case14] _______________________________

i = 14, inp = 'ftpruurruurururururuuruuur\n'
expected = 'ftp://ruur.ru/urururururuuruuur\n'

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
E       AssertionError: input='ftpruurruurururururuuruuur\n'
E         expected='ftp://ruur.ru/urururururuuruuur'
E         got='ftp://.ru/urruurururururuuruuur'
E       assert 'ftp://.ru/ur...urururuuruuur' == 'ftp://ruur.r...urururuuruuur'
E         - ftp://ruur.ru/urururururuuruuur
E         ?       ----
E         + ftp://.ru/urruurururururuuruuur
E         ?           ++++

tmp63m62z98.py:27: AssertionError
=========================== short test summary info ============================
FAILED tmp63m62z98.py::test_case[case5] - AssertionError: input='httpruhhphhh...
FAILED tmp63m62z98.py::test_case[case8] - AssertionError: input='httpruhttttp...
FAILED tmp63m62z98.py::test_case[case14] - AssertionError: input='ftpruurruur...
========================= 3 failed, 17 passed in 3.75s =========================
```
