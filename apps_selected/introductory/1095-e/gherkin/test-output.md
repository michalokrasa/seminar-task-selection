# introductory/1095-e

**Status:** FAIL (exit code 1)

## stdout

```
============================= test session starts ==============================
platform linux -- Python 3.10.18, pytest-7.4.4, pluggy-1.6.0
PyQt5 5.15.10 -- Qt runtime 5.15.17 -- Qt compiled 5.15.2
rootdir: /tmp/tmpsxqy47ox
configfile: pytest.ini
plugins: Faker-25.1.0, anyio-4.9.0, cov-5.0.0, mock-3.12.0, qt-4.3.1
collected 35 items

tmpeknn2kwf.py::test_case[case0] FAILED
tmpeknn2kwf.py::test_case[case1] PASSED
tmpeknn2kwf.py::test_case[case2] PASSED
tmpeknn2kwf.py::test_case[case3] PASSED
tmpeknn2kwf.py::test_case[case4] PASSED
tmpeknn2kwf.py::test_case[case5] FAILED
tmpeknn2kwf.py::test_case[case6] FAILED
tmpeknn2kwf.py::test_case[case7] FAILED
tmpeknn2kwf.py::test_case[case8] PASSED
tmpeknn2kwf.py::test_case[case9] PASSED
tmpeknn2kwf.py::test_case[case10] PASSED
tmpeknn2kwf.py::test_case[case11] PASSED
tmpeknn2kwf.py::test_case[case12] PASSED
tmpeknn2kwf.py::test_case[case13] PASSED
tmpeknn2kwf.py::test_case[case14] PASSED
tmpeknn2kwf.py::test_case[case15] PASSED
tmpeknn2kwf.py::test_case[case16] PASSED
tmpeknn2kwf.py::test_case[case17] PASSED
tmpeknn2kwf.py::test_case[case18] PASSED
tmpeknn2kwf.py::test_case[case19] PASSED
tmpeknn2kwf.py::test_case[case20] PASSED
tmpeknn2kwf.py::test_case[case21] PASSED
tmpeknn2kwf.py::test_case[case22] PASSED
tmpeknn2kwf.py::test_case[case23] PASSED
tmpeknn2kwf.py::test_case[case24] FAILED
tmpeknn2kwf.py::test_case[case25] PASSED
tmpeknn2kwf.py::test_case[case26] PASSED
tmpeknn2kwf.py::test_case[case27] PASSED
tmpeknn2kwf.py::test_case[case28] PASSED
tmpeknn2kwf.py::test_case[case29] FAILED
tmpeknn2kwf.py::test_case[case30] PASSED
tmpeknn2kwf.py::test_case[case31] PASSED
tmpeknn2kwf.py::test_case[case32] PASSED
tmpeknn2kwf.py::test_case[case33] PASSED
tmpeknn2kwf.py::test_case[case34] PASSED

=================================== FAILURES ===================================
_______________________________ test_case[case0] _______________________________

i = 0, inp = '6\n(((())\n', expected = '3\n'

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
E       AssertionError: input='6\n(((())\n'
E         expected='3'
E         got='0'
E       assert '0' == '3'
E         - 3
E         + 0

tmpeknn2kwf.py:27: AssertionError
_______________________________ test_case[case5] _______________________________

i = 5, inp = '2\n((\n', expected = '1\n'

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
E       AssertionError: input='2\n((\n'
E         expected='1'
E         got='0'
E       assert '0' == '1'
E         - 1
E         + 0

tmpeknn2kwf.py:27: AssertionError
_______________________________ test_case[case6] _______________________________

i = 6, inp = '2\n))\n', expected = '1\n'

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
E       AssertionError: input='2\n))\n'
E         expected='1'
E         got='0'
E       assert '0' == '1'
E         - 1
E         + 0

tmpeknn2kwf.py:27: AssertionError
_______________________________ test_case[case7] _______________________________

i = 7, inp = '4\n())(\n', expected = '0\n'

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
E       AssertionError: input='4\n())(\n'
E         expected='0'
E         got='1'
E       assert '1' == '0'
E         - 0
E         + 1

tmpeknn2kwf.py:27: AssertionError
______________________________ test_case[case24] _______________________________

i = 24, inp = '4\n))((\n', expected = '0\n'

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
E       AssertionError: input='4\n))((\n'
E         expected='0'
E         got='2'
E       assert '2' == '0'
E         - 0
E         + 2

tmpeknn2kwf.py:27: AssertionError
______________________________ test_case[case29] _______________________________

i = 29, inp = '2\n)(\n', expected = '0\n'

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
E       AssertionError: input='2\n)(\n'
E         expected='0'
E         got='1'
E       assert '1' == '0'
E         - 0
E         + 1

tmpeknn2kwf.py:27: AssertionError
=========================== short test summary info ============================
FAILED tmpeknn2kwf.py::test_case[case0] - AssertionError: input='6\n(((())\n'
FAILED tmpeknn2kwf.py::test_case[case5] - AssertionError: input='2\n((\n'
FAILED tmpeknn2kwf.py::test_case[case6] - AssertionError: input='2\n))\n'
FAILED tmpeknn2kwf.py::test_case[case7] - AssertionError: input='4\n())(\n'
FAILED tmpeknn2kwf.py::test_case[case24] - AssertionError: input='4\n))((\n'
FAILED tmpeknn2kwf.py::test_case[case29] - AssertionError: input='2\n)(\n'
========================= 6 failed, 29 passed in 6.01s =========================
```
