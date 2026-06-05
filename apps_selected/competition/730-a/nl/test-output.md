# competition/730-a

**Status:** FAIL (exit code 1)

## stdout

```
============================= test session starts ==============================
platform linux -- Python 3.10.18, pytest-7.4.4, pluggy-1.6.0
PyQt5 5.15.10 -- Qt runtime 5.15.17 -- Qt compiled 5.15.2
rootdir: /tmp/tmpq5y657oe
configfile: pytest.ini
plugins: Faker-25.1.0, anyio-4.9.0, cov-5.0.0, mock-3.12.0, qt-4.3.1
collected 20 items

tmpvl5xzvmw.py::test_case[case0] FAILED
tmpvl5xzvmw.py::test_case[case1] FAILED
tmpvl5xzvmw.py::test_case[case2] PASSED
tmpvl5xzvmw.py::test_case[case3] FAILED
tmpvl5xzvmw.py::test_case[case4] FAILED
tmpvl5xzvmw.py::test_case[case5] FAILED
tmpvl5xzvmw.py::test_case[case6] FAILED
tmpvl5xzvmw.py::test_case[case7] FAILED
tmpvl5xzvmw.py::test_case[case8] FAILED
tmpvl5xzvmw.py::test_case[case9] FAILED
tmpvl5xzvmw.py::test_case[case10] FAILED
tmpvl5xzvmw.py::test_case[case11] FAILED
tmpvl5xzvmw.py::test_case[case12] FAILED
tmpvl5xzvmw.py::test_case[case13] FAILED
tmpvl5xzvmw.py::test_case[case14] FAILED
tmpvl5xzvmw.py::test_case[case15] FAILED
tmpvl5xzvmw.py::test_case[case16] PASSED
tmpvl5xzvmw.py::test_case[case17] FAILED
tmpvl5xzvmw.py::test_case[case18] FAILED
tmpvl5xzvmw.py::test_case[case19] FAILED

=================================== FAILURES ===================================
_______________________________ test_case[case0] _______________________________

i = 0, inp = '5\n4 5 1 7 4\n'
expected = '1\n8\n01010\n00011\n01010\n10010\n00011\n11000\n00011\n11000\n'

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
E       AssertionError: input='5\n4 5 1 7 4\n'
E         expected='1\n8\n01010\n00011\n01010\n10010\n00011\n11000\n00011\n11000'
E         got='7\n0'
E       assert '7\n0' == '1\n8\n01010\...n00011\n11000'
E         + 7
E         + 0
E         - 1
E         - 8
E         - 01010
E         - 00011
E         - 01010...
E         
E         ...Full output truncated (5 lines hidden), use '-vv' to show

tmpvl5xzvmw.py:27: AssertionError
_______________________________ test_case[case1] _______________________________

i = 1, inp = '2\n1 2\n', expected = '0\n2\n11\n11\n'

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
E       AssertionError: input='2\n1 2\n'
E         expected='0\n2\n11\n11'
E         got='2\n0'
E       assert '2\n0' == '0\n2\n11\n11'
E         - 0
E           2
E         + 0
E         - 11
E         - 11

tmpvl5xzvmw.py:27: AssertionError
_______________________________ test_case[case3] _______________________________

i = 3, inp = '10\n6 8 7 6 8 7 6 7 8 7\n'
expected = '6\n4\n0100100010\n0000000111\n0000110000\n0110000000\n'

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
E       AssertionError: input='10\n6 8 7 6 8 7 6 7 8 7\n'
E         expected='6\n4\n0100100010\n0000000111\n0000110000\n0110000000'
E         got='8\n0'
E       assert '8\n0' == '6\n4\n010010...0\n0110000000'
E         + 8
E         + 0
E         - 6
E         - 4
E         - 0100100010
E         - 0000000111
E         - 0000110000
E         - 0110000000

tmpvl5xzvmw.py:27: AssertionError
_______________________________ test_case[case4] _______________________________

i = 4, inp = '5\n4 4 4 7 3\n'
expected = '2\n6\n00110\n01010\n10010\n00011\n00110\n11000\n'

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
E       AssertionError: input='5\n4 4 4 7 3\n'
E         expected='2\n6\n00110\n01010\n10010\n00011\n00110\n11000'
E         got='7\n0'
E       assert '7\n0' == '2\n6\n00110\...n00110\n11000'
E         + 7
E         + 0
E         - 2
E         - 6
E         - 00110
E         - 01010
E         - 10010...
E         
E         ...Full output truncated (3 lines hidden), use '-vv' to show

tmpvl5xzvmw.py:27: AssertionError
_______________________________ test_case[case5] _______________________________

i = 5, inp = '5\n4 7 5 2 2\n'
expected = '2\n5\n01100\n01100\n11000\n01100\n11000\n'

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
E       AssertionError: input='5\n4 7 5 2 2\n'
E         expected='2\n5\n01100\n01100\n11000\n01100\n11000'
E         got='7\n0'
E       assert '7\n0' == '2\n5\n01100\...n01100\n11000'
E         + 7
E         + 0
E         - 2
E         - 5
E         - 01100
E         - 01100
E         - 11000
E         - 01100
E         - 11000

tmpvl5xzvmw.py:27: AssertionError
_______________________________ test_case[case6] _______________________________

i = 6, inp = '6\n5 4 2 4 3 2\n'
expected = '2\n4\n100100\n110000\n000110\n110000\n'

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
E       AssertionError: input='6\n5 4 2 4 3 2\n'
E         expected='2\n4\n100100\n110000\n000110\n110000'
E         got='5\n0'
E       assert '5\n0' == '2\n4\n100100...00110\n110000'
E         + 5
E         + 0
E         - 2
E         - 4
E         - 100100
E         - 110000
E         - 000110
E         - 110000

tmpvl5xzvmw.py:27: AssertionError
_______________________________ test_case[case7] _______________________________

i = 7, inp = '7\n7 8 2 7 10 11 5\n'
expected = '2\n17\n0000110\n0000110\n0000110\n0100010\n0001110\n1100000\n0001110\n1100000\n0000011\n0001100\n1100000\n0000011\n0001100\n1100000\n0000011\n0001100\n1100000\n'

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
E       AssertionError: input='7\n7 8 2 7 10 11 5\n'
E         expected='2\n17\n0000110\n0000110\n0000110\n0100010\n0001110\n1100000\n0001110\n1100000\n0000011\n0001100\n1100000\n0000011\n0001100\n1100000\n0000011\n0001100\n1100000'
E         got='11\n0'
E       assert '11\n0' == '2\n17\n00001...1100\n1100000'
E         + 11
E         + 0
E         - 2
E         - 17
E         - 0000110
E         - 0000110
E         - 0000110...
E         
E         ...Full output truncated (14 lines hidden), use '-vv' to show

tmpvl5xzvmw.py:27: AssertionError
_______________________________ test_case[case8] _______________________________

i = 8, inp = '10\n2 3 3 3 2 6 2 5 3 5\n'
expected = '2\n6\n0000010001\n0000010100\n0000010101\n0000000111\n0001010000\n0110000000\n'

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
E       AssertionError: input='10\n2 3 3 3 2 6 2 5 3 5\n'
E         expected='2\n6\n0000010001\n0000010100\n0000010101\n0000000111\n0001010000\n0110000000'
E         got='6\n0'
E       assert '6\n0' == '2\n6\n000001...0\n0110000000'
E         - 2
E           6
E         + 0
E         - 0000010001
E         - 0000010100
E         - 0000010101
E         - 0000000111
E         - 0001010000
E         - 0110000000

tmpvl5xzvmw.py:27: AssertionError
_______________________________ test_case[case9] _______________________________

i = 9, inp = '2\n62 64\n'
expected = '0\n64\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11...\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n'

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
E       AssertionError: input='2\n62 64\n'
E         expected='0\n64\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11'
E         got='64\n0'
E       assert '64\n0' == '0\n64\n11\n1...1\n11\n11\n11'
E         - 0
E           64
E         + 0
E         - 11
E         - 11
E         - 11
E         - 11...
E         
E         ...Full output truncated (60 lines hidden), use '-vv' to show

tmpvl5xzvmw.py:27: AssertionError
______________________________ test_case[case10] _______________________________

i = 10, inp = '2\n71 70\n'
expected = '0\n71\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11...\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n'

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
E       AssertionError: input='2\n71 70\n'
E         expected='0\n71\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11'
E         got='71\n0'
E       assert '71\n0' == '0\n71\n11\n1...1\n11\n11\n11'
E         - 0
E           71
E         + 0
E         - 11
E         - 11
E         - 11
E         - 11...
E         
E         ...Full output truncated (67 lines hidden), use '-vv' to show

tmpvl5xzvmw.py:27: AssertionError
______________________________ test_case[case11] _______________________________

i = 11, inp = '5\n4 5 4 3 3\n', expected = '3\n2\n01100\n11000\n'

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
E       AssertionError: input='5\n4 5 4 3 3\n'
E         expected='3\n2\n01100\n11000'
E         got='5\n0'
E       assert '5\n0' == '3\n2\n01100\n11000'
E         + 5
E         + 0
E         - 3
E         - 2
E         - 01100
E         - 11000

tmpvl5xzvmw.py:27: AssertionError
______________________________ test_case[case12] _______________________________

i = 12, inp = '6\n4 2 3 2 2 2\n'
expected = '1\n4\n101000\n100001\n001110\n110000\n'

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
E       AssertionError: input='6\n4 2 3 2 2 2\n'
E         expected='1\n4\n101000\n100001\n001110\n110000'
E         got='4\n0'
E       assert '4\n0' == '1\n4\n101000...01110\n110000'
E         - 1
E           4
E         + 0
E         - 101000
E         - 100001
E         - 001110
E         - 110000

tmpvl5xzvmw.py:27: AssertionError
______________________________ test_case[case13] _______________________________

i = 13, inp = '7\n4 6 5 8 8 2 6\n'
expected = '2\n12\n0001100\n0001100\n0000101\n0101000\n0001101\n0110000\n0000101\n0011000\n1100000\n0000101\n0011000\n1100000\n'

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
E       AssertionError: input='7\n4 6 5 8 8 2 6\n'
E         expected='2\n12\n0001100\n0001100\n0000101\n0101000\n0001101\n0110000\n0000101\n0011000\n1100000\n0000101\n0011000\n1100000'
E         got='8\n0'
E       assert '8\n0' == '2\n12\n00011...1000\n1100000'
E         + 8
E         + 0
E         - 2
E         - 12
E         - 0001100
E         - 0001100
E         - 0000101...
E         
E         ...Full output truncated (9 lines hidden), use '-vv' to show

tmpvl5xzvmw.py:27: AssertionError
______________________________ test_case[case14] _______________________________

i = 14, inp = '10\n4 5 3 3 3 4 2 3 2 2\n'
expected = '2\n5\n0100010000\n1100000000\n0000110100\n0011000000\n1100000000\n'

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
E       AssertionError: input='10\n4 5 3 3 3 4 2 3 2 2\n'
E         expected='2\n5\n0100010000\n1100000000\n0000110100\n0011000000\n1100000000'
E         got='5\n0'
E       assert '5\n0' == '2\n5\n010001...0\n1100000000'
E         - 2
E           5
E         + 0
E         - 0100010000
E         - 1100000000
E         - 0000110100
E         - 0011000000
E         - 1100000000

tmpvl5xzvmw.py:27: AssertionError
______________________________ test_case[case15] _______________________________

i = 15, inp = '2\n61 60\n'
expected = '0\n61\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11...\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n'

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
E       AssertionError: input='2\n61 60\n'
E         expected='0\n61\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11\n11'
E         got='61\n0'
E       assert '61\n0' == '0\n61\n11\n1...1\n11\n11\n11'
E         - 0
E           61
E         + 0
E         - 11
E         - 11
E         - 11
E         - 11...
E         
E         ...Full output truncated (57 lines hidden), use '-vv' to show

tmpvl5xzvmw.py:27: AssertionError
______________________________ test_case[case17] _______________________________

i = 17, inp = '4\n1 1 6 2\n'
expected = '0\n6\n0011\n0011\n0110\n1010\n0011\n0011\n'

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
E       AssertionError: input='4\n1 1 6 2\n'
E         expected='0\n6\n0011\n0011\n0110\n1010\n0011\n0011'
E         got='6\n0'
E       assert '6\n0' == '0\n6\n0011\n...0\n0011\n0011'
E         - 0
E           6
E         + 0
E         - 0011
E         - 0011
E         - 0110
E         - 1010
E         - 0011
E         - 0011

tmpvl5xzvmw.py:27: AssertionError
______________________________ test_case[case18] _______________________________

i = 18, inp = '3\n1 2 6\n', expected = '0\n6\n011\n011\n101\n011\n011\n011\n'

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
E       AssertionError: input='3\n1 2 6\n'
E         expected='0\n6\n011\n011\n101\n011\n011\n011'
E         got='6\n0'
E       assert '6\n0' == '0\n6\n011\n0...011\n011\n011'
E         - 0
E           6
E         + 0
E         - 011
E         - 011
E         - 101
E         - 011
E         - 011
E         - 011

tmpvl5xzvmw.py:27: AssertionError
______________________________ test_case[case19] _______________________________

i = 19, inp = '7\n2 5 4 1 6 3 4\n'
expected = '1\n8\n0100100\n0000101\n0110100\n0000111\n0110000\n0000011\n0010100\n1100000\n'

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
E       AssertionError: input='7\n2 5 4 1 6 3 4\n'
E         expected='1\n8\n0100100\n0000101\n0110100\n0000111\n0110000\n0000011\n0010100\n1100000'
E         got='6\n0'
E       assert '6\n0' == '1\n8\n010010...0100\n1100000'
E         + 6
E         + 0
E         - 1
E         - 8
E         - 0100100
E         - 0000101
E         - 0110100...
E         
E         ...Full output truncated (5 lines hidden), use '-vv' to show

tmpvl5xzvmw.py:27: AssertionError
=========================== short test summary info ============================
FAILED tmpvl5xzvmw.py::test_case[case0] - AssertionError: input='5\n4 5 1 7 4\n'
FAILED tmpvl5xzvmw.py::test_case[case1] - AssertionError: input='2\n1 2\n'
FAILED tmpvl5xzvmw.py::test_case[case3] - AssertionError: input='10\n6 8 7 6 ...
FAILED tmpvl5xzvmw.py::test_case[case4] - AssertionError: input='5\n4 4 4 7 3\n'
FAILED tmpvl5xzvmw.py::test_case[case5] - AssertionError: input='5\n4 7 5 2 2\n'
FAILED tmpvl5xzvmw.py::test_case[case6] - AssertionError: input='6\n5 4 2 4 3...
FAILED tmpvl5xzvmw.py::test_case[case7] - AssertionError: input='7\n7 8 2 7 1...
FAILED tmpvl5xzvmw.py::test_case[case8] - AssertionError: input='10\n2 3 3 3 ...
FAILED tmpvl5xzvmw.py::test_case[case9] - AssertionError: input='2\n62 64\n'
FAILED tmpvl5xzvmw.py::test_case[case10] - AssertionError: input='2\n71 70\n'
FAILED tmpvl5xzvmw.py::test_case[case11] - AssertionError: input='5\n4 5 4 3 ...
FAILED tmpvl5xzvmw.py::test_case[case12] - AssertionError: input='6\n4 2 3 2 ...
FAILED tmpvl5xzvmw.py::test_case[case13] - AssertionError: input='7\n4 6 5 8 ...
FAILED tmpvl5xzvmw.py::test_case[case14] - AssertionError: input='10\n4 5 3 3...
FAILED tmpvl5xzvmw.py::test_case[case15] - AssertionError: input='2\n61 60\n'
FAILED tmpvl5xzvmw.py::test_case[case17] - AssertionError: input='4\n1 1 6 2\n'
FAILED tmpvl5xzvmw.py::test_case[case18] - AssertionError: input='3\n1 2 6\n'
FAILED tmpvl5xzvmw.py::test_case[case19] - AssertionError: input='7\n2 5 4 1 ...
========================= 18 failed, 2 passed in 3.98s =========================
```
