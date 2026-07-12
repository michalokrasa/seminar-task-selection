# interview/748-b

**Status:** FAIL (exit code 1)

## stdout

```
============================= test session starts ==============================
platform linux -- Python 3.10.18, pytest-7.4.4, pluggy-1.6.0
PyQt5 5.15.10 -- Qt runtime 5.15.17 -- Qt compiled 5.15.2
rootdir: /tmp/tmpna3yqr5k
configfile: pytest.ini
plugins: Faker-25.1.0, anyio-4.9.0, cov-5.0.0, mock-3.12.0, qt-4.3.1
collected 64 items

tmp88cnums4.py::test_case[case0] FAILED
tmp88cnums4.py::test_case[case1] FAILED
tmp88cnums4.py::test_case[case2] FAILED
tmp88cnums4.py::test_case[case3] FAILED
tmp88cnums4.py::test_case[case4] FAILED
tmp88cnums4.py::test_case[case5] FAILED
tmp88cnums4.py::test_case[case6] FAILED
tmp88cnums4.py::test_case[case7] FAILED
tmp88cnums4.py::test_case[case8] FAILED
tmp88cnums4.py::test_case[case9] FAILED
tmp88cnums4.py::test_case[case10] FAILED
tmp88cnums4.py::test_case[case11] FAILED
tmp88cnums4.py::test_case[case12] FAILED
tmp88cnums4.py::test_case[case13] FAILED
tmp88cnums4.py::test_case[case14] FAILED
tmp88cnums4.py::test_case[case15] FAILED
tmp88cnums4.py::test_case[case16] FAILED
tmp88cnums4.py::test_case[case17] FAILED
tmp88cnums4.py::test_case[case18] FAILED
tmp88cnums4.py::test_case[case19] FAILED
tmp88cnums4.py::test_case[case20] FAILED
tmp88cnums4.py::test_case[case21] FAILED
tmp88cnums4.py::test_case[case22] FAILED
tmp88cnums4.py::test_case[case23] FAILED
tmp88cnums4.py::test_case[case24] FAILED
tmp88cnums4.py::test_case[case25] FAILED
tmp88cnums4.py::test_case[case26] FAILED
tmp88cnums4.py::test_case[case27] FAILED
tmp88cnums4.py::test_case[case28] FAILED
tmp88cnums4.py::test_case[case29] FAILED
tmp88cnums4.py::test_case[case30] FAILED
tmp88cnums4.py::test_case[case31] FAILED
tmp88cnums4.py::test_case[case32] FAILED
tmp88cnums4.py::test_case[case33] FAILED
tmp88cnums4.py::test_case[case34] FAILED
tmp88cnums4.py::test_case[case35] FAILED
tmp88cnums4.py::test_case[case36] FAILED
tmp88cnums4.py::test_case[case37] FAILED
tmp88cnums4.py::test_case[case38] FAILED
tmp88cnums4.py::test_case[case39] FAILED
tmp88cnums4.py::test_case[case40] FAILED
tmp88cnums4.py::test_case[case41] FAILED
tmp88cnums4.py::test_case[case42] FAILED
tmp88cnums4.py::test_case[case43] FAILED
tmp88cnums4.py::test_case[case44] FAILED
tmp88cnums4.py::test_case[case45] FAILED
tmp88cnums4.py::test_case[case46] FAILED
tmp88cnums4.py::test_case[case47] FAILED
tmp88cnums4.py::test_case[case48] FAILED
tmp88cnums4.py::test_case[case49] FAILED
tmp88cnums4.py::test_case[case50] FAILED
tmp88cnums4.py::test_case[case51] FAILED
tmp88cnums4.py::test_case[case52] FAILED
tmp88cnums4.py::test_case[case53] FAILED
tmp88cnums4.py::test_case[case54] FAILED
tmp88cnums4.py::test_case[case55] FAILED
tmp88cnums4.py::test_case[case56] FAILED
tmp88cnums4.py::test_case[case57] FAILED
tmp88cnums4.py::test_case[case58] FAILED
tmp88cnums4.py::test_case[case59] FAILED
tmp88cnums4.py::test_case[case60] FAILED
tmp88cnums4.py::test_case[case61] FAILED
tmp88cnums4.py::test_case[case62] FAILED
tmp88cnums4.py::test_case[case63] FAILED

=================================== FAILURES ===================================
_______________________________ test_case[case0] _______________________________

i = 0, inp = 'helloworld\nehoolwlroz\n', expected = '3\nh e\nl o\nd z\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='helloworld\nehoolwlroz\n'
E         expected='3\nh e\nl o\nd z'
E         got=''
E       assert '' == '3\nh e\nl o\nd z'
E         - 3
E         - h e
E         - l o
E         - d z

tmp88cnums4.py:27: AssertionError
_______________________________ test_case[case1] _______________________________

i = 1, inp = 'hastalavistababy\nhastalavistababy\n', expected = '0\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='hastalavistababy\nhastalavistababy\n'
E         expected='0'
E         got=''
E       assert '' == '0'
E         - 0

tmp88cnums4.py:27: AssertionError
_______________________________ test_case[case2] _______________________________

i = 2, inp = 'merrychristmas\nchristmasmerry\n', expected = '-1\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='merrychristmas\nchristmasmerry\n'
E         expected='-1'
E         got=''
E       assert '' == '-1'
E         - -1

tmp88cnums4.py:27: AssertionError
_______________________________ test_case[case3] _______________________________

i = 3, inp = 'kusyvdgccw\nkusyvdgccw\n', expected = '0\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='kusyvdgccw\nkusyvdgccw\n'
E         expected='0'
E         got=''
E       assert '' == '0'
E         - 0

tmp88cnums4.py:27: AssertionError
_______________________________ test_case[case4] _______________________________

i = 4, inp = 'bbbbbabbab\naaaaabaaba\n', expected = '1\nb a\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='bbbbbabbab\naaaaabaaba\n'
E         expected='1\nb a'
E         got=''
E       assert '' == '1\nb a'
E         - 1
E         - b a

tmp88cnums4.py:27: AssertionError
_______________________________ test_case[case5] _______________________________

i = 5, inp = 'zzzzzzzzzzzzzzzzzzzzz\nqwertyuiopasdfghjklzx\n', expected = '-1\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='zzzzzzzzzzzzzzzzzzzzz\nqwertyuiopasdfghjklzx\n'
E         expected='-1'
E         got=''
E       assert '' == '-1'
E         - -1

tmp88cnums4.py:27: AssertionError
_______________________________ test_case[case6] _______________________________

i = 6, inp = 'accdccdcdccacddbcacc\naccbccbcbccacbbdcacc\n'
expected = '1\nd b\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='accdccdcdccacddbcacc\naccbccbcbccacbbdcacc\n'
E         expected='1\nd b'
E         got=''
E       assert '' == '1\nd b'
E         - 1
E         - d b

tmp88cnums4.py:27: AssertionError
_______________________________ test_case[case7] _______________________________

i = 7
inp = 'giiibdbebjdaihdghahccdeffjhfgidfbdhjdggajfgaidadjd\ngiiibdbebjdaihdghahccdeffjhfgidfbdhjdggajfgaidadjd\n'
expected = '0\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='giiibdbebjdaihdghahccdeffjhfgidfbdhjdggajfgaidadjd\ngiiibdbebjdaihdghahccdeffjhfgidfbdhjdggajfgaidadjd\n'
E         expected='0'
E         got=''
E       assert '' == '0'
E         - 0

tmp88cnums4.py:27: AssertionError
_______________________________ test_case[case8] _______________________________

i = 8
inp = 'gndggadlmdefgejidmmcglbjdcmglncfmbjjndjcibnjbabfab\nfihffahlmhogfojnhmmcflkjhcmflicgmkjjihjcnkijkakgak\n'
expected = '5\ng f\nn i\nd h\ne o\nb k\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='gndggadlmdefgejidmmcglbjdcmglncfmbjjndjcibnjbabfab\nfihffahlmhogfojnhmmcflkjhcmflicgmkjjihjcnkijkakgak\n'
E         expected='5\ng f\nn i\nd h\ne o\nb k'
E         got=''
E       assert '' == '5\ng f\nn i\nd h\ne o\nb k'
E         - 5
E         - g f
E         - n i
E         - d h
E         - e o
E         - b k

tmp88cnums4.py:27: AssertionError
_______________________________ test_case[case9] _______________________________

i = 9
inp = 'ijpanyhovzwjjxsvaiyhchfaulcsdgfszjnwtoqbtaqygfmxuwvynvlhqhvmkjbooklxfhmqlqvfoxlnoclfxtbhvnkmhjcmrsdc\nijpanyhovzwjjxsvaiyhchfaulcsdgfszjnwtoqbtaqygfmxuwvynvlhqhvmkjbooklxfhmqlqvfoxlnoclfxtbhvnkmhjcmrsdc\n'
expected = '0\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='ijpanyhovzwjjxsvaiyhchfaulcsdgfszjnwtoqbtaqygfmxuwvynvlhqhvmkjbooklxfhmqlqvfoxlnoclfxtbhvnkmhjcmrsdc\nijpanyhovzwjjxsvaiyhchfaulcsdgfszjnwtoqbtaqygfmxuwvynvlhqhvmkjbooklxfhmqlqvfoxlnoclfxtbhvnkmhjcmrsdc\n'
E         expected='0'
E         got=''
E       assert '' == '0'
E         - 0

tmp88cnums4.py:27: AssertionError
______________________________ test_case[case10] _______________________________

i = 10, inp = 'ab\naa\n', expected = '-1\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='ab\naa\n'
E         expected='-1'
E         got=''
E       assert '' == '-1'
E         - -1

tmp88cnums4.py:27: AssertionError
______________________________ test_case[case11] _______________________________

i = 11, inp = 'a\nz\n', expected = '1\na z\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='a\nz\n'
E         expected='1\na z'
E         got=''
E       assert '' == '1\na z'
E         - 1
E         - a z

tmp88cnums4.py:27: AssertionError
______________________________ test_case[case12] _______________________________

i = 12, inp = 'zz\nzy\n', expected = '-1\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='zz\nzy\n'
E         expected='-1'
E         got=''
E       assert '' == '-1'
E         - -1

tmp88cnums4.py:27: AssertionError
______________________________ test_case[case13] _______________________________

i = 13, inp = 'as\ndf\n', expected = '2\na d\ns f\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='as\ndf\n'
E         expected='2\na d\ns f'
E         got=''
E       assert '' == '2\na d\ns f'
E         - 2
E         - a d
E         - s f

tmp88cnums4.py:27: AssertionError
______________________________ test_case[case14] _______________________________

i = 14, inp = 'abc\nbca\n', expected = '-1\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='abc\nbca\n'
E         expected='-1'
E         got=''
E       assert '' == '-1'
E         - -1

tmp88cnums4.py:27: AssertionError
______________________________ test_case[case15] _______________________________

i = 15, inp = 'rtfg\nrftg\n', expected = '1\nt f\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='rtfg\nrftg\n'
E         expected='1\nt f'
E         got=''
E       assert '' == '1\nt f'
E         - 1
E         - t f

tmp88cnums4.py:27: AssertionError
______________________________ test_case[case16] _______________________________

i = 16, inp = 'y\ny\n', expected = '0\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='y\ny\n'
E         expected='0'
E         got=''
E       assert '' == '0'
E         - 0

tmp88cnums4.py:27: AssertionError
______________________________ test_case[case17] _______________________________

i = 17, inp = 'qwertyuiopasdfghjklzx\nzzzzzzzzzzzzzzzzzzzzz\n'
expected = '-1\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='qwertyuiopasdfghjklzx\nzzzzzzzzzzzzzzzzzzzzz\n'
E         expected='-1'
E         got=''
E       assert '' == '-1'
E         - -1

tmp88cnums4.py:27: AssertionError
______________________________ test_case[case18] _______________________________

i = 18, inp = 'qazwsxedcrfvtgbyhnujmik\nqwertyuiasdfghjkzxcvbnm\n'
expected = '-1\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='qazwsxedcrfvtgbyhnujmik\nqwertyuiasdfghjkzxcvbnm\n'
E         expected='-1'
E         got=''
E       assert '' == '-1'
E         - -1

tmp88cnums4.py:27: AssertionError
______________________________ test_case[case19] _______________________________

i = 19, inp = 'aaaaaa\nabcdef\n', expected = '-1\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='aaaaaa\nabcdef\n'
E         expected='-1'
E         got=''
E       assert '' == '-1'
E         - -1

tmp88cnums4.py:27: AssertionError
______________________________ test_case[case20] _______________________________

i = 20, inp = 'qwerty\nffffff\n', expected = '-1\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='qwerty\nffffff\n'
E         expected='-1'
E         got=''
E       assert '' == '-1'
E         - -1

tmp88cnums4.py:27: AssertionError
______________________________ test_case[case21] _______________________________

i = 21
inp = 'dofbgdppdvmwjwtdyphhmqliydxyjfxoopxiscevowleccmhwybsxitvujkfliamvqinlrpytyaqdlbywccprukoisyaseibuqbfqjcabkieimsggsakp...scevowleccmhwybsxitvujkfliamvqinlrpytyaqdlbywccprukoisyaseibuqbfqjcabkieimsggsakpnqliwhehnemewhychqrfiuyaecoydnromrh\n'
expected = '0\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='dofbgdppdvmwjwtdyphhmqliydxyjfxoopxiscevowleccmhwybsxitvujkfliamvqinlrpytyaqdlbywccprukoisyaseibuqbfqjcabkieimsggsakpnqliwhehnemewhychqrfiuyaecoydnromrh\ndofbgdppdvmwjwtdyphhmqliydxyjfxoopxiscevowleccmhwybsxitvujkfliamvqinlrpytyaqdlbywccprukoisyaseibuqbfqjcabkieimsggsakpnqliwhehnemewhychqrfiuyaecoydnromrh\n'
E         expected='0'
E         got=''
E       assert '' == '0'
E         - 0

tmp88cnums4.py:27: AssertionError
______________________________ test_case[case22] _______________________________

i = 22
inp = 'acdbccddadbcbabbebbaebdcedbbcebeaccecdabadeabeecbacacdcbccedeadadedeccedecdaabcedccccbbcbcedcaccdede\ndcbaccbbdbacadaaeaadeabcebaaceaedccecbdadbedaeecadcdcbcaccebedbdbebeccebecbddacebccccaacacebcdccbebe\n'
expected = '-1\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='acdbccddadbcbabbebbaebdcedbbcebeaccecdabadeabeecbacacdcbccedeadadedeccedecdaabcedccccbbcbcedcaccdede\ndcbaccbbdbacadaaeaadeabcebaaceaedccecbdadbedaeecadcdcbcaccebedbdbebeccebecbddacebccccaacacebcdccbebe\n'
E         expected='-1'
E         got=''
E       assert '' == '-1'
E         - -1

tmp88cnums4.py:27: AssertionError
______________________________ test_case[case23] _______________________________

i = 23, inp = 'bacccbbacabbcaacbbba\nbacccbbacabbcaacbbba\n', expected = '0\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='bacccbbacabbcaacbbba\nbacccbbacabbcaacbbba\n'
E         expected='0'
E         got=''
E       assert '' == '0'
E         - 0

tmp88cnums4.py:27: AssertionError
______________________________ test_case[case24] _______________________________

i = 24, inp = 'dbadbddddb\nacbacaaaac\n', expected = '-1\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='dbadbddddb\nacbacaaaac\n'
E         expected='-1'
E         got=''
E       assert '' == '-1'
E         - -1

tmp88cnums4.py:27: AssertionError
______________________________ test_case[case25] _______________________________

i = 25, inp = 'dacbdbbbdd\nadbdadddaa\n', expected = '-1\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='dacbdbbbdd\nadbdadddaa\n'
E         expected='-1'
E         got=''
E       assert '' == '-1'
E         - -1

tmp88cnums4.py:27: AssertionError
______________________________ test_case[case26] _______________________________

i = 26, inp = 'bbbbcbcbbc\ndaddbabddb\n', expected = '-1\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='bbbbcbcbbc\ndaddbabddb\n'
E         expected='-1'
E         got=''
E       assert '' == '-1'
E         - -1

tmp88cnums4.py:27: AssertionError
______________________________ test_case[case27] _______________________________

i = 27, inp = 'dddddbcdbd\nbcbbbdacdb\n', expected = '-1\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='dddddbcdbd\nbcbbbdacdb\n'
E         expected='-1'
E         got=''
E       assert '' == '-1'
E         - -1

tmp88cnums4.py:27: AssertionError
______________________________ test_case[case28] _______________________________

i = 28, inp = 'cbadcbcdaa\nabbbababbb\n', expected = '-1\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='cbadcbcdaa\nabbbababbb\n'
E         expected='-1'
E         got=''
E       assert '' == '-1'
E         - -1

tmp88cnums4.py:27: AssertionError
______________________________ test_case[case29] _______________________________

i = 29
inp = 'dmkgadidjgdjikgkehhfkhgkeamhdkfemikkjhhkdjfaenmkdgenijinamngjgkmgmmedfdehkhdigdnnkhmdkdindhkhndnakdgdhkdefagkedndnije...ecmggcimkahfdeinhflmlfadfnmncdnddhbkbhgejblnbffcgdbeilfigegfifaebnijeihkanehififlmhcbdcikhieghenbejneldkhaebjggncckk\n'
expected = '-1\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='dmkgadidjgdjikgkehhfkhgkeamhdkfemikkjhhkdjfaenmkdgenijinamngjgkmgmmedfdehkhdigdnnkhmdkdindhkhndnakdgdhkdefagkedndnijekdmkdfedkhekgdkhgkimfeakdhhhgkkff\nbdenailbmnbmlcnehjjkcgnehadgickhdlecmggcimkahfdeinhflmlfadfnmncdnddhbkbhgejblnbffcgdbeilfigegfifaebnijeihkanehififlmhcbdcikhieghenbejneldkhaebjggncckk\n'
E         expected='-1'
E         got=''
E       assert '' == '-1'
E         - -1

tmp88cnums4.py:27: AssertionError
______________________________ test_case[case30] _______________________________

i = 30, inp = 'acbbccabaa\nabbbbbabaa\n', expected = '-1\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='acbbccabaa\nabbbbbabaa\n'
E         expected='-1'
E         got=''
E       assert '' == '-1'
E         - -1

tmp88cnums4.py:27: AssertionError
______________________________ test_case[case31] _______________________________

i = 31, inp = 'ccccaccccc\naaaabaaaac\n', expected = '-1\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='ccccaccccc\naaaabaaaac\n'
E         expected='-1'
E         got=''
E       assert '' == '-1'
E         - -1

tmp88cnums4.py:27: AssertionError
______________________________ test_case[case32] _______________________________

i = 32, inp = 'acbacacbbb\nacbacacbbb\n', expected = '0\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='acbacacbbb\nacbacacbbb\n'
E         expected='0'
E         got=''
E       assert '' == '0'
E         - 0

tmp88cnums4.py:27: AssertionError
______________________________ test_case[case33] _______________________________

i = 33, inp = 'abbababbcc\nccccccccbb\n', expected = '-1\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='abbababbcc\nccccccccbb\n'
E         expected='-1'
E         got=''
E       assert '' == '-1'
E         - -1

tmp88cnums4.py:27: AssertionError
______________________________ test_case[case34] _______________________________

i = 34
inp = 'jbcbbjiifdcbeajgdeabddbfcecafejddcigfcaedbgicjihifgbahjihcjefgabgbccdiibfjgacehbbdjceacdbdeaiibaicih\nhhihhhddcfihddhjfddhffhcididcdhffidjciddfhjdihdhdcjhdhhdhihdcjdhjhiifddhchjdidhhhfhiddifhfddddhddidh\n'
expected = '-1\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='jbcbbjiifdcbeajgdeabddbfcecafejddcigfcaedbgicjihifgbahjihcjefgabgbccdiibfjgacehbbdjceacdbdeaiibaicih\nhhihhhddcfihddhjfddhffhcididcdhffidjciddfhjdihdhdcjhdhhdhihdcjdhjhiifddhchjdidhhhfhiddifhfddddhddidh\n'
E         expected='-1'
E         got=''
E       assert '' == '-1'
E         - -1

tmp88cnums4.py:27: AssertionError
______________________________ test_case[case35] _______________________________

i = 35
inp = 'ahaeheedefeehahfefhjhhedheeeedhehhfhdejdhffhhejhhhejadhefhahhadjjhdhheeeehfdaffhhefehhhefhhhhehehjda\neiefbdfgdhffieihfhjajifgjddffgifjbhigfagjhhjicaijbdaegidhiejiegaabgjidcfcjhgehhjjchcbjjdhjbiidjdjage\n'
expected = '-1\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='ahaeheedefeehahfefhjhhedheeeedhehhfhdejdhffhhejhhhejadhefhahhadjjhdhheeeehfdaffhhefehhhefhhhhehehjda\neiefbdfgdhffieihfhjajifgjddffgifjbhigfagjhhjicaijbdaegidhiejiegaabgjidcfcjhgehhjjchcbjjdhjbiidjdjage\n'
E         expected='-1'
E         got=''
E       assert '' == '-1'
E         - -1

tmp88cnums4.py:27: AssertionError
______________________________ test_case[case36] _______________________________

i = 36
inp = 'fficficbidbcbfaddifbffdbbiaccbbciiaidbcbbiadcccbccbbaibabcbbdbcibcciibiccfifbiiicadibbiaafadacdficbc\nddjhdghbgcbhadeccjdbddcbfjeiiaaigjejcaiabgechiiahibfejbeahafcfhjbihgjfgihdgdagjjhecjafjeedecehcdjhai\n'
expected = '-1\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='fficficbidbcbfaddifbffdbbiaccbbciiaidbcbbiadcccbccbbaibabcbbdbcibcciibiccfifbiiicadibbiaafadacdficbc\nddjhdghbgcbhadeccjdbddcbfjeiiaaigjejcaiabgechiiahibfejbeahafcfhjbihgjfgihdgdagjjhecjafjeedecehcdjhai\n'
E         expected='-1'
E         got=''
E       assert '' == '-1'
E         - -1

tmp88cnums4.py:27: AssertionError
______________________________ test_case[case37] _______________________________

i = 37, inp = 'z\nz\n', expected = '0\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='z\nz\n'
E         expected='0'
E         got=''
E       assert '' == '0'
E         - 0

tmp88cnums4.py:27: AssertionError
______________________________ test_case[case38] _______________________________

i = 38, inp = 'a\nz\n', expected = '1\na z\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='a\nz\n'
E         expected='1\na z'
E         got=''
E       assert '' == '1\na z'
E         - 1
E         - a z

tmp88cnums4.py:27: AssertionError
______________________________ test_case[case39] _______________________________

i = 39, inp = 'z\na\n', expected = '1\nz a\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='z\na\n'
E         expected='1\nz a'
E         got=''
E       assert '' == '1\nz a'
E         - 1
E         - z a

tmp88cnums4.py:27: AssertionError
______________________________ test_case[case40] _______________________________

i = 40, inp = 'aa\nzz\n', expected = '1\na z\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='aa\nzz\n'
E         expected='1\na z'
E         got=''
E       assert '' == '1\na z'
E         - 1
E         - a z

tmp88cnums4.py:27: AssertionError
______________________________ test_case[case41] _______________________________

i = 41, inp = 'az\nza\n', expected = '1\na z\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='az\nza\n'
E         expected='1\na z'
E         got=''
E       assert '' == '1\na z'
E         - 1
E         - a z

tmp88cnums4.py:27: AssertionError
______________________________ test_case[case42] _______________________________

i = 42, inp = 'aa\nza\n', expected = '-1\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='aa\nza\n'
E         expected='-1'
E         got=''
E       assert '' == '-1'
E         - -1

tmp88cnums4.py:27: AssertionError
______________________________ test_case[case43] _______________________________

i = 43, inp = 'za\nzz\n', expected = '-1\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='za\nzz\n'
E         expected='-1'
E         got=''
E       assert '' == '-1'
E         - -1

tmp88cnums4.py:27: AssertionError
______________________________ test_case[case44] _______________________________

i = 44, inp = 'aa\nab\n', expected = '-1\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='aa\nab\n'
E         expected='-1'
E         got=''
E       assert '' == '-1'
E         - -1

tmp88cnums4.py:27: AssertionError
______________________________ test_case[case45] _______________________________

i = 45, inp = 'hehe\nheeh\n', expected = '-1\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='hehe\nheeh\n'
E         expected='-1'
E         got=''
E       assert '' == '-1'
E         - -1

tmp88cnums4.py:27: AssertionError
______________________________ test_case[case46] _______________________________

i = 46, inp = 'bd\ncc\n', expected = '-1\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='bd\ncc\n'
E         expected='-1'
E         got=''
E       assert '' == '-1'
E         - -1

tmp88cnums4.py:27: AssertionError
______________________________ test_case[case47] _______________________________

i = 47, inp = 'he\nhh\n', expected = '-1\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='he\nhh\n'
E         expected='-1'
E         got=''
E       assert '' == '-1'
E         - -1

tmp88cnums4.py:27: AssertionError
______________________________ test_case[case48] _______________________________

i = 48, inp = 'hee\nheh\n', expected = '-1\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='hee\nheh\n'
E         expected='-1'
E         got=''
E       assert '' == '-1'
E         - -1

tmp88cnums4.py:27: AssertionError
______________________________ test_case[case49] _______________________________

i = 49, inp = 'aa\nac\n', expected = '-1\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='aa\nac\n'
E         expected='-1'
E         got=''
E       assert '' == '-1'
E         - -1

tmp88cnums4.py:27: AssertionError
______________________________ test_case[case50] _______________________________

i = 50, inp = 'ab\naa\n', expected = '-1\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='ab\naa\n'
E         expected='-1'
E         got=''
E       assert '' == '-1'
E         - -1

tmp88cnums4.py:27: AssertionError
______________________________ test_case[case51] _______________________________

i = 51, inp = 'hello\nehlol\n', expected = '-1\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='hello\nehlol\n'
E         expected='-1'
E         got=''
E       assert '' == '-1'
E         - -1

tmp88cnums4.py:27: AssertionError
______________________________ test_case[case52] _______________________________

i = 52, inp = 'ac\naa\n', expected = '-1\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='ac\naa\n'
E         expected='-1'
E         got=''
E       assert '' == '-1'
E         - -1

tmp88cnums4.py:27: AssertionError
______________________________ test_case[case53] _______________________________

i = 53, inp = 'aaabbb\nbbbaab\n', expected = '-1\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='aaabbb\nbbbaab\n'
E         expected='-1'
E         got=''
E       assert '' == '-1'
E         - -1

tmp88cnums4.py:27: AssertionError
______________________________ test_case[case54] _______________________________

i = 54, inp = 'aa\nfa\n', expected = '-1\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='aa\nfa\n'
E         expected='-1'
E         got=''
E       assert '' == '-1'
E         - -1

tmp88cnums4.py:27: AssertionError
______________________________ test_case[case55] _______________________________

i = 55, inp = 'hg\nee\n', expected = '-1\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='hg\nee\n'
E         expected='-1'
E         got=''
E       assert '' == '-1'
E         - -1

tmp88cnums4.py:27: AssertionError
______________________________ test_case[case56] _______________________________

i = 56, inp = 'helloworld\nehoolwlrow\n', expected = '-1\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='helloworld\nehoolwlrow\n'
E         expected='-1'
E         got=''
E       assert '' == '-1'
E         - -1

tmp88cnums4.py:27: AssertionError
______________________________ test_case[case57] _______________________________

i = 57, inp = 'abb\nbab\n', expected = '-1\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='abb\nbab\n'
E         expected='-1'
E         got=''
E       assert '' == '-1'
E         - -1

tmp88cnums4.py:27: AssertionError
______________________________ test_case[case58] _______________________________

i = 58, inp = 'aaa\naae\n', expected = '-1\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='aaa\naae\n'
E         expected='-1'
E         got=''
E       assert '' == '-1'
E         - -1

tmp88cnums4.py:27: AssertionError
______________________________ test_case[case59] _______________________________

i = 59, inp = 'aba\nbaa\n', expected = '-1\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='aba\nbaa\n'
E         expected='-1'
E         got=''
E       assert '' == '-1'
E         - -1

tmp88cnums4.py:27: AssertionError
______________________________ test_case[case60] _______________________________

i = 60, inp = 'aa\nba\n', expected = '-1\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='aa\nba\n'
E         expected='-1'
E         got=''
E       assert '' == '-1'
E         - -1

tmp88cnums4.py:27: AssertionError
______________________________ test_case[case61] _______________________________

i = 61, inp = 'da\naa\n', expected = '-1\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='da\naa\n'
E         expected='-1'
E         got=''
E       assert '' == '-1'
E         - -1

tmp88cnums4.py:27: AssertionError
______________________________ test_case[case62] _______________________________

i = 62, inp = 'aaa\naab\n', expected = '-1\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='aaa\naab\n'
E         expected='-1'
E         got=''
E       assert '' == '-1'
E         - -1

tmp88cnums4.py:27: AssertionError
______________________________ test_case[case63] _______________________________

i = 63, inp = 'xy\nzz\n', expected = '-1\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='xy\nzz\n'
E         expected='-1'
E         got=''
E       assert '' == '-1'
E         - -1

tmp88cnums4.py:27: AssertionError
=========================== short test summary info ============================
FAILED tmp88cnums4.py::test_case[case0] - AssertionError: input='helloworld\n...
FAILED tmp88cnums4.py::test_case[case1] - AssertionError: input='hastalavista...
FAILED tmp88cnums4.py::test_case[case2] - AssertionError: input='merrychristm...
FAILED tmp88cnums4.py::test_case[case3] - AssertionError: input='kusyvdgccw\n...
FAILED tmp88cnums4.py::test_case[case4] - AssertionError: input='bbbbbabbab\n...
FAILED tmp88cnums4.py::test_case[case5] - AssertionError: input='zzzzzzzzzzzz...
FAILED tmp88cnums4.py::test_case[case6] - AssertionError: input='accdccdcdcca...
FAILED tmp88cnums4.py::test_case[case7] - AssertionError: input='giiibdbebjda...
FAILED tmp88cnums4.py::test_case[case8] - AssertionError: input='gndggadlmdef...
FAILED tmp88cnums4.py::test_case[case9] - AssertionError: input='ijpanyhovzwj...
FAILED tmp88cnums4.py::test_case[case10] - AssertionError: input='ab\naa\n'
FAILED tmp88cnums4.py::test_case[case11] - AssertionError: input='a\nz\n'
FAILED tmp88cnums4.py::test_case[case12] - AssertionError: input='zz\nzy\n'
FAILED tmp88cnums4.py::test_case[case13] - AssertionError: input='as\ndf\n'
FAILED tmp88cnums4.py::test_case[case14] - AssertionError: input='abc\nbca\n'
FAILED tmp88cnums4.py::test_case[case15] - AssertionError: input='rtfg\nrftg\n'
FAILED tmp88cnums4.py::test_case[case16] - AssertionError: input='y\ny\n'
FAILED tmp88cnums4.py::test_case[case17] - AssertionError: input='qwertyuiopa...
FAILED tmp88cnums4.py::test_case[case18] - AssertionError: input='qazwsxedcrf...
FAILED tmp88cnums4.py::test_case[case19] - AssertionError: input='aaaaaa\nabc...
FAILED tmp88cnums4.py::test_case[case20] - AssertionError: input='qwerty\nfff...
FAILED tmp88cnums4.py::test_case[case21] - AssertionError: input='dofbgdppdvm...
FAILED tmp88cnums4.py::test_case[case22] - AssertionError: input='acdbccddadb...
FAILED tmp88cnums4.py::test_case[case23] - AssertionError: input='bacccbbacab...
FAILED tmp88cnums4.py::test_case[case24] - AssertionError: input='dbadbddddb\...
FAILED tmp88cnums4.py::test_case[case25] - AssertionError: input='dacbdbbbdd\...
FAILED tmp88cnums4.py::test_case[case26] - AssertionError: input='bbbbcbcbbc\...
FAILED tmp88cnums4.py::test_case[case27] - AssertionError: input='dddddbcdbd\...
FAILED tmp88cnums4.py::test_case[case28] - AssertionError: input='cbadcbcdaa\...
FAILED tmp88cnums4.py::test_case[case29] - AssertionError: input='dmkgadidjgd...
FAILED tmp88cnums4.py::test_case[case30] - AssertionError: input='acbbccabaa\...
FAILED tmp88cnums4.py::test_case[case31] - AssertionError: input='ccccaccccc\...
FAILED tmp88cnums4.py::test_case[case32] - AssertionError: input='acbacacbbb\...
FAILED tmp88cnums4.py::test_case[case33] - AssertionError: input='abbababbcc\...
FAILED tmp88cnums4.py::test_case[case34] - AssertionError: input='jbcbbjiifdc...
FAILED tmp88cnums4.py::test_case[case35] - AssertionError: input='ahaeheedefe...
FAILED tmp88cnums4.py::test_case[case36] - AssertionError: input='fficficbidb...
FAILED tmp88cnums4.py::test_case[case37] - AssertionError: input='z\nz\n'
FAILED tmp88cnums4.py::test_case[case38] - AssertionError: input='a\nz\n'
FAILED tmp88cnums4.py::test_case[case39] - AssertionError: input='z\na\n'
FAILED tmp88cnums4.py::test_case[case40] - AssertionError: input='aa\nzz\n'
FAILED tmp88cnums4.py::test_case[case41] - AssertionError: input='az\nza\n'
FAILED tmp88cnums4.py::test_case[case42] - AssertionError: input='aa\nza\n'
FAILED tmp88cnums4.py::test_case[case43] - AssertionError: input='za\nzz\n'
FAILED tmp88cnums4.py::test_case[case44] - AssertionError: input='aa\nab\n'
FAILED tmp88cnums4.py::test_case[case45] - AssertionError: input='hehe\nheeh\n'
FAILED tmp88cnums4.py::test_case[case46] - AssertionError: input='bd\ncc\n'
FAILED tmp88cnums4.py::test_case[case47] - AssertionError: input='he\nhh\n'
FAILED tmp88cnums4.py::test_case[case48] - AssertionError: input='hee\nheh\n'
FAILED tmp88cnums4.py::test_case[case49] - AssertionError: input='aa\nac\n'
FAILED tmp88cnums4.py::test_case[case50] - AssertionError: input='ab\naa\n'
FAILED tmp88cnums4.py::test_case[case51] - AssertionError: input='hello\nehlo...
FAILED tmp88cnums4.py::test_case[case52] - AssertionError: input='ac\naa\n'
FAILED tmp88cnums4.py::test_case[case53] - AssertionError: input='aaabbb\nbbb...
FAILED tmp88cnums4.py::test_case[case54] - AssertionError: input='aa\nfa\n'
FAILED tmp88cnums4.py::test_case[case55] - AssertionError: input='hg\nee\n'
FAILED tmp88cnums4.py::test_case[case56] - AssertionError: input='helloworld\...
FAILED tmp88cnums4.py::test_case[case57] - AssertionError: input='abb\nbab\n'
FAILED tmp88cnums4.py::test_case[case58] - AssertionError: input='aaa\naae\n'
FAILED tmp88cnums4.py::test_case[case59] - AssertionError: input='aba\nbaa\n'
FAILED tmp88cnums4.py::test_case[case60] - AssertionError: input='aa\nba\n'
FAILED tmp88cnums4.py::test_case[case61] - AssertionError: input='da\naa\n'
FAILED tmp88cnums4.py::test_case[case62] - AssertionError: input='aaa\naab\n'
FAILED tmp88cnums4.py::test_case[case63] - AssertionError: input='xy\nzz\n'
============================= 64 failed in 11.28s ==============================
```
