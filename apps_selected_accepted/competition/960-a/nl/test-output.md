# competition/960-a

**Status:** FAIL (exit code 1)

## stdout

```
============================= test session starts ==============================
platform linux -- Python 3.10.18, pytest-7.4.4, pluggy-1.6.0
PyQt5 5.15.10 -- Qt runtime 5.15.17 -- Qt compiled 5.15.2
rootdir: /tmp/tmpiqnn5gkc
configfile: pytest.ini
plugins: Faker-25.1.0, anyio-4.9.0, cov-5.0.0, mock-3.12.0, qt-4.3.1
collected 42 items

tmpxmws0ta3.py::test_case[case0] PASSED
tmpxmws0ta3.py::test_case[case1] PASSED
tmpxmws0ta3.py::test_case[case2] PASSED
tmpxmws0ta3.py::test_case[case3] PASSED
tmpxmws0ta3.py::test_case[case4] PASSED
tmpxmws0ta3.py::test_case[case5] PASSED
tmpxmws0ta3.py::test_case[case6] PASSED
tmpxmws0ta3.py::test_case[case7] PASSED
tmpxmws0ta3.py::test_case[case8] PASSED
tmpxmws0ta3.py::test_case[case9] PASSED
tmpxmws0ta3.py::test_case[case10] PASSED
tmpxmws0ta3.py::test_case[case11] PASSED
tmpxmws0ta3.py::test_case[case12] PASSED
tmpxmws0ta3.py::test_case[case13] FAILED
tmpxmws0ta3.py::test_case[case14] FAILED
tmpxmws0ta3.py::test_case[case15] PASSED
tmpxmws0ta3.py::test_case[case16] FAILED
tmpxmws0ta3.py::test_case[case17] PASSED
tmpxmws0ta3.py::test_case[case18] FAILED
tmpxmws0ta3.py::test_case[case19] FAILED
tmpxmws0ta3.py::test_case[case20] PASSED
tmpxmws0ta3.py::test_case[case21] PASSED
tmpxmws0ta3.py::test_case[case22] PASSED
tmpxmws0ta3.py::test_case[case23] PASSED
tmpxmws0ta3.py::test_case[case24] PASSED
tmpxmws0ta3.py::test_case[case25] PASSED
tmpxmws0ta3.py::test_case[case26] PASSED
tmpxmws0ta3.py::test_case[case27] PASSED
tmpxmws0ta3.py::test_case[case28] PASSED
tmpxmws0ta3.py::test_case[case29] PASSED
tmpxmws0ta3.py::test_case[case30] PASSED
tmpxmws0ta3.py::test_case[case31] PASSED
tmpxmws0ta3.py::test_case[case32] FAILED
tmpxmws0ta3.py::test_case[case33] PASSED
tmpxmws0ta3.py::test_case[case34] FAILED
tmpxmws0ta3.py::test_case[case35] PASSED
tmpxmws0ta3.py::test_case[case36] PASSED
tmpxmws0ta3.py::test_case[case37] PASSED
tmpxmws0ta3.py::test_case[case38] PASSED
tmpxmws0ta3.py::test_case[case39] PASSED
tmpxmws0ta3.py::test_case[case40] PASSED
tmpxmws0ta3.py::test_case[case41] PASSED

=================================== FAILURES ===================================
______________________________ test_case[case13] _______________________________

i = 13, inp = 'bbb\n', expected = 'NO\n'

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
E       AssertionError: input='bbb\n'
E         expected='NO'
E         got='YES'
E       assert 'YES' == 'NO'
E         - NO
E         + YES

tmpxmws0ta3.py:27: AssertionError
______________________________ test_case[case14] _______________________________

i = 14, inp = 'bc\n', expected = 'NO\n'

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
E       AssertionError: input='bc\n'
E         expected='NO'
E         got='YES'
E       assert 'YES' == 'NO'
E         - NO
E         + YES

tmpxmws0ta3.py:27: AssertionError
______________________________ test_case[case16] _______________________________

i = 16, inp = 'aaa\n', expected = 'NO\n'

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
E       AssertionError: input='aaa\n'
E         expected='NO'
E         got='YES'
E       assert 'YES' == 'NO'
E         - NO
E         + YES

tmpxmws0ta3.py:27: AssertionError
______________________________ test_case[case18] _______________________________

i = 18, inp = 'a\n', expected = 'NO\n'

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
E       AssertionError: input='a\n'
E         expected='NO'
E         got='YES'
E       assert 'YES' == 'NO'
E         - NO
E         + YES

tmpxmws0ta3.py:27: AssertionError
______________________________ test_case[case19] _______________________________

i = 19, inp = 'b\n', expected = 'NO\n'

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
E       AssertionError: input='b\n'
E         expected='NO'
E         got='YES'
E       assert 'YES' == 'NO'
E         - NO
E         + YES

tmpxmws0ta3.py:27: AssertionError
______________________________ test_case[case32] _______________________________

i = 32, inp = 'aa\n', expected = 'NO\n'

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
E       AssertionError: input='aa\n'
E         expected='NO'
E         got='YES'
E       assert 'YES' == 'NO'
E         - NO
E         + YES

tmpxmws0ta3.py:27: AssertionError
______________________________ test_case[case34] _______________________________

i = 34, inp = 'bbcc\n', expected = 'NO\n'

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
E       AssertionError: input='bbcc\n'
E         expected='NO'
E         got='YES'
E       assert 'YES' == 'NO'
E         - NO
E         + YES

tmpxmws0ta3.py:27: AssertionError
=========================== short test summary info ============================
FAILED tmpxmws0ta3.py::test_case[case13] - AssertionError: input='bbb\n'
FAILED tmpxmws0ta3.py::test_case[case14] - AssertionError: input='bc\n'
FAILED tmpxmws0ta3.py::test_case[case16] - AssertionError: input='aaa\n'
FAILED tmpxmws0ta3.py::test_case[case18] - AssertionError: input='a\n'
FAILED tmpxmws0ta3.py::test_case[case19] - AssertionError: input='b\n'
FAILED tmpxmws0ta3.py::test_case[case32] - AssertionError: input='aa\n'
FAILED tmpxmws0ta3.py::test_case[case34] - AssertionError: input='bbcc\n'
========================= 7 failed, 35 passed in 7.65s =========================
```
