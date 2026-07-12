# introductory/1154-c

**Status:** FAIL (exit code 1)

## stdout

```
============================= test session starts ==============================
platform linux -- Python 3.10.18, pytest-7.4.4, pluggy-1.6.0
PyQt5 5.15.10 -- Qt runtime 5.15.17 -- Qt compiled 5.15.2
rootdir: /tmp/tmp6y2fxkry
configfile: pytest.ini
plugins: Faker-25.1.0, anyio-4.9.0, cov-5.0.0, mock-3.12.0, qt-4.3.1
collected 56 items

tmppwuts5gu.py::test_case[case0] PASSED
tmppwuts5gu.py::test_case[case1] PASSED
tmppwuts5gu.py::test_case[case2] FAILED
tmppwuts5gu.py::test_case[case3] FAILED
tmppwuts5gu.py::test_case[case4] PASSED
tmppwuts5gu.py::test_case[case5] PASSED
tmppwuts5gu.py::test_case[case6] PASSED
tmppwuts5gu.py::test_case[case7] PASSED
tmppwuts5gu.py::test_case[case8] PASSED
tmppwuts5gu.py::test_case[case9] PASSED
tmppwuts5gu.py::test_case[case10] PASSED
tmppwuts5gu.py::test_case[case11] PASSED
tmppwuts5gu.py::test_case[case12] PASSED
tmppwuts5gu.py::test_case[case13] PASSED
tmppwuts5gu.py::test_case[case14] FAILED
tmppwuts5gu.py::test_case[case15] PASSED
tmppwuts5gu.py::test_case[case16] FAILED
tmppwuts5gu.py::test_case[case17] PASSED
tmppwuts5gu.py::test_case[case18] FAILED
tmppwuts5gu.py::test_case[case19] PASSED
tmppwuts5gu.py::test_case[case20] PASSED
tmppwuts5gu.py::test_case[case21] PASSED
tmppwuts5gu.py::test_case[case22] PASSED
tmppwuts5gu.py::test_case[case23] PASSED
tmppwuts5gu.py::test_case[case24] PASSED
tmppwuts5gu.py::test_case[case25] PASSED
tmppwuts5gu.py::test_case[case26] FAILED
tmppwuts5gu.py::test_case[case27] PASSED
tmppwuts5gu.py::test_case[case28] PASSED
tmppwuts5gu.py::test_case[case29] PASSED
tmppwuts5gu.py::test_case[case30] PASSED
tmppwuts5gu.py::test_case[case31] PASSED
tmppwuts5gu.py::test_case[case32] FAILED
tmppwuts5gu.py::test_case[case33] PASSED
tmppwuts5gu.py::test_case[case34] PASSED
tmppwuts5gu.py::test_case[case35] PASSED
tmppwuts5gu.py::test_case[case36] PASSED
tmppwuts5gu.py::test_case[case37] PASSED
tmppwuts5gu.py::test_case[case38] PASSED
tmppwuts5gu.py::test_case[case39] PASSED
tmppwuts5gu.py::test_case[case40] PASSED
tmppwuts5gu.py::test_case[case41] PASSED
tmppwuts5gu.py::test_case[case42] FAILED
tmppwuts5gu.py::test_case[case43] PASSED
tmppwuts5gu.py::test_case[case44] PASSED
tmppwuts5gu.py::test_case[case45] PASSED
tmppwuts5gu.py::test_case[case46] PASSED
tmppwuts5gu.py::test_case[case47] PASSED
tmppwuts5gu.py::test_case[case48] PASSED
tmppwuts5gu.py::test_case[case49] PASSED
tmppwuts5gu.py::test_case[case50] PASSED
tmppwuts5gu.py::test_case[case51] PASSED
tmppwuts5gu.py::test_case[case52] PASSED
tmppwuts5gu.py::test_case[case53] PASSED
tmppwuts5gu.py::test_case[case54] PASSED
tmppwuts5gu.py::test_case[case55] FAILED

=================================== FAILURES ===================================
_______________________________ test_case[case2] _______________________________

i = 2, inp = '1 100 1\n', expected = '3\n'

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
E       AssertionError: input='1 100 1\n'
E         expected='3'
E         got='4'
E       assert '4' == '3'
E         - 3
E         + 4

tmppwuts5gu.py:27: AssertionError
_______________________________ test_case[case3] _______________________________

i = 3, inp = '30 20 10\n', expected = '39\n'

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
E       AssertionError: input='30 20 10\n'
E         expected='39'
E         got='38'
E       assert '38' == '39'
E         - 39
E         + 38

tmppwuts5gu.py:27: AssertionError
______________________________ test_case[case14] _______________________________

i = 14, inp = '200 2 3\n', expected = '9\n'

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
E       AssertionError: input='200 2 3\n'
E         expected='9'
E         got='10'
E       assert '10' == '9'
E         - 9
E         + 10

tmppwuts5gu.py:27: AssertionError
______________________________ test_case[case16] _______________________________

i = 16, inp = '201 4 5\n', expected = '16\n'

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
E       AssertionError: input='201 4 5\n'
E         expected='16'
E         got='17'
E       assert '17' == '16'
E         - 16
E         + 17

tmppwuts5gu.py:27: AssertionError
______________________________ test_case[case18] _______________________________

i = 18, inp = '202 4 5\n', expected = '16\n'

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
E       AssertionError: input='202 4 5\n'
E         expected='16'
E         got='17'
E       assert '17' == '16'
E         - 16
E         + 17

tmppwuts5gu.py:27: AssertionError
______________________________ test_case[case26] _______________________________

i = 26, inp = '20 16 12\n', expected = '46\n'

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
E       AssertionError: input='20 16 12\n'
E         expected='46'
E         got='45'
E       assert '45' == '46'
E         - 46
E         + 45

tmppwuts5gu.py:27: AssertionError
______________________________ test_case[case32] _______________________________

i = 32, inp = '309767158 518372594 115844198\n', expected = '405454697\n'

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
E       AssertionError: input='309767158 518372594 115844198\n'
E         expected='405454697'
E         got='405454696'
E       assert '405454696' == '405454697'
E         - 405454697
E         ?         ^
E         + 405454696
E         ?         ^

tmppwuts5gu.py:27: AssertionError
______________________________ test_case[case42] _______________________________

i = 42, inp = '10012219 123221 1234\n', expected = '4323\n'

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
E       AssertionError: input='10012219 123221 1234\n'
E         expected='4323'
E         got='4322'
E       assert '4322' == '4323'
E         - 4323
E         ?    ^
E         + 4322
E         ?    ^

tmppwuts5gu.py:27: AssertionError
______________________________ test_case[case55] _______________________________

i = 55, inp = '31750 16654 16655\n', expected = '58291\n'

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
E       AssertionError: input='31750 16654 16655\n'
E         expected='58291'
E         got='58292'
E       assert '58292' == '58291'
E         - 58291
E         ?     ^
E         + 58292
E         ?     ^

tmppwuts5gu.py:27: AssertionError
=========================== short test summary info ============================
FAILED tmppwuts5gu.py::test_case[case2] - AssertionError: input='1 100 1\n'
FAILED tmppwuts5gu.py::test_case[case3] - AssertionError: input='30 20 10\n'
FAILED tmppwuts5gu.py::test_case[case14] - AssertionError: input='200 2 3\n'
FAILED tmppwuts5gu.py::test_case[case16] - AssertionError: input='201 4 5\n'
FAILED tmppwuts5gu.py::test_case[case18] - AssertionError: input='202 4 5\n'
FAILED tmppwuts5gu.py::test_case[case26] - AssertionError: input='20 16 12\n'
FAILED tmppwuts5gu.py::test_case[case32] - AssertionError: input='309767158 5...
FAILED tmppwuts5gu.py::test_case[case42] - AssertionError: input='10012219 12...
FAILED tmppwuts5gu.py::test_case[case55] - AssertionError: input='31750 16654...
========================= 9 failed, 47 passed in 9.70s =========================
```
