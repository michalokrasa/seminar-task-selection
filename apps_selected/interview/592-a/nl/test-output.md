# interview/592-a

**Status:** FAIL (exit code 1)

## stdout

```
============================= test session starts ==============================
platform linux -- Python 3.10.18, pytest-7.4.4, pluggy-1.6.0
PyQt5 5.15.10 -- Qt runtime 5.15.17 -- Qt compiled 5.15.2
rootdir: /tmp/tmpmwevembs
configfile: pytest.ini
plugins: Faker-25.1.0, anyio-4.9.0, cov-5.0.0, mock-3.12.0, qt-4.3.1
collected 56 items

tmp3om7o9kj.py::test_case[case0] PASSED
tmp3om7o9kj.py::test_case[case1] FAILED
tmp3om7o9kj.py::test_case[case2] PASSED
tmp3om7o9kj.py::test_case[case3] PASSED
tmp3om7o9kj.py::test_case[case4] PASSED
tmp3om7o9kj.py::test_case[case5] PASSED
tmp3om7o9kj.py::test_case[case6] PASSED
tmp3om7o9kj.py::test_case[case7] PASSED
tmp3om7o9kj.py::test_case[case8] PASSED
tmp3om7o9kj.py::test_case[case9] PASSED
tmp3om7o9kj.py::test_case[case10] PASSED
tmp3om7o9kj.py::test_case[case11] PASSED
tmp3om7o9kj.py::test_case[case12] PASSED
tmp3om7o9kj.py::test_case[case13] PASSED
tmp3om7o9kj.py::test_case[case14] PASSED
tmp3om7o9kj.py::test_case[case15] PASSED
tmp3om7o9kj.py::test_case[case16] PASSED
tmp3om7o9kj.py::test_case[case17] PASSED
tmp3om7o9kj.py::test_case[case18] PASSED
tmp3om7o9kj.py::test_case[case19] PASSED
tmp3om7o9kj.py::test_case[case20] PASSED
tmp3om7o9kj.py::test_case[case21] PASSED
tmp3om7o9kj.py::test_case[case22] PASSED
tmp3om7o9kj.py::test_case[case23] PASSED
tmp3om7o9kj.py::test_case[case24] PASSED
tmp3om7o9kj.py::test_case[case25] PASSED
tmp3om7o9kj.py::test_case[case26] PASSED
tmp3om7o9kj.py::test_case[case27] PASSED
tmp3om7o9kj.py::test_case[case28] PASSED
tmp3om7o9kj.py::test_case[case29] PASSED
tmp3om7o9kj.py::test_case[case30] PASSED
tmp3om7o9kj.py::test_case[case31] PASSED
tmp3om7o9kj.py::test_case[case32] PASSED
tmp3om7o9kj.py::test_case[case33] PASSED
tmp3om7o9kj.py::test_case[case34] PASSED
tmp3om7o9kj.py::test_case[case35] PASSED
tmp3om7o9kj.py::test_case[case36] PASSED
tmp3om7o9kj.py::test_case[case37] PASSED
tmp3om7o9kj.py::test_case[case38] PASSED
tmp3om7o9kj.py::test_case[case39] FAILED
tmp3om7o9kj.py::test_case[case40] FAILED
tmp3om7o9kj.py::test_case[case41] FAILED
tmp3om7o9kj.py::test_case[case42] PASSED
tmp3om7o9kj.py::test_case[case43] PASSED
tmp3om7o9kj.py::test_case[case44] PASSED
tmp3om7o9kj.py::test_case[case45] PASSED
tmp3om7o9kj.py::test_case[case46] PASSED
tmp3om7o9kj.py::test_case[case47] PASSED
tmp3om7o9kj.py::test_case[case48] PASSED
tmp3om7o9kj.py::test_case[case49] FAILED
tmp3om7o9kj.py::test_case[case50] FAILED
tmp3om7o9kj.py::test_case[case51] FAILED
tmp3om7o9kj.py::test_case[case52] PASSED
tmp3om7o9kj.py::test_case[case53] PASSED
tmp3om7o9kj.py::test_case[case54] PASSED
tmp3om7o9kj.py::test_case[case55] FAILED

=================================== FAILURES ===================================
_______________________________ test_case[case1] _______________________________

i = 1
inp = '..B.....\n..W.....\n......B.\n........\n.....W..\n......B.\n........\n........\n'
expected = 'B\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='..B.....\n..W.....\n......B.\n........\n.....W..\n......B.\n........\n........\n'
E         expected='B'
E         got='A'
E       assert 'A' == 'B'
E         - B
E         + A

tmp3om7o9kj.py:27: AssertionError
______________________________ test_case[case39] _______________________________

i = 39
inp = 'BBBB.BBB\n.B....WB\nBB.B...B\nWWWW.WWB\nBB...BWW\nWWW..BBB\nW.BW.BB.\nWWWWWWW.\n'
expected = 'B\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='BBBB.BBB\n.B....WB\nBB.B...B\nWWWW.WWB\nBB...BWW\nWWW..BBB\nW.BW.BB.\nWWWWWWW.\n'
E         expected='B'
E         got='A'
E       assert 'A' == 'B'
E         - B
E         + A

tmp3om7o9kj.py:27: AssertionError
______________________________ test_case[case40] _______________________________

i = 40
inp = 'B.BBBBBB\nW.WWBBBW\nW.BB.WBB\nW.W.BBBW\nW.BWW.WB\nB..B..BB\nB.B.W.BB\nWWWWW.WW\n'
expected = 'B\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='B.BBBBBB\nW.WWBBBW\nW.BB.WBB\nW.W.BBBW\nW.BWW.WB\nB..B..BB\nB.B.W.BB\nWWWWW.WW\n'
E         expected='B'
E         got='A'
E       assert 'A' == 'B'
E         - B
E         + A

tmp3om7o9kj.py:27: AssertionError
______________________________ test_case[case41] _______________________________

i = 41
inp = 'BBBBBB.B\n.BBWBB.B\nWWW..B.W\n..WW.W.W\nBWB..W.W\n..BW.B.W\nB..B....\nWWWW.WWW\n'
expected = 'B\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='BBBBBB.B\n.BBWBB.B\nWWW..B.W\n..WW.W.W\nBWB..W.W\n..BW.B.W\nB..B....\nWWWW.WWW\n'
E         expected='B'
E         got='A'
E       assert 'A' == 'B'
E         - B
E         + A

tmp3om7o9kj.py:27: AssertionError
______________________________ test_case[case49] _______________________________

i = 49
inp = '........\nB.......\nW.......\n.......B\n........\n........\n........\n...W....\n'
expected = 'B\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='........\nB.......\nW.......\n.......B\n........\n........\n........\n...W....\n'
E         expected='B'
E         got='A'
E       assert 'A' == 'B'
E         - B
E         + A

tmp3om7o9kj.py:27: AssertionError
______________________________ test_case[case50] _______________________________

i = 50
inp = '........\n.B......\n.W......\n........\n....B...\n........\n........\n.......W\n'
expected = 'B\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='........\n.B......\n.W......\n........\n....B...\n........\n........\n.......W\n'
E         expected='B'
E         got='A'
E       assert 'A' == 'B'
E         - B
E         + A

tmp3om7o9kj.py:27: AssertionError
______________________________ test_case[case51] _______________________________

i = 51
inp = '........\n..B.....\n..W...B.\n........\n.....W..\n......B.\n........\n........\n'
expected = 'B\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='........\n..B.....\n..W...B.\n........\n.....W..\n......B.\n........\n........\n'
E         expected='B'
E         got='A'
E       assert 'A' == 'B'
E         - B
E         + A

tmp3om7o9kj.py:27: AssertionError
______________________________ test_case[case55] _______________________________

i = 55
inp = '........\nB.......\nW.......\n.W......\n........\nB.......\n........\n........\n'
expected = 'B\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='........\nB.......\nW.......\n.W......\n........\nB.......\n........\n........\n'
E         expected='B'
E         got='A'
E       assert 'A' == 'B'
E         - B
E         + A

tmp3om7o9kj.py:27: AssertionError
=========================== short test summary info ============================
FAILED tmp3om7o9kj.py::test_case[case1] - AssertionError: input='..B.....\n.....
FAILED tmp3om7o9kj.py::test_case[case39] - AssertionError: input='BBBB.BBB\n....
FAILED tmp3om7o9kj.py::test_case[case40] - AssertionError: input='B.BBBBBB\nW...
FAILED tmp3om7o9kj.py::test_case[case41] - AssertionError: input='BBBBBB.B\n....
FAILED tmp3om7o9kj.py::test_case[case49] - AssertionError: input='........\nB...
FAILED tmp3om7o9kj.py::test_case[case50] - AssertionError: input='........\n....
FAILED tmp3om7o9kj.py::test_case[case51] - AssertionError: input='........\n....
FAILED tmp3om7o9kj.py::test_case[case55] - AssertionError: input='........\nB...
========================= 8 failed, 48 passed in 9.51s =========================
```
