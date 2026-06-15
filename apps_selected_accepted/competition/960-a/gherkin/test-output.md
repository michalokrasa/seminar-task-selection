# competition/960-a

**Status:** FAIL (exit code 1)

## stdout

```
============================= test session starts ==============================
platform linux -- Python 3.10.18, pytest-7.4.4, pluggy-1.6.0
PyQt5 5.15.10 -- Qt runtime 5.15.17 -- Qt compiled 5.15.2
rootdir: /tmp/tmp8g6ra4f7
configfile: pytest.ini
plugins: Faker-25.1.0, anyio-4.9.0, cov-5.0.0, mock-3.12.0, qt-4.3.1
collected 42 items

tmpp83rh8p_.py::test_case[case0] FAILED
tmpp83rh8p_.py::test_case[case1] PASSED
tmpp83rh8p_.py::test_case[case2] PASSED
tmpp83rh8p_.py::test_case[case3] PASSED
tmpp83rh8p_.py::test_case[case4] FAILED
tmpp83rh8p_.py::test_case[case5] PASSED
tmpp83rh8p_.py::test_case[case6] FAILED
tmpp83rh8p_.py::test_case[case7] PASSED
tmpp83rh8p_.py::test_case[case8] PASSED
tmpp83rh8p_.py::test_case[case9] PASSED
tmpp83rh8p_.py::test_case[case10] PASSED
tmpp83rh8p_.py::test_case[case11] PASSED
tmpp83rh8p_.py::test_case[case12] PASSED
tmpp83rh8p_.py::test_case[case13] PASSED
tmpp83rh8p_.py::test_case[case14] PASSED
tmpp83rh8p_.py::test_case[case15] PASSED
tmpp83rh8p_.py::test_case[case16] PASSED
tmpp83rh8p_.py::test_case[case17] PASSED
tmpp83rh8p_.py::test_case[case18] FAILED
tmpp83rh8p_.py::test_case[case19] PASSED
tmpp83rh8p_.py::test_case[case20] FAILED
tmpp83rh8p_.py::test_case[case21] PASSED
tmpp83rh8p_.py::test_case[case22] FAILED
tmpp83rh8p_.py::test_case[case23] PASSED
tmpp83rh8p_.py::test_case[case24] PASSED
tmpp83rh8p_.py::test_case[case25] PASSED
tmpp83rh8p_.py::test_case[case26] PASSED
tmpp83rh8p_.py::test_case[case27] PASSED
tmpp83rh8p_.py::test_case[case28] FAILED
tmpp83rh8p_.py::test_case[case29] PASSED
tmpp83rh8p_.py::test_case[case30] FAILED
tmpp83rh8p_.py::test_case[case31] FAILED
tmpp83rh8p_.py::test_case[case32] PASSED
tmpp83rh8p_.py::test_case[case33] PASSED
tmpp83rh8p_.py::test_case[case34] PASSED
tmpp83rh8p_.py::test_case[case35] FAILED
tmpp83rh8p_.py::test_case[case36] PASSED
tmpp83rh8p_.py::test_case[case37] PASSED
tmpp83rh8p_.py::test_case[case38] PASSED
tmpp83rh8p_.py::test_case[case39] PASSED
tmpp83rh8p_.py::test_case[case40] FAILED
tmpp83rh8p_.py::test_case[case41] PASSED

=================================== FAILURES ===================================
_______________________________ test_case[case0] _______________________________

i = 0, inp = 'aaabccc\n', expected = 'YES\n'

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
E       AssertionError: input='aaabccc\n'
E         expected='YES'
E         got='NO'
E       assert 'NO' == 'YES'
E         - YES
E         + NO

tmpp83rh8p_.py:27: AssertionError
_______________________________ test_case[case4] _______________________________

i = 4, inp = 'aaacccbb\n', expected = 'NO\n'

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
E       AssertionError: input='aaacccbb\n'
E         expected='NO'
E         got='YES'
E       assert 'YES' == 'NO'
E         - NO
E         + YES

tmpp83rh8p_.py:27: AssertionError
_______________________________ test_case[case6] _______________________________

i = 6, inp = 'acba\n', expected = 'NO\n'

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
E       AssertionError: input='acba\n'
E         expected='NO'
E         got='YES'
E       assert 'YES' == 'NO'
E         - NO
E         + YES

tmpp83rh8p_.py:27: AssertionError
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

tmpp83rh8p_.py:27: AssertionError
______________________________ test_case[case20] _______________________________

i = 20, inp = 'abca\n', expected = 'NO\n'

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
E       AssertionError: input='abca\n'
E         expected='NO'
E         got='YES'
E       assert 'YES' == 'NO'
E         - NO
E         + YES

tmpp83rh8p_.py:27: AssertionError
______________________________ test_case[case22] _______________________________

i = 22, inp = 'abac\n', expected = 'NO\n'

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
E       AssertionError: input='abac\n'
E         expected='NO'
E         got='YES'
E       assert 'YES' == 'NO'
E         - NO
E         + YES

tmpp83rh8p_.py:27: AssertionError
______________________________ test_case[case28] _______________________________

i = 28, inp = 'ac\n', expected = 'NO\n'

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
E       AssertionError: input='ac\n'
E         expected='NO'
E         got='YES'
E       assert 'YES' == 'NO'
E         - NO
E         + YES

tmpp83rh8p_.py:27: AssertionError
______________________________ test_case[case30] _______________________________

i = 30, inp = 'abacc\n', expected = 'NO\n'

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
E       AssertionError: input='abacc\n'
E         expected='NO'
E         got='YES'
E       assert 'YES' == 'NO'
E         - NO
E         + YES

tmpp83rh8p_.py:27: AssertionError
______________________________ test_case[case31] _______________________________

i = 31, inp = 'ababc\n', expected = 'NO\n'

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
E       AssertionError: input='ababc\n'
E         expected='NO'
E         got='YES'
E       assert 'YES' == 'NO'
E         - NO
E         + YES

tmpp83rh8p_.py:27: AssertionError
______________________________ test_case[case35] _______________________________

i = 35, inp = 'aaabcbc\n', expected = 'NO\n'

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
E       AssertionError: input='aaabcbc\n'
E         expected='NO'
E         got='YES'
E       assert 'YES' == 'NO'
E         - NO
E         + YES

tmpp83rh8p_.py:27: AssertionError
______________________________ test_case[case40] _______________________________

i = 40, inp = 'abababccc\n', expected = 'NO\n'

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
E       AssertionError: input='abababccc\n'
E         expected='NO'
E         got='YES'
E       assert 'YES' == 'NO'
E         - NO
E         + YES

tmpp83rh8p_.py:27: AssertionError
=========================== short test summary info ============================
FAILED tmpp83rh8p_.py::test_case[case0] - AssertionError: input='aaabccc\n'
FAILED tmpp83rh8p_.py::test_case[case4] - AssertionError: input='aaacccbb\n'
FAILED tmpp83rh8p_.py::test_case[case6] - AssertionError: input='acba\n'
FAILED tmpp83rh8p_.py::test_case[case18] - AssertionError: input='a\n'
FAILED tmpp83rh8p_.py::test_case[case20] - AssertionError: input='abca\n'
FAILED tmpp83rh8p_.py::test_case[case22] - AssertionError: input='abac\n'
FAILED tmpp83rh8p_.py::test_case[case28] - AssertionError: input='ac\n'
FAILED tmpp83rh8p_.py::test_case[case30] - AssertionError: input='abacc\n'
FAILED tmpp83rh8p_.py::test_case[case31] - AssertionError: input='ababc\n'
FAILED tmpp83rh8p_.py::test_case[case35] - AssertionError: input='aaabcbc\n'
FAILED tmpp83rh8p_.py::test_case[case40] - AssertionError: input='abababccc\n'
======================== 11 failed, 31 passed in 7.08s =========================
```
