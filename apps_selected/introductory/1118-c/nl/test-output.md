# introductory/1118-c

**Status:** FAIL (exit code 1)

## stdout

```
============================= test session starts ==============================
platform linux -- Python 3.10.18, pytest-7.4.4, pluggy-1.6.0
PyQt5 5.15.10 -- Qt runtime 5.15.17 -- Qt compiled 5.15.2
rootdir: /tmp/tmpslm1u0k8
configfile: pytest.ini
plugins: Faker-25.1.0, anyio-4.9.0, cov-5.0.0, mock-3.12.0, qt-4.3.1
collected 45 items

tmp6z_5dthr.py::test_case[case0] FAILED
tmp6z_5dthr.py::test_case[case1] FAILED
tmp6z_5dthr.py::test_case[case2] FAILED
tmp6z_5dthr.py::test_case[case3] FAILED
tmp6z_5dthr.py::test_case[case4] FAILED
tmp6z_5dthr.py::test_case[case5] FAILED
tmp6z_5dthr.py::test_case[case6] FAILED
tmp6z_5dthr.py::test_case[case7] FAILED
tmp6z_5dthr.py::test_case[case8] FAILED
tmp6z_5dthr.py::test_case[case9] FAILED
tmp6z_5dthr.py::test_case[case10] FAILED
tmp6z_5dthr.py::test_case[case11] FAILED
tmp6z_5dthr.py::test_case[case12] FAILED
tmp6z_5dthr.py::test_case[case13] FAILED
tmp6z_5dthr.py::test_case[case14] FAILED
tmp6z_5dthr.py::test_case[case15] FAILED
tmp6z_5dthr.py::test_case[case16] FAILED
tmp6z_5dthr.py::test_case[case17] FAILED
tmp6z_5dthr.py::test_case[case18] FAILED
tmp6z_5dthr.py::test_case[case19] FAILED
tmp6z_5dthr.py::test_case[case20] FAILED
tmp6z_5dthr.py::test_case[case21] FAILED
tmp6z_5dthr.py::test_case[case22] FAILED
tmp6z_5dthr.py::test_case[case23] FAILED
tmp6z_5dthr.py::test_case[case24] FAILED
tmp6z_5dthr.py::test_case[case25] FAILED
tmp6z_5dthr.py::test_case[case26] FAILED
tmp6z_5dthr.py::test_case[case27] FAILED
tmp6z_5dthr.py::test_case[case28] FAILED
tmp6z_5dthr.py::test_case[case29] FAILED
tmp6z_5dthr.py::test_case[case30] FAILED
tmp6z_5dthr.py::test_case[case31] FAILED
tmp6z_5dthr.py::test_case[case32] FAILED
tmp6z_5dthr.py::test_case[case33] FAILED
tmp6z_5dthr.py::test_case[case34] FAILED
tmp6z_5dthr.py::test_case[case35] FAILED
tmp6z_5dthr.py::test_case[case36] FAILED
tmp6z_5dthr.py::test_case[case37] FAILED
tmp6z_5dthr.py::test_case[case38] FAILED
tmp6z_5dthr.py::test_case[case39] FAILED
tmp6z_5dthr.py::test_case[case40] FAILED
tmp6z_5dthr.py::test_case[case41] FAILED
tmp6z_5dthr.py::test_case[case42] FAILED
tmp6z_5dthr.py::test_case[case43] FAILED
tmp6z_5dthr.py::test_case[case44] FAILED

=================================== FAILURES ===================================
_______________________________ test_case[case0] _______________________________

i = 0, inp = '4\n1 8 8 1 2 2 2 2 2 2 2 2 1 8 8 1\n'
expected = 'YES\n1 2 2 1 \n2 8 8 2 \n2 8 8 2 \n1 2 2 1 \n'

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
E       AssertionError: input='4\n1 8 8 1 2 2 2 2 2 2 2 2 1 8 8 1\n'
E         expected='YES\n1 2 2 1 \n2 8 8 2 \n2 8 8 2 \n1 2 2 1'
E         got=''
E       assert '' == 'YES\n1 2 2 1...8 2 \n1 2 2 1'
E         - YES
E         - 1 2 2 1 
E         - 2 8 8 2 
E         - 2 8 8 2 
E         - 1 2 2 1

tmp6z_5dthr.py:27: AssertionError
_______________________________ test_case[case1] _______________________________

i = 1, inp = '3\n1 1 1 1 1 3 3 3 3\n'
expected = 'YES\n1 3 1 \n3 1 3 \n1 3 1 \n'

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
E       AssertionError: input='3\n1 1 1 1 1 3 3 3 3\n'
E         expected='YES\n1 3 1 \n3 1 3 \n1 3 1'
E         got=''
E       assert '' == 'YES\n1 3 1 \n3 1 3 \n1 3 1'
E         - YES
E         - 1 3 1 
E         - 3 1 3 
E         - 1 3 1

tmp6z_5dthr.py:27: AssertionError
_______________________________ test_case[case2] _______________________________

i = 2, inp = '4\n1 2 1 9 8 4 3 8 8 3 4 8 9 2 1 1\n', expected = 'NO\n'

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
E       AssertionError: input='4\n1 2 1 9 8 4 3 8 8 3 4 8 9 2 1 1\n'
E         expected='NO'
E         got=''
E       assert '' == 'NO'
E         - NO

tmp6z_5dthr.py:27: AssertionError
_______________________________ test_case[case3] _______________________________

i = 3, inp = '1\n10\n', expected = 'YES\n10 \n'

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
E       AssertionError: input='1\n10\n'
E         expected='YES\n10'
E         got=''
E       assert '' == 'YES\n10'
E         - YES
E         - 10

tmp6z_5dthr.py:27: AssertionError
_______________________________ test_case[case4] _______________________________

i = 4, inp = '2\n3 3 3 3\n', expected = 'YES\n3 3 \n3 3 \n'

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
E       AssertionError: input='2\n3 3 3 3\n'
E         expected='YES\n3 3 \n3 3'
E         got=''
E       assert '' == 'YES\n3 3 \n3 3'
E         - YES
E         - 3 3 
E         - 3 3

tmp6z_5dthr.py:27: AssertionError
_______________________________ test_case[case5] _______________________________

i = 5
inp = '7\n5 9 5 4 1 9 8 4 5 1 4 10 7 7 8 4 2 4 4 5 4 4 10 3 4 6 8 1 9 9 5 6 8 7 1 8 6 6 7 5 3 1 1 4 7 2 3 3 8\n'
expected = 'YES\n1 3 4 2 4 3 1 \n4 5 6 5 6 5 4 \n7 8 9 10 9 8 7 \n1 4 8 7 8 4 1 \n7 8 9 10 9 8 7 \n4 5 6 5 6 5 4 \n1 3 4 2 4 3 1 \n'

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
E       AssertionError: input='7\n5 9 5 4 1 9 8 4 5 1 4 10 7 7 8 4 2 4 4 5 4 4 10 3 4 6 8 1 9 9 5 6 8 7 1 8 6 6 7 5 3 1 1 4 7 2 3 3 8\n'
E         expected='YES\n1 3 4 2 4 3 1 \n4 5 6 5 6 5 4 \n7 8 9 10 9 8 7 \n1 4 8 7 8 4 1 \n7 8 9 10 9 8 7 \n4 5 6 5 6 5 4 \n1 3 4 2 4 3 1'
E         got=''
E       assert '' == 'YES\n1 3 4 2...1 3 4 2 4 3 1'
E         - YES
E         - 1 3 4 2 4 3 1 
E         - 4 5 6 5 6 5 4 
E         - 7 8 9 10 9 8 7 
E         - 1 4 8 7 8 4 1 
E         - 7 8 9 10 9 8 7 
E         - 4 5 6 5 6 5 4 
E         - 1 3 4 2 4 3 1

tmp6z_5dthr.py:27: AssertionError
_______________________________ test_case[case6] _______________________________

i = 6
inp = '7\n1 8 9 6 4 7 4 3 5 5 4 2 1 8 10 7 7 7 8 8 1 10 1 4 6 2 2 1 6 9 6 1 6 4 8 10 4 4 7 3 4 7 10 2 2 9 4 3 3\n'
expected = 'NO\n'

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
E       AssertionError: input='7\n1 8 9 6 4 7 4 3 5 5 4 2 1 8 10 7 7 7 8 8 1 10 1 4 6 2 2 1 6 9 6 1 6 4 8 10 4 4 7 3 4 7 10 2 2 9 4 3 3\n'
E         expected='NO'
E         got=''
E       assert '' == 'NO'
E         - NO

tmp6z_5dthr.py:27: AssertionError
_______________________________ test_case[case7] _______________________________

i = 7, inp = '3\n1 1 2 2 3 3 4 4 5\n', expected = 'NO\n'

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
E       AssertionError: input='3\n1 1 2 2 3 3 4 4 5\n'
E         expected='NO'
E         got=''
E       assert '' == 'NO'
E         - NO

tmp6z_5dthr.py:27: AssertionError
_______________________________ test_case[case8] _______________________________

i = 8, inp = '4\n1 1 1 1 1 2 2 2 2 2 2 2 2 2 2 2\n', expected = 'NO\n'

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
E       AssertionError: input='4\n1 1 1 1 1 2 2 2 2 2 2 2 2 2 2 2\n'
E         expected='NO'
E         got=''
E       assert '' == 'NO'
E         - NO

tmp6z_5dthr.py:27: AssertionError
_______________________________ test_case[case9] _______________________________

i = 9, inp = '3\n1 1 2 2 3 3 4 4 4\n', expected = 'NO\n'

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
E       AssertionError: input='3\n1 1 2 2 3 3 4 4 4\n'
E         expected='NO'
E         got=''
E       assert '' == 'NO'
E         - NO

tmp6z_5dthr.py:27: AssertionError
______________________________ test_case[case10] _______________________________

i = 10, inp = '5\n4 4 3 5 1 1 2 3 2 2 1 3 3 2 2 5 3 4 3 3 2 2 4 1 3\n'
expected = 'YES\n1 2 4 2 1 \n3 3 5 3 3 \n2 4 2 4 2 \n3 3 5 3 3 \n1 2 4 2 1 \n'

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
E       AssertionError: input='5\n4 4 3 5 1 1 2 3 2 2 1 3 3 2 2 5 3 4 3 3 2 2 4 1 3\n'
E         expected='YES\n1 2 4 2 1 \n3 3 5 3 3 \n2 4 2 4 2 \n3 3 5 3 3 \n1 2 4 2 1'
E         got=''
E       assert '' == 'YES\n1 2 4 2...3 \n1 2 4 2 1'
E         - YES
E         - 1 2 4 2 1 
E         - 3 3 5 3 3 
E         - 2 4 2 4 2 
E         - 3 3 5 3 3 
E         - 1 2 4 2 1

tmp6z_5dthr.py:27: AssertionError
______________________________ test_case[case11] _______________________________

i = 11, inp = '5\n1 1 1 1 2 2 2 2 3 3 3 3 4 4 4 4 5 5 6 6 7 7 8 8 9\n'
expected = 'YES\n1 2 6 2 1 \n3 4 8 4 3 \n5 7 9 7 5 \n3 4 8 4 3 \n1 2 6 2 1 \n'

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
E       AssertionError: input='5\n1 1 1 1 2 2 2 2 3 3 3 3 4 4 4 4 5 5 6 6 7 7 8 8 9\n'
E         expected='YES\n1 2 6 2 1 \n3 4 8 4 3 \n5 7 9 7 5 \n3 4 8 4 3 \n1 2 6 2 1'
E         got=''
E       assert '' == 'YES\n1 2 6 2...3 \n1 2 6 2 1'
E         - YES
E         - 1 2 6 2 1 
E         - 3 4 8 4 3 
E         - 5 7 9 7 5 
E         - 3 4 8 4 3 
E         - 1 2 6 2 1

tmp6z_5dthr.py:27: AssertionError
______________________________ test_case[case12] _______________________________

i = 12, inp = '2\n1000 1000 1000 1000\n'
expected = 'YES\n1000 1000 \n1000 1000 \n'

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
E       AssertionError: input='2\n1000 1000 1000 1000\n'
E         expected='YES\n1000 1000 \n1000 1000'
E         got=''
E       assert '' == 'YES\n1000 1000 \n1000 1000'
E         - YES
E         - 1000 1000 
E         - 1000 1000

tmp6z_5dthr.py:27: AssertionError
______________________________ test_case[case13] _______________________________

i = 13, inp = '3\n17 17 18 18 19 19 20 20 21\n', expected = 'NO\n'

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
E       AssertionError: input='3\n17 17 18 18 19 19 20 20 21\n'
E         expected='NO'
E         got=''
E       assert '' == 'NO'
E         - NO

tmp6z_5dthr.py:27: AssertionError
______________________________ test_case[case14] _______________________________

i = 14, inp = '3\n1 4 3 3 5 3 1 4 5\n', expected = 'NO\n'

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
E       AssertionError: input='3\n1 4 3 3 5 3 1 4 5\n'
E         expected='NO'
E         got=''
E       assert '' == 'NO'
E         - NO

tmp6z_5dthr.py:27: AssertionError
______________________________ test_case[case15] _______________________________

i = 15, inp = '3\n17 17 18 18 19 19 20 20 219\n', expected = 'NO\n'

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
E       AssertionError: input='3\n17 17 18 18 19 19 20 20 219\n'
E         expected='NO'
E         got=''
E       assert '' == 'NO'
E         - NO

tmp6z_5dthr.py:27: AssertionError
______________________________ test_case[case16] _______________________________

i = 16, inp = '3\n3 4 2 1 1 3 2 3 4\n', expected = 'NO\n'

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
E       AssertionError: input='3\n3 4 2 1 1 3 2 3 4\n'
E         expected='NO'
E         got=''
E       assert '' == 'NO'
E         - NO

tmp6z_5dthr.py:27: AssertionError
______________________________ test_case[case17] _______________________________

i = 17, inp = '3\n1 2 2 3 3 4 4 5 5\n', expected = 'NO\n'

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
E       AssertionError: input='3\n1 2 2 3 3 4 4 5 5\n'
E         expected='NO'
E         got=''
E       assert '' == 'NO'
E         - NO

tmp6z_5dthr.py:27: AssertionError
______________________________ test_case[case18] _______________________________

i = 18, inp = '3\n19 19 7 7 20 20 21 21 3\n', expected = 'NO\n'

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
E       AssertionError: input='3\n19 19 7 7 20 20 21 21 3\n'
E         expected='NO'
E         got=''
E       assert '' == 'NO'
E         - NO

tmp6z_5dthr.py:27: AssertionError
______________________________ test_case[case19] _______________________________

i = 19, inp = '3\n13 13 42 42 69 69 420 420 666\n', expected = 'NO\n'

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
E       AssertionError: input='3\n13 13 42 42 69 69 420 420 666\n'
E         expected='NO'
E         got=''
E       assert '' == 'NO'
E         - NO

tmp6z_5dthr.py:27: AssertionError
______________________________ test_case[case20] _______________________________

i = 20, inp = '3\n1 1 2 2 4 4 8 8 16\n', expected = 'NO\n'

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
E       AssertionError: input='3\n1 1 2 2 4 4 8 8 16\n'
E         expected='NO'
E         got=''
E       assert '' == 'NO'
E         - NO

tmp6z_5dthr.py:27: AssertionError
______________________________ test_case[case21] _______________________________

i = 21, inp = '5\n2 2 2 2 2 2 2 2 2 3 3 3 3 9 9 9 9 7 7 8 8 6 6 5 5\n'
expected = 'YES\n2 2 6 2 2 \n3 9 8 9 3 \n5 7 2 7 5 \n3 9 8 9 3 \n2 2 6 2 2 \n'

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
E       AssertionError: input='5\n2 2 2 2 2 2 2 2 2 3 3 3 3 9 9 9 9 7 7 8 8 6 6 5 5\n'
E         expected='YES\n2 2 6 2 2 \n3 9 8 9 3 \n5 7 2 7 5 \n3 9 8 9 3 \n2 2 6 2 2'
E         got=''
E       assert '' == 'YES\n2 2 6 2...3 \n2 2 6 2 2'
E         - YES
E         - 2 2 6 2 2 
E         - 3 9 8 9 3 
E         - 5 7 2 7 5 
E         - 3 9 8 9 3 
E         - 2 2 6 2 2

tmp6z_5dthr.py:27: AssertionError
______________________________ test_case[case22] _______________________________

i = 22, inp = '3\n2 2 4 4 8 8 16 16 32\n', expected = 'NO\n'

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
E       AssertionError: input='3\n2 2 4 4 8 8 16 16 32\n'
E         expected='NO'
E         got=''
E       assert '' == 'NO'
E         - NO

tmp6z_5dthr.py:27: AssertionError
______________________________ test_case[case23] _______________________________

i = 23
inp = '7\n1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 3 3 3 3 3 3 3 3 3\n'
expected = 'YES\n1 1 1 2 1 1 1 \n1 1 2 3 2 1 1 \n2 2 2 3 2 2 2 \n2 3 3 3 3 3 2 \n2 2 2 3 2 2 2 \n1 1 2 3 2 1 1 \n1 1 1 2 1 1 1 \n'

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
E       AssertionError: input='7\n1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 3 3 3 3 3 3 3 3 3\n'
E         expected='YES\n1 1 1 2 1 1 1 \n1 1 2 3 2 1 1 \n2 2 2 3 2 2 2 \n2 3 3 3 3 3 2 \n2 2 2 3 2 2 2 \n1 1 2 3 2 1 1 \n1 1 1 2 1 1 1'
E         got=''
E       assert '' == 'YES\n1 1 1 2...1 1 1 2 1 1 1'
E         - YES
E         - 1 1 1 2 1 1 1 
E         - 1 1 2 3 2 1 1 
E         - 2 2 2 3 2 2 2 
E         - 2 3 3 3 3 3 2 
E         - 2 2 2 3 2 2 2 
E         - 1 1 2 3 2 1 1 
E         - 1 1 1 2 1 1 1

tmp6z_5dthr.py:27: AssertionError
______________________________ test_case[case24] _______________________________

i = 24, inp = '3\n1 1 1 1 2 3 3 4 4\n'
expected = 'YES\n1 4 1 \n3 2 3 \n1 4 1 \n'

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
E       AssertionError: input='3\n1 1 1 1 2 3 3 4 4\n'
E         expected='YES\n1 4 1 \n3 2 3 \n1 4 1'
E         got=''
E       assert '' == 'YES\n1 4 1 \n3 2 3 \n1 4 1'
E         - YES
E         - 1 4 1 
E         - 3 2 3 
E         - 1 4 1

tmp6z_5dthr.py:27: AssertionError
______________________________ test_case[case25] _______________________________

i = 25
inp = '9\n1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 5\n'
expected = 'YES\n1 1 1 1 4 1 1 1 1 \n1 2 2 2 4 2 2 2 1 \n2 2 3 3 4 3 3 2 2 \n3 3 3 4 4 4 3 3 3 \n4 4 4 4 5 4 4 4 4 \n3 3 3 4 4 4 3 3 3 \n2 2 3 3 4 3 3 2 2 \n1 2 2 2 4 2 2 2 1 \n1 1 1 1 4 1 1 1 1 \n'

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
E       AssertionError: input='9\n1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 5\n'
E         expected='YES\n1 1 1 1 4 1 1 1 1 \n1 2 2 2 4 2 2 2 1 \n2 2 3 3 4 3 3 2 2 \n3 3 3 4 4 4 3 3 3 \n4 4 4 4 5 4 4 4 4 \n3 3 3 4 4 4 3 3 3 \n2 2 3 3 4 3 3 2 2 \n1 2 2 2 4 2 2 2 1 \n1 1 1 1 4 1 1 1 1'
E         got=''
E       assert '' == 'YES\n1 1 1 1...1 1 4 1 1 1 1'
E         - YES
E         - 1 1 1 1 4 1 1 1 1 
E         - 1 2 2 2 4 2 2 2 1 
E         - 2 2 3 3 4 3 3 2 2 
E         - 3 3 3 4 4 4 3 3 3 
E         - 4 4 4 4 5 4 4 4 4 
E         - 3 3 3 4 4 4 3 3 3 ...
E         
E         ...Full output truncated (3 lines hidden), use '-vv' to show

tmp6z_5dthr.py:27: AssertionError
______________________________ test_case[case26] _______________________________

i = 26
inp = '7\n1 1 1 1 2 2 2 2 3 3 3 3 4 4 4 4 5 5 5 5 6 6 6 6 7 7 7 7 8 8 8 8 9 9 9 9 10 10 10 10 11 11 11 11 12 12 12 12 13\n'
expected = 'YES\n1 2 3 10 3 2 1 \n4 5 6 11 6 5 4 \n7 8 9 12 9 8 7 \n10 11 12 13 12 11 10 \n7 8 9 12 9 8 7 \n4 5 6 11 6 5 4 \n1 2 3 10 3 2 1 \n'

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
E       AssertionError: input='7\n1 1 1 1 2 2 2 2 3 3 3 3 4 4 4 4 5 5 5 5 6 6 6 6 7 7 7 7 8 8 8 8 9 9 9 9 10 10 10 10 11 11 11 11 12 12 12 12 13\n'
E         expected='YES\n1 2 3 10 3 2 1 \n4 5 6 11 6 5 4 \n7 8 9 12 9 8 7 \n10 11 12 13 12 11 10 \n7 8 9 12 9 8 7 \n4 5 6 11 6 5 4 \n1 2 3 10 3 2 1'
E         got=''
E       assert '' == 'YES\n1 2 3 1... 2 3 10 3 2 1'
E         - YES
E         - 1 2 3 10 3 2 1 
E         - 4 5 6 11 6 5 4 
E         - 7 8 9 12 9 8 7 
E         - 10 11 12 13 12 11 10 
E         - 7 8 9 12 9 8 7 
E         - 4 5 6 11 6 5 4 
E         - 1 2 3 10 3 2 1

tmp6z_5dthr.py:27: AssertionError
______________________________ test_case[case27] _______________________________

i = 27, inp = '3\n1 1 6 6 2 3 3 4 4\n', expected = 'NO\n'

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
E       AssertionError: input='3\n1 1 6 6 2 3 3 4 4\n'
E         expected='NO'
E         got=''
E       assert '' == 'NO'
E         - NO

tmp6z_5dthr.py:27: AssertionError
______________________________ test_case[case28] _______________________________

i = 28, inp = '5\n3 3 4 4 5 5 5 6 6 1 1 1 1 1 1 1 1 1 1 1 1 2 2 2 2\n'
expected = 'YES\n1 1 4 1 1 \n1 2 6 2 1 \n3 5 5 5 3 \n1 2 6 2 1 \n1 1 4 1 1 \n'

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
E       AssertionError: input='5\n3 3 4 4 5 5 5 6 6 1 1 1 1 1 1 1 1 1 1 1 1 2 2 2 2\n'
E         expected='YES\n1 1 4 1 1 \n1 2 6 2 1 \n3 5 5 5 3 \n1 2 6 2 1 \n1 1 4 1 1'
E         got=''
E       assert '' == 'YES\n1 1 4 1...1 \n1 1 4 1 1'
E         - YES
E         - 1 1 4 1 1 
E         - 1 2 6 2 1 
E         - 3 5 5 5 3 
E         - 1 2 6 2 1 
E         - 1 1 4 1 1

tmp6z_5dthr.py:27: AssertionError
______________________________ test_case[case29] _______________________________

i = 29
inp = '11\n1 1 1 1 1 1 1 1 1 1 1 1 2 2 2 2 2 2 2 2 2 2 2 2 3 3 3 3 3 3 3 3 3 3 3 3 4 4 4 4 4 4 4 4 4 4 4 4 5 5 5 5 5 5 5 5 5...6 6 6 7 7 7 7 7 7 7 7 7 7 7 7 8 8 8 8 8 8 8 8 8 8 8 8 9 9 9 9 9 9 9 9 9 9 9 9 10 10 10 10 10 10 10 10 10 10 10 10 11\n'
expected = 'YES\n1 1 1 2 2 9 2 2 1 1 1 \n2 3 3 3 4 9 4 3 3 3 2 \n4 4 5 5 5 10 5 5 5 4 4 \n6 6 6 7 7 10 7 7 6 6 6 \n7 8 8 8 9 10 9... 8 9 10 9 8 8 8 7 \n6 6 6 7 7 10 7 7 6 6 6 \n4 4 5 5 5 10 5 5 5 4 4 \n2 3 3 3 4 9 4 3 3 3 2 \n1 1 1 2 2 9 2 2 1 1 1 \n'

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
E       AssertionError: input='11\n1 1 1 1 1 1 1 1 1 1 1 1 2 2 2 2 2 2 2 2 2 2 2 2 3 3 3 3 3 3 3 3 3 3 3 3 4 4 4 4 4 4 4 4 4 4 4 4 5 5 5 5 5 5 5 5 5 5 5 5 6 6 6 6 6 6 6 6 6 6 6 6 7 7 7 7 7 7 7 7 7 7 7 7 8 8 8 8 8 8 8 8 8 8 8 8 9 9 9 9 9 9 9 9 9 9 9 9 10 10 10 10 10 10 10 10 10 10 10 10 11\n'
E         expected='YES\n1 1 1 2 2 9 2 2 1 1 1 \n2 3 3 3 4 9 4 3 3 3 2 \n4 4 5 5 5 10 5 5 5 4 4 \n6 6 6 7 7 10 7 7 6 6 6 \n7 8 8 8 9 10 9 8 8 8 7 \n9 9 10 10 10 11 10 10 10 9 9 \n7 8 8 8 9 10 9 8 8 8 7 \n6 6 6 7 7 10 7 7 6 6 6 \n4 4 5 5 5 10 5 5 5 4 4 \n2 3 3 3 4 9 4 3 3 3 2 \n1 1 1 2 2 9 2 2 1 1 1'
E         got=''
E       assert '' == 'YES\n1 1 1 2...2 9 2 2 1 1 1'
E         - YES
E         - 1 1 1 2 2 9 2 2 1 1 1 
E         - 2 3 3 3 4 9 4 3 3 3 2 
E         - 4 4 5 5 5 10 5 5 5 4 4 
E         - 6 6 6 7 7 10 7 7 6 6 6 
E         - 7 8 8 8 9 10 9 8 8 8 7 
E         - 9 9 10 10 10 11 10 10 10 9 9 ...
E         
E         ...Full output truncated (5 lines hidden), use '-vv' to show

tmp6z_5dthr.py:27: AssertionError
______________________________ test_case[case30] _______________________________

i = 30, inp = '3\n1 1 1 1 1 1 1 1 2\n'
expected = 'YES\n1 1 1 \n1 2 1 \n1 1 1 \n'

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
E       AssertionError: input='3\n1 1 1 1 1 1 1 1 2\n'
E         expected='YES\n1 1 1 \n1 2 1 \n1 1 1'
E         got=''
E       assert '' == 'YES\n1 1 1 \n1 2 1 \n1 1 1'
E         - YES
E         - 1 1 1 
E         - 1 2 1 
E         - 1 1 1

tmp6z_5dthr.py:27: AssertionError
______________________________ test_case[case31] _______________________________

i = 31
inp = '13\n1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 4 4 4 4 4 4 4 4 4...8 8 8 8 8 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 11 11 11 11 11 11 11 11 11\n'
expected = 'YES\n1 1 1 1 2 2 10 2 2 1 1 1 1 \n2 2 3 3 3 3 10 3 3 3 3 2 2 \n4 4 4 4 5 5 10 5 5 4 4 4 4 \n5 5 6 6 6 6 10 6 6 6 6 5 ...\n5 5 6 6 6 6 10 6 6 6 6 5 5 \n4 4 4 4 5 5 10 5 5 4 4 4 4 \n2 2 3 3 3 3 10 3 3 3 3 2 2 \n1 1 1 1 2 2 10 2 2 1 1 1 1 \n'

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
E       AssertionError: input='13\n1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 11 11 11 11 11 11 11 11 11\n'
E         expected='YES\n1 1 1 1 2 2 10 2 2 1 1 1 1 \n2 2 3 3 3 3 10 3 3 3 3 2 2 \n4 4 4 4 5 5 10 5 5 4 4 4 4 \n5 5 6 6 6 6 10 6 6 6 6 5 5 \n7 7 7 7 8 8 11 8 8 7 7 7 7 \n8 8 9 9 9 9 11 9 9 9 9 8 8 \n10 10 10 10 11 11 11 11 11 10 10 10 10 \n8 8 9 9 9 9 11 9 9 9 9 8 8 \n7 7 7 7 8 8 11 8 8 7 7 7 7 \n5 5 6 6 6 6 10 6 6 6 6 5 5 \n4 4 4 4 5 5 10 5 5 4 4 4 4 \n2 2 3 3 3 3 10 3 3 3 3 2 2 \n1 1 1 1 2 2 10 2 2 1 1 1 1'
E         got=''
E       assert '' == 'YES\n1 1 1 1...0 2 2 1 1 1 1'
E         - YES
E         - 1 1 1 1 2 2 10 2 2 1 1 1 1 
E         - 2 2 3 3 3 3 10 3 3 3 3 2 2 
E         - 4 4 4 4 5 5 10 5 5 4 4 4 4 
E         - 5 5 6 6 6 6 10 6 6 6 6 5 5 
E         - 7 7 7 7 8 8 11 8 8 7 7 7 7 
E         - 8 8 9 9 9 9 11 9 9 9 9 8 8 ...
E         
E         ...Full output truncated (7 lines hidden), use '-vv' to show

tmp6z_5dthr.py:27: AssertionError
______________________________ test_case[case32] _______________________________

i = 32
inp = '13\n1 1 1 1 1 1 1 1 1 1 1 1 2 2 2 2 2 2 2 2 2 2 2 2 3 3 3 3 3 3 3 3 3 3 3 3 4 4 4 4 4 4 4 4 4 4 4 4 5 5 5 5 5 5 5 5 5...11 11 12 12 12 12 12 12 12 12 12 12 12 12 13 13 13 13 13 13 13 13 13 13 13 13 14 14 14 14 14 14 14 14 14 14 14 14 15\n'
expected = 'YES\n1 1 1 2 2 2 13 2 2 2 1 1 1 \n3 3 3 4 4 4 13 4 4 4 3 3 3 \n5 5 5 6 6 6 13 6 6 6 5 5 5 \n7 7 7 8 8 8 14 8 8 8 7 7 ...\n7 7 7 8 8 8 14 8 8 8 7 7 7 \n5 5 5 6 6 6 13 6 6 6 5 5 5 \n3 3 3 4 4 4 13 4 4 4 3 3 3 \n1 1 1 2 2 2 13 2 2 2 1 1 1 \n'

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
E       AssertionError: input='13\n1 1 1 1 1 1 1 1 1 1 1 1 2 2 2 2 2 2 2 2 2 2 2 2 3 3 3 3 3 3 3 3 3 3 3 3 4 4 4 4 4 4 4 4 4 4 4 4 5 5 5 5 5 5 5 5 5 5 5 5 6 6 6 6 6 6 6 6 6 6 6 6 7 7 7 7 7 7 7 7 7 7 7 7 8 8 8 8 8 8 8 8 8 8 8 8 9 9 9 9 9 9 9 9 9 9 9 9 10 10 10 10 10 10 10 10 10 10 10 10 11 11 11 11 11 11 11 11 11 11 11 11 12 12 12 12 12 12 12 12 12 12 12 12 13 13 13 13 13 13 13 13 13 13 13 13 14 14 14 14 14 14 14 14 14 14 14 14 15\n'
E         expected='YES\n1 1 1 2 2 2 13 2 2 2 1 1 1 \n3 3 3 4 4 4 13 4 4 4 3 3 3 \n5 5 5 6 6 6 13 6 6 6 5 5 5 \n7 7 7 8 8 8 14 8 8 8 7 7 7 \n9 9 9 10 10 10 14 10 10 10 9 9 9 \n11 11 11 12 12 12 14 12 12 12 11 11 11 \n13 13 13 14 14 14 15 14 14 14 13 13 13 \n11 11 11 12 12 12 14 12 12 12 11 11 11 \n9 9 9 10 10 10 14 10 10 10 9 9 9 \n7 7 7 8 8 8 14 8 8 8 7 7 7 \n5 5 5 6 6 6 13 6 6 6 5 5 5 \n3 3 3 4 4 4 13 4 4 4 3 3 3 \n1 1 1 2 2 2 13 2 2 2 1 1 1'
E         got=''
E       assert '' == 'YES\n1 1 1 2...3 2 2 2 1 1 1'
E         - YES
E         - 1 1 1 2 2 2 13 2 2 2 1 1 1 
E         - 3 3 3 4 4 4 13 4 4 4 3 3 3 
E         - 5 5 5 6 6 6 13 6 6 6 5 5 5 
E         - 7 7 7 8 8 8 14 8 8 8 7 7 7 
E         - 9 9 9 10 10 10 14 10 10 10 9 9 9 
E         - 11 11 11 12 12 12 14 12 12 12 11 11 11 ...
E         
E         ...Full output truncated (7 lines hidden), use '-vv' to show

tmp6z_5dthr.py:27: AssertionError
______________________________ test_case[case33] _______________________________

i = 33
inp = '9\n1 1 1 1 1 1 1 1 2 2 2 2 2 2 2 2 3 3 3 3 3 3 3 3 4 4 4 4 4 4 4 4 5 5 5 5 5 5 5 5 6 6 6 6 6 6 6 6 7 7 7 7 7 7 7 7 8 8 8 8 8 8 8 8 9 9 9 9 9 9 9 9 10 10 10 10 10 10 10 10 11\n'
expected = 'YES\n1 1 2 2 9 2 2 1 1 \n3 3 4 4 9 4 4 3 3 \n5 5 6 6 10 6 6 5 5 \n7 7 8 8 10 8 8 7 7 \n9 9 10 10 11 10 10 9 9 \n7 7 8 8 10 8 8 7 7 \n5 5 6 6 10 6 6 5 5 \n3 3 4 4 9 4 4 3 3 \n1 1 2 2 9 2 2 1 1 \n'

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
E       AssertionError: input='9\n1 1 1 1 1 1 1 1 2 2 2 2 2 2 2 2 3 3 3 3 3 3 3 3 4 4 4 4 4 4 4 4 5 5 5 5 5 5 5 5 6 6 6 6 6 6 6 6 7 7 7 7 7 7 7 7 8 8 8 8 8 8 8 8 9 9 9 9 9 9 9 9 10 10 10 10 10 10 10 10 11\n'
E         expected='YES\n1 1 2 2 9 2 2 1 1 \n3 3 4 4 9 4 4 3 3 \n5 5 6 6 10 6 6 5 5 \n7 7 8 8 10 8 8 7 7 \n9 9 10 10 11 10 10 9 9 \n7 7 8 8 10 8 8 7 7 \n5 5 6 6 10 6 6 5 5 \n3 3 4 4 9 4 4 3 3 \n1 1 2 2 9 2 2 1 1'
E         got=''
E       assert '' == 'YES\n1 1 2 2...2 2 9 2 2 1 1'
E         - YES
E         - 1 1 2 2 9 2 2 1 1 
E         - 3 3 4 4 9 4 4 3 3 
E         - 5 5 6 6 10 6 6 5 5 
E         - 7 7 8 8 10 8 8 7 7 
E         - 9 9 10 10 11 10 10 9 9 
E         - 7 7 8 8 10 8 8 7 7 ...
E         
E         ...Full output truncated (3 lines hidden), use '-vv' to show

tmp6z_5dthr.py:27: AssertionError
______________________________ test_case[case34] _______________________________

i = 34
inp = '9\n1 1 1 1 2 2 2 2 3 3 3 3 4 4 4 4 5 5 5 5 6 6 6 6 7 7 7 7 8 8 8 8 9 9 9 9 10 10 10 10 11 11 11 11 12 12 12 12 13 13 13 13 14 14 14 14 15 15 15 15 16 16 16 16 17 17 17 17 18 18 18 18 19 19 19 19 20 20 20 20 21\n'
expected = 'YES\n1 2 3 4 17 4 3 2 1 \n5 6 7 8 18 8 7 6 5 \n9 10 11 12 19 12 11 10 9 \n13 14 15 16 20 16 15 14 13 \n17 18 19 20 21 20 19 18 17 \n13 14 15 16 20 16 15 14 13 \n9 10 11 12 19 12 11 10 9 \n5 6 7 8 18 8 7 6 5 \n1 2 3 4 17 4 3 2 1 \n'

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
E       AssertionError: input='9\n1 1 1 1 2 2 2 2 3 3 3 3 4 4 4 4 5 5 5 5 6 6 6 6 7 7 7 7 8 8 8 8 9 9 9 9 10 10 10 10 11 11 11 11 12 12 12 12 13 13 13 13 14 14 14 14 15 15 15 15 16 16 16 16 17 17 17 17 18 18 18 18 19 19 19 19 20 20 20 20 21\n'
E         expected='YES\n1 2 3 4 17 4 3 2 1 \n5 6 7 8 18 8 7 6 5 \n9 10 11 12 19 12 11 10 9 \n13 14 15 16 20 16 15 14 13 \n17 18 19 20 21 20 19 18 17 \n13 14 15 16 20 16 15 14 13 \n9 10 11 12 19 12 11 10 9 \n5 6 7 8 18 8 7 6 5 \n1 2 3 4 17 4 3 2 1'
E         got=''
E       assert '' == 'YES\n1 2 3 4... 4 17 4 3 2 1'
E         - YES
E         - 1 2 3 4 17 4 3 2 1 
E         - 5 6 7 8 18 8 7 6 5 
E         - 9 10 11 12 19 12 11 10 9 
E         - 13 14 15 16 20 16 15 14 13 
E         - 17 18 19 20 21 20 19 18 17 
E         - 13 14 15 16 20 16 15 14 13 ...
E         
E         ...Full output truncated (3 lines hidden), use '-vv' to show

tmp6z_5dthr.py:27: AssertionError
______________________________ test_case[case35] _______________________________

i = 35
inp = '7\n1 1 1 1 1 1 1 1 2 2 2 2 2 2 2 2 3 3 3 3 3 3 3 3 4 4 4 4 4 4 4 4 5 5 5 5 5 5 5 5 6 6 6 6 6 6 6 6 7\n'
expected = 'YES\n1 1 2 5 2 1 1 \n2 3 3 6 3 3 2 \n4 4 5 6 5 4 4 \n5 6 6 7 6 6 5 \n4 4 5 6 5 4 4 \n2 3 3 6 3 3 2 \n1 1 2 5 2 1 1 \n'

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
E       AssertionError: input='7\n1 1 1 1 1 1 1 1 2 2 2 2 2 2 2 2 3 3 3 3 3 3 3 3 4 4 4 4 4 4 4 4 5 5 5 5 5 5 5 5 6 6 6 6 6 6 6 6 7\n'
E         expected='YES\n1 1 2 5 2 1 1 \n2 3 3 6 3 3 2 \n4 4 5 6 5 4 4 \n5 6 6 7 6 6 5 \n4 4 5 6 5 4 4 \n2 3 3 6 3 3 2 \n1 1 2 5 2 1 1'
E         got=''
E       assert '' == 'YES\n1 1 2 5...1 1 2 5 2 1 1'
E         - YES
E         - 1 1 2 5 2 1 1 
E         - 2 3 3 6 3 3 2 
E         - 4 4 5 6 5 4 4 
E         - 5 6 6 7 6 6 5 
E         - 4 4 5 6 5 4 4 
E         - 2 3 3 6 3 3 2 
E         - 1 1 2 5 2 1 1

tmp6z_5dthr.py:27: AssertionError
______________________________ test_case[case36] _______________________________

i = 36
inp = '9\n1 1 1 1 1 1 1 1 1 1 1 1 2 2 2 2 2 2 2 2 2 2 2 2 3 3 3 3 3 3 3 3 3 3 3 3 4 4 4 4 4 4 4 4 4 4 4 4 5 5 5 5 5 5 5 5 5 5 5 5 6 6 6 6 6 6 6 6 6 6 6 6 7 7 7 7 7 7 7 7 7\n'
expected = 'YES\n1 1 1 2 6 2 1 1 1 \n2 2 3 3 6 3 3 2 2 \n3 4 4 4 7 4 4 4 3 \n5 5 5 6 7 6 5 5 5 \n6 6 7 7 7 7 7 6 6 \n5 5 5 6 7 6 5 5 5 \n3 4 4 4 7 4 4 4 3 \n2 2 3 3 6 3 3 2 2 \n1 1 1 2 6 2 1 1 1 \n'

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
E       AssertionError: input='9\n1 1 1 1 1 1 1 1 1 1 1 1 2 2 2 2 2 2 2 2 2 2 2 2 3 3 3 3 3 3 3 3 3 3 3 3 4 4 4 4 4 4 4 4 4 4 4 4 5 5 5 5 5 5 5 5 5 5 5 5 6 6 6 6 6 6 6 6 6 6 6 6 7 7 7 7 7 7 7 7 7\n'
E         expected='YES\n1 1 1 2 6 2 1 1 1 \n2 2 3 3 6 3 3 2 2 \n3 4 4 4 7 4 4 4 3 \n5 5 5 6 7 6 5 5 5 \n6 6 7 7 7 7 7 6 6 \n5 5 5 6 7 6 5 5 5 \n3 4 4 4 7 4 4 4 3 \n2 2 3 3 6 3 3 2 2 \n1 1 1 2 6 2 1 1 1'
E         got=''
E       assert '' == 'YES\n1 1 1 2...1 2 6 2 1 1 1'
E         - YES
E         - 1 1 1 2 6 2 1 1 1 
E         - 2 2 3 3 6 3 3 2 2 
E         - 3 4 4 4 7 4 4 4 3 
E         - 5 5 5 6 7 6 5 5 5 
E         - 6 6 7 7 7 7 7 6 6 
E         - 5 5 5 6 7 6 5 5 5 ...
E         
E         ...Full output truncated (3 lines hidden), use '-vv' to show

tmp6z_5dthr.py:27: AssertionError
______________________________ test_case[case37] _______________________________

i = 37
inp = '13\n1 1 1 1 2 2 2 2 3 3 3 3 4 4 4 4 5 5 5 5 6 6 6 6 7 7 7 7 8 8 8 8 9 9 9 9 10 10 10 10 11 11 11 11 12 12 12 12 13 13...33 33 34 34 34 34 35 35 35 35 36 36 36 36 37 37 37 37 38 38 38 38 39 39 39 39 40 40 40 40 41 41 41 41 42 42 42 42 43\n'
expected = 'YES\n1 2 3 4 5 6 37 6 5 4 3 2 1 \n7 8 9 10 11 12 38 12 11 10 9 8 7 \n13 14 15 16 17 18 39 18 17 16 15 14 13 \n19 20 2...2 21 20 19 \n13 14 15 16 17 18 39 18 17 16 15 14 13 \n7 8 9 10 11 12 38 12 11 10 9 8 7 \n1 2 3 4 5 6 37 6 5 4 3 2 1 \n'

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
E       AssertionError: input='13\n1 1 1 1 2 2 2 2 3 3 3 3 4 4 4 4 5 5 5 5 6 6 6 6 7 7 7 7 8 8 8 8 9 9 9 9 10 10 10 10 11 11 11 11 12 12 12 12 13 13 13 13 14 14 14 14 15 15 15 15 16 16 16 16 17 17 17 17 18 18 18 18 19 19 19 19 20 20 20 20 21 21 21 21 22 22 22 22 23 23 23 23 24 24 24 24 25 25 25 25 26 26 26 26 27 27 27 27 28 28 28 28 29 29 29 29 30 30 30 30 31 31 31 31 32 32 32 32 33 33 33 33 34 34 34 34 35 35 35 35 36 36 36 36 37 37 37 37 38 38 38 38 39 39 39 39 40 40 40 40 41 41 41 41 42 42 42 42 43\n'
E         expected='YES\n1 2 3 4 5 6 37 6 5 4 3 2 1 \n7 8 9 10 11 12 38 12 11 10 9 8 7 \n13 14 15 16 17 18 39 18 17 16 15 14 13 \n19 20 21 22 23 24 40 24 23 22 21 20 19 \n25 26 27 28 29 30 41 30 29 28 27 26 25 \n31 32 33 34 35 36 42 36 35 34 33 32 31 \n37 38 39 40 41 42 43 42 41 40 39 38 37 \n31 32 33 34 35 36 42 36 35 34 33 32 31 \n25 26 27 28 29 30 41 30 29 28 27 26 25 \n19 20 21 22 23 24 40 24 23 22 21 20 19 \n13 14 15 16 17 18 39 18 17 16 15 14 13 \n7 8 9 10 11 12 38 12 11 10 9 8 7 \n1 2 3 4 5 6 37 6 5 4 3 2 1'
E         got=''
E       assert '' == 'YES\n1 2 3 4...7 6 5 4 3 2 1'
E         - YES
E         - 1 2 3 4 5 6 37 6 5 4 3 2 1 
E         - 7 8 9 10 11 12 38 12 11 10 9 8 7 
E         - 13 14 15 16 17 18 39 18 17 16 15 14 13 
E         - 19 20 21 22 23 24 40 24 23 22 21 20 19 
E         - 25 26 27 28 29 30 41 30 29 28 27 26 25 
E         - 31 32 33 34 35 36 42 36 35 34 33 32 31 ...
E         
E         ...Full output truncated (7 lines hidden), use '-vv' to show

tmp6z_5dthr.py:27: AssertionError
______________________________ test_case[case38] _______________________________

i = 38, inp = '3\n1 1 1 1 2 3 3 3 3\n'
expected = 'YES\n1 3 1 \n3 2 3 \n1 3 1 \n'

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
E       AssertionError: input='3\n1 1 1 1 2 3 3 3 3\n'
E         expected='YES\n1 3 1 \n3 2 3 \n1 3 1'
E         got=''
E       assert '' == 'YES\n1 3 1 \n3 2 3 \n1 3 1'
E         - YES
E         - 1 3 1 
E         - 3 2 3 
E         - 1 3 1

tmp6z_5dthr.py:27: AssertionError
______________________________ test_case[case39] _______________________________

i = 39, inp = '5\n1 3 6 3 1 2 4 7 4 2 5 8 9 8 5 2 4 7 4 2 1 3 6 3 1\n'
expected = 'YES\n1 2 6 2 1 \n3 4 8 4 3 \n5 7 9 7 5 \n3 4 8 4 3 \n1 2 6 2 1 \n'

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
E       AssertionError: input='5\n1 3 6 3 1 2 4 7 4 2 5 8 9 8 5 2 4 7 4 2 1 3 6 3 1\n'
E         expected='YES\n1 2 6 2 1 \n3 4 8 4 3 \n5 7 9 7 5 \n3 4 8 4 3 \n1 2 6 2 1'
E         got=''
E       assert '' == 'YES\n1 2 6 2...3 \n1 2 6 2 1'
E         - YES
E         - 1 2 6 2 1 
E         - 3 4 8 4 3 
E         - 5 7 9 7 5 
E         - 3 4 8 4 3 
E         - 1 2 6 2 1

tmp6z_5dthr.py:27: AssertionError
______________________________ test_case[case40] _______________________________

i = 40, inp = '5\n1 1 1 1 2 2 7 7 3 3 3 3 3 3 4 4 4 4 4 4 4 5 5 6 6\n'
expected = 'NO\n'

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
E       AssertionError: input='5\n1 1 1 1 2 2 7 7 3 3 3 3 3 3 4 4 4 4 4 4 4 5 5 6 6\n'
E         expected='NO'
E         got=''
E       assert '' == 'NO'
E         - NO

tmp6z_5dthr.py:27: AssertionError
______________________________ test_case[case41] _______________________________

i = 41, inp = '5\n1 1 1 1 2 2 2 2 3 3 3 3 100 11 11 9 9 8 8 7 7 6 6 5 5\n'
expected = 'NO\n'

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
E       AssertionError: input='5\n1 1 1 1 2 2 2 2 3 3 3 3 100 11 11 9 9 8 8 7 7 6 6 5 5\n'
E         expected='NO'
E         got=''
E       assert '' == 'NO'
E         - NO

tmp6z_5dthr.py:27: AssertionError
______________________________ test_case[case42] _______________________________

i = 42, inp = '5\n2 2 2 2 5 5 6 6 7 9 9 1 1 8 8 1 1 1 1 1 1 1 1 1 1\n'
expected = 'YES\n1 1 6 1 1 \n1 2 9 2 1 \n5 8 7 8 5 \n1 2 9 2 1 \n1 1 6 1 1 \n'

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
E       AssertionError: input='5\n2 2 2 2 5 5 6 6 7 9 9 1 1 8 8 1 1 1 1 1 1 1 1 1 1\n'
E         expected='YES\n1 1 6 1 1 \n1 2 9 2 1 \n5 8 7 8 5 \n1 2 9 2 1 \n1 1 6 1 1'
E         got=''
E       assert '' == 'YES\n1 1 6 1...1 \n1 1 6 1 1'
E         - YES
E         - 1 1 6 1 1 
E         - 1 2 9 2 1 
E         - 5 8 7 8 5 
E         - 1 2 9 2 1 
E         - 1 1 6 1 1

tmp6z_5dthr.py:27: AssertionError
______________________________ test_case[case43] _______________________________

i = 43, inp = '2\n1 1 1 2\n', expected = 'NO\n'

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
E       AssertionError: input='2\n1 1 1 2\n'
E         expected='NO'
E         got=''
E       assert '' == 'NO'
E         - NO

tmp6z_5dthr.py:27: AssertionError
______________________________ test_case[case44] _______________________________

i = 44, inp = '2\n1 1 1 3\n', expected = 'NO\n'

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
E       AssertionError: input='2\n1 1 1 3\n'
E         expected='NO'
E         got=''
E       assert '' == 'NO'
E         - NO

tmp6z_5dthr.py:27: AssertionError
=========================== short test summary info ============================
FAILED tmp6z_5dthr.py::test_case[case0] - AssertionError: input='4\n1 8 8 1 2...
FAILED tmp6z_5dthr.py::test_case[case1] - AssertionError: input='3\n1 1 1 1 1...
FAILED tmp6z_5dthr.py::test_case[case2] - AssertionError: input='4\n1 2 1 9 8...
FAILED tmp6z_5dthr.py::test_case[case3] - AssertionError: input='1\n10\n'
FAILED tmp6z_5dthr.py::test_case[case4] - AssertionError: input='2\n3 3 3 3\n'
FAILED tmp6z_5dthr.py::test_case[case5] - AssertionError: input='7\n5 9 5 4 1...
FAILED tmp6z_5dthr.py::test_case[case6] - AssertionError: input='7\n1 8 9 6 4...
FAILED tmp6z_5dthr.py::test_case[case7] - AssertionError: input='3\n1 1 2 2 3...
FAILED tmp6z_5dthr.py::test_case[case8] - AssertionError: input='4\n1 1 1 1 1...
FAILED tmp6z_5dthr.py::test_case[case9] - AssertionError: input='3\n1 1 2 2 3...
FAILED tmp6z_5dthr.py::test_case[case10] - AssertionError: input='5\n4 4 3 5 ...
FAILED tmp6z_5dthr.py::test_case[case11] - AssertionError: input='5\n1 1 1 1 ...
FAILED tmp6z_5dthr.py::test_case[case12] - AssertionError: input='2\n1000 100...
FAILED tmp6z_5dthr.py::test_case[case13] - AssertionError: input='3\n17 17 18...
FAILED tmp6z_5dthr.py::test_case[case14] - AssertionError: input='3\n1 4 3 3 ...
FAILED tmp6z_5dthr.py::test_case[case15] - AssertionError: input='3\n17 17 18...
FAILED tmp6z_5dthr.py::test_case[case16] - AssertionError: input='3\n3 4 2 1 ...
FAILED tmp6z_5dthr.py::test_case[case17] - AssertionError: input='3\n1 2 2 3 ...
FAILED tmp6z_5dthr.py::test_case[case18] - AssertionError: input='3\n19 19 7 ...
FAILED tmp6z_5dthr.py::test_case[case19] - AssertionError: input='3\n13 13 42...
FAILED tmp6z_5dthr.py::test_case[case20] - AssertionError: input='3\n1 1 2 2 ...
FAILED tmp6z_5dthr.py::test_case[case21] - AssertionError: input='5\n2 2 2 2 ...
FAILED tmp6z_5dthr.py::test_case[case22] - AssertionError: input='3\n2 2 4 4 ...
FAILED tmp6z_5dthr.py::test_case[case23] - AssertionError: input='7\n1 1 1 1 ...
FAILED tmp6z_5dthr.py::test_case[case24] - AssertionError: input='3\n1 1 1 1 ...
FAILED tmp6z_5dthr.py::test_case[case25] - AssertionError: input='9\n1 1 1 1 ...
FAILED tmp6z_5dthr.py::test_case[case26] - AssertionError: input='7\n1 1 1 1 ...
FAILED tmp6z_5dthr.py::test_case[case27] - AssertionError: input='3\n1 1 6 6 ...
FAILED tmp6z_5dthr.py::test_case[case28] - AssertionError: input='5\n3 3 4 4 ...
FAILED tmp6z_5dthr.py::test_case[case29] - AssertionError: input='11\n1 1 1 1...
FAILED tmp6z_5dthr.py::test_case[case30] - AssertionError: input='3\n1 1 1 1 ...
FAILED tmp6z_5dthr.py::test_case[case31] - AssertionError: input='13\n1 1 1 1...
FAILED tmp6z_5dthr.py::test_case[case32] - AssertionError: input='13\n1 1 1 1...
FAILED tmp6z_5dthr.py::test_case[case33] - AssertionError: input='9\n1 1 1 1 ...
FAILED tmp6z_5dthr.py::test_case[case34] - AssertionError: input='9\n1 1 1 1 ...
FAILED tmp6z_5dthr.py::test_case[case35] - AssertionError: input='7\n1 1 1 1 ...
FAILED tmp6z_5dthr.py::test_case[case36] - AssertionError: input='9\n1 1 1 1 ...
FAILED tmp6z_5dthr.py::test_case[case37] - AssertionError: input='13\n1 1 1 1...
FAILED tmp6z_5dthr.py::test_case[case38] - AssertionError: input='3\n1 1 1 1 ...
FAILED tmp6z_5dthr.py::test_case[case39] - AssertionError: input='5\n1 3 6 3 ...
FAILED tmp6z_5dthr.py::test_case[case40] - AssertionError: input='5\n1 1 1 1 ...
FAILED tmp6z_5dthr.py::test_case[case41] - AssertionError: input='5\n1 1 1 1 ...
FAILED tmp6z_5dthr.py::test_case[case42] - AssertionError: input='5\n2 2 2 2 ...
FAILED tmp6z_5dthr.py::test_case[case43] - AssertionError: input='2\n1 1 1 2\n'
FAILED tmp6z_5dthr.py::test_case[case44] - AssertionError: input='2\n1 1 1 3\n'
============================== 45 failed in 8.31s ==============================
```
