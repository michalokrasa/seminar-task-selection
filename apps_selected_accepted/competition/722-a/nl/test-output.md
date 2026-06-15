# competition/722-a

**Status:** FAIL (exit code 1)

## stdout

```
============================= test session starts ==============================
platform linux -- Python 3.10.18, pytest-7.4.4, pluggy-1.6.0
PyQt5 5.15.10 -- Qt runtime 5.15.17 -- Qt compiled 5.15.2
rootdir: /tmp/tmpwk1drrvl
configfile: pytest.ini
plugins: Faker-25.1.0, anyio-4.9.0, cov-5.0.0, mock-3.12.0, qt-4.3.1
collected 52 items

tmpytic7wsy.py::test_case[case0] PASSED
tmpytic7wsy.py::test_case[case1] PASSED
tmpytic7wsy.py::test_case[case2] FAILED
tmpytic7wsy.py::test_case[case3] PASSED
tmpytic7wsy.py::test_case[case4] PASSED
tmpytic7wsy.py::test_case[case5] FAILED
tmpytic7wsy.py::test_case[case6] FAILED
tmpytic7wsy.py::test_case[case7] FAILED
tmpytic7wsy.py::test_case[case8] FAILED
tmpytic7wsy.py::test_case[case9] FAILED
tmpytic7wsy.py::test_case[case10] FAILED
tmpytic7wsy.py::test_case[case11] PASSED
tmpytic7wsy.py::test_case[case12] PASSED
tmpytic7wsy.py::test_case[case13] FAILED
tmpytic7wsy.py::test_case[case14] PASSED
tmpytic7wsy.py::test_case[case15] PASSED
tmpytic7wsy.py::test_case[case16] FAILED
tmpytic7wsy.py::test_case[case17] FAILED
tmpytic7wsy.py::test_case[case18] FAILED
tmpytic7wsy.py::test_case[case19] FAILED
tmpytic7wsy.py::test_case[case20] PASSED
tmpytic7wsy.py::test_case[case21] PASSED
tmpytic7wsy.py::test_case[case22] PASSED
tmpytic7wsy.py::test_case[case23] FAILED
tmpytic7wsy.py::test_case[case24] PASSED
tmpytic7wsy.py::test_case[case25] FAILED
tmpytic7wsy.py::test_case[case26] PASSED
tmpytic7wsy.py::test_case[case27] FAILED
tmpytic7wsy.py::test_case[case28] PASSED
tmpytic7wsy.py::test_case[case29] PASSED
tmpytic7wsy.py::test_case[case30] FAILED
tmpytic7wsy.py::test_case[case31] FAILED
tmpytic7wsy.py::test_case[case32] PASSED
tmpytic7wsy.py::test_case[case33] FAILED
tmpytic7wsy.py::test_case[case34] FAILED
tmpytic7wsy.py::test_case[case35] FAILED
tmpytic7wsy.py::test_case[case36] FAILED
tmpytic7wsy.py::test_case[case37] PASSED
tmpytic7wsy.py::test_case[case38] PASSED
tmpytic7wsy.py::test_case[case39] PASSED
tmpytic7wsy.py::test_case[case40] PASSED
tmpytic7wsy.py::test_case[case41] PASSED
tmpytic7wsy.py::test_case[case42] PASSED
tmpytic7wsy.py::test_case[case43] PASSED
tmpytic7wsy.py::test_case[case44] PASSED
tmpytic7wsy.py::test_case[case45] FAILED
tmpytic7wsy.py::test_case[case46] PASSED
tmpytic7wsy.py::test_case[case47] PASSED
tmpytic7wsy.py::test_case[case48] FAILED
tmpytic7wsy.py::test_case[case49] FAILED
tmpytic7wsy.py::test_case[case50] PASSED
tmpytic7wsy.py::test_case[case51] PASSED

=================================== FAILURES ===================================
_______________________________ test_case[case2] _______________________________

i = 2, inp = '24\n99:99\n', expected = '09:09\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='24\n99:99\n'
E         expected='09:09'
E         got='03:39'
E       assert '03:39' == '09:09'
E         - 09:09
E         + 03:39

tmpytic7wsy.py:27: AssertionError
_______________________________ test_case[case5] _______________________________

i = 5, inp = '24\n23:80\n', expected = '23:00\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='24\n23:80\n'
E         expected='23:00'
E         got='23:20'
E       assert '23:20' == '23:00'
E         - 23:00
E         ?     -
E         + 23:20
E         ?    +

tmpytic7wsy.py:27: AssertionError
_______________________________ test_case[case6] _______________________________

i = 6, inp = '24\n73:16\n', expected = '03:16\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='24\n73:16\n'
E         expected='03:16'
E         got='01:16'
E       assert '01:16' == '03:16'
E         - 03:16
E         ?  ^
E         + 01:16
E         ?  ^

tmpytic7wsy.py:27: AssertionError
_______________________________ test_case[case7] _______________________________

i = 7, inp = '12\n03:77\n', expected = '03:07\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='12\n03:77\n'
E         expected='03:07'
E         got='03:17'
E       assert '03:17' == '03:07'
E         - 03:07
E         ?    ^
E         + 03:17
E         ?    ^

tmpytic7wsy.py:27: AssertionError
_______________________________ test_case[case8] _______________________________

i = 8, inp = '12\n47:83\n', expected = '07:03\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='12\n47:83\n'
E         expected='07:03'
E         got='07:23'
E       assert '07:23' == '07:03'
E         - 07:03
E         ?    ^
E         + 07:23
E         ?    ^

tmpytic7wsy.py:27: AssertionError
_______________________________ test_case[case9] _______________________________

i = 9, inp = '24\n23:88\n', expected = '23:08\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='24\n23:88\n'
E         expected='23:08'
E         got='23:28'
E       assert '23:28' == '23:08'
E         - 23:08
E         ?    ^
E         + 23:28
E         ?    ^

tmpytic7wsy.py:27: AssertionError
______________________________ test_case[case10] _______________________________

i = 10, inp = '24\n51:67\n', expected = '01:07\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='24\n51:67\n'
E         expected='01:07'
E         got='03:07'
E       assert '03:07' == '01:07'
E         - 01:07
E         ?  ^
E         + 03:07
E         ?  ^

tmpytic7wsy.py:27: AssertionError
______________________________ test_case[case13] _______________________________

i = 13, inp = '12\n07:74\n', expected = '07:04\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='12\n07:74\n'
E         expected='07:04'
E         got='07:14'
E       assert '07:14' == '07:04'
E         - 07:04
E         ?    ^
E         + 07:14
E         ?    ^

tmpytic7wsy.py:27: AssertionError
______________________________ test_case[case16] _______________________________

i = 16, inp = '24\n42:59\n', expected = '02:59\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='24\n42:59\n'
E         expected='02:59'
E         got='18:59'
E       assert '18:59' == '02:59'
E         - 02:59
E         + 18:59

tmpytic7wsy.py:27: AssertionError
______________________________ test_case[case17] _______________________________

i = 17, inp = '24\n19:87\n', expected = '19:07\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='24\n19:87\n'
E         expected='19:07'
E         got='19:27'
E       assert '19:27' == '19:07'
E         - 19:07
E         ?    ^
E         + 19:27
E         ?    ^

tmpytic7wsy.py:27: AssertionError
______________________________ test_case[case18] _______________________________

i = 18, inp = '24\n26:98\n', expected = '06:08\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='24\n26:98\n'
E         expected='06:08'
E         got='02:38'
E       assert '02:38' == '06:08'
E         - 06:08
E         + 02:38

tmpytic7wsy.py:27: AssertionError
______________________________ test_case[case19] _______________________________

i = 19, inp = '12\n12:91\n', expected = '12:01\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='12\n12:91\n'
E         expected='12:01'
E         got='12:31'
E       assert '12:31' == '12:01'
E         - 12:01
E         ?    ^
E         + 12:31
E         ?    ^

tmpytic7wsy.py:27: AssertionError
______________________________ test_case[case23] _______________________________

i = 23, inp = '12\n33:83\n', expected = '03:03\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='12\n33:83\n'
E         expected='03:03'
E         got='03:23'
E       assert '03:23' == '03:03'
E         - 03:03
E         ?    ^
E         + 03:23
E         ?    ^

tmpytic7wsy.py:27: AssertionError
______________________________ test_case[case25] _______________________________

i = 25, inp = '24\n65:12\n', expected = '05:12\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='24\n65:12\n'
E         expected='05:12'
E         got='17:12'
E       assert '17:12' == '05:12'
E         - 05:12
E         + 17:12

tmpytic7wsy.py:27: AssertionError
______________________________ test_case[case27] _______________________________

i = 27, inp = '24\n48:91\n', expected = '08:01\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='24\n48:91\n'
E         expected='08:01'
E         got='00:31'
E       assert '00:31' == '08:01'
E         - 08:01
E         + 00:31

tmpytic7wsy.py:27: AssertionError
______________________________ test_case[case30] _______________________________

i = 30, inp = '12\n02:86\n', expected = '02:06\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='12\n02:86\n'
E         expected='02:06'
E         got='02:26'
E       assert '02:26' == '02:06'
E         - 02:06
E         ?    ^
E         + 02:26
E         ?    ^

tmpytic7wsy.py:27: AssertionError
______________________________ test_case[case31] _______________________________

i = 31, inp = '12\n99:96\n', expected = '09:06\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='12\n99:96\n'
E         expected='09:06'
E         got='09:36'
E       assert '09:36' == '09:06'
E         - 09:06
E         ?    ^
E         + 09:36
E         ?    ^

tmpytic7wsy.py:27: AssertionError
______________________________ test_case[case33] _______________________________

i = 33, inp = '24\n55:49\n', expected = '05:49\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='24\n55:49\n'
E         expected='05:49'
E         got='07:49'
E       assert '07:49' == '05:49'
E         - 05:49
E         ?  ^
E         + 07:49
E         ?  ^

tmpytic7wsy.py:27: AssertionError
______________________________ test_case[case34] _______________________________

i = 34, inp = '24\n01:97\n', expected = '01:07\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='24\n01:97\n'
E         expected='01:07'
E         got='01:37'
E       assert '01:37' == '01:07'
E         - 01:07
E         ?    ^
E         + 01:37
E         ?    ^

tmpytic7wsy.py:27: AssertionError
______________________________ test_case[case35] _______________________________

i = 35, inp = '24\n39:68\n', expected = '09:08\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='24\n39:68\n'
E         expected='09:08'
E         got='15:08'
E       assert '15:08' == '09:08'
E         - 09:08
E         + 15:08

tmpytic7wsy.py:27: AssertionError
______________________________ test_case[case36] _______________________________

i = 36, inp = '24\n24:00\n', expected = '04:00\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='24\n24:00\n'
E         expected='04:00'
E         got='00:00'
E       assert '00:00' == '04:00'
E         - 04:00
E         ?  ^
E         + 00:00
E         ?  ^

tmpytic7wsy.py:27: AssertionError
______________________________ test_case[case45] _______________________________

i = 45, inp = '24\n30:40\n', expected = '00:40\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='24\n30:40\n'
E         expected='00:40'
E         got='06:40'
E       assert '06:40' == '00:40'
E         - 00:40
E         ?  ^
E         + 06:40
E         ?  ^

tmpytic7wsy.py:27: AssertionError
______________________________ test_case[case48] _______________________________

i = 48, inp = '24\n30:00\n', expected = '00:00\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='24\n30:00\n'
E         expected='00:00'
E         got='06:00'
E       assert '06:00' == '00:00'
E         - 00:00
E         ?  ^
E         + 06:00
E         ?  ^

tmpytic7wsy.py:27: AssertionError
______________________________ test_case[case49] _______________________________

i = 49, inp = '24\n34:00\n', expected = '04:00\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='24\n34:00\n'
E         expected='04:00'
E         got='10:00'
E       assert '10:00' == '04:00'
E         - 04:00
E         ?  -
E         + 10:00
E         ? +

tmpytic7wsy.py:27: AssertionError
=========================== short test summary info ============================
FAILED tmpytic7wsy.py::test_case[case2] - AssertionError: input='24\n99:99\n'
FAILED tmpytic7wsy.py::test_case[case5] - AssertionError: input='24\n23:80\n'
FAILED tmpytic7wsy.py::test_case[case6] - AssertionError: input='24\n73:16\n'
FAILED tmpytic7wsy.py::test_case[case7] - AssertionError: input='12\n03:77\n'
FAILED tmpytic7wsy.py::test_case[case8] - AssertionError: input='12\n47:83\n'
FAILED tmpytic7wsy.py::test_case[case9] - AssertionError: input='24\n23:88\n'
FAILED tmpytic7wsy.py::test_case[case10] - AssertionError: input='24\n51:67\n'
FAILED tmpytic7wsy.py::test_case[case13] - AssertionError: input='12\n07:74\n'
FAILED tmpytic7wsy.py::test_case[case16] - AssertionError: input='24\n42:59\n'
FAILED tmpytic7wsy.py::test_case[case17] - AssertionError: input='24\n19:87\n'
FAILED tmpytic7wsy.py::test_case[case18] - AssertionError: input='24\n26:98\n'
FAILED tmpytic7wsy.py::test_case[case19] - AssertionError: input='12\n12:91\n'
FAILED tmpytic7wsy.py::test_case[case23] - AssertionError: input='12\n33:83\n'
FAILED tmpytic7wsy.py::test_case[case25] - AssertionError: input='24\n65:12\n'
FAILED tmpytic7wsy.py::test_case[case27] - AssertionError: input='24\n48:91\n'
FAILED tmpytic7wsy.py::test_case[case30] - AssertionError: input='12\n02:86\n'
FAILED tmpytic7wsy.py::test_case[case31] - AssertionError: input='12\n99:96\n'
FAILED tmpytic7wsy.py::test_case[case33] - AssertionError: input='24\n55:49\n'
FAILED tmpytic7wsy.py::test_case[case34] - AssertionError: input='24\n01:97\n'
FAILED tmpytic7wsy.py::test_case[case35] - AssertionError: input='24\n39:68\n'
FAILED tmpytic7wsy.py::test_case[case36] - AssertionError: input='24\n24:00\n'
FAILED tmpytic7wsy.py::test_case[case45] - AssertionError: input='24\n30:40\n'
FAILED tmpytic7wsy.py::test_case[case48] - AssertionError: input='24\n30:00\n'
FAILED tmpytic7wsy.py::test_case[case49] - AssertionError: input='24\n34:00\n'
======================== 24 failed, 28 passed in 9.25s =========================
```
