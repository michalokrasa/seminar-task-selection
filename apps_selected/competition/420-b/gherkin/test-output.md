# competition/420-b

**Status:** FAIL (exit code 1)

## stdout

```
============================= test session starts ==============================
platform linux -- Python 3.10.18, pytest-7.4.4, pluggy-1.6.0
PyQt5 5.15.10 -- Qt runtime 5.15.17 -- Qt compiled 5.15.2
rootdir: /tmp/tmpxj5qw0rw
configfile: pytest.ini
plugins: Faker-25.1.0, anyio-4.9.0, cov-5.0.0, mock-3.12.0, qt-4.3.1
collected 38 items

tmpgx43tyky.py::test_case[case0] FAILED
tmpgx43tyky.py::test_case[case1] PASSED
tmpgx43tyky.py::test_case[case2] FAILED
tmpgx43tyky.py::test_case[case3] FAILED
tmpgx43tyky.py::test_case[case4] FAILED
tmpgx43tyky.py::test_case[case5] FAILED
tmpgx43tyky.py::test_case[case6] FAILED
tmpgx43tyky.py::test_case[case7] FAILED
tmpgx43tyky.py::test_case[case8] FAILED
tmpgx43tyky.py::test_case[case9] FAILED
tmpgx43tyky.py::test_case[case10] FAILED
tmpgx43tyky.py::test_case[case11] PASSED
tmpgx43tyky.py::test_case[case12] FAILED
tmpgx43tyky.py::test_case[case13] FAILED
tmpgx43tyky.py::test_case[case14] PASSED
tmpgx43tyky.py::test_case[case15] FAILED
tmpgx43tyky.py::test_case[case16] PASSED
tmpgx43tyky.py::test_case[case17] FAILED
tmpgx43tyky.py::test_case[case18] PASSED
tmpgx43tyky.py::test_case[case19] PASSED
tmpgx43tyky.py::test_case[case20] FAILED
tmpgx43tyky.py::test_case[case21] FAILED
tmpgx43tyky.py::test_case[case22] FAILED
tmpgx43tyky.py::test_case[case23] FAILED
tmpgx43tyky.py::test_case[case24] FAILED
tmpgx43tyky.py::test_case[case25] FAILED
tmpgx43tyky.py::test_case[case26] PASSED
tmpgx43tyky.py::test_case[case27] FAILED
tmpgx43tyky.py::test_case[case28] FAILED
tmpgx43tyky.py::test_case[case29] FAILED
tmpgx43tyky.py::test_case[case30] FAILED
tmpgx43tyky.py::test_case[case31] FAILED
tmpgx43tyky.py::test_case[case32] FAILED
tmpgx43tyky.py::test_case[case33] PASSED
tmpgx43tyky.py::test_case[case34] FAILED
tmpgx43tyky.py::test_case[case35] PASSED
tmpgx43tyky.py::test_case[case36] FAILED
tmpgx43tyky.py::test_case[case37] PASSED

=================================== FAILURES ===================================
_______________________________ test_case[case0] _______________________________

i = 0, inp = '5 4\n+ 1\n+ 2\n- 2\n- 1\n', expected = '4\n1 3 4 5 '

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
E       AssertionError: input='5 4\n+ 1\n+ 2\n- 2\n- 1\n'
E         expected='4\n1 3 4 5'
E         got='5\n1 2 3 4 5'
E       assert '5\n1 2 3 4 5' == '4\n1 3 4 5'
E         - 4
E         + 5
E         - 1 3 4 5
E         + 1 2 3 4 5
E         ?   ++

tmpgx43tyky.py:27: AssertionError
_______________________________ test_case[case2] _______________________________

i = 2, inp = '2 4\n+ 1\n- 1\n+ 2\n- 2\n', expected = '0\n'

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
E       AssertionError: input='2 4\n+ 1\n- 1\n+ 2\n- 2\n'
E         expected='0'
E         got='2\n1 2'
E       assert '2\n1 2' == '0'
E         - 0
E         + 2
E         + 1 2

tmpgx43tyky.py:27: AssertionError
_______________________________ test_case[case3] _______________________________

i = 3, inp = '5 6\n+ 1\n- 1\n- 3\n+ 3\n+ 4\n- 4\n', expected = '3\n2 3 5 '

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
E       AssertionError: input='5 6\n+ 1\n- 1\n- 3\n+ 3\n+ 4\n- 4\n'
E         expected='3\n2 3 5'
E         got='4\n1 2 4 5'
E       assert '4\n1 2 4 5' == '3\n2 3 5'
E         - 3
E         - 2 3 5
E         + 4
E         + 1 2 4 5

tmpgx43tyky.py:27: AssertionError
_______________________________ test_case[case4] _______________________________

i = 4, inp = '2 4\n+ 1\n- 2\n+ 2\n- 1\n', expected = '0\n'

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
E       AssertionError: input='2 4\n+ 1\n- 2\n+ 2\n- 1\n'
E         expected='0'
E         got='1\n1'
E       assert '1\n1' == '0'
E         - 0
E         + 1
E         + 1

tmpgx43tyky.py:27: AssertionError
_______________________________ test_case[case5] _______________________________

i = 5, inp = '1 1\n+ 1\n', expected = '1\n1 '

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
E       AssertionError: input='1 1\n+ 1\n'
E         expected='1\n1'
E         got='0'
E       assert '0' == '1\n1'
E         + 0
E         - 1
E         - 1

tmpgx43tyky.py:27: AssertionError
_______________________________ test_case[case6] _______________________________

i = 6, inp = '2 1\n- 2\n', expected = '2\n1 2 '

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
E       AssertionError: input='2 1\n- 2\n'
E         expected='2\n1 2'
E         got='1\n1'
E       assert '1\n1' == '2\n1 2'
E         - 2
E         - 1 2
E         + 1
E         + 1

tmpgx43tyky.py:27: AssertionError
_______________________________ test_case[case7] _______________________________

i = 7, inp = '3 5\n- 1\n+ 1\n+ 2\n- 2\n+ 3\n', expected = '1\n1 '

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
E       AssertionError: input='3 5\n- 1\n+ 1\n+ 2\n- 2\n+ 3\n'
E         expected='1\n1'
E         got='1\n2'
E       assert '1\n2' == '1\n1'
E           1
E         - 1
E         + 2

tmpgx43tyky.py:27: AssertionError
_______________________________ test_case[case8] _______________________________

i = 8, inp = '10 8\n+ 1\n- 1\n- 2\n- 3\n+ 3\n+ 7\n- 7\n+ 9\n'
expected = '6\n3 4 5 6 8 10 '

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
E       AssertionError: input='10 8\n+ 1\n- 1\n- 2\n- 3\n+ 3\n+ 7\n- 7\n+ 9\n'
E         expected='6\n3 4 5 6 8 10'
E         got='7\n1 4 5 6 7 8 10'
E       assert '7\n1 4 5 6 7 8 10' == '6\n3 4 5 6 8 10'
E         - 6
E         + 7
E         - 3 4 5 6 8 10
E         ? ^
E         + 1 4 5 6 7 8 10
E         ? ^       ++

tmpgx43tyky.py:27: AssertionError
_______________________________ test_case[case9] _______________________________

i = 9, inp = '5 5\n+ 5\n+ 2\n+ 3\n+ 4\n+ 1\n', expected = '1\n5 '

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
E       AssertionError: input='5 5\n+ 5\n+ 2\n+ 3\n+ 4\n+ 1\n'
E         expected='1\n5'
E         got='0'
E       assert '0' == '1\n5'
E         + 0
E         - 1
E         - 5

tmpgx43tyky.py:27: AssertionError
______________________________ test_case[case10] _______________________________

i = 10, inp = '5 4\n+ 1\n- 1\n+ 1\n+ 2\n', expected = '4\n1 3 4 5 '

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
E       AssertionError: input='5 4\n+ 1\n- 1\n+ 1\n+ 2\n'
E         expected='4\n1 3 4 5'
E         got='3\n3 4 5'
E       assert '3\n3 4 5' == '4\n1 3 4 5'
E         - 4
E         + 3
E         - 1 3 4 5
E         ? --
E         + 3 4 5

tmpgx43tyky.py:27: AssertionError
______________________________ test_case[case12] _______________________________

i = 12
inp = '1 20\n- 1\n+ 1\n- 1\n+ 1\n- 1\n+ 1\n- 1\n+ 1\n- 1\n+ 1\n- 1\n+ 1\n- 1\n+ 1\n- 1\n+ 1\n- 1\n+ 1\n- 1\n+ 1\n'
expected = '1\n1 '

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
E       AssertionError: input='1 20\n- 1\n+ 1\n- 1\n+ 1\n- 1\n+ 1\n- 1\n+ 1\n- 1\n+ 1\n- 1\n+ 1\n- 1\n+ 1\n- 1\n+ 1\n- 1\n+ 1\n- 1\n+ 1\n'
E         expected='1\n1'
E         got='0'
E       assert '0' == '1\n1'
E         + 0
E         - 1
E         - 1

tmpgx43tyky.py:27: AssertionError
______________________________ test_case[case13] _______________________________

i = 13, inp = '20 1\n- 16\n'
expected = '20\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 '

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
E       AssertionError: input='20 1\n- 16\n'
E         expected='20\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20'
E         got='19\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 17 18 19 20'
E       assert '19\n1 2 3 4 ...5 17 18 19 20' == '20\n1 2 3 4 ...6 17 18 19 20'
E         - 20
E         + 19
E         - 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
E         ?                                     ---
E         + 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 17 18 19 20

tmpgx43tyky.py:27: AssertionError
______________________________ test_case[case15] _______________________________

i = 15
inp = '20 50\n+ 5\n+ 11\n- 5\n+ 6\n- 16\n- 13\n+ 5\n+ 7\n- 8\n- 7\n- 10\n+ 10\n- 20\n- 19\n+ 17\n- 2\n+ 2\n+ 19\n+ 18\n- 2\n...n- 15\n+ 2\n+ 5\n- 2\n+ 9\n- 11\n+ 2\n- 19\n+ 7\n+ 12\n+ 16\n+ 19\n- 18\n- 2\n+ 18\n- 9\n- 10\n+ 9\n+ 13\n- 14\n- 16\n'
expected = '2\n1 3 '

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
E       AssertionError: input='20 50\n+ 5\n+ 11\n- 5\n+ 6\n- 16\n- 13\n+ 5\n+ 7\n- 8\n- 7\n- 10\n+ 10\n- 20\n- 19\n+ 17\n- 2\n+ 2\n+ 19\n+ 18\n- 2\n- 6\n- 5\n+ 6\n+ 4\n- 14\n+ 14\n- 9\n+ 15\n- 17\n- 15\n+ 2\n+ 5\n- 2\n+ 9\n- 11\n+ 2\n- 19\n+ 7\n+ 12\n+ 16\n+ 19\n- 18\n- 2\n+ 18\n- 9\n- 10\n+ 9\n+ 13\n- 14\n- 16\n'
E         expected='2\n1 3'
E         got='5\n1 3 11 15 17'
E       assert '5\n1 3 11 15 17' == '2\n1 3'
E         - 2
E         - 1 3
E         + 5
E         + 1 3 11 15 17

tmpgx43tyky.py:27: AssertionError
______________________________ test_case[case17] _______________________________

i = 17, inp = '4 4\n+ 2\n- 1\n- 3\n- 2\n', expected = '1\n4 '

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
E       AssertionError: input='4 4\n+ 2\n- 1\n- 3\n- 2\n'
E         expected='1\n4'
E         got='2\n2 4'
E       assert '2\n2 4' == '1\n4'
E         - 1
E         - 4
E         + 2
E         + 2 4

tmpgx43tyky.py:27: AssertionError
______________________________ test_case[case20] _______________________________

i = 20, inp = '6 6\n- 5\n- 6\n- 3\n- 1\n- 2\n- 4\n', expected = '1\n4 '

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
E       AssertionError: input='6 6\n- 5\n- 6\n- 3\n- 1\n- 2\n- 4\n'
E         expected='1\n4'
E         got='0'
E       assert '0' == '1\n4'
E         + 0
E         - 1
E         - 4

tmpgx43tyky.py:27: AssertionError
______________________________ test_case[case21] _______________________________

i = 21, inp = '10 7\n- 8\n+ 1\n+ 2\n+ 3\n- 2\n- 3\n- 1\n'
expected = '6\n4 5 6 7 9 10 '

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
E       AssertionError: input='10 7\n- 8\n+ 1\n+ 2\n+ 3\n- 2\n- 3\n- 1\n'
E         expected='6\n4 5 6 7 9 10'
E         got='9\n1 2 3 4 5 6 7 9 10'
E       assert '9\n1 2 3 4 5 6 7 9 10' == '6\n4 5 6 7 9 10'
E         - 6
E         + 9
E         - 4 5 6 7 9 10
E         + 1 2 3 4 5 6 7 9 10
E         ? ++++++

tmpgx43tyky.py:27: AssertionError
______________________________ test_case[case22] _______________________________

i = 22, inp = '10 7\n- 8\n+ 1\n+ 2\n+ 3\n- 2\n- 3\n- 1\n'
expected = '6\n4 5 6 7 9 10 '

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
E       AssertionError: input='10 7\n- 8\n+ 1\n+ 2\n+ 3\n- 2\n- 3\n- 1\n'
E         expected='6\n4 5 6 7 9 10'
E         got='9\n1 2 3 4 5 6 7 9 10'
E       assert '9\n1 2 3 4 5 6 7 9 10' == '6\n4 5 6 7 9 10'
E         - 6
E         + 9
E         - 4 5 6 7 9 10
E         + 1 2 3 4 5 6 7 9 10
E         ? ++++++

tmpgx43tyky.py:27: AssertionError
______________________________ test_case[case23] _______________________________

i = 23, inp = '4 10\n+ 2\n- 1\n- 2\n- 3\n+ 3\n+ 2\n+ 4\n- 2\n+ 2\n+ 1\n'
expected = '1\n3 '

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
E       AssertionError: input='4 10\n+ 2\n- 1\n- 2\n- 3\n+ 3\n+ 2\n+ 4\n- 2\n+ 2\n+ 1\n'
E         expected='1\n3'
E         got='0'
E       assert '0' == '1\n3'
E         + 0
E         - 1
E         - 3

tmpgx43tyky.py:27: AssertionError
______________________________ test_case[case24] _______________________________

i = 24, inp = '4 9\n+ 2\n- 1\n- 2\n- 3\n+ 3\n+ 2\n+ 4\n- 2\n+ 2\n'
expected = '1\n3 '

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
E       AssertionError: input='4 9\n+ 2\n- 1\n- 2\n- 3\n+ 3\n+ 2\n+ 4\n- 2\n+ 2\n'
E         expected='1\n3'
E         got='0'
E       assert '0' == '1\n3'
E         + 0
E         - 1
E         - 3

tmpgx43tyky.py:27: AssertionError
______________________________ test_case[case25] _______________________________

i = 25, inp = '10 8\n+ 1\n- 1\n- 4\n+ 4\n+ 3\n+ 7\n- 7\n+ 9\n'
expected = '6\n2 4 5 6 8 10 '

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
E       AssertionError: input='10 8\n+ 1\n- 1\n- 4\n+ 4\n+ 3\n+ 7\n- 7\n+ 9\n'
E         expected='6\n2 4 5 6 8 10'
E         got='7\n1 2 5 6 7 8 10'
E       assert '7\n1 2 5 6 7 8 10' == '6\n2 4 5 6 8 10'
E         - 6
E         + 7
E         - 2 4 5 6 8 10
E         ?   --
E         + 1 2 5 6 7 8 10
E         ? ++      ++

tmpgx43tyky.py:27: AssertionError
______________________________ test_case[case27] _______________________________

i = 27, inp = '10 5\n+ 2\n- 2\n+ 2\n- 2\n- 3\n'
expected = '9\n1 3 4 5 6 7 8 9 10 '

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
E       AssertionError: input='10 5\n+ 2\n- 2\n+ 2\n- 2\n- 3\n'
E         expected='9\n1 3 4 5 6 7 8 9 10'
E         got='9\n1 2 4 5 6 7 8 9 10'
E       assert '9\n1 2 4 5 6 7 8 9 10' == '9\n1 3 4 5 6 7 8 9 10'
E           9
E         - 1 3 4 5 6 7 8 9 10
E         ?   ^
E         + 1 2 4 5 6 7 8 9 10
E         ?   ^

tmpgx43tyky.py:27: AssertionError
______________________________ test_case[case28] _______________________________

i = 28, inp = '10 11\n+ 1\n- 1\n- 2\n+ 3\n- 3\n- 4\n+ 5\n- 5\n- 6\n+ 6\n+ 7\n'
expected = '4\n6 8 9 10 '

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
E       AssertionError: input='10 11\n+ 1\n- 1\n- 2\n+ 3\n- 3\n- 4\n+ 5\n- 5\n- 6\n+ 6\n+ 7\n'
E         expected='4\n6 8 9 10'
E         got='6\n1 3 5 8 9 10'
E       assert '6\n1 3 5 8 9 10' == '4\n6 8 9 10'
E         - 4
E         - 6 8 9 10
E         + 6
E         + 1 3 5 8 9 10

tmpgx43tyky.py:27: AssertionError
______________________________ test_case[case29] _______________________________

i = 29, inp = '10 10\n+ 1\n- 1\n- 2\n+ 3\n- 3\n- 4\n+ 5\n- 5\n- 6\n+ 6\n'
expected = '5\n6 7 8 9 10 '

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
E       AssertionError: input='10 10\n+ 1\n- 1\n- 2\n+ 3\n- 3\n- 4\n+ 5\n- 5\n- 6\n+ 6\n'
E         expected='5\n6 7 8 9 10'
E         got='7\n1 3 5 7 8 9 10'
E       assert '7\n1 3 5 7 8 9 10' == '5\n6 7 8 9 10'
E         - 5
E         + 7
E         - 6 7 8 9 10
E         ? ^
E         + 1 3 5 7 8 9 10
E         ? ^^^^^

tmpgx43tyky.py:27: AssertionError
______________________________ test_case[case30] _______________________________

i = 30, inp = '10 9\n+ 1\n- 1\n- 2\n+ 3\n- 3\n- 4\n+ 5\n- 5\n- 6\n'
expected = '5\n6 7 8 9 10 '

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
E       AssertionError: input='10 9\n+ 1\n- 1\n- 2\n+ 3\n- 3\n- 4\n+ 5\n- 5\n- 6\n'
E         expected='5\n6 7 8 9 10'
E         got='7\n1 3 5 7 8 9 10'
E       assert '7\n1 3 5 7 8 9 10' == '5\n6 7 8 9 10'
E         - 5
E         + 7
E         - 6 7 8 9 10
E         ? ^
E         + 1 3 5 7 8 9 10
E         ? ^^^^^

tmpgx43tyky.py:27: AssertionError
______________________________ test_case[case31] _______________________________

i = 31
inp = '10 12\n+ 1\n- 1\n- 2\n+ 3\n- 3\n- 4\n+ 5\n- 5\n- 6\n+ 6\n+ 7\n- 7\n'
expected = '4\n6 8 9 10 '

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
E       AssertionError: input='10 12\n+ 1\n- 1\n- 2\n+ 3\n- 3\n- 4\n+ 5\n- 5\n- 6\n+ 6\n+ 7\n- 7\n'
E         expected='4\n6 8 9 10'
E         got='7\n1 3 5 7 8 9 10'
E       assert '7\n1 3 5 7 8 9 10' == '4\n6 8 9 10'
E         - 4
E         - 6 8 9 10
E         + 7
E         + 1 3 5 7 8 9 10

tmpgx43tyky.py:27: AssertionError
______________________________ test_case[case32] _______________________________

i = 32, inp = '2 2\n- 1\n+ 1\n', expected = '2\n1 2 '

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
E       AssertionError: input='2 2\n- 1\n+ 1\n'
E         expected='2\n1 2'
E         got='1\n2'
E       assert '1\n2' == '2\n1 2'
E         - 2
E         - 1 2
E         + 1
E         + 2

tmpgx43tyky.py:27: AssertionError
______________________________ test_case[case34] _______________________________

i = 34, inp = '2 3\n+ 1\n+ 2\n- 1\n', expected = '0\n'

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
E       AssertionError: input='2 3\n+ 1\n+ 2\n- 1\n'
E         expected='0'
E         got='1\n1'
E       assert '1\n1' == '0'
E         - 0
E         + 1
E         + 1

tmpgx43tyky.py:27: AssertionError
______________________________ test_case[case36] _______________________________

i = 36, inp = '5 3\n+ 1\n- 1\n+ 2\n', expected = '3\n3 4 5 '

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
E       AssertionError: input='5 3\n+ 1\n- 1\n+ 2\n'
E         expected='3\n3 4 5'
E         got='4\n1 3 4 5'
E       assert '4\n1 3 4 5' == '3\n3 4 5'
E         - 3
E         + 4
E         - 3 4 5
E         + 1 3 4 5
E         ? ++

tmpgx43tyky.py:27: AssertionError
=========================== short test summary info ============================
FAILED tmpgx43tyky.py::test_case[case0] - AssertionError: input='5 4\n+ 1\n+ ...
FAILED tmpgx43tyky.py::test_case[case2] - AssertionError: input='2 4\n+ 1\n- ...
FAILED tmpgx43tyky.py::test_case[case3] - AssertionError: input='5 6\n+ 1\n- ...
FAILED tmpgx43tyky.py::test_case[case4] - AssertionError: input='2 4\n+ 1\n- ...
FAILED tmpgx43tyky.py::test_case[case5] - AssertionError: input='1 1\n+ 1\n'
FAILED tmpgx43tyky.py::test_case[case6] - AssertionError: input='2 1\n- 2\n'
FAILED tmpgx43tyky.py::test_case[case7] - AssertionError: input='3 5\n- 1\n+ ...
FAILED tmpgx43tyky.py::test_case[case8] - AssertionError: input='10 8\n+ 1\n-...
FAILED tmpgx43tyky.py::test_case[case9] - AssertionError: input='5 5\n+ 5\n+ ...
FAILED tmpgx43tyky.py::test_case[case10] - AssertionError: input='5 4\n+ 1\n-...
FAILED tmpgx43tyky.py::test_case[case12] - AssertionError: input='1 20\n- 1\n...
FAILED tmpgx43tyky.py::test_case[case13] - AssertionError: input='20 1\n- 16\n'
FAILED tmpgx43tyky.py::test_case[case15] - AssertionError: input='20 50\n+ 5\...
FAILED tmpgx43tyky.py::test_case[case17] - AssertionError: input='4 4\n+ 2\n-...
FAILED tmpgx43tyky.py::test_case[case20] - AssertionError: input='6 6\n- 5\n-...
FAILED tmpgx43tyky.py::test_case[case21] - AssertionError: input='10 7\n- 8\n...
FAILED tmpgx43tyky.py::test_case[case22] - AssertionError: input='10 7\n- 8\n...
FAILED tmpgx43tyky.py::test_case[case23] - AssertionError: input='4 10\n+ 2\n...
FAILED tmpgx43tyky.py::test_case[case24] - AssertionError: input='4 9\n+ 2\n-...
FAILED tmpgx43tyky.py::test_case[case25] - AssertionError: input='10 8\n+ 1\n...
FAILED tmpgx43tyky.py::test_case[case27] - AssertionError: input='10 5\n+ 2\n...
FAILED tmpgx43tyky.py::test_case[case28] - AssertionError: input='10 11\n+ 1\...
FAILED tmpgx43tyky.py::test_case[case29] - AssertionError: input='10 10\n+ 1\...
FAILED tmpgx43tyky.py::test_case[case30] - AssertionError: input='10 9\n+ 1\n...
FAILED tmpgx43tyky.py::test_case[case31] - AssertionError: input='10 12\n+ 1\...
FAILED tmpgx43tyky.py::test_case[case32] - AssertionError: input='2 2\n- 1\n+...
FAILED tmpgx43tyky.py::test_case[case34] - AssertionError: input='2 3\n+ 1\n+...
FAILED tmpgx43tyky.py::test_case[case36] - AssertionError: input='5 3\n+ 1\n-...
======================== 28 failed, 10 passed in 7.37s =========================
```
