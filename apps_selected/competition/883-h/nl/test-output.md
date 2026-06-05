# competition/883-h

**Status:** FAIL (exit code 1)

## stdout

```
============================= test session starts ==============================
platform linux -- Python 3.10.18, pytest-7.4.4, pluggy-1.6.0
PyQt5 5.15.10 -- Qt runtime 5.15.17 -- Qt compiled 5.15.2
rootdir: /tmp/tmputcjk0s1
configfile: pytest.ini
plugins: Faker-25.1.0, anyio-4.9.0, cov-5.0.0, mock-3.12.0, qt-4.3.1
collected 27 items

tmpw0u0qboq.py::test_case[case0] FAILED
tmpw0u0qboq.py::test_case[case1] FAILED
tmpw0u0qboq.py::test_case[case2] FAILED
tmpw0u0qboq.py::test_case[case3] PASSED
tmpw0u0qboq.py::test_case[case4] FAILED
tmpw0u0qboq.py::test_case[case5] FAILED
tmpw0u0qboq.py::test_case[case6] FAILED
tmpw0u0qboq.py::test_case[case7] FAILED
tmpw0u0qboq.py::test_case[case8] FAILED
tmpw0u0qboq.py::test_case[case9] PASSED
tmpw0u0qboq.py::test_case[case10] FAILED
tmpw0u0qboq.py::test_case[case11] PASSED
tmpw0u0qboq.py::test_case[case12] PASSED
tmpw0u0qboq.py::test_case[case13] FAILED
tmpw0u0qboq.py::test_case[case14] PASSED
tmpw0u0qboq.py::test_case[case15] PASSED
tmpw0u0qboq.py::test_case[case16] PASSED
tmpw0u0qboq.py::test_case[case17] PASSED
tmpw0u0qboq.py::test_case[case18] PASSED
tmpw0u0qboq.py::test_case[case19] PASSED
tmpw0u0qboq.py::test_case[case20] PASSED
tmpw0u0qboq.py::test_case[case21] PASSED
tmpw0u0qboq.py::test_case[case22] PASSED
tmpw0u0qboq.py::test_case[case23] PASSED
tmpw0u0qboq.py::test_case[case24] PASSED
tmpw0u0qboq.py::test_case[case25] PASSED
tmpw0u0qboq.py::test_case[case26] PASSED

=================================== FAILURES ===================================
_______________________________ test_case[case0] _______________________________

i = 0, inp = '6\naabaac\n', expected = '2\naba aca '

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='6\naabaac\n'
E         expected='2\naba aca'
E         got='2\naca aba'
E       assert '2\naca aba' == '2\naba aca'
E           2
E         - aba aca
E         + aca aba

tmpw0u0qboq.py:27: AssertionError
_______________________________ test_case[case1] _______________________________

i = 1, inp = '8\n0rTrT022\n', expected = '1\n02TrrT20 '

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='8\n0rTrT022\n'
E         expected='1\n02TrrT20'
E         got='1\n2Tr00rT2'
E       assert '1\n2Tr00rT2' == '1\n02TrrT20'
E           1
E         - 02TrrT20
E         ? -      -
E         + 2Tr00rT2
E         ?    ++

tmpw0u0qboq.py:27: AssertionError
_______________________________ test_case[case2] _______________________________

i = 2, inp = '2\naA\n', expected = '2\na A \n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='2\naA\n'
E         expected='2\na A'
E         got='2\nA a'
E       assert '2\nA a' == '2\na A'
E           2
E         - a A
E         + A a

tmpw0u0qboq.py:27: AssertionError
_______________________________ test_case[case4] _______________________________

i = 4, inp = '10\n6IIC6CCIIC\n', expected = '1\n6CCIIIICC6 '

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='10\n6IIC6CCIIC\n'
E         expected='1\n6CCIIIICC6'
E         got='1\nCCII66IICC'
E       assert '1\nCCII66IICC' == '1\n6CCIIIICC6'
E           1
E         - 6CCIIIICC6
E         ? -        -
E         + CCII66IICC
E         ?     ++

tmpw0u0qboq.py:27: AssertionError
_______________________________ test_case[case5] _______________________________

i = 5, inp = '20\nqqqoqqoqMoqMMMqqMMqM\n'
expected = '4\nMMMMM oqoqo qqMqq qqMqq '

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='20\nqqqoqqoqMoqMMMqqMMqM\n'
E         expected='4\nMMMMM oqoqo qqMqq qqMqq'
E         got='2\nMMMoqqoMMM qqqqqqqq'
E       assert '2\nMMMoqqoMMM qqqqqqqq' == '4\nMMMMM oqoqo qqMqq qqMqq'
E         - 4
E         - MMMMM oqoqo qqMqq qqMqq
E         + 2
E         + MMMoqqoMMM qqqqqqqq

tmpw0u0qboq.py:27: AssertionError
_______________________________ test_case[case6] _______________________________

i = 6, inp = '45\nf3409ufEFU32rfsFJSKDFJ234234ASkjffjsdfsdfsj33\n'
expected = '15\n202 323 343 393 4A4 FDF JEJ SFS dKd fUf fff fjf jkj srs sus '

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='45\nf3409ufEFU32rfsFJSKDFJ234234ASkjffjsdfsdfsj33\n'
E         expected='15\n202 323 343 393 4A4 FDF JEJ SFS dKd fUf fff fjf jkj srs sus'
E         got='15\ndjd jkj SAS JDJ sKs srs 222 FUF 4F4 3E3 3u3 393 f0f f4f fff'
E       assert '15\ndjd jkj ...3 f0f f4f fff' == '15\n202 323 ...f jkj srs sus'
E           15
E         - 202 323 343 393 4A4 FDF JEJ SFS dKd fUf fff fjf jkj srs sus
E         + djd jkj SAS JDJ sKs srs 222 FUF 4F4 3E3 3u3 393 f0f f4f fff

tmpw0u0qboq.py:27: AssertionError
_______________________________ test_case[case7] _______________________________

i = 7, inp = '30\n8M8MMMMMlrMlMMrMMllMMrllMMrMrl\n'
expected = '2\n8MMMMMMlMMMMMM8 MMlllrrrrrlllMM '

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='30\n8M8MMMMMlrMlMMrMMllMMrllMMrMrl\n'
E         expected='2\n8MMMMMMlMMMMMM8 MMlllrrrrrlllMM'
E         got='2\nrrlllMMrMMlllrr MMMMMM8l8MMMMMM'
E       assert '2\nrrlllMMrM...MMMM8l8MMMMMM' == '2\n8MMMMMMlM...lllrrrrrlllMM'
E           2
E         - 8MMMMMMlMMMMMM8 MMlllrrrrrlllMM
E         + rrlllMMrMMlllrr MMMMMM8l8MMMMMM

tmpw0u0qboq.py:27: AssertionError
_______________________________ test_case[case8] _______________________________

i = 8, inp = '40\nTddTddddTddddddTdddTdddddddddddddddddddd\n'
expected = '8\nddTdd ddddd ddTdd ddTdd ddTdd ddTdd ddddd ddddd '

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='40\nTddTddddTddddddTdddTdddddddddddddddddddd\n'
E         expected='8\nddTdd ddddd ddTdd ddTdd ddTdd ddTdd ddddd ddddd'
E         got='2\ndddddddddddddddddddd dddddddTTTTddddddd'
E       assert '2\nddddddddd...ddTTTTddddddd' == '8\nddTdd ddd...d ddddd ddddd'
E         - 8
E         - ddTdd ddddd ddTdd ddTdd ddTdd ddTdd ddddd ddddd
E         + 2
E         + dddddddddddddddddddd dddddddTTTTddddddd

tmpw0u0qboq.py:27: AssertionError
______________________________ test_case[case10] _______________________________

i = 10
inp = '115\nz9c2f5fxz9z999c9z999f9f9x99559f5Vf955c59E9ccz5fcc99xfzcEx29xuE55f995u592xE58Exc9zVff885u9cf59cV5xc999fx5x55u992fx9x\n'
expected = '5\n22555555555555555555522 89999999999899999999998 999999EEVccEccVEE999999 ccccfffffffVfffffffcccc uuxxxxxxzzzzzzzxxxxxxuu '

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='115\nz9c2f5fxz9z999c9z999f9f9x99559f5Vf955c59E9ccz5fcc99xfzcEx29xuE55f995u592xE58Exc9zVff885u9cf59cV5xc999fx5x55u992fx9x\n'
E         expected='5\n22555555555555555555522 89999999999899999999998 999999EEVccEccVEE999999 ccccfffffffVfffffffcccc uuxxxxxxzzzzzzzxxxxxxuu'
E         got='5\n8uuEEVxxxxx8xxxxxVEEuu8 x555555555fEf555555555x ffffff22cccVccc22ffffff ccc99999999599999999ccc 99999999zzzzzzz99999999'
E       assert '5\n8uuEEVxxx...zzzzz99999999' == '5\n225555555...zzzzzxxxxxxuu'
E           5
E         - 22555555555555555555522 89999999999899999999998 999999EEVccEccVEE999999 ccccfffffffVfffffffcccc uuxxxxxxzzzzzzzxxxxxxuu
E         + 8uuEEVxxxxx8xxxxxVEEuu8 x555555555fEf555555555x ffffff22cccVccc22ffffff ccc99999999599999999ccc 99999999zzzzzzz99999999

tmpw0u0qboq.py:27: AssertionError
______________________________ test_case[case13] _______________________________

i = 13, inp = '2\n9E\n', expected = '2\n9 E \n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='2\n9E\n'
E         expected='2\n9 E'
E         got='2\nE 9'
E       assert '2\nE 9' == '2\n9 E'
E           2
E         - 9 E
E         + E 9

tmpw0u0qboq.py:27: AssertionError
=========================== short test summary info ============================
FAILED tmpw0u0qboq.py::test_case[case0] - AssertionError: input='6\naabaac\n'
FAILED tmpw0u0qboq.py::test_case[case1] - AssertionError: input='8\n0rTrT022\n'
FAILED tmpw0u0qboq.py::test_case[case2] - AssertionError: input='2\naA\n'
FAILED tmpw0u0qboq.py::test_case[case4] - AssertionError: input='10\n6IIC6CCI...
FAILED tmpw0u0qboq.py::test_case[case5] - AssertionError: input='20\nqqqoqqoq...
FAILED tmpw0u0qboq.py::test_case[case6] - AssertionError: input='45\nf3409ufE...
FAILED tmpw0u0qboq.py::test_case[case7] - AssertionError: input='30\n8M8MMMMM...
FAILED tmpw0u0qboq.py::test_case[case8] - AssertionError: input='40\nTddTdddd...
FAILED tmpw0u0qboq.py::test_case[case10] - AssertionError: input='115\nz9c2f5...
FAILED tmpw0u0qboq.py::test_case[case13] - AssertionError: input='2\n9E\n'
======================== 10 failed, 17 passed in 5.44s =========================
```
