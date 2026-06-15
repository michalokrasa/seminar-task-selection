# competition/420-b

**Status:** FAIL (exit code 1)

## stdout

```
============================= test session starts ==============================
platform linux -- Python 3.10.18, pytest-7.4.4, pluggy-1.6.0
PyQt5 5.15.10 -- Qt runtime 5.15.17 -- Qt compiled 5.15.2
rootdir: /tmp/tmpafshuzcn
configfile: pytest.ini
plugins: Faker-25.1.0, anyio-4.9.0, cov-5.0.0, mock-3.12.0, qt-4.3.1
collected 38 items

tmpdkrfaq4k.py::test_case[case0] FAILED
tmpdkrfaq4k.py::test_case[case1] FAILED
tmpdkrfaq4k.py::test_case[case2] PASSED
tmpdkrfaq4k.py::test_case[case3] FAILED
tmpdkrfaq4k.py::test_case[case4] FAILED
tmpdkrfaq4k.py::test_case[case5] PASSED
tmpdkrfaq4k.py::test_case[case6] FAILED
tmpdkrfaq4k.py::test_case[case7] FAILED
tmpdkrfaq4k.py::test_case[case8] FAILED
tmpdkrfaq4k.py::test_case[case9] PASSED
tmpdkrfaq4k.py::test_case[case10] FAILED
tmpdkrfaq4k.py::test_case[case11] FAILED
tmpdkrfaq4k.py::test_case[case12] FAILED
tmpdkrfaq4k.py::test_case[case13] FAILED
tmpdkrfaq4k.py::test_case[case14] FAILED
tmpdkrfaq4k.py::test_case[case15] FAILED
tmpdkrfaq4k.py::test_case[case16] FAILED
tmpdkrfaq4k.py::test_case[case17] FAILED
tmpdkrfaq4k.py::test_case[case18] FAILED
tmpdkrfaq4k.py::test_case[case19] FAILED
tmpdkrfaq4k.py::test_case[case20] FAILED
tmpdkrfaq4k.py::test_case[case21] FAILED
tmpdkrfaq4k.py::test_case[case22] FAILED
tmpdkrfaq4k.py::test_case[case23] FAILED
tmpdkrfaq4k.py::test_case[case24] FAILED
tmpdkrfaq4k.py::test_case[case25] FAILED
tmpdkrfaq4k.py::test_case[case26] FAILED
tmpdkrfaq4k.py::test_case[case27] FAILED
tmpdkrfaq4k.py::test_case[case28] FAILED
tmpdkrfaq4k.py::test_case[case29] FAILED
tmpdkrfaq4k.py::test_case[case30] FAILED
tmpdkrfaq4k.py::test_case[case31] FAILED
tmpdkrfaq4k.py::test_case[case32] FAILED
tmpdkrfaq4k.py::test_case[case33] FAILED
tmpdkrfaq4k.py::test_case[case34] PASSED
tmpdkrfaq4k.py::test_case[case35] FAILED
tmpdkrfaq4k.py::test_case[case36] FAILED
tmpdkrfaq4k.py::test_case[case37] FAILED

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
E         got='1\n1'
E       assert '1\n1' == '4\n1 3 4 5'
E         - 4
E         - 1 3 4 5
E         + 1
E         + 1

tmpdkrfaq4k.py:27: AssertionError
_______________________________ test_case[case1] _______________________________

i = 1, inp = '3 2\n+ 1\n- 2\n', expected = '1\n3 '

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
E       AssertionError: input='3 2\n+ 1\n- 2\n'
E         expected='1\n3'
E         got=''
E       assert '' == '1\n3'
E         - 1
E         - 3

tmpdkrfaq4k.py:27: AssertionError
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
E         got=''
E       assert '' == '3\n2 3 5'
E         - 3
E         - 2 3 5

tmpdkrfaq4k.py:27: AssertionError
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
E         got=''
E       assert '' == '0'
E         - 0

tmpdkrfaq4k.py:27: AssertionError
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
E         got=''
E       assert '' == '2\n1 2'
E         - 2
E         - 1 2

tmpdkrfaq4k.py:27: AssertionError
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
E         got=''
E       assert '' == '1\n1'
E         - 1
E         - 1

tmpdkrfaq4k.py:27: AssertionError
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
E         got=''
E       assert '' == '6\n3 4 5 6 8 10'
E         - 6
E         - 3 4 5 6 8 10

tmpdkrfaq4k.py:27: AssertionError
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
E         got='1\n1'
E       assert '1\n1' == '4\n1 3 4 5'
E         - 4
E         - 1 3 4 5
E         + 1
E         + 1

tmpdkrfaq4k.py:27: AssertionError
______________________________ test_case[case11] _______________________________

i = 11, inp = '10 3\n+ 1\n+ 2\n- 7\n', expected = '7\n3 4 5 6 8 9 10 '

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
E       AssertionError: input='10 3\n+ 1\n+ 2\n- 7\n'
E         expected='7\n3 4 5 6 8 9 10'
E         got=''
E       assert '' == '7\n3 4 5 6 8 9 10'
E         - 7
E         - 3 4 5 6 8 9 10

tmpdkrfaq4k.py:27: AssertionError
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
E         got=''
E       assert '' == '1\n1'
E         - 1
E         - 1

tmpdkrfaq4k.py:27: AssertionError
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
E         got=''
E       assert '' == '20\n1 2 3 4 ...6 17 18 19 20'
E         - 20
E         - 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20

tmpdkrfaq4k.py:27: AssertionError
______________________________ test_case[case14] _______________________________

i = 14
inp = '50 20\n- 6\n+ 40\n- 3\n- 23\n+ 31\n- 27\n- 40\n+ 25\n+ 29\n- 41\n- 16\n+ 23\n+ 20\n+ 13\n- 45\n+ 40\n+ 24\n+ 22\n- 23\n+ 17\n'
expected = '34\n1 2 4 5 7 8 9 10 11 12 14 15 18 19 21 26 28 30 32 33 34 35 36 37 38 39 42 43 44 46 47 48 49 50 '

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
E       AssertionError: input='50 20\n- 6\n+ 40\n- 3\n- 23\n+ 31\n- 27\n- 40\n+ 25\n+ 29\n- 41\n- 16\n+ 23\n+ 20\n+ 13\n- 45\n+ 40\n+ 24\n+ 22\n- 23\n+ 17\n'
E         expected='34\n1 2 4 5 7 8 9 10 11 12 14 15 18 19 21 26 28 30 32 33 34 35 36 37 38 39 42 43 44 46 47 48 49 50'
E         got=''
E       assert '' == '34\n1 2 4 5 ...6 47 48 49 50'
E         - 34
E         - 1 2 4 5 7 8 9 10 11 12 14 15 18 19 21 26 28 30 32 33 34 35 36 37 38 39 42 43 44 46 47 48 49 50

tmpdkrfaq4k.py:27: AssertionError
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
E         got=''
E       assert '' == '2\n1 3'
E         - 2
E         - 1 3

tmpdkrfaq4k.py:27: AssertionError
______________________________ test_case[case16] _______________________________

i = 16, inp = '100 5\n- 60\n- 58\n+ 25\n- 32\n+ 86\n'
expected = '95\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 26 27 28 29 30 31 33 34 35 36 37 38 39 40 41 42 43...61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 87 88 89 90 91 92 93 94 95 96 97 98 99 100 '

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
E       AssertionError: input='100 5\n- 60\n- 58\n+ 25\n- 32\n+ 86\n'
E         expected='95\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 26 27 28 29 30 31 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 59 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 87 88 89 90 91 92 93 94 95 96 97 98 99 100'
E         got=''
E       assert '' == '95\n1 2 3 4 ... 97 98 99 100'
E         - 95
E         - 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 26 27 28 29 30 31 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 59 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 87 88 89 90 91 92 93 94 95 96 97 98 99 100

tmpdkrfaq4k.py:27: AssertionError
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
E         got=''
E       assert '' == '1\n4'
E         - 1
E         - 4

tmpdkrfaq4k.py:27: AssertionError
______________________________ test_case[case18] _______________________________

i = 18, inp = '3 3\n- 2\n+ 1\n+ 2\n', expected = '1\n3 '

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
E       AssertionError: input='3 3\n- 2\n+ 1\n+ 2\n'
E         expected='1\n3'
E         got=''
E       assert '' == '1\n3'
E         - 1
E         - 3

tmpdkrfaq4k.py:27: AssertionError
______________________________ test_case[case19] _______________________________

i = 19, inp = '5 4\n- 1\n- 2\n+ 3\n+ 4\n', expected = '1\n5 '

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
E       AssertionError: input='5 4\n- 1\n- 2\n+ 3\n+ 4\n'
E         expected='1\n5'
E         got=''
E       assert '' == '1\n5'
E         - 1
E         - 5

tmpdkrfaq4k.py:27: AssertionError
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
E         got=''
E       assert '' == '1\n4'
E         - 1
E         - 4

tmpdkrfaq4k.py:27: AssertionError
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
E         got=''
E       assert '' == '6\n4 5 6 7 9 10'
E         - 6
E         - 4 5 6 7 9 10

tmpdkrfaq4k.py:27: AssertionError
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
E         got=''
E       assert '' == '6\n4 5 6 7 9 10'
E         - 6
E         - 4 5 6 7 9 10

tmpdkrfaq4k.py:27: AssertionError
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
E         got=''
E       assert '' == '1\n3'
E         - 1
E         - 3

tmpdkrfaq4k.py:27: AssertionError
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
E         got=''
E       assert '' == '1\n3'
E         - 1
E         - 3

tmpdkrfaq4k.py:27: AssertionError
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
E         got=''
E       assert '' == '6\n2 4 5 6 8 10'
E         - 6
E         - 2 4 5 6 8 10

tmpdkrfaq4k.py:27: AssertionError
______________________________ test_case[case26] _______________________________

i = 26, inp = '10 6\n+ 2\n- 2\n+ 2\n- 2\n+ 2\n- 3\n'
expected = '8\n1 4 5 6 7 8 9 10 '

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
E       AssertionError: input='10 6\n+ 2\n- 2\n+ 2\n- 2\n+ 2\n- 3\n'
E         expected='8\n1 4 5 6 7 8 9 10'
E         got=''
E       assert '' == '8\n1 4 5 6 7 8 9 10'
E         - 8
E         - 1 4 5 6 7 8 9 10

tmpdkrfaq4k.py:27: AssertionError
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
E         got=''
E       assert '' == '9\n1 3 4 5 6 7 8 9 10'
E         - 9
E         - 1 3 4 5 6 7 8 9 10

tmpdkrfaq4k.py:27: AssertionError
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
E         got=''
E       assert '' == '4\n6 8 9 10'
E         - 4
E         - 6 8 9 10

tmpdkrfaq4k.py:27: AssertionError
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
E         got=''
E       assert '' == '5\n6 7 8 9 10'
E         - 5
E         - 6 7 8 9 10

tmpdkrfaq4k.py:27: AssertionError
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
E         got=''
E       assert '' == '5\n6 7 8 9 10'
E         - 5
E         - 6 7 8 9 10

tmpdkrfaq4k.py:27: AssertionError
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
E         got=''
E       assert '' == '4\n6 8 9 10'
E         - 4
E         - 6 8 9 10

tmpdkrfaq4k.py:27: AssertionError
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
E         got=''
E       assert '' == '2\n1 2'
E         - 2
E         - 1 2

tmpdkrfaq4k.py:27: AssertionError
______________________________ test_case[case33] _______________________________

i = 33, inp = '7 4\n- 2\n- 3\n+ 3\n- 6\n', expected = '4\n1 4 5 7 '

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
E       AssertionError: input='7 4\n- 2\n- 3\n+ 3\n- 6\n'
E         expected='4\n1 4 5 7'
E         got=''
E       assert '' == '4\n1 4 5 7'
E         - 4
E         - 1 4 5 7

tmpdkrfaq4k.py:27: AssertionError
______________________________ test_case[case35] _______________________________

i = 35, inp = '5 5\n- 2\n+ 1\n+ 2\n- 2\n+ 4\n', expected = '2\n3 5 '

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
E       AssertionError: input='5 5\n- 2\n+ 1\n+ 2\n- 2\n+ 4\n'
E         expected='2\n3 5'
E         got=''
E       assert '' == '2\n3 5'
E         - 2
E         - 3 5

tmpdkrfaq4k.py:27: AssertionError
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
E         got='0'
E       assert '0' == '3\n3 4 5'
E         + 0
E         - 3
E         - 3 4 5

tmpdkrfaq4k.py:27: AssertionError
______________________________ test_case[case37] _______________________________

i = 37, inp = '4 4\n- 1\n+ 1\n- 1\n+ 2\n', expected = '2\n3 4 '

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
E       AssertionError: input='4 4\n- 1\n+ 1\n- 1\n+ 2\n'
E         expected='2\n3 4'
E         got=''
E       assert '' == '2\n3 4'
E         - 2
E         - 3 4

tmpdkrfaq4k.py:27: AssertionError
=========================== short test summary info ============================
FAILED tmpdkrfaq4k.py::test_case[case0] - AssertionError: input='5 4\n+ 1\n+ ...
FAILED tmpdkrfaq4k.py::test_case[case1] - AssertionError: input='3 2\n+ 1\n- ...
FAILED tmpdkrfaq4k.py::test_case[case3] - AssertionError: input='5 6\n+ 1\n- ...
FAILED tmpdkrfaq4k.py::test_case[case4] - AssertionError: input='2 4\n+ 1\n- ...
FAILED tmpdkrfaq4k.py::test_case[case6] - AssertionError: input='2 1\n- 2\n'
FAILED tmpdkrfaq4k.py::test_case[case7] - AssertionError: input='3 5\n- 1\n+ ...
FAILED tmpdkrfaq4k.py::test_case[case8] - AssertionError: input='10 8\n+ 1\n-...
FAILED tmpdkrfaq4k.py::test_case[case10] - AssertionError: input='5 4\n+ 1\n-...
FAILED tmpdkrfaq4k.py::test_case[case11] - AssertionError: input='10 3\n+ 1\n...
FAILED tmpdkrfaq4k.py::test_case[case12] - AssertionError: input='1 20\n- 1\n...
FAILED tmpdkrfaq4k.py::test_case[case13] - AssertionError: input='20 1\n- 16\n'
FAILED tmpdkrfaq4k.py::test_case[case14] - AssertionError: input='50 20\n- 6\...
FAILED tmpdkrfaq4k.py::test_case[case15] - AssertionError: input='20 50\n+ 5\...
FAILED tmpdkrfaq4k.py::test_case[case16] - AssertionError: input='100 5\n- 60...
FAILED tmpdkrfaq4k.py::test_case[case17] - AssertionError: input='4 4\n+ 2\n-...
FAILED tmpdkrfaq4k.py::test_case[case18] - AssertionError: input='3 3\n- 2\n+...
FAILED tmpdkrfaq4k.py::test_case[case19] - AssertionError: input='5 4\n- 1\n-...
FAILED tmpdkrfaq4k.py::test_case[case20] - AssertionError: input='6 6\n- 5\n-...
FAILED tmpdkrfaq4k.py::test_case[case21] - AssertionError: input='10 7\n- 8\n...
FAILED tmpdkrfaq4k.py::test_case[case22] - AssertionError: input='10 7\n- 8\n...
FAILED tmpdkrfaq4k.py::test_case[case23] - AssertionError: input='4 10\n+ 2\n...
FAILED tmpdkrfaq4k.py::test_case[case24] - AssertionError: input='4 9\n+ 2\n-...
FAILED tmpdkrfaq4k.py::test_case[case25] - AssertionError: input='10 8\n+ 1\n...
FAILED tmpdkrfaq4k.py::test_case[case26] - AssertionError: input='10 6\n+ 2\n...
FAILED tmpdkrfaq4k.py::test_case[case27] - AssertionError: input='10 5\n+ 2\n...
FAILED tmpdkrfaq4k.py::test_case[case28] - AssertionError: input='10 11\n+ 1\...
FAILED tmpdkrfaq4k.py::test_case[case29] - AssertionError: input='10 10\n+ 1\...
FAILED tmpdkrfaq4k.py::test_case[case30] - AssertionError: input='10 9\n+ 1\n...
FAILED tmpdkrfaq4k.py::test_case[case31] - AssertionError: input='10 12\n+ 1\...
FAILED tmpdkrfaq4k.py::test_case[case32] - AssertionError: input='2 2\n- 1\n+...
FAILED tmpdkrfaq4k.py::test_case[case33] - AssertionError: input='7 4\n- 2\n-...
FAILED tmpdkrfaq4k.py::test_case[case35] - AssertionError: input='5 5\n- 2\n+...
FAILED tmpdkrfaq4k.py::test_case[case36] - AssertionError: input='5 3\n+ 1\n-...
FAILED tmpdkrfaq4k.py::test_case[case37] - AssertionError: input='4 4\n- 1\n+...
========================= 34 failed, 4 passed in 7.34s =========================
```
