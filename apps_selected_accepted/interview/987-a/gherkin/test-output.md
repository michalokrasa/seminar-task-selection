# interview/987-a

**Status:** FAIL (exit code 1)

## stdout

```
============================= test session starts ==============================
platform linux -- Python 3.10.18, pytest-7.4.4, pluggy-1.6.0
PyQt5 5.15.10 -- Qt runtime 5.15.17 -- Qt compiled 5.15.2
rootdir: /tmp/tmpeyhu5m28
configfile: pytest.ini
plugins: Faker-25.1.0, anyio-4.9.0, cov-5.0.0, mock-3.12.0, qt-4.3.1
collected 64 items

tmpdebrs9di.py::test_case[case0] FAILED
tmpdebrs9di.py::test_case[case1] FAILED
tmpdebrs9di.py::test_case[case2] PASSED
tmpdebrs9di.py::test_case[case3] FAILED
tmpdebrs9di.py::test_case[case4] FAILED
tmpdebrs9di.py::test_case[case5] FAILED
tmpdebrs9di.py::test_case[case6] FAILED
tmpdebrs9di.py::test_case[case7] FAILED
tmpdebrs9di.py::test_case[case8] FAILED
tmpdebrs9di.py::test_case[case9] FAILED
tmpdebrs9di.py::test_case[case10] FAILED
tmpdebrs9di.py::test_case[case11] FAILED
tmpdebrs9di.py::test_case[case12] FAILED
tmpdebrs9di.py::test_case[case13] FAILED
tmpdebrs9di.py::test_case[case14] FAILED
tmpdebrs9di.py::test_case[case15] FAILED
tmpdebrs9di.py::test_case[case16] FAILED
tmpdebrs9di.py::test_case[case17] FAILED
tmpdebrs9di.py::test_case[case18] PASSED
tmpdebrs9di.py::test_case[case19] FAILED
tmpdebrs9di.py::test_case[case20] FAILED
tmpdebrs9di.py::test_case[case21] FAILED
tmpdebrs9di.py::test_case[case22] FAILED
tmpdebrs9di.py::test_case[case23] FAILED
tmpdebrs9di.py::test_case[case24] FAILED
tmpdebrs9di.py::test_case[case25] FAILED
tmpdebrs9di.py::test_case[case26] PASSED
tmpdebrs9di.py::test_case[case27] FAILED
tmpdebrs9di.py::test_case[case28] FAILED
tmpdebrs9di.py::test_case[case29] FAILED
tmpdebrs9di.py::test_case[case30] FAILED
tmpdebrs9di.py::test_case[case31] FAILED
tmpdebrs9di.py::test_case[case32] PASSED
tmpdebrs9di.py::test_case[case33] FAILED
tmpdebrs9di.py::test_case[case34] PASSED
tmpdebrs9di.py::test_case[case35] FAILED
tmpdebrs9di.py::test_case[case36] FAILED
tmpdebrs9di.py::test_case[case37] FAILED
tmpdebrs9di.py::test_case[case38] PASSED
tmpdebrs9di.py::test_case[case39] FAILED
tmpdebrs9di.py::test_case[case40] FAILED
tmpdebrs9di.py::test_case[case41] FAILED
tmpdebrs9di.py::test_case[case42] PASSED
tmpdebrs9di.py::test_case[case43] PASSED
tmpdebrs9di.py::test_case[case44] FAILED
tmpdebrs9di.py::test_case[case45] FAILED
tmpdebrs9di.py::test_case[case46] PASSED
tmpdebrs9di.py::test_case[case47] FAILED
tmpdebrs9di.py::test_case[case48] PASSED
tmpdebrs9di.py::test_case[case49] FAILED
tmpdebrs9di.py::test_case[case50] PASSED
tmpdebrs9di.py::test_case[case51] PASSED
tmpdebrs9di.py::test_case[case52] FAILED
tmpdebrs9di.py::test_case[case53] PASSED
tmpdebrs9di.py::test_case[case54] FAILED
tmpdebrs9di.py::test_case[case55] PASSED
tmpdebrs9di.py::test_case[case56] PASSED
tmpdebrs9di.py::test_case[case57] PASSED
tmpdebrs9di.py::test_case[case58] PASSED
tmpdebrs9di.py::test_case[case59] PASSED
tmpdebrs9di.py::test_case[case60] PASSED
tmpdebrs9di.py::test_case[case61] PASSED
tmpdebrs9di.py::test_case[case62] PASSED
tmpdebrs9di.py::test_case[case63] PASSED

=================================== FAILURES ===================================
_______________________________ test_case[case0] _______________________________

i = 0, inp = '4\nred\npurple\nyellow\norange\n', expected = '2\nTime\nSpace\n'

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
E       AssertionError: input='4\nred\npurple\nyellow\norange\n'
E         expected='2\nTime\nSpace'
E         got='2\nSpace\nTime'
E       assert '2\nSpace\nTime' == '2\nTime\nSpace'
E           2
E         - Time
E         - Space
E         + Space
E         ?      +
E         + Time

tmpdebrs9di.py:27: AssertionError
_______________________________ test_case[case1] _______________________________

i = 1, inp = '0\n', expected = '6\nReality\nTime\nMind\nSpace\nPower\nSoul\n'

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
E       AssertionError: input='0\n'
E         expected='6\nReality\nTime\nMind\nSpace\nPower\nSoul'
E         got='6\nMind\nPower\nReality\nSoul\nSpace\nTime'
E       assert '6\nMind\nPow...\nSpace\nTime' == '6\nReality\n...\nPower\nSoul'
E           6
E         + Mind
E         + Power
E           Reality
E         + Soul
E         - Time
E         - Mind...
E         
E         ...Full output truncated (4 lines hidden), use '-vv' to show

tmpdebrs9di.py:27: AssertionError
_______________________________ test_case[case3] _______________________________

i = 3, inp = '1\npurple\n', expected = '5\nMind\nSpace\nReality\nSoul\nTime\n'

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
E       AssertionError: input='1\npurple\n'
E         expected='5\nMind\nSpace\nReality\nSoul\nTime'
E         got='5\nMind\nReality\nSoul\nSpace\nTime'
E       assert '5\nMind\nRea...\nSpace\nTime' == '5\nMind\nSpa...y\nSoul\nTime'
E           5
E           Mind
E         - Space
E           Reality
E           Soul
E         + Space
E           Time

tmpdebrs9di.py:27: AssertionError
_______________________________ test_case[case4] _______________________________

i = 4, inp = '3\nblue\norange\npurple\n', expected = '3\nReality\nMind\nTime\n'

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
E       AssertionError: input='3\nblue\norange\npurple\n'
E         expected='3\nReality\nMind\nTime'
E         got='3\nMind\nReality\nTime'
E       assert '3\nMind\nReality\nTime' == '3\nReality\nMind\nTime'
E           3
E         + Mind
E           Reality
E         - Mind
E           Time

tmpdebrs9di.py:27: AssertionError
_______________________________ test_case[case5] _______________________________

i = 5, inp = '2\nyellow\nred\n', expected = '4\nTime\nPower\nSoul\nSpace\n'

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
E       AssertionError: input='2\nyellow\nred\n'
E         expected='4\nTime\nPower\nSoul\nSpace'
E         got='4\nPower\nSoul\nSpace\nTime'
E       assert '4\nPower\nSoul\nSpace\nTime' == '4\nTime\nPower\nSoul\nSpace'
E           4
E         - Time
E           Power
E           Soul
E         - Space
E         + Space
E         ?      +
E         + Time

tmpdebrs9di.py:27: AssertionError
_______________________________ test_case[case6] _______________________________

i = 6, inp = '1\ngreen\n', expected = '5\nReality\nSpace\nMind\nPower\nSoul\n'

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
E       AssertionError: input='1\ngreen\n'
E         expected='5\nReality\nSpace\nMind\nPower\nSoul'
E         got='5\nMind\nPower\nReality\nSoul\nSpace'
E       assert '5\nMind\nPow...\nSoul\nSpace' == '5\nReality\n...\nPower\nSoul'
E           5
E         - Reality
E         - Space
E           Mind
E           Power
E         + Reality
E         - Soul...
E         
E         ...Full output truncated (3 lines hidden), use '-vv' to show

tmpdebrs9di.py:27: AssertionError
_______________________________ test_case[case7] _______________________________

i = 7, inp = '2\npurple\ngreen\n', expected = '4\nSpace\nReality\nSoul\nMind\n'

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
E       AssertionError: input='2\npurple\ngreen\n'
E         expected='4\nSpace\nReality\nSoul\nMind'
E         got='4\nMind\nReality\nSoul\nSpace'
E       assert '4\nMind\nRea...\nSoul\nSpace' == '4\nSpace\nRe...y\nSoul\nMind'
E           4
E         - Space
E         + Mind
E           Reality
E           Soul
E         - Mind
E         + Space

tmpdebrs9di.py:27: AssertionError
_______________________________ test_case[case8] _______________________________

i = 8, inp = '1\nblue\n', expected = '5\nMind\nSoul\nTime\nPower\nReality\n'

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
E       AssertionError: input='1\nblue\n'
E         expected='5\nMind\nSoul\nTime\nPower\nReality'
E         got='5\nMind\nPower\nReality\nSoul\nTime'
E       assert '5\nMind\nPow...y\nSoul\nTime' == '5\nMind\nSou...ower\nReality'
E           5
E           Mind
E         + Power
E         + Reality
E           Soul
E         - Time
E         ?     -...
E         
E         ...Full output truncated (3 lines hidden), use '-vv' to show

tmpdebrs9di.py:27: AssertionError
_______________________________ test_case[case9] _______________________________

i = 9, inp = '2\npurple\nblue\n', expected = '4\nReality\nTime\nSoul\nMind\n'

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
E       AssertionError: input='2\npurple\nblue\n'
E         expected='4\nReality\nTime\nSoul\nMind'
E         got='4\nMind\nReality\nSoul\nTime'
E       assert '4\nMind\nReality\nSoul\nTime' == '4\nReality\nTime\nSoul\nMind'
E           4
E         + Mind
E           Reality
E         - Time
E           Soul
E         - Mind
E         + Time

tmpdebrs9di.py:27: AssertionError
______________________________ test_case[case10] _______________________________

i = 10, inp = '2\ngreen\nblue\n', expected = '4\nPower\nMind\nSoul\nReality\n'

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
E       AssertionError: input='2\ngreen\nblue\n'
E         expected='4\nPower\nMind\nSoul\nReality'
E         got='4\nMind\nPower\nReality\nSoul'
E       assert '4\nMind\nPow...Reality\nSoul' == '4\nPower\nMi...Soul\nReality'
E           4
E         + Mind
E           Power
E         - Mind
E         - Soul
E         - Reality
E         + Reality
E         ?        +
E         + Soul

tmpdebrs9di.py:27: AssertionError
______________________________ test_case[case11] _______________________________

i = 11, inp = '3\npurple\ngreen\nblue\n', expected = '3\nSoul\nReality\nMind\n'

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
E       AssertionError: input='3\npurple\ngreen\nblue\n'
E         expected='3\nSoul\nReality\nMind'
E         got='3\nMind\nReality\nSoul'
E       assert '3\nMind\nReality\nSoul' == '3\nSoul\nReality\nMind'
E           3
E         - Soul
E         + Mind
E           Reality
E         - Mind
E         + Soul

tmpdebrs9di.py:27: AssertionError
______________________________ test_case[case12] _______________________________

i = 12, inp = '1\norange\n', expected = '5\nReality\nTime\nSpace\nMind\nPower\n'

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
E       AssertionError: input='1\norange\n'
E         expected='5\nReality\nTime\nSpace\nMind\nPower'
E         got='5\nMind\nPower\nReality\nSpace\nTime'
E       assert '5\nMind\nPow...\nSpace\nTime' == '5\nReality\n...\nMind\nPower'
E           5
E         + Mind
E         + Power
E           Reality
E         - Time
E           Space
E         + Time
E         - Mind
E         - Power

tmpdebrs9di.py:27: AssertionError
______________________________ test_case[case13] _______________________________

i = 13, inp = '2\npurple\norange\n'
expected = '4\nTime\nSpace\nReality\nMind\n'

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
E       AssertionError: input='2\npurple\norange\n'
E         expected='4\nTime\nSpace\nReality\nMind'
E         got='4\nMind\nReality\nSpace\nTime'
E       assert '4\nMind\nRea...\nSpace\nTime' == '4\nTime\nSpa...Reality\nMind'
E           4
E         - Time
E         + Mind
E         + Reality
E           Space
E         + Time
E         - Reality
E         - Mind

tmpdebrs9di.py:27: AssertionError
______________________________ test_case[case14] _______________________________

i = 14, inp = '2\norange\ngreen\n'
expected = '4\nMind\nReality\nSpace\nPower\n'

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
E       AssertionError: input='2\norange\ngreen\n'
E         expected='4\nMind\nReality\nSpace\nPower'
E         got='4\nMind\nPower\nReality\nSpace'
E       assert '4\nMind\nPow...eality\nSpace' == '4\nMind\nRea...nSpace\nPower'
E           4
E           Mind
E         + Power
E           Reality
E         - Space
E         ?      -
E         + Space
E         - Power

tmpdebrs9di.py:27: AssertionError
______________________________ test_case[case15] _______________________________

i = 15, inp = '3\norange\npurple\ngreen\n'
expected = '3\nReality\nSpace\nMind\n'

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
E       AssertionError: input='3\norange\npurple\ngreen\n'
E         expected='3\nReality\nSpace\nMind'
E         got='3\nMind\nReality\nSpace'
E       assert '3\nMind\nReality\nSpace' == '3\nReality\nSpace\nMind'
E           3
E         + Mind
E           Reality
E         - Space
E         ?      -
E         + Space
E         - Mind

tmpdebrs9di.py:27: AssertionError
______________________________ test_case[case16] _______________________________

i = 16, inp = '2\norange\nblue\n', expected = '4\nPower\nReality\nMind\nTime\n'

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
E       AssertionError: input='2\norange\nblue\n'
E         expected='4\nPower\nReality\nMind\nTime'
E         got='4\nMind\nPower\nReality\nTime'
E       assert '4\nMind\nPow...Reality\nTime' == '4\nPower\nRe...y\nMind\nTime'
E           4
E         + Mind
E           Power
E           Reality
E         - Mind
E           Time

tmpdebrs9di.py:27: AssertionError
______________________________ test_case[case17] _______________________________

i = 17, inp = '3\nblue\ngreen\norange\n', expected = '3\nMind\nReality\nPower\n'

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
E       AssertionError: input='3\nblue\ngreen\norange\n'
E         expected='3\nMind\nReality\nPower'
E         got='3\nMind\nPower\nReality'
E       assert '3\nMind\nPower\nReality' == '3\nMind\nReality\nPower'
E           3
E           Mind
E         + Power
E         - Reality
E         ?        -
E         + Reality
E         - Power

tmpdebrs9di.py:27: AssertionError
______________________________ test_case[case19] _______________________________

i = 19, inp = '1\nred\n', expected = '5\nSoul\nTime\nPower\nMind\nSpace\n'

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
E       AssertionError: input='1\nred\n'
E         expected='5\nSoul\nTime\nPower\nMind\nSpace'
E         got='5\nMind\nPower\nSoul\nSpace\nTime'
E       assert '5\nMind\nPow...\nSpace\nTime' == '5\nSoul\nTim...\nMind\nSpace'
E           5
E         + Mind
E         + Power
E           Soul
E         - Time
E         - Power
E         - Mind...
E         
E         ...Full output truncated (4 lines hidden), use '-vv' to show

tmpdebrs9di.py:27: AssertionError
______________________________ test_case[case20] _______________________________

i = 20, inp = '2\nred\npurple\n', expected = '4\nSoul\nMind\nSpace\nTime\n'

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
E       AssertionError: input='2\nred\npurple\n'
E         expected='4\nSoul\nMind\nSpace\nTime'
E         got='4\nMind\nSoul\nSpace\nTime'
E       assert '4\nMind\nSoul\nSpace\nTime' == '4\nSoul\nMind\nSpace\nTime'
E           4
E         + Mind
E           Soul
E         - Mind
E           Space
E           Time

tmpdebrs9di.py:27: AssertionError
______________________________ test_case[case21] _______________________________

i = 21, inp = '2\nred\ngreen\n', expected = '4\nSoul\nSpace\nPower\nMind\n'

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
E       AssertionError: input='2\nred\ngreen\n'
E         expected='4\nSoul\nSpace\nPower\nMind'
E         got='4\nMind\nPower\nSoul\nSpace'
E       assert '4\nMind\nPower\nSoul\nSpace' == '4\nSoul\nSpace\nPower\nMind'
E           4
E         + Mind
E         + Power
E           Soul
E         - Space
E         ?      -
E         + Space
E         - Power
E         - Mind

tmpdebrs9di.py:27: AssertionError
______________________________ test_case[case22] _______________________________

i = 22, inp = '3\nred\npurple\ngreen\n', expected = '3\nMind\nSpace\nSoul\n'

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
E       AssertionError: input='3\nred\npurple\ngreen\n'
E         expected='3\nMind\nSpace\nSoul'
E         got='3\nMind\nSoul\nSpace'
E       assert '3\nMind\nSoul\nSpace' == '3\nMind\nSpace\nSoul'
E           3
E           Mind
E         + Soul
E         - Space
E         ?      -
E         + Space
E         - Soul

tmpdebrs9di.py:27: AssertionError
______________________________ test_case[case23] _______________________________

i = 23, inp = '2\nblue\nred\n', expected = '4\nSoul\nTime\nPower\nMind\n'

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
E       AssertionError: input='2\nblue\nred\n'
E         expected='4\nSoul\nTime\nPower\nMind'
E         got='4\nMind\nPower\nSoul\nTime'
E       assert '4\nMind\nPower\nSoul\nTime' == '4\nSoul\nTime\nPower\nMind'
E           4
E         + Mind
E         + Power
E           Soul
E         - Time
E         ?     -
E         + Time
E         - Power
E         - Mind

tmpdebrs9di.py:27: AssertionError
______________________________ test_case[case24] _______________________________

i = 24, inp = '3\nred\nblue\npurple\n', expected = '3\nTime\nSoul\nMind\n'

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
E       AssertionError: input='3\nred\nblue\npurple\n'
E         expected='3\nTime\nSoul\nMind'
E         got='3\nMind\nSoul\nTime'
E       assert '3\nMind\nSoul\nTime' == '3\nTime\nSoul\nMind'
E           3
E         - Time
E         + Mind
E           Soul
E         - Mind
E         + Time

tmpdebrs9di.py:27: AssertionError
______________________________ test_case[case25] _______________________________

i = 25, inp = '3\nred\nblue\ngreen\n', expected = '3\nSoul\nMind\nPower\n'

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
E       AssertionError: input='3\nred\nblue\ngreen\n'
E         expected='3\nSoul\nMind\nPower'
E         got='3\nMind\nPower\nSoul'
E       assert '3\nMind\nPower\nSoul' == '3\nSoul\nMind\nPower'
E           3
E         - Soul
E           Mind
E         - Power
E         + Power
E         ?      +
E         + Soul

tmpdebrs9di.py:27: AssertionError
______________________________ test_case[case27] _______________________________

i = 27, inp = '2\norange\nred\n', expected = '4\nTime\nSpace\nMind\nPower\n'

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
E       AssertionError: input='2\norange\nred\n'
E         expected='4\nTime\nSpace\nMind\nPower'
E         got='4\nMind\nPower\nSpace\nTime'
E       assert '4\nMind\nPower\nSpace\nTime' == '4\nTime\nSpace\nMind\nPower'
E           4
E         - Time
E         + Mind
E         + Power
E           Space
E         + Time
E         - Mind
E         - Power

tmpdebrs9di.py:27: AssertionError
______________________________ test_case[case28] _______________________________

i = 28, inp = '3\nred\norange\npurple\n', expected = '3\nTime\nSpace\nMind\n'

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
E       AssertionError: input='3\nred\norange\npurple\n'
E         expected='3\nTime\nSpace\nMind'
E         got='3\nMind\nSpace\nTime'
E       assert '3\nMind\nSpace\nTime' == '3\nTime\nSpace\nMind'
E           3
E         - Time
E         + Mind
E           Space
E         - Mind
E         + Time

tmpdebrs9di.py:27: AssertionError
______________________________ test_case[case29] _______________________________

i = 29, inp = '3\nred\norange\ngreen\n', expected = '3\nPower\nMind\nSpace\n'

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
E       AssertionError: input='3\nred\norange\ngreen\n'
E         expected='3\nPower\nMind\nSpace'
E         got='3\nMind\nPower\nSpace'
E       assert '3\nMind\nPower\nSpace' == '3\nPower\nMind\nSpace'
E           3
E         + Mind
E           Power
E         - Mind
E           Space

tmpdebrs9di.py:27: AssertionError
______________________________ test_case[case30] _______________________________

i = 30, inp = '4\nred\norange\ngreen\npurple\n', expected = '2\nSpace\nMind\n'

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
E       AssertionError: input='4\nred\norange\ngreen\npurple\n'
E         expected='2\nSpace\nMind'
E         got='2\nMind\nSpace'
E       assert '2\nMind\nSpace' == '2\nSpace\nMind'
E           2
E         + Mind
E         - Space
E         ?      -
E         + Space
E         - Mind

tmpdebrs9di.py:27: AssertionError
______________________________ test_case[case31] _______________________________

i = 31, inp = '3\nblue\norange\nred\n', expected = '3\nPower\nMind\nTime\n'

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
E       AssertionError: input='3\nblue\norange\nred\n'
E         expected='3\nPower\nMind\nTime'
E         got='3\nMind\nPower\nTime'
E       assert '3\nMind\nPower\nTime' == '3\nPower\nMind\nTime'
E           3
E         + Mind
E           Power
E         - Mind
E           Time

tmpdebrs9di.py:27: AssertionError
______________________________ test_case[case33] _______________________________

i = 33, inp = '4\ngreen\norange\nred\nblue\n', expected = '2\nPower\nMind\n'

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
E       AssertionError: input='4\ngreen\norange\nred\nblue\n'
E         expected='2\nPower\nMind'
E         got='2\nMind\nPower'
E       assert '2\nMind\nPower' == '2\nPower\nMind'
E           2
E         + Mind
E         - Power
E         ?      -
E         + Power
E         - Mind

tmpdebrs9di.py:27: AssertionError
______________________________ test_case[case35] _______________________________

i = 35, inp = '1\nyellow\n', expected = '5\nSoul\nTime\nSpace\nReality\nPower\n'

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
E       AssertionError: input='1\nyellow\n'
E         expected='5\nSoul\nTime\nSpace\nReality\nPower'
E         got='5\nPower\nReality\nSoul\nSpace\nTime'
E       assert '5\nPower\nRe...\nSpace\nTime' == '5\nSoul\nTim...eality\nPower'
E           5
E         + Power
E         + Reality
E           Soul
E         - Time
E           Space
E         + Time
E         - Reality
E         - Power

tmpdebrs9di.py:27: AssertionError
______________________________ test_case[case36] _______________________________

i = 36, inp = '2\npurple\nyellow\n'
expected = '4\nReality\nSpace\nSoul\nTime\n'

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
E       AssertionError: input='2\npurple\nyellow\n'
E         expected='4\nReality\nSpace\nSoul\nTime'
E         got='4\nReality\nSoul\nSpace\nTime'
E       assert '4\nReality\n...\nSpace\nTime' == '4\nReality\n...e\nSoul\nTime'
E           4
E           Reality
E         + Soul
E           Space
E         - Soul
E           Time

tmpdebrs9di.py:27: AssertionError
______________________________ test_case[case37] _______________________________

i = 37, inp = '2\ngreen\nyellow\n'
expected = '4\nReality\nSoul\nPower\nSpace\n'

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
E       AssertionError: input='2\ngreen\nyellow\n'
E         expected='4\nReality\nSoul\nPower\nSpace'
E         got='4\nPower\nReality\nSoul\nSpace'
E       assert '4\nPower\nRe...\nSoul\nSpace' == '4\nReality\n...nPower\nSpace'
E           4
E         + Power
E           Reality
E           Soul
E         - Power
E           Space

tmpdebrs9di.py:27: AssertionError
______________________________ test_case[case39] _______________________________

i = 39, inp = '2\nblue\nyellow\n', expected = '4\nTime\nReality\nPower\nSoul\n'

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
E       AssertionError: input='2\nblue\nyellow\n'
E         expected='4\nTime\nReality\nPower\nSoul'
E         got='4\nPower\nReality\nSoul\nTime'
E       assert '4\nPower\nRe...y\nSoul\nTime' == '4\nTime\nRea...\nPower\nSoul'
E           4
E         - Time
E         + Power
E           Reality
E         - Power
E         - Soul
E         + Soul
E         ?     +
E         + Time

tmpdebrs9di.py:27: AssertionError
______________________________ test_case[case40] _______________________________

i = 40, inp = '3\nyellow\nblue\npurple\n', expected = '3\nTime\nSoul\nReality\n'

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
E       AssertionError: input='3\nyellow\nblue\npurple\n'
E         expected='3\nTime\nSoul\nReality'
E         got='3\nReality\nSoul\nTime'
E       assert '3\nReality\nSoul\nTime' == '3\nTime\nSoul\nReality'
E           3
E         - Time
E         + Reality
E           Soul
E         - Reality
E         + Time

tmpdebrs9di.py:27: AssertionError
______________________________ test_case[case41] _______________________________

i = 41, inp = '3\ngreen\nyellow\nblue\n', expected = '3\nPower\nSoul\nReality\n'

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
E       AssertionError: input='3\ngreen\nyellow\nblue\n'
E         expected='3\nPower\nSoul\nReality'
E         got='3\nPower\nReality\nSoul'
E       assert '3\nPower\nReality\nSoul' == '3\nPower\nSoul\nReality'
E           3
E           Power
E         - Soul
E         - Reality
E         + Reality
E         ?        +
E         + Soul

tmpdebrs9di.py:27: AssertionError
______________________________ test_case[case44] _______________________________

i = 44, inp = '3\nyellow\npurple\norange\n'
expected = '3\nSpace\nTime\nReality\n'

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
E       AssertionError: input='3\nyellow\npurple\norange\n'
E         expected='3\nSpace\nTime\nReality'
E         got='3\nReality\nSpace\nTime'
E       assert '3\nReality\nSpace\nTime' == '3\nSpace\nTime\nReality'
E           3
E         + Reality
E           Space
E         - Time
E         ?     -
E         + Time
E         - Reality

tmpdebrs9di.py:27: AssertionError
______________________________ test_case[case45] _______________________________

i = 45, inp = '3\norange\nyellow\ngreen\n'
expected = '3\nPower\nSpace\nReality\n'

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
E       AssertionError: input='3\norange\nyellow\ngreen\n'
E         expected='3\nPower\nSpace\nReality'
E         got='3\nPower\nReality\nSpace'
E       assert '3\nPower\nReality\nSpace' == '3\nPower\nSpace\nReality'
E           3
E           Power
E         - Space
E         - Reality
E         + Reality
E         ?        +
E         + Space

tmpdebrs9di.py:27: AssertionError
______________________________ test_case[case47] _______________________________

i = 47, inp = '3\nyellow\nblue\norange\n'
expected = '3\nTime\nReality\nPower\n'

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
E       AssertionError: input='3\nyellow\nblue\norange\n'
E         expected='3\nTime\nReality\nPower'
E         got='3\nPower\nReality\nTime'
E       assert '3\nPower\nReality\nTime' == '3\nTime\nReality\nPower'
E           3
E         - Time
E         + Power
E           Reality
E         - Power
E         + Time

tmpdebrs9di.py:27: AssertionError
______________________________ test_case[case49] _______________________________

i = 49, inp = '4\nblue\norange\nyellow\ngreen\n'
expected = '2\nReality\nPower\n'

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
E       AssertionError: input='4\nblue\norange\nyellow\ngreen\n'
E         expected='2\nReality\nPower'
E         got='2\nPower\nReality'
E       assert '2\nPower\nReality' == '2\nReality\nPower'
E           2
E         + Power
E         - Reality
E         ?        -
E         + Reality
E         - Power

tmpdebrs9di.py:27: AssertionError
______________________________ test_case[case52] _______________________________

i = 52, inp = '3\nred\ngreen\nyellow\n', expected = '3\nSpace\nPower\nSoul\n'

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
E       AssertionError: input='3\nred\ngreen\nyellow\n'
E         expected='3\nSpace\nPower\nSoul'
E         got='3\nPower\nSoul\nSpace'
E       assert '3\nPower\nSoul\nSpace' == '3\nSpace\nPower\nSoul'
E           3
E         - Space
E           Power
E         - Soul
E         + Soul
E         ?     +
E         + Space

tmpdebrs9di.py:27: AssertionError
______________________________ test_case[case54] _______________________________

i = 54, inp = '3\nred\nyellow\nblue\n', expected = '3\nSoul\nTime\nPower\n'

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
E       AssertionError: input='3\nred\nyellow\nblue\n'
E         expected='3\nSoul\nTime\nPower'
E         got='3\nPower\nSoul\nTime'
E       assert '3\nPower\nSoul\nTime' == '3\nSoul\nTime\nPower'
E           3
E         + Power
E           Soul
E         - Time
E         ?     -
E         + Time
E         - Power

tmpdebrs9di.py:27: AssertionError
=========================== short test summary info ============================
FAILED tmpdebrs9di.py::test_case[case0] - AssertionError: input='4\nred\npurp...
FAILED tmpdebrs9di.py::test_case[case1] - AssertionError: input='0\n'
FAILED tmpdebrs9di.py::test_case[case3] - AssertionError: input='1\npurple\n'
FAILED tmpdebrs9di.py::test_case[case4] - AssertionError: input='3\nblue\nora...
FAILED tmpdebrs9di.py::test_case[case5] - AssertionError: input='2\nyellow\nr...
FAILED tmpdebrs9di.py::test_case[case6] - AssertionError: input='1\ngreen\n'
FAILED tmpdebrs9di.py::test_case[case7] - AssertionError: input='2\npurple\ng...
FAILED tmpdebrs9di.py::test_case[case8] - AssertionError: input='1\nblue\n'
FAILED tmpdebrs9di.py::test_case[case9] - AssertionError: input='2\npurple\nb...
FAILED tmpdebrs9di.py::test_case[case10] - AssertionError: input='2\ngreen\nb...
FAILED tmpdebrs9di.py::test_case[case11] - AssertionError: input='3\npurple\n...
FAILED tmpdebrs9di.py::test_case[case12] - AssertionError: input='1\norange\n'
FAILED tmpdebrs9di.py::test_case[case13] - AssertionError: input='2\npurple\n...
FAILED tmpdebrs9di.py::test_case[case14] - AssertionError: input='2\norange\n...
FAILED tmpdebrs9di.py::test_case[case15] - AssertionError: input='3\norange\n...
FAILED tmpdebrs9di.py::test_case[case16] - AssertionError: input='2\norange\n...
FAILED tmpdebrs9di.py::test_case[case17] - AssertionError: input='3\nblue\ngr...
FAILED tmpdebrs9di.py::test_case[case19] - AssertionError: input='1\nred\n'
FAILED tmpdebrs9di.py::test_case[case20] - AssertionError: input='2\nred\npur...
FAILED tmpdebrs9di.py::test_case[case21] - AssertionError: input='2\nred\ngre...
FAILED tmpdebrs9di.py::test_case[case22] - AssertionError: input='3\nred\npur...
FAILED tmpdebrs9di.py::test_case[case23] - AssertionError: input='2\nblue\nre...
FAILED tmpdebrs9di.py::test_case[case24] - AssertionError: input='3\nred\nblu...
FAILED tmpdebrs9di.py::test_case[case25] - AssertionError: input='3\nred\nblu...
FAILED tmpdebrs9di.py::test_case[case27] - AssertionError: input='2\norange\n...
FAILED tmpdebrs9di.py::test_case[case28] - AssertionError: input='3\nred\nora...
FAILED tmpdebrs9di.py::test_case[case29] - AssertionError: input='3\nred\nora...
FAILED tmpdebrs9di.py::test_case[case30] - AssertionError: input='4\nred\nora...
FAILED tmpdebrs9di.py::test_case[case31] - AssertionError: input='3\nblue\nor...
FAILED tmpdebrs9di.py::test_case[case33] - AssertionError: input='4\ngreen\no...
FAILED tmpdebrs9di.py::test_case[case35] - AssertionError: input='1\nyellow\n'
FAILED tmpdebrs9di.py::test_case[case36] - AssertionError: input='2\npurple\n...
FAILED tmpdebrs9di.py::test_case[case37] - AssertionError: input='2\ngreen\ny...
FAILED tmpdebrs9di.py::test_case[case39] - AssertionError: input='2\nblue\nye...
FAILED tmpdebrs9di.py::test_case[case40] - AssertionError: input='3\nyellow\n...
FAILED tmpdebrs9di.py::test_case[case41] - AssertionError: input='3\ngreen\ny...
FAILED tmpdebrs9di.py::test_case[case44] - AssertionError: input='3\nyellow\n...
FAILED tmpdebrs9di.py::test_case[case45] - AssertionError: input='3\norange\n...
FAILED tmpdebrs9di.py::test_case[case47] - AssertionError: input='3\nyellow\n...
FAILED tmpdebrs9di.py::test_case[case49] - AssertionError: input='4\nblue\nor...
FAILED tmpdebrs9di.py::test_case[case52] - AssertionError: input='3\nred\ngre...
FAILED tmpdebrs9di.py::test_case[case54] - AssertionError: input='3\nred\nyel...
======================== 42 failed, 22 passed in 11.09s ========================
```
