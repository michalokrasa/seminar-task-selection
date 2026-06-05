# competition/765-b

**Status:** FAIL (exit code 1)

## stdout

```
============================= test session starts ==============================
platform linux -- Python 3.10.18, pytest-7.4.4, pluggy-1.6.0
PyQt5 5.15.10 -- Qt runtime 5.15.17 -- Qt compiled 5.15.2
rootdir: /tmp/tmpw7792dyv
configfile: pytest.ini
plugins: Faker-25.1.0, anyio-4.9.0, cov-5.0.0, mock-3.12.0, qt-4.3.1
collected 59 items

tmpf_t3ojjm.py::test_case[case0] FAILED
tmpf_t3ojjm.py::test_case[case1] FAILED
tmpf_t3ojjm.py::test_case[case2] PASSED
tmpf_t3ojjm.py::test_case[case3] FAILED
tmpf_t3ojjm.py::test_case[case4] PASSED
tmpf_t3ojjm.py::test_case[case5] PASSED
tmpf_t3ojjm.py::test_case[case6] PASSED
tmpf_t3ojjm.py::test_case[case7] FAILED
tmpf_t3ojjm.py::test_case[case8] PASSED
tmpf_t3ojjm.py::test_case[case9] PASSED
tmpf_t3ojjm.py::test_case[case10] PASSED
tmpf_t3ojjm.py::test_case[case11] FAILED
tmpf_t3ojjm.py::test_case[case12] FAILED
tmpf_t3ojjm.py::test_case[case13] FAILED
tmpf_t3ojjm.py::test_case[case14] FAILED
tmpf_t3ojjm.py::test_case[case15] FAILED
tmpf_t3ojjm.py::test_case[case16] PASSED
tmpf_t3ojjm.py::test_case[case17] FAILED
tmpf_t3ojjm.py::test_case[case18] FAILED
tmpf_t3ojjm.py::test_case[case19] FAILED
tmpf_t3ojjm.py::test_case[case20] PASSED
tmpf_t3ojjm.py::test_case[case21] PASSED
tmpf_t3ojjm.py::test_case[case22] FAILED
tmpf_t3ojjm.py::test_case[case23] FAILED
tmpf_t3ojjm.py::test_case[case24] PASSED
tmpf_t3ojjm.py::test_case[case25] FAILED
tmpf_t3ojjm.py::test_case[case26] FAILED
tmpf_t3ojjm.py::test_case[case27] FAILED
tmpf_t3ojjm.py::test_case[case28] FAILED
tmpf_t3ojjm.py::test_case[case29] FAILED
tmpf_t3ojjm.py::test_case[case30] FAILED
tmpf_t3ojjm.py::test_case[case31] FAILED
tmpf_t3ojjm.py::test_case[case32] FAILED
tmpf_t3ojjm.py::test_case[case33] FAILED
tmpf_t3ojjm.py::test_case[case34] FAILED
tmpf_t3ojjm.py::test_case[case35] PASSED
tmpf_t3ojjm.py::test_case[case36] FAILED
tmpf_t3ojjm.py::test_case[case37] FAILED
tmpf_t3ojjm.py::test_case[case38] PASSED
tmpf_t3ojjm.py::test_case[case39] FAILED
tmpf_t3ojjm.py::test_case[case40] FAILED
tmpf_t3ojjm.py::test_case[case41] FAILED
tmpf_t3ojjm.py::test_case[case42] FAILED
tmpf_t3ojjm.py::test_case[case43] PASSED
tmpf_t3ojjm.py::test_case[case44] FAILED
tmpf_t3ojjm.py::test_case[case45] FAILED
tmpf_t3ojjm.py::test_case[case46] FAILED
tmpf_t3ojjm.py::test_case[case47] PASSED
tmpf_t3ojjm.py::test_case[case48] FAILED
tmpf_t3ojjm.py::test_case[case49] FAILED
tmpf_t3ojjm.py::test_case[case50] FAILED
tmpf_t3ojjm.py::test_case[case51] FAILED
tmpf_t3ojjm.py::test_case[case52] PASSED
tmpf_t3ojjm.py::test_case[case53] FAILED
tmpf_t3ojjm.py::test_case[case54] FAILED
tmpf_t3ojjm.py::test_case[case55] FAILED
tmpf_t3ojjm.py::test_case[case56] FAILED
tmpf_t3ojjm.py::test_case[case57] PASSED
tmpf_t3ojjm.py::test_case[case58] FAILED

=================================== FAILURES ===================================
_______________________________ test_case[case0] _______________________________

i = 0, inp = 'abacaba\n', expected = 'YES\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='abacaba\n'
E         expected='YES'
E         got='NO'
E       assert 'NO' == 'YES'
E         - YES
E         + NO

tmpf_t3ojjm.py:27: AssertionError
_______________________________ test_case[case1] _______________________________

i = 1, inp = 'jinotega\n', expected = 'NO\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='jinotega\n'
E         expected='NO'
E         got='YES'
E       assert 'YES' == 'NO'
E         - NO
E         + YES

tmpf_t3ojjm.py:27: AssertionError
_______________________________ test_case[case3] _______________________________

i = 3, inp = 'aba\n', expected = 'YES\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='aba\n'
E         expected='YES'
E         got='NO'
E       assert 'NO' == 'YES'
E         - YES
E         + NO

tmpf_t3ojjm.py:27: AssertionError
_______________________________ test_case[case7] _______________________________

i = 7, inp = 'fihyxmbnzq\n', expected = 'NO\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='fihyxmbnzq\n'
E         expected='NO'
E         got='YES'
E       assert 'YES' == 'NO'
E         - NO
E         + YES

tmpf_t3ojjm.py:27: AssertionError
______________________________ test_case[case11] _______________________________

i = 11, inp = 'bbbbbb\n', expected = 'NO\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='bbbbbb\n'
E         expected='NO'
E         got='YES'
E       assert 'YES' == 'NO'
E         - NO
E         + YES

tmpf_t3ojjm.py:27: AssertionError
______________________________ test_case[case12] _______________________________

i = 12, inp = 'aabbbd\n', expected = 'NO\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='aabbbd\n'
E         expected='NO'
E         got='YES'
E       assert 'YES' == 'NO'
E         - NO
E         + YES

tmpf_t3ojjm.py:27: AssertionError
______________________________ test_case[case13] _______________________________

i = 13, inp = 'abdefghijklmnopqrstuvwxyz\n', expected = 'NO\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='abdefghijklmnopqrstuvwxyz\n'
E         expected='NO'
E         got='YES'
E       assert 'YES' == 'NO'
E         - NO
E         + YES

tmpf_t3ojjm.py:27: AssertionError
______________________________ test_case[case14] _______________________________

i = 14, inp = 'abcdeghijklmnopqrstuvwxyz\n', expected = 'NO\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='abcdeghijklmnopqrstuvwxyz\n'
E         expected='NO'
E         got='YES'
E       assert 'YES' == 'NO'
E         - NO
E         + YES

tmpf_t3ojjm.py:27: AssertionError
______________________________ test_case[case15] _______________________________

i = 15, inp = 'abcdefghijklmnopqrsuvwxyz\n', expected = 'NO\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='abcdefghijklmnopqrsuvwxyz\n'
E         expected='NO'
E         got='YES'
E       assert 'YES' == 'NO'
E         - NO
E         + YES

tmpf_t3ojjm.py:27: AssertionError
______________________________ test_case[case17] _______________________________

i = 17, inp = 'abcdefghijklmnopqrsutvwxyz\n', expected = 'NO\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='abcdefghijklmnopqrsutvwxyz\n'
E         expected='NO'
E         got='YES'
E       assert 'YES' == 'NO'
E         - NO
E         + YES

tmpf_t3ojjm.py:27: AssertionError
______________________________ test_case[case18] _______________________________

i = 18, inp = 'acdef\n', expected = 'NO\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='acdef\n'
E         expected='NO'
E         got='YES'
E       assert 'YES' == 'NO'
E         - NO
E         + YES

tmpf_t3ojjm.py:27: AssertionError
______________________________ test_case[case19] _______________________________

i = 19, inp = 'z\n', expected = 'NO\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='z\n'
E         expected='NO'
E         got='YES'
E       assert 'YES' == 'NO'
E         - NO
E         + YES

tmpf_t3ojjm.py:27: AssertionError
______________________________ test_case[case22] _______________________________

i = 22
inp = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa...aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbbabbbabbaaabbaaaaabaabbaa\n'
expected = 'YES\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbbabbbabbaaabbaaaaabaabbaa\n'
E         expected='YES'
E         got='NO'
E       assert 'NO' == 'YES'
E         - YES
E         + NO

tmpf_t3ojjm.py:27: AssertionError
______________________________ test_case[case23] _______________________________

i = 23
inp = 'aababbabbaabbbbbaabababaabbbaaaaabbabbabbaabbbbabaabbaaababbaaacbbabbbbbbcbcababbccaaacbaccaccaababbccaacccaabaaccaaa...addddbaabbddbdabbdacbacbacaaaabbacadbcddddadaddabbdccaddbaaacbceebbceadbeaadecddbbbcaaecbdeaebaddbbdebbcbaabcacbdcdc\n'
expected = 'YES\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='aababbabbaabbbbbaabababaabbbaaaaabbabbabbaabbbbabaabbaaababbaaacbbabbbbbbcbcababbccaaacbaccaccaababbccaacccaabaaccaaabacacbaabacbaacbaaabcbbbcbbaacaabcbcbccbacabbcbabcaccaaaaaabcbacabcbabbbbbabccbbcacbaaabbccbbaaaaaaaaaaaadbbbabdacabdaddddbaabbddbdabbdacbacbacaaaabbacadbcddddadaddabbdccaddbaaacbceebbceadbeaadecddbbbcaaecbdeaebaddbbdebbcbaabcacbdcdc\n'
E         expected='YES'
E         got='NO'
E       assert 'NO' == 'YES'
E         - YES
E         + NO

tmpf_t3ojjm.py:27: AssertionError
______________________________ test_case[case25] _______________________________

i = 25, inp = 'b\n', expected = 'NO\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='b\n'
E         expected='NO'
E         got='YES'
E       assert 'YES' == 'NO'
E         - NO
E         + YES

tmpf_t3ojjm.py:27: AssertionError
______________________________ test_case[case26] _______________________________

i = 26, inp = 'ac\n', expected = 'NO\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='ac\n'
E         expected='NO'
E         got='YES'
E       assert 'YES' == 'NO'
E         - NO
E         + YES

tmpf_t3ojjm.py:27: AssertionError
______________________________ test_case[case27] _______________________________

i = 27, inp = 'cde\n', expected = 'NO\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='cde\n'
E         expected='NO'
E         got='YES'
E       assert 'YES' == 'NO'
E         - NO
E         + YES

tmpf_t3ojjm.py:27: AssertionError
______________________________ test_case[case28] _______________________________

i = 28, inp = 'abd\n', expected = 'NO\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='abd\n'
E         expected='NO'
E         got='YES'
E       assert 'YES' == 'NO'
E         - NO
E         + YES

tmpf_t3ojjm.py:27: AssertionError
______________________________ test_case[case29] _______________________________

i = 29, inp = 'zx\n', expected = 'NO\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='zx\n'
E         expected='NO'
E         got='YES'
E       assert 'YES' == 'NO'
E         - NO
E         + YES

tmpf_t3ojjm.py:27: AssertionError
______________________________ test_case[case30] _______________________________

i = 30, inp = 'bcd\n', expected = 'NO\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='bcd\n'
E         expected='NO'
E         got='YES'
E       assert 'YES' == 'NO'
E         - NO
E         + YES

tmpf_t3ojjm.py:27: AssertionError
______________________________ test_case[case31] _______________________________

i = 31, inp = 'aaac\n', expected = 'NO\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='aaac\n'
E         expected='NO'
E         got='YES'
E       assert 'YES' == 'NO'
E         - NO
E         + YES

tmpf_t3ojjm.py:27: AssertionError
______________________________ test_case[case32] _______________________________

i = 32, inp = 'aacb\n', expected = 'NO\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='aacb\n'
E         expected='NO'
E         got='YES'
E       assert 'YES' == 'NO'
E         - NO
E         + YES

tmpf_t3ojjm.py:27: AssertionError
______________________________ test_case[case33] _______________________________

i = 33, inp = 'acd\n', expected = 'NO\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='acd\n'
E         expected='NO'
E         got='YES'
E       assert 'YES' == 'NO'
E         - NO
E         + YES

tmpf_t3ojjm.py:27: AssertionError
______________________________ test_case[case34] _______________________________

i = 34
inp = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaz\n'
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
E       AssertionError: input='aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaz\n'
E         expected='NO'
E         got='YES'
E       assert 'YES' == 'NO'
E         - NO
E         + YES

tmpf_t3ojjm.py:27: AssertionError
______________________________ test_case[case36] _______________________________

i = 36, inp = 'bc\n', expected = 'NO\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='bc\n'
E         expected='NO'
E         got='YES'
E       assert 'YES' == 'NO'
E         - NO
E         + YES

tmpf_t3ojjm.py:27: AssertionError
______________________________ test_case[case37] _______________________________

i = 37, inp = 'aaaaaaaaad\n', expected = 'NO\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='aaaaaaaaad\n'
E         expected='NO'
E         got='YES'
E       assert 'YES' == 'NO'
E         - NO
E         + YES

tmpf_t3ojjm.py:27: AssertionError
______________________________ test_case[case39] _______________________________

i = 39, inp = 'abcb\n', expected = 'YES\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='abcb\n'
E         expected='YES'
E         got='NO'
E       assert 'NO' == 'YES'
E         - YES
E         + NO

tmpf_t3ojjm.py:27: AssertionError
______________________________ test_case[case40] _______________________________

i = 40, inp = 'aac\n', expected = 'NO\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='aac\n'
E         expected='NO'
E         got='YES'
E       assert 'YES' == 'NO'
E         - NO
E         + YES

tmpf_t3ojjm.py:27: AssertionError
______________________________ test_case[case41] _______________________________

i = 41, inp = 'abcbcb\n', expected = 'YES\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='abcbcb\n'
E         expected='YES'
E         got='NO'
E       assert 'NO' == 'YES'
E         - YES
E         + NO

tmpf_t3ojjm.py:27: AssertionError
______________________________ test_case[case42] _______________________________

i = 42, inp = 'bb\n', expected = 'NO\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='bb\n'
E         expected='NO'
E         got='YES'
E       assert 'YES' == 'NO'
E         - NO
E         + YES

tmpf_t3ojjm.py:27: AssertionError
______________________________ test_case[case44] _______________________________

i = 44, inp = 'bbb\n', expected = 'NO\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='bbb\n'
E         expected='NO'
E         got='YES'
E       assert 'YES' == 'NO'
E         - NO
E         + YES

tmpf_t3ojjm.py:27: AssertionError
______________________________ test_case[case45] _______________________________

i = 45, inp = 'x\n', expected = 'NO\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='x\n'
E         expected='NO'
E         got='YES'
E       assert 'YES' == 'NO'
E         - NO
E         + YES

tmpf_t3ojjm.py:27: AssertionError
______________________________ test_case[case46] _______________________________

i = 46
inp = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaazz\n'
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
E       AssertionError: input='aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaazz\n'
E         expected='NO'
E         got='YES'
E       assert 'YES' == 'NO'
E         - NO
E         + YES

tmpf_t3ojjm.py:27: AssertionError
______________________________ test_case[case48] _______________________________

i = 48, inp = 'za\n', expected = 'NO\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='za\n'
E         expected='NO'
E         got='YES'
E       assert 'YES' == 'NO'
E         - NO
E         + YES

tmpf_t3ojjm.py:27: AssertionError
______________________________ test_case[case49] _______________________________

i = 49, inp = 'ade\n', expected = 'NO\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='ade\n'
E         expected='NO'
E         got='YES'
E       assert 'YES' == 'NO'
E         - NO
E         + YES

tmpf_t3ojjm.py:27: AssertionError
______________________________ test_case[case50] _______________________________

i = 50, inp = 'bbbbbbbbbb\n', expected = 'NO\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='bbbbbbbbbb\n'
E         expected='NO'
E         got='YES'
E       assert 'YES' == 'NO'
E         - NO
E         + YES

tmpf_t3ojjm.py:27: AssertionError
______________________________ test_case[case51] _______________________________

i = 51, inp = 'bac\n', expected = 'NO\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='bac\n'
E         expected='NO'
E         got='YES'
E       assert 'YES' == 'NO'
E         - NO
E         + YES

tmpf_t3ojjm.py:27: AssertionError
______________________________ test_case[case53] _______________________________

i = 53, inp = 'aaacb\n', expected = 'NO\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='aaacb\n'
E         expected='NO'
E         got='YES'
E       assert 'YES' == 'NO'
E         - NO
E         + YES

tmpf_t3ojjm.py:27: AssertionError
______________________________ test_case[case54] _______________________________

i = 54, inp = 'aaaaac\n', expected = 'NO\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='aaaaac\n'
E         expected='NO'
E         got='YES'
E       assert 'YES' == 'NO'
E         - NO
E         + YES

tmpf_t3ojjm.py:27: AssertionError
______________________________ test_case[case55] _______________________________

i = 55, inp = 'aaaaaaaaaaad\n', expected = 'NO\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='aaaaaaaaaaad\n'
E         expected='NO'
E         got='YES'
E       assert 'YES' == 'NO'
E         - NO
E         + YES

tmpf_t3ojjm.py:27: AssertionError
______________________________ test_case[case56] _______________________________

i = 56, inp = 'c\n', expected = 'NO\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='c\n'
E         expected='NO'
E         got='YES'
E       assert 'YES' == 'NO'
E         - NO
E         + YES

tmpf_t3ojjm.py:27: AssertionError
______________________________ test_case[case58] _______________________________

i = 58, inp = 'aaaaaaac\n', expected = 'NO\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='aaaaaaac\n'
E         expected='NO'
E         got='YES'
E       assert 'YES' == 'NO'
E         - NO
E         + YES

tmpf_t3ojjm.py:27: AssertionError
=========================== short test summary info ============================
FAILED tmpf_t3ojjm.py::test_case[case0] - AssertionError: input='abacaba\n'
FAILED tmpf_t3ojjm.py::test_case[case1] - AssertionError: input='jinotega\n'
FAILED tmpf_t3ojjm.py::test_case[case3] - AssertionError: input='aba\n'
FAILED tmpf_t3ojjm.py::test_case[case7] - AssertionError: input='fihyxmbnzq\n'
FAILED tmpf_t3ojjm.py::test_case[case11] - AssertionError: input='bbbbbb\n'
FAILED tmpf_t3ojjm.py::test_case[case12] - AssertionError: input='aabbbd\n'
FAILED tmpf_t3ojjm.py::test_case[case13] - AssertionError: input='abdefghijkl...
FAILED tmpf_t3ojjm.py::test_case[case14] - AssertionError: input='abcdeghijkl...
FAILED tmpf_t3ojjm.py::test_case[case15] - AssertionError: input='abcdefghijk...
FAILED tmpf_t3ojjm.py::test_case[case17] - AssertionError: input='abcdefghijk...
FAILED tmpf_t3ojjm.py::test_case[case18] - AssertionError: input='acdef\n'
FAILED tmpf_t3ojjm.py::test_case[case19] - AssertionError: input='z\n'
FAILED tmpf_t3ojjm.py::test_case[case22] - AssertionError: input='aaaaaaaaaaa...
FAILED tmpf_t3ojjm.py::test_case[case23] - AssertionError: input='aababbabbaa...
FAILED tmpf_t3ojjm.py::test_case[case25] - AssertionError: input='b\n'
FAILED tmpf_t3ojjm.py::test_case[case26] - AssertionError: input='ac\n'
FAILED tmpf_t3ojjm.py::test_case[case27] - AssertionError: input='cde\n'
FAILED tmpf_t3ojjm.py::test_case[case28] - AssertionError: input='abd\n'
FAILED tmpf_t3ojjm.py::test_case[case29] - AssertionError: input='zx\n'
FAILED tmpf_t3ojjm.py::test_case[case30] - AssertionError: input='bcd\n'
FAILED tmpf_t3ojjm.py::test_case[case31] - AssertionError: input='aaac\n'
FAILED tmpf_t3ojjm.py::test_case[case32] - AssertionError: input='aacb\n'
FAILED tmpf_t3ojjm.py::test_case[case33] - AssertionError: input='acd\n'
FAILED tmpf_t3ojjm.py::test_case[case34] - AssertionError: input='aaaaaaaaaaa...
FAILED tmpf_t3ojjm.py::test_case[case36] - AssertionError: input='bc\n'
FAILED tmpf_t3ojjm.py::test_case[case37] - AssertionError: input='aaaaaaaaad\n'
FAILED tmpf_t3ojjm.py::test_case[case39] - AssertionError: input='abcb\n'
FAILED tmpf_t3ojjm.py::test_case[case40] - AssertionError: input='aac\n'
FAILED tmpf_t3ojjm.py::test_case[case41] - AssertionError: input='abcbcb\n'
FAILED tmpf_t3ojjm.py::test_case[case42] - AssertionError: input='bb\n'
FAILED tmpf_t3ojjm.py::test_case[case44] - AssertionError: input='bbb\n'
FAILED tmpf_t3ojjm.py::test_case[case45] - AssertionError: input='x\n'
FAILED tmpf_t3ojjm.py::test_case[case46] - AssertionError: input='aaaaaaaaaaa...
FAILED tmpf_t3ojjm.py::test_case[case48] - AssertionError: input='za\n'
FAILED tmpf_t3ojjm.py::test_case[case49] - AssertionError: input='ade\n'
FAILED tmpf_t3ojjm.py::test_case[case50] - AssertionError: input='bbbbbbbbbb\n'
FAILED tmpf_t3ojjm.py::test_case[case51] - AssertionError: input='bac\n'
FAILED tmpf_t3ojjm.py::test_case[case53] - AssertionError: input='aaacb\n'
FAILED tmpf_t3ojjm.py::test_case[case54] - AssertionError: input='aaaaac\n'
FAILED tmpf_t3ojjm.py::test_case[case55] - AssertionError: input='aaaaaaaaaaa...
FAILED tmpf_t3ojjm.py::test_case[case56] - AssertionError: input='c\n'
FAILED tmpf_t3ojjm.py::test_case[case58] - AssertionError: input='aaaaaaac\n'
======================== 42 failed, 17 passed in 9.94s =========================
```
