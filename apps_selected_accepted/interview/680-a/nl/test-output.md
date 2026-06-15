# interview/680-a

**Status:** FAIL (exit code 1)

## stdout

```
============================= test session starts ==============================
platform linux -- Python 3.10.18, pytest-7.4.4, pluggy-1.6.0
PyQt5 5.15.10 -- Qt runtime 5.15.17 -- Qt compiled 5.15.2
rootdir: /tmp/tmpbs77r2ht
configfile: pytest.ini
plugins: Faker-25.1.0, anyio-4.9.0, cov-5.0.0, mock-3.12.0, qt-4.3.1
collected 48 items

tmplgdjapcm.py::test_case[case0] FAILED
tmplgdjapcm.py::test_case[case1] FAILED
tmplgdjapcm.py::test_case[case2] FAILED
tmplgdjapcm.py::test_case[case3] FAILED
tmplgdjapcm.py::test_case[case4] FAILED
tmplgdjapcm.py::test_case[case5] FAILED
tmplgdjapcm.py::test_case[case6] FAILED
tmplgdjapcm.py::test_case[case7] FAILED
tmplgdjapcm.py::test_case[case8] FAILED
tmplgdjapcm.py::test_case[case9] FAILED
tmplgdjapcm.py::test_case[case10] FAILED
tmplgdjapcm.py::test_case[case11] FAILED
tmplgdjapcm.py::test_case[case12] FAILED
tmplgdjapcm.py::test_case[case13] FAILED
tmplgdjapcm.py::test_case[case14] FAILED
tmplgdjapcm.py::test_case[case15] FAILED
tmplgdjapcm.py::test_case[case16] FAILED
tmplgdjapcm.py::test_case[case17] FAILED
tmplgdjapcm.py::test_case[case18] FAILED
tmplgdjapcm.py::test_case[case19] FAILED
tmplgdjapcm.py::test_case[case20] FAILED
tmplgdjapcm.py::test_case[case21] FAILED
tmplgdjapcm.py::test_case[case22] FAILED
tmplgdjapcm.py::test_case[case23] FAILED
tmplgdjapcm.py::test_case[case24] FAILED
tmplgdjapcm.py::test_case[case25] FAILED
tmplgdjapcm.py::test_case[case26] FAILED
tmplgdjapcm.py::test_case[case27] FAILED
tmplgdjapcm.py::test_case[case28] FAILED
tmplgdjapcm.py::test_case[case29] FAILED
tmplgdjapcm.py::test_case[case30] FAILED
tmplgdjapcm.py::test_case[case31] FAILED
tmplgdjapcm.py::test_case[case32] FAILED
tmplgdjapcm.py::test_case[case33] FAILED
tmplgdjapcm.py::test_case[case34] FAILED
tmplgdjapcm.py::test_case[case35] FAILED
tmplgdjapcm.py::test_case[case36] FAILED
tmplgdjapcm.py::test_case[case37] FAILED
tmplgdjapcm.py::test_case[case38] FAILED
tmplgdjapcm.py::test_case[case39] FAILED
tmplgdjapcm.py::test_case[case40] FAILED
tmplgdjapcm.py::test_case[case41] FAILED
tmplgdjapcm.py::test_case[case42] FAILED
tmplgdjapcm.py::test_case[case43] FAILED
tmplgdjapcm.py::test_case[case44] FAILED
tmplgdjapcm.py::test_case[case45] FAILED
tmplgdjapcm.py::test_case[case46] FAILED
tmplgdjapcm.py::test_case[case47] FAILED

=================================== FAILURES ===================================
_______________________________ test_case[case0] _______________________________

i = 0, inp = '7 3 7 3 20\n', expected = '26\n'

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
E       AssertionError: input='7 3 7 3 20\n'
E         expected='26'
E         got=''
E       assert '' == '26'
E         - 26

tmplgdjapcm.py:27: AssertionError
_______________________________ test_case[case1] _______________________________

i = 1, inp = '7 9 3 1 8\n', expected = '28\n'

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
E       AssertionError: input='7 9 3 1 8\n'
E         expected='28'
E         got=''
E       assert '' == '28'
E         - 28

tmplgdjapcm.py:27: AssertionError
_______________________________ test_case[case2] _______________________________

i = 2, inp = '10 10 10 10 10\n', expected = '20\n'

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
E       AssertionError: input='10 10 10 10 10\n'
E         expected='20'
E         got=''
E       assert '' == '20'
E         - 20

tmplgdjapcm.py:27: AssertionError
_______________________________ test_case[case3] _______________________________

i = 3, inp = '8 7 1 8 7\n', expected = '15\n'

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
E       AssertionError: input='8 7 1 8 7\n'
E         expected='15'
E         got=''
E       assert '' == '15'
E         - 15

tmplgdjapcm.py:27: AssertionError
_______________________________ test_case[case4] _______________________________

i = 4, inp = '7 7 7 8 8\n', expected = '16\n'

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
E       AssertionError: input='7 7 7 8 8\n'
E         expected='16'
E         got=''
E       assert '' == '16'
E         - 16

tmplgdjapcm.py:27: AssertionError
_______________________________ test_case[case5] _______________________________

i = 5, inp = '8 8 8 2 2\n', expected = '4\n'

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
E       AssertionError: input='8 8 8 2 2\n'
E         expected='4'
E         got=''
E       assert '' == '4'
E         - 4

tmplgdjapcm.py:27: AssertionError
_______________________________ test_case[case6] _______________________________

i = 6, inp = '8 8 2 2 2\n', expected = '6\n'

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
E       AssertionError: input='8 8 2 2 2\n'
E         expected='6'
E         got=''
E       assert '' == '6'
E         - 6

tmplgdjapcm.py:27: AssertionError
_______________________________ test_case[case7] _______________________________

i = 7, inp = '5 50 5 5 60\n', expected = '110\n'

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
E       AssertionError: input='5 50 5 5 60\n'
E         expected='110'
E         got=''
E       assert '' == '110'
E         - 110

tmplgdjapcm.py:27: AssertionError
_______________________________ test_case[case8] _______________________________

i = 8, inp = '100 100 100 100 100\n', expected = '200\n'

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
E       AssertionError: input='100 100 100 100 100\n'
E         expected='200'
E         got=''
E       assert '' == '200'
E         - 200

tmplgdjapcm.py:27: AssertionError
_______________________________ test_case[case9] _______________________________

i = 9, inp = '1 1 1 1 1\n', expected = '2\n'

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
E       AssertionError: input='1 1 1 1 1\n'
E         expected='2'
E         got=''
E       assert '' == '2'
E         - 2

tmplgdjapcm.py:27: AssertionError
______________________________ test_case[case10] _______________________________

i = 10, inp = '29 29 20 20 20\n', expected = '58\n'

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
E       AssertionError: input='29 29 20 20 20\n'
E         expected='58'
E         got=''
E       assert '' == '58'
E         - 58

tmplgdjapcm.py:27: AssertionError
______________________________ test_case[case11] _______________________________

i = 11, inp = '20 29 20 29 20\n', expected = '58\n'

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
E       AssertionError: input='20 29 20 29 20\n'
E         expected='58'
E         got=''
E       assert '' == '58'
E         - 58

tmplgdjapcm.py:27: AssertionError
______________________________ test_case[case12] _______________________________

i = 12, inp = '31 31 20 20 20\n', expected = '60\n'

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
E       AssertionError: input='31 31 20 20 20\n'
E         expected='60'
E         got=''
E       assert '' == '60'
E         - 60

tmplgdjapcm.py:27: AssertionError
______________________________ test_case[case13] _______________________________

i = 13, inp = '20 20 20 31 31\n', expected = '60\n'

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
E       AssertionError: input='20 20 20 31 31\n'
E         expected='60'
E         got=''
E       assert '' == '60'
E         - 60

tmplgdjapcm.py:27: AssertionError
______________________________ test_case[case14] _______________________________

i = 14, inp = '20 31 20 31 20\n', expected = '60\n'

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
E       AssertionError: input='20 31 20 31 20\n'
E         expected='60'
E         got=''
E       assert '' == '60'
E         - 60

tmplgdjapcm.py:27: AssertionError
______________________________ test_case[case15] _______________________________

i = 15, inp = '20 20 20 30 30\n', expected = '60\n'

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
E       AssertionError: input='20 20 20 30 30\n'
E         expected='60'
E         got=''
E       assert '' == '60'
E         - 60

tmplgdjapcm.py:27: AssertionError
______________________________ test_case[case16] _______________________________

i = 16, inp = '30 30 20 20 20\n', expected = '60\n'

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
E       AssertionError: input='30 30 20 20 20\n'
E         expected='60'
E         got=''
E       assert '' == '60'
E         - 60

tmplgdjapcm.py:27: AssertionError
______________________________ test_case[case17] _______________________________

i = 17, inp = '8 1 8 8 8\n', expected = '9\n'

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
E       AssertionError: input='8 1 8 8 8\n'
E         expected='9'
E         got=''
E       assert '' == '9'
E         - 9

tmplgdjapcm.py:27: AssertionError
______________________________ test_case[case18] _______________________________

i = 18, inp = '1 1 1 8 1\n', expected = '9\n'

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
E       AssertionError: input='1 1 1 8 1\n'
E         expected='9'
E         got=''
E       assert '' == '9'
E         - 9

tmplgdjapcm.py:27: AssertionError
______________________________ test_case[case19] _______________________________

i = 19, inp = '1 2 3 4 5\n', expected = '15\n'

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
E       AssertionError: input='1 2 3 4 5\n'
E         expected='15'
E         got=''
E       assert '' == '15'
E         - 15

tmplgdjapcm.py:27: AssertionError
______________________________ test_case[case20] _______________________________

i = 20, inp = '100 99 98 97 96\n', expected = '490\n'

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
E       AssertionError: input='100 99 98 97 96\n'
E         expected='490'
E         got=''
E       assert '' == '490'
E         - 490

tmplgdjapcm.py:27: AssertionError
______________________________ test_case[case21] _______________________________

i = 21, inp = '1 1 100 100 100\n', expected = '2\n'

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
E       AssertionError: input='1 1 100 100 100\n'
E         expected='2'
E         got=''
E       assert '' == '2'
E         - 2

tmplgdjapcm.py:27: AssertionError
______________________________ test_case[case22] _______________________________

i = 22, inp = '100 100 99 99 98\n', expected = '296\n'

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
E       AssertionError: input='100 100 99 99 98\n'
E         expected='296'
E         got=''
E       assert '' == '296'
E         - 296

tmplgdjapcm.py:27: AssertionError
______________________________ test_case[case23] _______________________________

i = 23, inp = '98 99 100 99 100\n', expected = '296\n'

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
E       AssertionError: input='98 99 100 99 100\n'
E         expected='296'
E         got=''
E       assert '' == '296'
E         - 296

tmplgdjapcm.py:27: AssertionError
______________________________ test_case[case24] _______________________________

i = 24, inp = '1 90 1 91 1\n', expected = '181\n'

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
E       AssertionError: input='1 90 1 91 1\n'
E         expected='181'
E         got=''
E       assert '' == '181'
E         - 181

tmplgdjapcm.py:27: AssertionError
______________________________ test_case[case25] _______________________________

i = 25, inp = '60 1 75 1 92\n', expected = '227\n'

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
E       AssertionError: input='60 1 75 1 92\n'
E         expected='227'
E         got=''
E       assert '' == '227'
E         - 227

tmplgdjapcm.py:27: AssertionError
______________________________ test_case[case26] _______________________________

i = 26, inp = '15 40 90 40 90\n', expected = '95\n'

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
E       AssertionError: input='15 40 90 40 90\n'
E         expected='95'
E         got=''
E       assert '' == '95'
E         - 95

tmplgdjapcm.py:27: AssertionError
______________________________ test_case[case27] _______________________________

i = 27, inp = '1 1 15 20 20\n', expected = '17\n'

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
E       AssertionError: input='1 1 15 20 20\n'
E         expected='17'
E         got=''
E       assert '' == '17'
E         - 17

tmplgdjapcm.py:27: AssertionError
______________________________ test_case[case28] _______________________________

i = 28, inp = '90 11 11 10 10\n', expected = '110\n'

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
E       AssertionError: input='90 11 11 10 10\n'
E         expected='110'
E         got=''
E       assert '' == '110'
E         - 110

tmplgdjapcm.py:27: AssertionError
______________________________ test_case[case29] _______________________________

i = 29, inp = '20 21 22 23 24\n', expected = '110\n'

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
E       AssertionError: input='20 21 22 23 24\n'
E         expected='110'
E         got=''
E       assert '' == '110'
E         - 110

tmplgdjapcm.py:27: AssertionError
______________________________ test_case[case30] _______________________________

i = 30, inp = '1 1 2 98 99\n', expected = '199\n'

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
E       AssertionError: input='1 1 2 98 99\n'
E         expected='199'
E         got=''
E       assert '' == '199'
E         - 199

tmplgdjapcm.py:27: AssertionError
______________________________ test_case[case31] _______________________________

i = 31, inp = '3 7 7 7 10\n', expected = '13\n'

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
E       AssertionError: input='3 7 7 7 10\n'
E         expected='13'
E         got=''
E       assert '' == '13'
E         - 13

tmplgdjapcm.py:27: AssertionError
______________________________ test_case[case32] _______________________________

i = 32, inp = '1 3 3 3 1\n', expected = '2\n'

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
E       AssertionError: input='1 3 3 3 1\n'
E         expected='2'
E         got=''
E       assert '' == '2'
E         - 2

tmplgdjapcm.py:27: AssertionError
______________________________ test_case[case33] _______________________________

i = 33, inp = '1 9 9 9 10\n', expected = '11\n'

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
E       AssertionError: input='1 9 9 9 10\n'
E         expected='11'
E         got=''
E       assert '' == '11'
E         - 11

tmplgdjapcm.py:27: AssertionError
______________________________ test_case[case34] _______________________________

i = 34, inp = '100 1 1 1 1\n', expected = '101\n'

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
E       AssertionError: input='100 1 1 1 1\n'
E         expected='101'
E         got=''
E       assert '' == '101'
E         - 101

tmplgdjapcm.py:27: AssertionError
______________________________ test_case[case35] _______________________________

i = 35, inp = '2 2 2 100 100\n', expected = '6\n'

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
E       AssertionError: input='2 2 2 100 100\n'
E         expected='6'
E         got=''
E       assert '' == '6'
E         - 6

tmplgdjapcm.py:27: AssertionError
______________________________ test_case[case36] _______________________________

i = 36, inp = '1 2 2 2 2\n', expected = '3\n'

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
E       AssertionError: input='1 2 2 2 2\n'
E         expected='3'
E         got=''
E       assert '' == '3'
E         - 3

tmplgdjapcm.py:27: AssertionError
______________________________ test_case[case37] _______________________________

i = 37, inp = '1 1 2 2 5\n', expected = '7\n'

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
E       AssertionError: input='1 1 2 2 5\n'
E         expected='7'
E         got=''
E       assert '' == '7'
E         - 7

tmplgdjapcm.py:27: AssertionError
______________________________ test_case[case38] _______________________________

i = 38, inp = '1 2 3 4 1\n', expected = '9\n'

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
E       AssertionError: input='1 2 3 4 1\n'
E         expected='9'
E         got=''
E       assert '' == '9'
E         - 9

tmplgdjapcm.py:27: AssertionError
______________________________ test_case[case39] _______________________________

i = 39, inp = '11 10 10 10 10\n', expected = '21\n'

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
E       AssertionError: input='11 10 10 10 10\n'
E         expected='21'
E         got=''
E       assert '' == '21'
E         - 21

tmplgdjapcm.py:27: AssertionError
______________________________ test_case[case40] _______________________________

i = 40, inp = '2 2 2 10 10\n', expected = '6\n'

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
E       AssertionError: input='2 2 2 10 10\n'
E         expected='6'
E         got=''
E       assert '' == '6'
E         - 6

tmplgdjapcm.py:27: AssertionError
______________________________ test_case[case41] _______________________________

i = 41, inp = '1 1 1 1 4\n', expected = '5\n'

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
E       AssertionError: input='1 1 1 1 4\n'
E         expected='5'
E         got=''
E       assert '' == '5'
E         - 5

tmplgdjapcm.py:27: AssertionError
______________________________ test_case[case42] _______________________________

i = 42, inp = '98 98 98 98 23\n', expected = '121\n'

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
E       AssertionError: input='98 98 98 98 23\n'
E         expected='121'
E         got=''
E       assert '' == '121'
E         - 121

tmplgdjapcm.py:27: AssertionError
______________________________ test_case[case43] _______________________________

i = 43, inp = '1 2 3 100 100\n', expected = '6\n'

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
E       AssertionError: input='1 2 3 100 100\n'
E         expected='6'
E         got=''
E       assert '' == '6'
E         - 6

tmplgdjapcm.py:27: AssertionError
______________________________ test_case[case44] _______________________________

i = 44, inp = '2 2 5 10 10\n', expected = '9\n'

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
E       AssertionError: input='2 2 5 10 10\n'
E         expected='9'
E         got=''
E       assert '' == '9'
E         - 9

tmplgdjapcm.py:27: AssertionError
______________________________ test_case[case45] _______________________________

i = 45, inp = '2 2 3 3 3\n', expected = '4\n'

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
E       AssertionError: input='2 2 3 3 3\n'
E         expected='4'
E         got=''
E       assert '' == '4'
E         - 4

tmplgdjapcm.py:27: AssertionError
______________________________ test_case[case46] _______________________________

i = 46, inp = '1 1 1 1 2\n', expected = '3\n'

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
E       AssertionError: input='1 1 1 1 2\n'
E         expected='3'
E         got=''
E       assert '' == '3'
E         - 3

tmplgdjapcm.py:27: AssertionError
______________________________ test_case[case47] _______________________________

i = 47, inp = '12 12 7 7 7\n', expected = '21\n'

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
E       AssertionError: input='12 12 7 7 7\n'
E         expected='21'
E         got=''
E       assert '' == '21'
E         - 21

tmplgdjapcm.py:27: AssertionError
=========================== short test summary info ============================
FAILED tmplgdjapcm.py::test_case[case0] - AssertionError: input='7 3 7 3 20\n'
FAILED tmplgdjapcm.py::test_case[case1] - AssertionError: input='7 9 3 1 8\n'
FAILED tmplgdjapcm.py::test_case[case2] - AssertionError: input='10 10 10 10 ...
FAILED tmplgdjapcm.py::test_case[case3] - AssertionError: input='8 7 1 8 7\n'
FAILED tmplgdjapcm.py::test_case[case4] - AssertionError: input='7 7 7 8 8\n'
FAILED tmplgdjapcm.py::test_case[case5] - AssertionError: input='8 8 8 2 2\n'
FAILED tmplgdjapcm.py::test_case[case6] - AssertionError: input='8 8 2 2 2\n'
FAILED tmplgdjapcm.py::test_case[case7] - AssertionError: input='5 50 5 5 60\n'
FAILED tmplgdjapcm.py::test_case[case8] - AssertionError: input='100 100 100 ...
FAILED tmplgdjapcm.py::test_case[case9] - AssertionError: input='1 1 1 1 1\n'
FAILED tmplgdjapcm.py::test_case[case10] - AssertionError: input='29 29 20 20...
FAILED tmplgdjapcm.py::test_case[case11] - AssertionError: input='20 29 20 29...
FAILED tmplgdjapcm.py::test_case[case12] - AssertionError: input='31 31 20 20...
FAILED tmplgdjapcm.py::test_case[case13] - AssertionError: input='20 20 20 31...
FAILED tmplgdjapcm.py::test_case[case14] - AssertionError: input='20 31 20 31...
FAILED tmplgdjapcm.py::test_case[case15] - AssertionError: input='20 20 20 30...
FAILED tmplgdjapcm.py::test_case[case16] - AssertionError: input='30 30 20 20...
FAILED tmplgdjapcm.py::test_case[case17] - AssertionError: input='8 1 8 8 8\n'
FAILED tmplgdjapcm.py::test_case[case18] - AssertionError: input='1 1 1 8 1\n'
FAILED tmplgdjapcm.py::test_case[case19] - AssertionError: input='1 2 3 4 5\n'
FAILED tmplgdjapcm.py::test_case[case20] - AssertionError: input='100 99 98 9...
FAILED tmplgdjapcm.py::test_case[case21] - AssertionError: input='1 1 100 100...
FAILED tmplgdjapcm.py::test_case[case22] - AssertionError: input='100 100 99 ...
FAILED tmplgdjapcm.py::test_case[case23] - AssertionError: input='98 99 100 9...
FAILED tmplgdjapcm.py::test_case[case24] - AssertionError: input='1 90 1 91 1\n'
FAILED tmplgdjapcm.py::test_case[case25] - AssertionError: input='60 1 75 1 9...
FAILED tmplgdjapcm.py::test_case[case26] - AssertionError: input='15 40 90 40...
FAILED tmplgdjapcm.py::test_case[case27] - AssertionError: input='1 1 15 20 2...
FAILED tmplgdjapcm.py::test_case[case28] - AssertionError: input='90 11 11 10...
FAILED tmplgdjapcm.py::test_case[case29] - AssertionError: input='20 21 22 23...
FAILED tmplgdjapcm.py::test_case[case30] - AssertionError: input='1 1 2 98 99\n'
FAILED tmplgdjapcm.py::test_case[case31] - AssertionError: input='3 7 7 7 10\n'
FAILED tmplgdjapcm.py::test_case[case32] - AssertionError: input='1 3 3 3 1\n'
FAILED tmplgdjapcm.py::test_case[case33] - AssertionError: input='1 9 9 9 10\n'
FAILED tmplgdjapcm.py::test_case[case34] - AssertionError: input='100 1 1 1 1\n'
FAILED tmplgdjapcm.py::test_case[case35] - AssertionError: input='2 2 2 100 1...
FAILED tmplgdjapcm.py::test_case[case36] - AssertionError: input='1 2 2 2 2\n'
FAILED tmplgdjapcm.py::test_case[case37] - AssertionError: input='1 1 2 2 5\n'
FAILED tmplgdjapcm.py::test_case[case38] - AssertionError: input='1 2 3 4 1\n'
FAILED tmplgdjapcm.py::test_case[case39] - AssertionError: input='11 10 10 10...
FAILED tmplgdjapcm.py::test_case[case40] - AssertionError: input='2 2 2 10 10\n'
FAILED tmplgdjapcm.py::test_case[case41] - AssertionError: input='1 1 1 1 4\n'
FAILED tmplgdjapcm.py::test_case[case42] - AssertionError: input='98 98 98 98...
FAILED tmplgdjapcm.py::test_case[case43] - AssertionError: input='1 2 3 100 1...
FAILED tmplgdjapcm.py::test_case[case44] - AssertionError: input='2 2 5 10 10\n'
FAILED tmplgdjapcm.py::test_case[case45] - AssertionError: input='2 2 3 3 3\n'
FAILED tmplgdjapcm.py::test_case[case46] - AssertionError: input='1 1 1 1 2\n'
FAILED tmplgdjapcm.py::test_case[case47] - AssertionError: input='12 12 7 7 7\n'
============================== 48 failed in 8.59s ==============================
```
