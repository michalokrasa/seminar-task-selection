# competition/634-a

**Status:** FAIL (exit code 1)

## stdout

```
============================= test session starts ==============================
platform linux -- Python 3.10.18, pytest-7.4.4, pluggy-1.6.0
PyQt5 5.15.10 -- Qt runtime 5.15.17 -- Qt compiled 5.15.2
rootdir: /tmp/tmpcw1dbhlm
configfile: pytest.ini
plugins: Faker-25.1.0, anyio-4.9.0, cov-5.0.0, mock-3.12.0, qt-4.3.1
collected 29 items

tmpeg1035_f.py::test_case[case0] FAILED
tmpeg1035_f.py::test_case[case1] PASSED
tmpeg1035_f.py::test_case[case2] PASSED
tmpeg1035_f.py::test_case[case3] PASSED
tmpeg1035_f.py::test_case[case4] PASSED
tmpeg1035_f.py::test_case[case5] PASSED
tmpeg1035_f.py::test_case[case6] FAILED
tmpeg1035_f.py::test_case[case7] FAILED
tmpeg1035_f.py::test_case[case8] PASSED
tmpeg1035_f.py::test_case[case9] PASSED
tmpeg1035_f.py::test_case[case10] FAILED
tmpeg1035_f.py::test_case[case11] PASSED
tmpeg1035_f.py::test_case[case12] FAILED
tmpeg1035_f.py::test_case[case13] FAILED
tmpeg1035_f.py::test_case[case14] PASSED
tmpeg1035_f.py::test_case[case15] PASSED
tmpeg1035_f.py::test_case[case16] PASSED
tmpeg1035_f.py::test_case[case17] FAILED
tmpeg1035_f.py::test_case[case18] FAILED
tmpeg1035_f.py::test_case[case19] FAILED
tmpeg1035_f.py::test_case[case20] PASSED
tmpeg1035_f.py::test_case[case21] FAILED
tmpeg1035_f.py::test_case[case22] FAILED
tmpeg1035_f.py::test_case[case23] FAILED
tmpeg1035_f.py::test_case[case24] FAILED
tmpeg1035_f.py::test_case[case25] PASSED
tmpeg1035_f.py::test_case[case26] FAILED
tmpeg1035_f.py::test_case[case27] FAILED
tmpeg1035_f.py::test_case[case28] FAILED

=================================== FAILURES ===================================
_______________________________ test_case[case0] _______________________________

i = 0, inp = '3\n1 0 2\n2 0 1\n', expected = 'YES\n'

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
E       AssertionError: input='3\n1 0 2\n2 0 1\n'
E         expected='YES'
E         got='NO'
E       assert 'NO' == 'YES'
E         - YES
E         + NO

tmpeg1035_f.py:27: AssertionError
_______________________________ test_case[case6] _______________________________

i = 6, inp = '4\n3 0 1 2\n1 0 2 3\n', expected = 'YES\n'

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
E       AssertionError: input='4\n3 0 1 2\n1 0 2 3\n'
E         expected='YES'
E         got='NO'
E       assert 'NO' == 'YES'
E         - YES
E         + NO

tmpeg1035_f.py:27: AssertionError
_______________________________ test_case[case7] _______________________________

i = 7, inp = '3\n0 2 1\n1 2 0\n', expected = 'YES\n'

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
E       AssertionError: input='3\n0 2 1\n1 2 0\n'
E         expected='YES'
E         got='NO'
E       assert 'NO' == 'YES'
E         - YES
E         + NO

tmpeg1035_f.py:27: AssertionError
______________________________ test_case[case10] _______________________________

i = 10, inp = '4\n2 0 3 1\n3 1 0 2\n', expected = 'YES\n'

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
E       AssertionError: input='4\n2 0 3 1\n3 1 0 2\n'
E         expected='YES'
E         got='NO'
E       assert 'NO' == 'YES'
E         - YES
E         + NO

tmpeg1035_f.py:27: AssertionError
______________________________ test_case[case12] _______________________________

i = 12, inp = '3\n2 0 1\n1 0 2\n', expected = 'YES\n'

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
E       AssertionError: input='3\n2 0 1\n1 0 2\n'
E         expected='YES'
E         got='NO'
E       assert 'NO' == 'YES'
E         - YES
E         + NO

tmpeg1035_f.py:27: AssertionError
______________________________ test_case[case13] _______________________________

i = 13, inp = '10\n6 2 3 8 0 4 9 1 5 7\n2 3 8 4 0 9 1 5 7 6\n'
expected = 'YES\n'

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
E       AssertionError: input='10\n6 2 3 8 0 4 9 1 5 7\n2 3 8 4 0 9 1 5 7 6\n'
E         expected='YES'
E         got='NO'
E       assert 'NO' == 'YES'
E         - YES
E         + NO

tmpeg1035_f.py:27: AssertionError
______________________________ test_case[case17] _______________________________

i = 17, inp = '4\n0 1 2 3\n1 0 2 3\n', expected = 'YES\n'

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
E       AssertionError: input='4\n0 1 2 3\n1 0 2 3\n'
E         expected='YES'
E         got='NO'
E       assert 'NO' == 'YES'
E         - YES
E         + NO

tmpeg1035_f.py:27: AssertionError
______________________________ test_case[case18] _______________________________

i = 18, inp = '3\n0 1 2\n1 0 2\n', expected = 'YES\n'

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
E       AssertionError: input='3\n0 1 2\n1 0 2\n'
E         expected='YES'
E         got='NO'
E       assert 'NO' == 'YES'
E         - YES
E         + NO

tmpeg1035_f.py:27: AssertionError
______________________________ test_case[case19] _______________________________

i = 19, inp = '5\n1 2 0 3 4\n4 0 1 2 3\n', expected = 'YES\n'

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
E       AssertionError: input='5\n1 2 0 3 4\n4 0 1 2 3\n'
E         expected='YES'
E         got='NO'
E       assert 'NO' == 'YES'
E         - YES
E         + NO

tmpeg1035_f.py:27: AssertionError
______________________________ test_case[case21] _______________________________

i = 21, inp = '3\n0 1 2\n0 2 1\n', expected = 'YES\n'

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
E       AssertionError: input='3\n0 1 2\n0 2 1\n'
E         expected='YES'
E         got='NO'
E       assert 'NO' == 'YES'
E         - YES
E         + NO

tmpeg1035_f.py:27: AssertionError
______________________________ test_case[case22] _______________________________

i = 22, inp = '4\n0 1 2 3\n2 3 1 0\n', expected = 'YES\n'

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
E       AssertionError: input='4\n0 1 2 3\n2 3 1 0\n'
E         expected='YES'
E         got='NO'
E       assert 'NO' == 'YES'
E         - YES
E         + NO

tmpeg1035_f.py:27: AssertionError
______________________________ test_case[case23] _______________________________

i = 23, inp = '4\n0 2 3 1\n1 2 3 0\n', expected = 'YES\n'

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
E       AssertionError: input='4\n0 2 3 1\n1 2 3 0\n'
E         expected='YES'
E         got='NO'
E       assert 'NO' == 'YES'
E         - YES
E         + NO

tmpeg1035_f.py:27: AssertionError
______________________________ test_case[case24] _______________________________

i = 24, inp = '3\n0 2 1\n2 0 1\n', expected = 'YES\n'

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
E       AssertionError: input='3\n0 2 1\n2 0 1\n'
E         expected='YES'
E         got='NO'
E       assert 'NO' == 'YES'
E         - YES
E         + NO

tmpeg1035_f.py:27: AssertionError
______________________________ test_case[case26] _______________________________

i = 26, inp = '4\n1 2 3 0\n1 0 2 3\n', expected = 'YES\n'

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
E       AssertionError: input='4\n1 2 3 0\n1 0 2 3\n'
E         expected='YES'
E         got='NO'
E       assert 'NO' == 'YES'
E         - YES
E         + NO

tmpeg1035_f.py:27: AssertionError
______________________________ test_case[case27] _______________________________

i = 27, inp = '4\n0 1 3 2\n2 1 3 0\n', expected = 'YES\n'

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
E       AssertionError: input='4\n0 1 3 2\n2 1 3 0\n'
E         expected='YES'
E         got='NO'
E       assert 'NO' == 'YES'
E         - YES
E         + NO

tmpeg1035_f.py:27: AssertionError
______________________________ test_case[case28] _______________________________

i = 28, inp = '4\n1 2 3 0\n1 2 0 3\n', expected = 'YES\n'

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
E       AssertionError: input='4\n1 2 3 0\n1 2 0 3\n'
E         expected='YES'
E         got='NO'
E       assert 'NO' == 'YES'
E         - YES
E         + NO

tmpeg1035_f.py:27: AssertionError
=========================== short test summary info ============================
FAILED tmpeg1035_f.py::test_case[case0] - AssertionError: input='3\n1 0 2\n2 ...
FAILED tmpeg1035_f.py::test_case[case6] - AssertionError: input='4\n3 0 1 2\n...
FAILED tmpeg1035_f.py::test_case[case7] - AssertionError: input='3\n0 2 1\n1 ...
FAILED tmpeg1035_f.py::test_case[case10] - AssertionError: input='4\n2 0 3 1\...
FAILED tmpeg1035_f.py::test_case[case12] - AssertionError: input='3\n2 0 1\n1...
FAILED tmpeg1035_f.py::test_case[case13] - AssertionError: input='10\n6 2 3 8...
FAILED tmpeg1035_f.py::test_case[case17] - AssertionError: input='4\n0 1 2 3\...
FAILED tmpeg1035_f.py::test_case[case18] - AssertionError: input='3\n0 1 2\n1...
FAILED tmpeg1035_f.py::test_case[case19] - AssertionError: input='5\n1 2 0 3 ...
FAILED tmpeg1035_f.py::test_case[case21] - AssertionError: input='3\n0 1 2\n0...
FAILED tmpeg1035_f.py::test_case[case22] - AssertionError: input='4\n0 1 2 3\...
FAILED tmpeg1035_f.py::test_case[case23] - AssertionError: input='4\n0 2 3 1\...
FAILED tmpeg1035_f.py::test_case[case24] - AssertionError: input='3\n0 2 1\n2...
FAILED tmpeg1035_f.py::test_case[case26] - AssertionError: input='4\n1 2 3 0\...
FAILED tmpeg1035_f.py::test_case[case27] - AssertionError: input='4\n0 1 3 2\...
FAILED tmpeg1035_f.py::test_case[case28] - AssertionError: input='4\n1 2 3 0\...
======================== 16 failed, 13 passed in 5.65s =========================
```
