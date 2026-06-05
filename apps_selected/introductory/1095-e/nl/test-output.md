# introductory/1095-e

**Status:** FAIL (exit code 1)

## stdout

```
============================= test session starts ==============================
platform linux -- Python 3.10.18, pytest-7.4.4, pluggy-1.6.0
PyQt5 5.15.10 -- Qt runtime 5.15.17 -- Qt compiled 5.15.2
rootdir: /tmp/tmpm0jtj4nv
configfile: pytest.ini
plugins: Faker-25.1.0, anyio-4.9.0, cov-5.0.0, mock-3.12.0, qt-4.3.1
collected 35 items

tmpau_0i73v.py::test_case[case0] FAILED
tmpau_0i73v.py::test_case[case1] FAILED
tmpau_0i73v.py::test_case[case2] FAILED
tmpau_0i73v.py::test_case[case3] FAILED
tmpau_0i73v.py::test_case[case4] FAILED
tmpau_0i73v.py::test_case[case5] FAILED
tmpau_0i73v.py::test_case[case6] FAILED
tmpau_0i73v.py::test_case[case7] FAILED
tmpau_0i73v.py::test_case[case8] FAILED
tmpau_0i73v.py::test_case[case9] FAILED
tmpau_0i73v.py::test_case[case10] FAILED
tmpau_0i73v.py::test_case[case11] FAILED
tmpau_0i73v.py::test_case[case12] FAILED
tmpau_0i73v.py::test_case[case13] FAILED
tmpau_0i73v.py::test_case[case14] FAILED
tmpau_0i73v.py::test_case[case15] FAILED
tmpau_0i73v.py::test_case[case16] FAILED
tmpau_0i73v.py::test_case[case17] FAILED
tmpau_0i73v.py::test_case[case18] FAILED
tmpau_0i73v.py::test_case[case19] FAILED
tmpau_0i73v.py::test_case[case20] FAILED
tmpau_0i73v.py::test_case[case21] FAILED
tmpau_0i73v.py::test_case[case22] FAILED
tmpau_0i73v.py::test_case[case23] FAILED
tmpau_0i73v.py::test_case[case24] FAILED
tmpau_0i73v.py::test_case[case25] FAILED
tmpau_0i73v.py::test_case[case26] FAILED
tmpau_0i73v.py::test_case[case27] FAILED
tmpau_0i73v.py::test_case[case28] FAILED
tmpau_0i73v.py::test_case[case29] FAILED
tmpau_0i73v.py::test_case[case30] FAILED
tmpau_0i73v.py::test_case[case31] FAILED
tmpau_0i73v.py::test_case[case32] FAILED
tmpau_0i73v.py::test_case[case33] FAILED
tmpau_0i73v.py::test_case[case34] FAILED

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
E         got=''
E       assert '' == '3'
E         - 3

tmpau_0i73v.py:27: AssertionError
_______________________________ test_case[case1] _______________________________

i = 1, inp = '6\n()()()\n', expected = '0\n'

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
E       AssertionError: input='6\n()()()\n'
E         expected='0'
E         got=''
E       assert '' == '0'
E         - 0

tmpau_0i73v.py:27: AssertionError
_______________________________ test_case[case2] _______________________________

i = 2, inp = '1\n)\n', expected = '0\n'

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
E       AssertionError: input='1\n)\n'
E         expected='0'
E         got=''
E       assert '' == '0'
E         - 0

tmpau_0i73v.py:27: AssertionError
_______________________________ test_case[case3] _______________________________

i = 3, inp = '8\n)))(((((\n', expected = '0\n'

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
E       AssertionError: input='8\n)))(((((\n'
E         expected='0'
E         got=''
E       assert '' == '0'
E         - 0

tmpau_0i73v.py:27: AssertionError
_______________________________ test_case[case4] _______________________________

i = 4, inp = '10\n))()))((()\n', expected = '0\n'

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
E       AssertionError: input='10\n))()))((()\n'
E         expected='0'
E         got=''
E       assert '' == '0'
E         - 0

tmpau_0i73v.py:27: AssertionError
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
E         got=''
E       assert '' == '1'
E         - 1

tmpau_0i73v.py:27: AssertionError
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
E         got=''
E       assert '' == '1'
E         - 1

tmpau_0i73v.py:27: AssertionError
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
E         got=''
E       assert '' == '0'
E         - 0

tmpau_0i73v.py:27: AssertionError
_______________________________ test_case[case8] _______________________________

i = 8, inp = '4\n))))\n', expected = '0\n'

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
E       AssertionError: input='4\n))))\n'
E         expected='0'
E         got=''
E       assert '' == '0'
E         - 0

tmpau_0i73v.py:27: AssertionError
_______________________________ test_case[case9] _______________________________

i = 9, inp = '6\n))((((\n', expected = '0\n'

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
E       AssertionError: input='6\n))((((\n'
E         expected='0'
E         got=''
E       assert '' == '0'
E         - 0

tmpau_0i73v.py:27: AssertionError
______________________________ test_case[case10] _______________________________

i = 10, inp = '12\n()()))())()(\n', expected = '0\n'

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
E       AssertionError: input='12\n()()))())()(\n'
E         expected='0'
E         got=''
E       assert '' == '0'
E         - 0

tmpau_0i73v.py:27: AssertionError
______________________________ test_case[case11] _______________________________

i = 11, inp = '9\n(((()((()\n', expected = '0\n'

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
E       AssertionError: input='9\n(((()((()\n'
E         expected='0'
E         got=''
E       assert '' == '0'
E         - 0

tmpau_0i73v.py:27: AssertionError
______________________________ test_case[case12] _______________________________

i = 12, inp = '10\n)())((()((\n', expected = '0\n'

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
E       AssertionError: input='10\n)())((()((\n'
E         expected='0'
E         got=''
E       assert '' == '0'
E         - 0

tmpau_0i73v.py:27: AssertionError
______________________________ test_case[case13] _______________________________

i = 13, inp = '17\n))((()(((()()))()\n', expected = '0\n'

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
E       AssertionError: input='17\n))((()(((()()))()\n'
E         expected='0'
E         got=''
E       assert '' == '0'
E         - 0

tmpau_0i73v.py:27: AssertionError
______________________________ test_case[case14] _______________________________

i = 14, inp = '8\n())(((()\n', expected = '0\n'

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
E       AssertionError: input='8\n())(((()\n'
E         expected='0'
E         got=''
E       assert '' == '0'
E         - 0

tmpau_0i73v.py:27: AssertionError
______________________________ test_case[case15] _______________________________

i = 15, inp = '8\n())()(((\n', expected = '0\n'

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
E       AssertionError: input='8\n())()(((\n'
E         expected='0'
E         got=''
E       assert '' == '0'
E         - 0

tmpau_0i73v.py:27: AssertionError
______________________________ test_case[case16] _______________________________

i = 16, inp = '4\n)(((\n', expected = '0\n'

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
E       AssertionError: input='4\n)(((\n'
E         expected='0'
E         got=''
E       assert '' == '0'
E         - 0

tmpau_0i73v.py:27: AssertionError
______________________________ test_case[case17] _______________________________

i = 17, inp = '10\n)(()()(()(\n', expected = '0\n'

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
E       AssertionError: input='10\n)(()()(()(\n'
E         expected='0'
E         got=''
E       assert '' == '0'
E         - 0

tmpau_0i73v.py:27: AssertionError
______________________________ test_case[case18] _______________________________

i = 18, inp = '16\n((())()((()()(()\n', expected = '0\n'

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
E       AssertionError: input='16\n((())()((()()(()\n'
E         expected='0'
E         got=''
E       assert '' == '0'
E         - 0

tmpau_0i73v.py:27: AssertionError
______________________________ test_case[case19] _______________________________

i = 19, inp = '20\n(())(()((((()())()((\n', expected = '0\n'

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
E       AssertionError: input='20\n(())(()((((()())()((\n'
E         expected='0'
E         got=''
E       assert '' == '0'
E         - 0

tmpau_0i73v.py:27: AssertionError
______________________________ test_case[case20] _______________________________

i = 20, inp = '10\n(()(())(((\n', expected = '0\n'

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
E       AssertionError: input='10\n(()(())(((\n'
E         expected='0'
E         got=''
E       assert '' == '0'
E         - 0

tmpau_0i73v.py:27: AssertionError
______________________________ test_case[case21] _______________________________

i = 21, inp = '19\n)(()()()()))(()))))\n', expected = '0\n'

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
E       AssertionError: input='19\n)(()()()()))(()))))\n'
E         expected='0'
E         got=''
E       assert '' == '0'
E         - 0

tmpau_0i73v.py:27: AssertionError
______________________________ test_case[case22] _______________________________

i = 22, inp = '6\n)(()((\n', expected = '0\n'

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
E       AssertionError: input='6\n)(()((\n'
E         expected='0'
E         got=''
E       assert '' == '0'
E         - 0

tmpau_0i73v.py:27: AssertionError
______________________________ test_case[case23] _______________________________

i = 23, inp = '3\n))(\n', expected = '0\n'

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
E       AssertionError: input='3\n))(\n'
E         expected='0'
E         got=''
E       assert '' == '0'
E         - 0

tmpau_0i73v.py:27: AssertionError
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
E         got=''
E       assert '' == '0'
E         - 0

tmpau_0i73v.py:27: AssertionError
______________________________ test_case[case25] _______________________________

i = 25, inp = '6\n())(((\n', expected = '0\n'

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
E       AssertionError: input='6\n())(((\n'
E         expected='0'
E         got=''
E       assert '' == '0'
E         - 0

tmpau_0i73v.py:27: AssertionError
______________________________ test_case[case26] _______________________________

i = 26, inp = '6\n()))))\n', expected = '0\n'

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
E       AssertionError: input='6\n()))))\n'
E         expected='0'
E         got=''
E       assert '' == '0'
E         - 0

tmpau_0i73v.py:27: AssertionError
______________________________ test_case[case27] _______________________________

i = 27, inp = '3\n)))\n', expected = '0\n'

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
E       AssertionError: input='3\n)))\n'
E         expected='0'
E         got=''
E       assert '' == '0'
E         - 0

tmpau_0i73v.py:27: AssertionError
______________________________ test_case[case28] _______________________________

i = 28, inp = '12\n)())(())((((\n', expected = '0\n'

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
E       AssertionError: input='12\n)())(())((((\n'
E         expected='0'
E         got=''
E       assert '' == '0'
E         - 0

tmpau_0i73v.py:27: AssertionError
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
E         got=''
E       assert '' == '0'
E         - 0

tmpau_0i73v.py:27: AssertionError
______________________________ test_case[case30] _______________________________

i = 30, inp = '6\n)(((()\n', expected = '0\n'

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
E       AssertionError: input='6\n)(((()\n'
E         expected='0'
E         got=''
E       assert '' == '0'
E         - 0

tmpau_0i73v.py:27: AssertionError
______________________________ test_case[case31] _______________________________

i = 31, inp = '15\n(((((()(()(()()\n', expected = '0\n'

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
E       AssertionError: input='15\n(((((()(()(()()\n'
E         expected='0'
E         got=''
E       assert '' == '0'
E         - 0

tmpau_0i73v.py:27: AssertionError
______________________________ test_case[case32] _______________________________

i = 32, inp = '3\n(((\n', expected = '0\n'

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
E       AssertionError: input='3\n(((\n'
E         expected='0'
E         got=''
E       assert '' == '0'
E         - 0

tmpau_0i73v.py:27: AssertionError
______________________________ test_case[case33] _______________________________

i = 33, inp = '4\n)))(\n', expected = '0\n'

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
E       AssertionError: input='4\n)))(\n'
E         expected='0'
E         got=''
E       assert '' == '0'
E         - 0

tmpau_0i73v.py:27: AssertionError
______________________________ test_case[case34] _______________________________

i = 34, inp = '10\n())))((())\n', expected = '0\n'

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
E       AssertionError: input='10\n())))((())\n'
E         expected='0'
E         got=''
E       assert '' == '0'
E         - 0

tmpau_0i73v.py:27: AssertionError
=========================== short test summary info ============================
FAILED tmpau_0i73v.py::test_case[case0] - AssertionError: input='6\n(((())\n'
FAILED tmpau_0i73v.py::test_case[case1] - AssertionError: input='6\n()()()\n'
FAILED tmpau_0i73v.py::test_case[case2] - AssertionError: input='1\n)\n'
FAILED tmpau_0i73v.py::test_case[case3] - AssertionError: input='8\n)))(((((\n'
FAILED tmpau_0i73v.py::test_case[case4] - AssertionError: input='10\n))()))((...
FAILED tmpau_0i73v.py::test_case[case5] - AssertionError: input='2\n((\n'
FAILED tmpau_0i73v.py::test_case[case6] - AssertionError: input='2\n))\n'
FAILED tmpau_0i73v.py::test_case[case7] - AssertionError: input='4\n())(\n'
FAILED tmpau_0i73v.py::test_case[case8] - AssertionError: input='4\n))))\n'
FAILED tmpau_0i73v.py::test_case[case9] - AssertionError: input='6\n))((((\n'
FAILED tmpau_0i73v.py::test_case[case10] - AssertionError: input='12\n()()))(...
FAILED tmpau_0i73v.py::test_case[case11] - AssertionError: input='9\n(((()(((...
FAILED tmpau_0i73v.py::test_case[case12] - AssertionError: input='10\n)())(((...
FAILED tmpau_0i73v.py::test_case[case13] - AssertionError: input='17\n))((()(...
FAILED tmpau_0i73v.py::test_case[case14] - AssertionError: input='8\n())(((()\n'
FAILED tmpau_0i73v.py::test_case[case15] - AssertionError: input='8\n())()(((\n'
FAILED tmpau_0i73v.py::test_case[case16] - AssertionError: input='4\n)(((\n'
FAILED tmpau_0i73v.py::test_case[case17] - AssertionError: input='10\n)(()()(...
FAILED tmpau_0i73v.py::test_case[case18] - AssertionError: input='16\n((())()...
FAILED tmpau_0i73v.py::test_case[case19] - AssertionError: input='20\n(())(()...
FAILED tmpau_0i73v.py::test_case[case20] - AssertionError: input='10\n(()(())...
FAILED tmpau_0i73v.py::test_case[case21] - AssertionError: input='19\n)(()()(...
FAILED tmpau_0i73v.py::test_case[case22] - AssertionError: input='6\n)(()((\n'
FAILED tmpau_0i73v.py::test_case[case23] - AssertionError: input='3\n))(\n'
FAILED tmpau_0i73v.py::test_case[case24] - AssertionError: input='4\n))((\n'
FAILED tmpau_0i73v.py::test_case[case25] - AssertionError: input='6\n())(((\n'
FAILED tmpau_0i73v.py::test_case[case26] - AssertionError: input='6\n()))))\n'
FAILED tmpau_0i73v.py::test_case[case27] - AssertionError: input='3\n)))\n'
FAILED tmpau_0i73v.py::test_case[case28] - AssertionError: input='12\n)())(()...
FAILED tmpau_0i73v.py::test_case[case29] - AssertionError: input='2\n)(\n'
FAILED tmpau_0i73v.py::test_case[case30] - AssertionError: input='6\n)(((()\n'
FAILED tmpau_0i73v.py::test_case[case31] - AssertionError: input='15\n(((((()...
FAILED tmpau_0i73v.py::test_case[case32] - AssertionError: input='3\n(((\n'
FAILED tmpau_0i73v.py::test_case[case33] - AssertionError: input='4\n)))(\n'
FAILED tmpau_0i73v.py::test_case[case34] - AssertionError: input='10\n())))((...
============================== 35 failed in 6.44s ==============================
```
