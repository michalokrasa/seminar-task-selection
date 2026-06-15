# interview/987-a

**Status:** FAIL (exit code 1)

## stdout

```
============================= test session starts ==============================
platform linux -- Python 3.10.18, pytest-7.4.4, pluggy-1.6.0
PyQt5 5.15.10 -- Qt runtime 5.15.17 -- Qt compiled 5.15.2
rootdir: /tmp/tmpzxsem7a7
configfile: pytest.ini
plugins: Faker-25.1.0, anyio-4.9.0, cov-5.0.0, mock-3.12.0, qt-4.3.1
collected 64 items

tmp9tcvffj6.py::test_case[case0] PASSED
tmp9tcvffj6.py::test_case[case1] FAILED
tmp9tcvffj6.py::test_case[case2] PASSED
tmp9tcvffj6.py::test_case[case3] FAILED
tmp9tcvffj6.py::test_case[case4] FAILED
tmp9tcvffj6.py::test_case[case5] FAILED
tmp9tcvffj6.py::test_case[case6] FAILED
tmp9tcvffj6.py::test_case[case7] FAILED
tmp9tcvffj6.py::test_case[case8] FAILED
tmp9tcvffj6.py::test_case[case9] FAILED
tmp9tcvffj6.py::test_case[case10] FAILED
tmp9tcvffj6.py::test_case[case11] PASSED
tmp9tcvffj6.py::test_case[case12] FAILED
tmp9tcvffj6.py::test_case[case13] PASSED
tmp9tcvffj6.py::test_case[case14] FAILED
tmp9tcvffj6.py::test_case[case15] FAILED
tmp9tcvffj6.py::test_case[case16] FAILED
tmp9tcvffj6.py::test_case[case17] FAILED
tmp9tcvffj6.py::test_case[case18] FAILED
tmp9tcvffj6.py::test_case[case19] FAILED
tmp9tcvffj6.py::test_case[case20] FAILED
tmp9tcvffj6.py::test_case[case21] FAILED
tmp9tcvffj6.py::test_case[case22] FAILED
tmp9tcvffj6.py::test_case[case23] FAILED
tmp9tcvffj6.py::test_case[case24] PASSED
tmp9tcvffj6.py::test_case[case25] FAILED
tmp9tcvffj6.py::test_case[case26] FAILED
tmp9tcvffj6.py::test_case[case27] FAILED
tmp9tcvffj6.py::test_case[case28] PASSED
tmp9tcvffj6.py::test_case[case29] FAILED
tmp9tcvffj6.py::test_case[case30] PASSED
tmp9tcvffj6.py::test_case[case31] FAILED
tmp9tcvffj6.py::test_case[case32] FAILED
tmp9tcvffj6.py::test_case[case33] PASSED
tmp9tcvffj6.py::test_case[case34] PASSED
tmp9tcvffj6.py::test_case[case35] FAILED
tmp9tcvffj6.py::test_case[case36] FAILED
tmp9tcvffj6.py::test_case[case37] FAILED
tmp9tcvffj6.py::test_case[case38] FAILED
tmp9tcvffj6.py::test_case[case39] FAILED
tmp9tcvffj6.py::test_case[case40] PASSED
tmp9tcvffj6.py::test_case[case41] PASSED
tmp9tcvffj6.py::test_case[case42] FAILED
tmp9tcvffj6.py::test_case[case43] FAILED
tmp9tcvffj6.py::test_case[case44] FAILED
tmp9tcvffj6.py::test_case[case45] PASSED
tmp9tcvffj6.py::test_case[case46] FAILED
tmp9tcvffj6.py::test_case[case47] FAILED
tmp9tcvffj6.py::test_case[case48] FAILED
tmp9tcvffj6.py::test_case[case49] FAILED
tmp9tcvffj6.py::test_case[case50] PASSED
tmp9tcvffj6.py::test_case[case51] FAILED
tmp9tcvffj6.py::test_case[case52] FAILED
tmp9tcvffj6.py::test_case[case53] FAILED
tmp9tcvffj6.py::test_case[case54] FAILED
tmp9tcvffj6.py::test_case[case55] FAILED
tmp9tcvffj6.py::test_case[case56] PASSED
tmp9tcvffj6.py::test_case[case57] PASSED
tmp9tcvffj6.py::test_case[case58] FAILED
tmp9tcvffj6.py::test_case[case59] PASSED
tmp9tcvffj6.py::test_case[case60] PASSED
tmp9tcvffj6.py::test_case[case61] PASSED
tmp9tcvffj6.py::test_case[case62] PASSED
tmp9tcvffj6.py::test_case[case63] PASSED

=================================== FAILURES ===================================
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
E         got='6\nPower\nTime\nSpace\nSoul\nReality\nMind'
E       assert '6\nPower\nTi...Reality\nMind' == '6\nReality\n...\nPower\nSoul'
E           6
E         + Power
E         + Time
E         + Space
E         + Soul
E           Reality
E         - Time...
E         
E         ...Full output truncated (6 lines hidden), use '-vv' to show

tmp9tcvffj6.py:27: AssertionError
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
E         got='5\nTime\nSpace\nSoul\nReality\nMind'
E       assert '5\nTime\nSpa...Reality\nMind' == '5\nMind\nSpa...y\nSoul\nTime'
E           5
E         - Mind
E         + Time
E           Space
E         + Soul
E           Reality
E         + Mind
E         - Soul
E         - Time

tmp9tcvffj6.py:27: AssertionError
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
E         got='3\nTime\nReality\nMind'
E       assert '3\nTime\nReality\nMind' == '3\nReality\nMind\nTime'
E           3
E         + Time
E           Reality
E         - Mind
E         ?     -
E         + Mind
E         - Time

tmp9tcvffj6.py:27: AssertionError
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
E         got='4\nPower\nTime\nSpace\nSoul'
E       assert '4\nPower\nTime\nSpace\nSoul' == '4\nTime\nPower\nSoul\nSpace'
E           4
E         + Power
E           Time
E         - Power
E         - Soul
E         - Space
E         + Space
E         ?      +
E         + Soul

tmp9tcvffj6.py:27: AssertionError
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
E         got='5\nPower\nSpace\nSoul\nReality\nMind'
E       assert '5\nPower\nSp...Reality\nMind' == '5\nReality\n...\nPower\nSoul'
E           5
E         + Power
E         + Space
E         + Soul
E           Reality
E         - Space
E         - Mind...
E         
E         ...Full output truncated (4 lines hidden), use '-vv' to show

tmp9tcvffj6.py:27: AssertionError
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
E         got='4\nSpace\nSoul\nReality\nMind'
E       assert '4\nSpace\nSo...Reality\nMind' == '4\nSpace\nRe...y\nSoul\nMind'
E           4
E           Space
E         + Soul
E           Reality
E         - Soul
E           Mind

tmp9tcvffj6.py:27: AssertionError
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
E         got='5\nPower\nTime\nSoul\nReality\nMind'
E       assert '5\nPower\nTi...Reality\nMind' == '5\nMind\nSou...ower\nReality'
E           5
E         - Mind
E         + Power
E         + Time
E           Soul
E         - Time
E         - Power...
E         
E         ...Full output truncated (4 lines hidden), use '-vv' to show

tmp9tcvffj6.py:27: AssertionError
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
E         got='4\nTime\nSoul\nReality\nMind'
E       assert '4\nTime\nSoul\nReality\nMind' == '4\nReality\nTime\nSoul\nMind'
E           4
E         - Reality
E           Time
E           Soul
E         + Reality
E           Mind

tmp9tcvffj6.py:27: AssertionError
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
E         got='4\nPower\nSoul\nReality\nMind'
E       assert '4\nPower\nSo...Reality\nMind' == '4\nPower\nMi...Soul\nReality'
E           4
E           Power
E         - Mind
E           Soul
E         - Reality
E         + Reality
E         ?        +
E         + Mind

tmp9tcvffj6.py:27: AssertionError
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
E         got='5\nPower\nTime\nSpace\nReality\nMind'
E       assert '5\nPower\nTi...Reality\nMind' == '5\nReality\n...\nMind\nPower'
E           5
E         - Reality
E         + Power
E           Time
E           Space
E         + Reality
E         - Mind...
E         
E         ...Full output truncated (3 lines hidden), use '-vv' to show

tmp9tcvffj6.py:27: AssertionError
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
E         got='4\nPower\nSpace\nReality\nMind'
E       assert '4\nPower\nSp...Reality\nMind' == '4\nMind\nRea...nSpace\nPower'
E           4
E         - Mind
E         + Power
E         + Space
E           Reality
E         + Mind
E         - Space
E         - Power

tmp9tcvffj6.py:27: AssertionError
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
E         got='3\nSpace\nReality\nMind'
E       assert '3\nSpace\nReality\nMind' == '3\nReality\nSpace\nMind'
E           3
E         + Space
E           Reality
E         - Space
E           Mind

tmp9tcvffj6.py:27: AssertionError
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
E         got='4\nPower\nTime\nReality\nMind'
E       assert '4\nPower\nTi...Reality\nMind' == '4\nPower\nRe...y\nMind\nTime'
E           4
E           Power
E         + Time
E           Reality
E         - Mind
E         ?     -
E         + Mind
E         - Time

tmp9tcvffj6.py:27: AssertionError
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
E         got='3\nPower\nReality\nMind'
E       assert '3\nPower\nReality\nMind' == '3\nMind\nReality\nPower'
E           3
E         - Mind
E         + Power
E           Reality
E         - Power
E         + Mind

tmp9tcvffj6.py:27: AssertionError
______________________________ test_case[case18] _______________________________

i = 18, inp = '4\nblue\norange\ngreen\npurple\n'
expected = '2\nMind\nReality\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='4\nblue\norange\ngreen\npurple\n'
E         expected='2\nMind\nReality'
E         got='2\nReality\nMind'
E       assert '2\nReality\nMind' == '2\nMind\nReality'
E           2
E         - Mind
E         - Reality
E         + Reality
E         ?        +
E         + Mind

tmp9tcvffj6.py:27: AssertionError
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
E         got='5\nPower\nTime\nSpace\nSoul\nMind'
E       assert '5\nPower\nTi...e\nSoul\nMind' == '5\nSoul\nTim...\nMind\nSpace'
E           5
E         + Power
E         + Time
E         + Space
E           Soul
E         - Time
E         - Power...
E         
E         ...Full output truncated (4 lines hidden), use '-vv' to show

tmp9tcvffj6.py:27: AssertionError
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
E         got='4\nTime\nSpace\nSoul\nMind'
E       assert '4\nTime\nSpace\nSoul\nMind' == '4\nSoul\nMind\nSpace\nTime'
E           4
E         + Time
E         + Space
E           Soul
E         - Mind
E         ?     -
E         + Mind
E         - Space
E         - Time

tmp9tcvffj6.py:27: AssertionError
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
E         got='4\nPower\nSpace\nSoul\nMind'
E       assert '4\nPower\nSpace\nSoul\nMind' == '4\nSoul\nSpace\nPower\nMind'
E           4
E         + Power
E         + Space
E           Soul
E         - Space
E         - Power
E           Mind

tmp9tcvffj6.py:27: AssertionError
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
E         got='3\nSpace\nSoul\nMind'
E       assert '3\nSpace\nSoul\nMind' == '3\nMind\nSpace\nSoul'
E           3
E         - Mind
E           Space
E         - Soul
E         + Soul
E         ?     +
E         + Mind

tmp9tcvffj6.py:27: AssertionError
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
E         got='4\nPower\nTime\nSoul\nMind'
E       assert '4\nPower\nTime\nSoul\nMind' == '4\nSoul\nTime\nPower\nMind'
E           4
E         + Power
E         + Time
E           Soul
E         - Time
E         - Power
E           Mind

tmp9tcvffj6.py:27: AssertionError
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
E         got='3\nPower\nSoul\nMind'
E       assert '3\nPower\nSoul\nMind' == '3\nSoul\nMind\nPower'
E           3
E         + Power
E           Soul
E         - Mind
E         ?     -
E         + Mind
E         - Power

tmp9tcvffj6.py:27: AssertionError
______________________________ test_case[case26] _______________________________

i = 26, inp = '4\npurple\nblue\ngreen\nred\n', expected = '2\nMind\nSoul\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='4\npurple\nblue\ngreen\nred\n'
E         expected='2\nMind\nSoul'
E         got='2\nSoul\nMind'
E       assert '2\nSoul\nMind' == '2\nMind\nSoul'
E           2
E         - Mind
E         - Soul
E         + Soul
E         ?     +
E         + Mind

tmp9tcvffj6.py:27: AssertionError
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
E         got='4\nPower\nTime\nSpace\nMind'
E       assert '4\nPower\nTime\nSpace\nMind' == '4\nTime\nSpace\nMind\nPower'
E           4
E         + Power
E           Time
E           Space
E         - Mind
E         ?     -
E         + Mind
E         - Power

tmp9tcvffj6.py:27: AssertionError
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
E         got='3\nPower\nSpace\nMind'
E       assert '3\nPower\nSpace\nMind' == '3\nPower\nMind\nSpace'
E           3
E           Power
E         - Mind
E         - Space
E         + Space
E         ?      +
E         + Mind

tmp9tcvffj6.py:27: AssertionError
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
E         got='3\nPower\nTime\nMind'
E       assert '3\nPower\nTime\nMind' == '3\nPower\nMind\nTime'
E           3
E           Power
E         - Mind
E         - Time
E         + Time
E         ?     +
E         + Mind

tmp9tcvffj6.py:27: AssertionError
______________________________ test_case[case32] _______________________________

i = 32, inp = '4\norange\nblue\npurple\nred\n', expected = '2\nMind\nTime\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='4\norange\nblue\npurple\nred\n'
E         expected='2\nMind\nTime'
E         got='2\nTime\nMind'
E       assert '2\nTime\nMind' == '2\nMind\nTime'
E           2
E         - Mind
E         - Time
E         + Time
E         ?     +
E         + Mind

tmp9tcvffj6.py:27: AssertionError
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
E         got='5\nPower\nTime\nSpace\nSoul\nReality'
E       assert '5\nPower\nTi...Soul\nReality' == '5\nSoul\nTim...eality\nPower'
E           5
E         - Soul
E         + Power
E           Time
E           Space
E         + Soul
E         - Reality...
E         
E         ...Full output truncated (3 lines hidden), use '-vv' to show

tmp9tcvffj6.py:27: AssertionError
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
E         got='4\nTime\nSpace\nSoul\nReality'
E       assert '4\nTime\nSpa...Soul\nReality' == '4\nReality\n...e\nSoul\nTime'
E           4
E         - Reality
E         + Time
E           Space
E           Soul
E         - Time
E         + Reality

tmp9tcvffj6.py:27: AssertionError
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
E         got='4\nPower\nSpace\nSoul\nReality'
E       assert '4\nPower\nSp...Soul\nReality' == '4\nReality\n...nPower\nSpace'
E           4
E         - Reality
E         + Power
E         + Space
E           Soul
E         + Reality
E         - Power
E         - Space

tmp9tcvffj6.py:27: AssertionError
______________________________ test_case[case38] _______________________________

i = 38, inp = '3\npurple\nyellow\ngreen\n'
expected = '3\nReality\nSoul\nSpace\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='3\npurple\nyellow\ngreen\n'
E         expected='3\nReality\nSoul\nSpace'
E         got='3\nSpace\nSoul\nReality'
E       assert '3\nSpace\nSoul\nReality' == '3\nReality\nSoul\nSpace'
E           3
E         - Reality
E         + Space
E           Soul
E         - Space
E         + Reality

tmp9tcvffj6.py:27: AssertionError
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
E         got='4\nPower\nTime\nSoul\nReality'
E       assert '4\nPower\nTi...Soul\nReality' == '4\nTime\nRea...\nPower\nSoul'
E           4
E         + Power
E           Time
E         + Soul
E         - Reality
E         ?        -
E         + Reality
E         - Power
E         - Soul

tmp9tcvffj6.py:27: AssertionError
______________________________ test_case[case42] _______________________________

i = 42, inp = '4\nyellow\nblue\ngreen\npurple\n'
expected = '2\nReality\nSoul\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='4\nyellow\nblue\ngreen\npurple\n'
E         expected='2\nReality\nSoul'
E         got='2\nSoul\nReality'
E       assert '2\nSoul\nReality' == '2\nReality\nSoul'
E           2
E         + Soul
E         - Reality
E         ?        -
E         + Reality
E         - Soul

tmp9tcvffj6.py:27: AssertionError
______________________________ test_case[case43] _______________________________

i = 43, inp = '2\nyellow\norange\n'
expected = '4\nPower\nReality\nSpace\nTime\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='2\nyellow\norange\n'
E         expected='4\nPower\nReality\nSpace\nTime'
E         got='4\nPower\nTime\nSpace\nReality'
E       assert '4\nPower\nTi...pace\nReality' == '4\nPower\nRe...\nSpace\nTime'
E           4
E           Power
E         - Reality
E         + Time
E           Space
E         - Time
E         + Reality

tmp9tcvffj6.py:27: AssertionError
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
E         got='3\nTime\nSpace\nReality'
E       assert '3\nTime\nSpace\nReality' == '3\nSpace\nTime\nReality'
E           3
E         + Time
E           Space
E         - Time
E           Reality

tmp9tcvffj6.py:27: AssertionError
______________________________ test_case[case46] _______________________________

i = 46, inp = '4\ngreen\nyellow\norange\npurple\n'
expected = '2\nReality\nSpace\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='4\ngreen\nyellow\norange\npurple\n'
E         expected='2\nReality\nSpace'
E         got='2\nSpace\nReality'
E       assert '2\nSpace\nReality' == '2\nReality\nSpace'
E           2
E         + Space
E         - Reality
E         ?        -
E         + Reality
E         - Space

tmp9tcvffj6.py:27: AssertionError
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
E         got='3\nPower\nTime\nReality'
E       assert '3\nPower\nTime\nReality' == '3\nTime\nReality\nPower'
E           3
E         + Power
E           Time
E         - Reality
E         ?        -
E         + Reality
E         - Power

tmp9tcvffj6.py:27: AssertionError
______________________________ test_case[case48] _______________________________

i = 48, inp = '4\norange\npurple\nblue\nyellow\n'
expected = '2\nReality\nTime\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='4\norange\npurple\nblue\nyellow\n'
E         expected='2\nReality\nTime'
E         got='2\nTime\nReality'
E       assert '2\nTime\nReality' == '2\nReality\nTime'
E           2
E         + Time
E         - Reality
E         ?        -
E         + Reality
E         - Time

tmp9tcvffj6.py:27: AssertionError
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

tmp9tcvffj6.py:27: AssertionError
______________________________ test_case[case51] _______________________________

i = 51, inp = '3\nyellow\npurple\nred\n', expected = '3\nSoul\nSpace\nTime\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='3\nyellow\npurple\nred\n'
E         expected='3\nSoul\nSpace\nTime'
E         got='3\nTime\nSpace\nSoul'
E       assert '3\nTime\nSpace\nSoul' == '3\nSoul\nSpace\nTime'
E           3
E         - Soul
E         + Time
E           Space
E         - Time
E         + Soul

tmp9tcvffj6.py:27: AssertionError
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
E         got='3\nPower\nSpace\nSoul'
E       assert '3\nPower\nSpace\nSoul' == '3\nSpace\nPower\nSoul'
E           3
E         + Power
E           Space
E         - Power
E           Soul

tmp9tcvffj6.py:27: AssertionError
______________________________ test_case[case53] _______________________________

i = 53, inp = '4\nred\npurple\ngreen\nyellow\n', expected = '2\nSoul\nSpace\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='4\nred\npurple\ngreen\nyellow\n'
E         expected='2\nSoul\nSpace'
E         got='2\nSpace\nSoul'
E       assert '2\nSpace\nSoul' == '2\nSoul\nSpace'
E           2
E         - Soul
E         - Space
E         + Space
E         ?      +
E         + Soul

tmp9tcvffj6.py:27: AssertionError
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
E         got='3\nPower\nTime\nSoul'
E       assert '3\nPower\nTime\nSoul' == '3\nSoul\nTime\nPower'
E           3
E         - Soul
E         + Power
E           Time
E         - Power
E         + Soul

tmp9tcvffj6.py:27: AssertionError
______________________________ test_case[case55] _______________________________

i = 55, inp = '4\nblue\nyellow\nred\npurple\n', expected = '2\nSoul\nTime\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='4\nblue\nyellow\nred\npurple\n'
E         expected='2\nSoul\nTime'
E         got='2\nTime\nSoul'
E       assert '2\nTime\nSoul' == '2\nSoul\nTime'
E           2
E         - Soul
E         - Time
E         + Time
E         ?     +
E         + Soul

tmp9tcvffj6.py:27: AssertionError
______________________________ test_case[case58] _______________________________

i = 58, inp = '3\nred\nyellow\norange\n', expected = '3\nPower\nSpace\nTime\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='3\nred\nyellow\norange\n'
E         expected='3\nPower\nSpace\nTime'
E         got='3\nPower\nTime\nSpace'
E       assert '3\nPower\nTime\nSpace' == '3\nPower\nSpace\nTime'
E           3
E           Power
E         + Time
E         - Space
E         ?      -
E         + Space
E         - Time

tmp9tcvffj6.py:27: AssertionError
=========================== short test summary info ============================
FAILED tmp9tcvffj6.py::test_case[case1] - AssertionError: input='0\n'
FAILED tmp9tcvffj6.py::test_case[case3] - AssertionError: input='1\npurple\n'
FAILED tmp9tcvffj6.py::test_case[case4] - AssertionError: input='3\nblue\nora...
FAILED tmp9tcvffj6.py::test_case[case5] - AssertionError: input='2\nyellow\nr...
FAILED tmp9tcvffj6.py::test_case[case6] - AssertionError: input='1\ngreen\n'
FAILED tmp9tcvffj6.py::test_case[case7] - AssertionError: input='2\npurple\ng...
FAILED tmp9tcvffj6.py::test_case[case8] - AssertionError: input='1\nblue\n'
FAILED tmp9tcvffj6.py::test_case[case9] - AssertionError: input='2\npurple\nb...
FAILED tmp9tcvffj6.py::test_case[case10] - AssertionError: input='2\ngreen\nb...
FAILED tmp9tcvffj6.py::test_case[case12] - AssertionError: input='1\norange\n'
FAILED tmp9tcvffj6.py::test_case[case14] - AssertionError: input='2\norange\n...
FAILED tmp9tcvffj6.py::test_case[case15] - AssertionError: input='3\norange\n...
FAILED tmp9tcvffj6.py::test_case[case16] - AssertionError: input='2\norange\n...
FAILED tmp9tcvffj6.py::test_case[case17] - AssertionError: input='3\nblue\ngr...
FAILED tmp9tcvffj6.py::test_case[case18] - AssertionError: input='4\nblue\nor...
FAILED tmp9tcvffj6.py::test_case[case19] - AssertionError: input='1\nred\n'
FAILED tmp9tcvffj6.py::test_case[case20] - AssertionError: input='2\nred\npur...
FAILED tmp9tcvffj6.py::test_case[case21] - AssertionError: input='2\nred\ngre...
FAILED tmp9tcvffj6.py::test_case[case22] - AssertionError: input='3\nred\npur...
FAILED tmp9tcvffj6.py::test_case[case23] - AssertionError: input='2\nblue\nre...
FAILED tmp9tcvffj6.py::test_case[case25] - AssertionError: input='3\nred\nblu...
FAILED tmp9tcvffj6.py::test_case[case26] - AssertionError: input='4\npurple\n...
FAILED tmp9tcvffj6.py::test_case[case27] - AssertionError: input='2\norange\n...
FAILED tmp9tcvffj6.py::test_case[case29] - AssertionError: input='3\nred\nora...
FAILED tmp9tcvffj6.py::test_case[case31] - AssertionError: input='3\nblue\nor...
FAILED tmp9tcvffj6.py::test_case[case32] - AssertionError: input='4\norange\n...
FAILED tmp9tcvffj6.py::test_case[case35] - AssertionError: input='1\nyellow\n'
FAILED tmp9tcvffj6.py::test_case[case36] - AssertionError: input='2\npurple\n...
FAILED tmp9tcvffj6.py::test_case[case37] - AssertionError: input='2\ngreen\ny...
FAILED tmp9tcvffj6.py::test_case[case38] - AssertionError: input='3\npurple\n...
FAILED tmp9tcvffj6.py::test_case[case39] - AssertionError: input='2\nblue\nye...
FAILED tmp9tcvffj6.py::test_case[case42] - AssertionError: input='4\nyellow\n...
FAILED tmp9tcvffj6.py::test_case[case43] - AssertionError: input='2\nyellow\n...
FAILED tmp9tcvffj6.py::test_case[case44] - AssertionError: input='3\nyellow\n...
FAILED tmp9tcvffj6.py::test_case[case46] - AssertionError: input='4\ngreen\ny...
FAILED tmp9tcvffj6.py::test_case[case47] - AssertionError: input='3\nyellow\n...
FAILED tmp9tcvffj6.py::test_case[case48] - AssertionError: input='4\norange\n...
FAILED tmp9tcvffj6.py::test_case[case49] - AssertionError: input='4\nblue\nor...
FAILED tmp9tcvffj6.py::test_case[case51] - AssertionError: input='3\nyellow\n...
FAILED tmp9tcvffj6.py::test_case[case52] - AssertionError: input='3\nred\ngre...
FAILED tmp9tcvffj6.py::test_case[case53] - AssertionError: input='4\nred\npur...
FAILED tmp9tcvffj6.py::test_case[case54] - AssertionError: input='3\nred\nyel...
FAILED tmp9tcvffj6.py::test_case[case55] - AssertionError: input='4\nblue\nye...
FAILED tmp9tcvffj6.py::test_case[case58] - AssertionError: input='3\nred\nyel...
======================== 44 failed, 20 passed in 11.11s ========================
```
