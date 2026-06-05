# introductory/977-b

**Status:** FAIL (exit code 1)

## stdout

```
============================= test session starts ==============================
platform linux -- Python 3.10.18, pytest-7.4.4, pluggy-1.6.0
PyQt5 5.15.10 -- Qt runtime 5.15.17 -- Qt compiled 5.15.2
rootdir: /tmp/tmp476mv0b6
configfile: pytest.ini
plugins: Faker-25.1.0, anyio-4.9.0, cov-5.0.0, mock-3.12.0, qt-4.3.1
collected 22 items

tmp7jas3a82.py::test_case[case0] PASSED
tmp7jas3a82.py::test_case[case1] PASSED
tmp7jas3a82.py::test_case[case2] FAILED
tmp7jas3a82.py::test_case[case3] PASSED
tmp7jas3a82.py::test_case[case4] PASSED
tmp7jas3a82.py::test_case[case5] PASSED
tmp7jas3a82.py::test_case[case6] FAILED
tmp7jas3a82.py::test_case[case7] PASSED
tmp7jas3a82.py::test_case[case8] PASSED
tmp7jas3a82.py::test_case[case9] PASSED
tmp7jas3a82.py::test_case[case10] PASSED
tmp7jas3a82.py::test_case[case11] FAILED
tmp7jas3a82.py::test_case[case12] PASSED
tmp7jas3a82.py::test_case[case13] FAILED
tmp7jas3a82.py::test_case[case14] FAILED
tmp7jas3a82.py::test_case[case15] PASSED
tmp7jas3a82.py::test_case[case16] PASSED
tmp7jas3a82.py::test_case[case17] FAILED
tmp7jas3a82.py::test_case[case18] FAILED
tmp7jas3a82.py::test_case[case19] FAILED
tmp7jas3a82.py::test_case[case20] PASSED
tmp7jas3a82.py::test_case[case21] PASSED

=================================== FAILURES ===================================
_______________________________ test_case[case2] _______________________________

i = 2, inp = '26\nQWERTYUIOPASDFGHJKLZXCVBNM\n', expected = 'AS\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='26\nQWERTYUIOPASDFGHJKLZXCVBNM\n'
E         expected='AS'
E         got='QW'
E       assert 'QW' == 'AS'
E         - AS
E         + QW

tmp7jas3a82.py:27: AssertionError
_______________________________ test_case[case6] _______________________________

i = 6, inp = '50\nNYQAHBYYOXLTRYQDMVENEMAQNBAKGLGQOLXNAIFNQTOCLNNQIA\n'
expected = 'NQ\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='50\nNYQAHBYYOXLTRYQDMVENEMAQNBAKGLGQOLXNAIFNQTOCLNNQIA\n'
E         expected='NQ'
E         got='YQ'
E       assert 'YQ' == 'NQ'
E         - NQ
E         + YQ

tmp7jas3a82.py:27: AssertionError
______________________________ test_case[case11] _______________________________

i = 11, inp = '15\nMIRZOYANOVECLOX\n', expected = 'AN\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='15\nMIRZOYANOVECLOX\n'
E         expected='AN'
E         got='MI'
E       assert 'MI' == 'AN'
E         - AN
E         + MI

tmp7jas3a82.py:27: AssertionError
______________________________ test_case[case13] _______________________________

i = 13, inp = '8\nPUTINVOR\n', expected = 'IN\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='8\nPUTINVOR\n'
E         expected='IN'
E         got='PU'
E       assert 'PU' == 'IN'
E         - IN
E         + PU

tmp7jas3a82.py:27: AssertionError
______________________________ test_case[case14] _______________________________

i = 14, inp = '7\nKADUROV\n', expected = 'AD\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='7\nKADUROV\n'
E         expected='AD'
E         got='KA'
E       assert 'KA' == 'AD'
E         - AD
E         + KA

tmp7jas3a82.py:27: AssertionError
______________________________ test_case[case17] _______________________________

i = 17, inp = '3\nKEK\n', expected = 'EK\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='3\nKEK\n'
E         expected='EK'
E         got='KE'
E       assert 'KE' == 'EK'
E         - EK
E         + KE

tmp7jas3a82.py:27: AssertionError
______________________________ test_case[case18] _______________________________

i = 18, inp = '5\nFUFEL\n', expected = 'EL\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='5\nFUFEL\n'
E         expected='EL'
E         got='FU'
E       assert 'FU' == 'EL'
E         - EL
E         + FU

tmp7jas3a82.py:27: AssertionError
______________________________ test_case[case19] _______________________________

i = 19, inp = '9\nMIKEPIDOR\n', expected = 'DO\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='9\nMIKEPIDOR\n'
E         expected='DO'
E         got='MI'
E       assert 'MI' == 'DO'
E         - DO
E         + MI

tmp7jas3a82.py:27: AssertionError
=========================== short test summary info ============================
FAILED tmp7jas3a82.py::test_case[case2] - AssertionError: input='26\nQWERTYUI...
FAILED tmp7jas3a82.py::test_case[case6] - AssertionError: input='50\nNYQAHBYY...
FAILED tmp7jas3a82.py::test_case[case11] - AssertionError: input='15\nMIRZOYA...
FAILED tmp7jas3a82.py::test_case[case13] - AssertionError: input='8\nPUTINVOR\n'
FAILED tmp7jas3a82.py::test_case[case14] - AssertionError: input='7\nKADUROV\n'
FAILED tmp7jas3a82.py::test_case[case17] - AssertionError: input='3\nKEK\n'
FAILED tmp7jas3a82.py::test_case[case18] - AssertionError: input='5\nFUFEL\n'
FAILED tmp7jas3a82.py::test_case[case19] - AssertionError: input='9\nMIKEPIDO...
========================= 8 failed, 14 passed in 3.91s =========================
```
