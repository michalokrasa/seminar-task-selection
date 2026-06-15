# introductory/977-b

**Status:** FAIL (exit code 1)

## stdout

```
============================= test session starts ==============================
platform linux -- Python 3.10.18, pytest-7.4.4, pluggy-1.6.0
PyQt5 5.15.10 -- Qt runtime 5.15.17 -- Qt compiled 5.15.2
rootdir: /tmp/tmprjol9bir
configfile: pytest.ini
plugins: Faker-25.1.0, anyio-4.9.0, cov-5.0.0, mock-3.12.0, qt-4.3.1
collected 22 items

tmp__78uiz6.py::test_case[case0] FAILED
tmp__78uiz6.py::test_case[case1] FAILED
tmp__78uiz6.py::test_case[case2] FAILED
tmp__78uiz6.py::test_case[case3] FAILED
tmp__78uiz6.py::test_case[case4] FAILED
tmp__78uiz6.py::test_case[case5] FAILED
tmp__78uiz6.py::test_case[case6] FAILED
tmp__78uiz6.py::test_case[case7] FAILED
tmp__78uiz6.py::test_case[case8] FAILED
tmp__78uiz6.py::test_case[case9] FAILED
tmp__78uiz6.py::test_case[case10] FAILED
tmp__78uiz6.py::test_case[case11] FAILED
tmp__78uiz6.py::test_case[case12] FAILED
tmp__78uiz6.py::test_case[case13] FAILED
tmp__78uiz6.py::test_case[case14] FAILED
tmp__78uiz6.py::test_case[case15] FAILED
tmp__78uiz6.py::test_case[case16] FAILED
tmp__78uiz6.py::test_case[case17] FAILED
tmp__78uiz6.py::test_case[case18] FAILED
tmp__78uiz6.py::test_case[case19] FAILED
tmp__78uiz6.py::test_case[case20] FAILED
tmp__78uiz6.py::test_case[case21] FAILED

=================================== FAILURES ===================================
_______________________________ test_case[case0] _______________________________

i = 0, inp = '7\nABACABA\n', expected = 'AB\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='7\nABACABA\n'
E         expected='AB'
E         got=''
E       assert '' == 'AB'
E         - AB

tmp__78uiz6.py:27: AssertionError
_______________________________ test_case[case1] _______________________________

i = 1, inp = '5\nZZZAA\n', expected = 'ZZ\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='5\nZZZAA\n'
E         expected='ZZ'
E         got=''
E       assert '' == 'ZZ'
E         - ZZ

tmp__78uiz6.py:27: AssertionError
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
E         got=''
E       assert '' == 'AS'
E         - AS

tmp__78uiz6.py:27: AssertionError
_______________________________ test_case[case3] _______________________________

i = 3, inp = '2\nQA\n', expected = 'QA\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='2\nQA\n'
E         expected='QA'
E         got=''
E       assert '' == 'QA'
E         - QA

tmp__78uiz6.py:27: AssertionError
_______________________________ test_case[case4] _______________________________

i = 4, inp = '2\nWW\n', expected = 'WW\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='2\nWW\n'
E         expected='WW'
E         got=''
E       assert '' == 'WW'
E         - WW

tmp__78uiz6.py:27: AssertionError
_______________________________ test_case[case5] _______________________________

i = 5, inp = '11\nGGRRAATTZZZ\n', expected = 'ZZ\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='11\nGGRRAATTZZZ\n'
E         expected='ZZ'
E         got=''
E       assert '' == 'ZZ'
E         - ZZ

tmp__78uiz6.py:27: AssertionError
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
E         got=''
E       assert '' == 'NQ'
E         - NQ

tmp__78uiz6.py:27: AssertionError
_______________________________ test_case[case7] _______________________________

i = 7
inp = '100\nURXCAIZFIBNJTPCZHBQIBCILLPXZCFGMKKZMNPLCYGAVJVIBMCZEBSJWPSCPQDYCTTKPOKIJRSKIZPDGCHVOUTMPNECYORSFZFNC\n'
expected = 'IB\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='100\nURXCAIZFIBNJTPCZHBQIBCILLPXZCFGMKKZMNPLCYGAVJVIBMCZEBSJWPSCPQDYCTTKPOKIJRSKIZPDGCHVOUTMPNECYORSFZFNC\n'
E         expected='IB'
E         got=''
E       assert '' == 'IB'
E         - IB

tmp__78uiz6.py:27: AssertionError
_______________________________ test_case[case8] _______________________________

i = 8
inp = '100\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n'
expected = 'AA\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='100\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n'
E         expected='AA'
E         got=''
E       assert '' == 'AA'
E         - AA

tmp__78uiz6.py:27: AssertionError
_______________________________ test_case[case9] _______________________________

i = 9, inp = '10\nSQSQSQSQTG\n', expected = 'SQ\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='10\nSQSQSQSQTG\n'
E         expected='SQ'
E         got=''
E       assert '' == 'SQ'
E         - SQ

tmp__78uiz6.py:27: AssertionError
______________________________ test_case[case10] _______________________________

i = 10, inp = '5\nAZAZA\n', expected = 'AZ\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='5\nAZAZA\n'
E         expected='AZ'
E         got=''
E       assert '' == 'AZ'
E         - AZ

tmp__78uiz6.py:27: AssertionError
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
E         got=''
E       assert '' == 'AN'
E         - AN

tmp__78uiz6.py:27: AssertionError
______________________________ test_case[case12] _______________________________

i = 12, inp = '9\nEGORLETOV\n', expected = 'EG\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='9\nEGORLETOV\n'
E         expected='EG'
E         got=''
E       assert '' == 'EG'
E         - EG

tmp__78uiz6.py:27: AssertionError
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
E         got=''
E       assert '' == 'IN'
E         - IN

tmp__78uiz6.py:27: AssertionError
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
E         got=''
E       assert '' == 'AD'
E         - AD

tmp__78uiz6.py:27: AssertionError
______________________________ test_case[case15] _______________________________

i = 15, inp = '6\nAZAZAZ\n', expected = 'AZ\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='6\nAZAZAZ\n'
E         expected='AZ'
E         got=''
E       assert '' == 'AZ'
E         - AZ

tmp__78uiz6.py:27: AssertionError
______________________________ test_case[case16] _______________________________

i = 16, inp = '3\nLOL\n', expected = 'LO\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='3\nLOL\n'
E         expected='LO'
E         got=''
E       assert '' == 'LO'
E         - LO

tmp__78uiz6.py:27: AssertionError
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
E         got=''
E       assert '' == 'EK'
E         - EK

tmp__78uiz6.py:27: AssertionError
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
E         got=''
E       assert '' == 'EL'
E         - EL

tmp__78uiz6.py:27: AssertionError
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
E         got=''
E       assert '' == 'DO'
E         - DO

tmp__78uiz6.py:27: AssertionError
______________________________ test_case[case20] _______________________________

i = 20, inp = '9\nAAAAAAAAA\n', expected = 'AA\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='9\nAAAAAAAAA\n'
E         expected='AA'
E         got=''
E       assert '' == 'AA'
E         - AA

tmp__78uiz6.py:27: AssertionError
______________________________ test_case[case21] _______________________________

i = 21, inp = '23\nAABBBAAACCCCCAAADDDDDDD\n', expected = 'DD\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='23\nAABBBAAACCCCCAAADDDDDDD\n'
E         expected='DD'
E         got=''
E       assert '' == 'DD'
E         - DD

tmp__78uiz6.py:27: AssertionError
=========================== short test summary info ============================
FAILED tmp__78uiz6.py::test_case[case0] - AssertionError: input='7\nABACABA\n'
FAILED tmp__78uiz6.py::test_case[case1] - AssertionError: input='5\nZZZAA\n'
FAILED tmp__78uiz6.py::test_case[case2] - AssertionError: input='26\nQWERTYUI...
FAILED tmp__78uiz6.py::test_case[case3] - AssertionError: input='2\nQA\n'
FAILED tmp__78uiz6.py::test_case[case4] - AssertionError: input='2\nWW\n'
FAILED tmp__78uiz6.py::test_case[case5] - AssertionError: input='11\nGGRRAATT...
FAILED tmp__78uiz6.py::test_case[case6] - AssertionError: input='50\nNYQAHBYY...
FAILED tmp__78uiz6.py::test_case[case7] - AssertionError: input='100\nURXCAIZ...
FAILED tmp__78uiz6.py::test_case[case8] - AssertionError: input='100\nAAAAAAA...
FAILED tmp__78uiz6.py::test_case[case9] - AssertionError: input='10\nSQSQSQSQ...
FAILED tmp__78uiz6.py::test_case[case10] - AssertionError: input='5\nAZAZA\n'
FAILED tmp__78uiz6.py::test_case[case11] - AssertionError: input='15\nMIRZOYA...
FAILED tmp__78uiz6.py::test_case[case12] - AssertionError: input='9\nEGORLETO...
FAILED tmp__78uiz6.py::test_case[case13] - AssertionError: input='8\nPUTINVOR\n'
FAILED tmp__78uiz6.py::test_case[case14] - AssertionError: input='7\nKADUROV\n'
FAILED tmp__78uiz6.py::test_case[case15] - AssertionError: input='6\nAZAZAZ\n'
FAILED tmp__78uiz6.py::test_case[case16] - AssertionError: input='3\nLOL\n'
FAILED tmp__78uiz6.py::test_case[case17] - AssertionError: input='3\nKEK\n'
FAILED tmp__78uiz6.py::test_case[case18] - AssertionError: input='5\nFUFEL\n'
FAILED tmp__78uiz6.py::test_case[case19] - AssertionError: input='9\nMIKEPIDO...
FAILED tmp__78uiz6.py::test_case[case20] - AssertionError: input='9\nAAAAAAAA...
FAILED tmp__78uiz6.py::test_case[case21] - AssertionError: input='23\nAABBBAA...
============================== 22 failed in 4.10s ==============================
```
