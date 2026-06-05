# competition/245-b

**Status:** FAIL (exit code 1)

## stdout

```
============================= test session starts ==============================
platform linux -- Python 3.10.18, pytest-7.4.4, pluggy-1.6.0
PyQt5 5.15.10 -- Qt runtime 5.15.17 -- Qt compiled 5.15.2
rootdir: /tmp/tmpuw00wmms
configfile: pytest.ini
plugins: Faker-25.1.0, anyio-4.9.0, cov-5.0.0, mock-3.12.0, qt-4.3.1
collected 20 items

tmp_8szm6jk.py::test_case[case0] FAILED
tmp_8szm6jk.py::test_case[case1] FAILED
tmp_8szm6jk.py::test_case[case2] FAILED
tmp_8szm6jk.py::test_case[case3] FAILED
tmp_8szm6jk.py::test_case[case4] FAILED
tmp_8szm6jk.py::test_case[case5] FAILED
tmp_8szm6jk.py::test_case[case6] FAILED
tmp_8szm6jk.py::test_case[case7] FAILED
tmp_8szm6jk.py::test_case[case8] FAILED
tmp_8szm6jk.py::test_case[case9] FAILED
tmp_8szm6jk.py::test_case[case10] FAILED
tmp_8szm6jk.py::test_case[case11] FAILED
tmp_8szm6jk.py::test_case[case12] FAILED
tmp_8szm6jk.py::test_case[case13] FAILED
tmp_8szm6jk.py::test_case[case14] FAILED
tmp_8szm6jk.py::test_case[case15] FAILED
tmp_8szm6jk.py::test_case[case16] FAILED
tmp_8szm6jk.py::test_case[case17] FAILED
tmp_8szm6jk.py::test_case[case18] FAILED
tmp_8szm6jk.py::test_case[case19] FAILED

=================================== FAILURES ===================================
_______________________________ test_case[case0] _______________________________

i = 0, inp = 'httpsunrux\n', expected = 'http://sun.ru/x\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='httpsunrux\n'
E         expected='http://sun.ru/x'
E         got='http://s.ru/unrux'
E       assert 'http://s.ru/unrux' == 'http://sun.ru/x'
E         - http://sun.ru/x
E         ?         --
E         + http://s.ru/unrux
E         ?             ++++

tmp_8szm6jk.py:27: AssertionError
_______________________________ test_case[case1] _______________________________

i = 1, inp = 'ftphttprururu\n', expected = 'ftp://http.ru/ruru\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='ftphttprururu\n'
E         expected='ftp://http.ru/ruru'
E         got='ftp://h.ru/ttprururu'
E       assert 'ftp://h.ru/ttprururu' == 'ftp://http.ru/ruru'
E         - ftp://http.ru/ruru
E         ?        ---
E         + ftp://h.ru/ttprururu
E         ?            +++    ++

tmp_8szm6jk.py:27: AssertionError
_______________________________ test_case[case2] _______________________________

i = 2, inp = 'httpuururrururruruurururrrrrurrurrurruruuruuu\n'
expected = 'http://uu.ru/rrururruruurururrrrrurrurrurruruuruuu\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='httpuururrururruruurururrrrrurrurrurruruuruuu\n'
E         expected='http://uu.ru/rrururruruurururrrrrurrurrurruruuruuu'
E         got='http://u.ru/ururrururruruurururrrrrurrurrurruruuruuu'
E       assert 'http://u.ru/...rrurruruuruuu' == 'http://uu.ru...rrurruruuruuu'
E         - http://uu.ru/rrururruruurururrrrrurrurrurruruuruuu
E         ?         -
E         + http://u.ru/ururrururruruurururrrrrurrurrurruruuruuu
E         ?             +++

tmp_8szm6jk.py:27: AssertionError
_______________________________ test_case[case3] _______________________________

i = 3, inp = 'httpabuaruauabbaruru\n', expected = 'http://abua.ru/auabbaruru\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='httpabuaruauabbaruru\n'
E         expected='http://abua.ru/auabbaruru'
E         got='http://a.ru/buaruauabbaruru'
E       assert 'http://a.ru/buaruauabbaruru' == 'http://abua.ru/auabbaruru'
E         - http://abua.ru/auabbaruru
E         ?         ---
E         + http://a.ru/buaruauabbaruru
E         ?             +++++

tmp_8szm6jk.py:27: AssertionError
_______________________________ test_case[case4] _______________________________

i = 4, inp = 'httpuurrruurruuruuruuurrrurururuurruuuuuuruurr\n'
expected = 'http://uurr.ru/urruuruuruuurrrurururuurruuuuuuruurr\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='httpuurrruurruuruuruuurrrurururuurruuuuuuruurr\n'
E         expected='http://uurr.ru/urruuruuruuurrrurururuurruuuuuuruurr'
E         got='http://u.ru/urrruurruuruuruuurrrurururuurruuuuuuruurr'
E       assert 'http://u.ru/...rruuuuuuruurr' == 'http://uurr....rruuuuuuruurr'
E         - http://uurr.ru/urruuruuruuurrrurururuurruuuuuuruurr
E         ?         ---
E         + http://u.ru/urrruurruuruuruuurrrurururuurruuuuuuruurr
E         ?             +++++

tmp_8szm6jk.py:27: AssertionError
_______________________________ test_case[case5] _______________________________

i = 5, inp = 'httpruhhphhhpuhruruhhpruhhphruhhru\n'
expected = 'http://ruhhphhhpuh.ru/ruhhpruhhphruhhru\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='httpruhhphhhpuhruruhhpruhhphruhhru\n'
E         expected='http://ruhhphhhpuh.ru/ruhhpruhhphruhhru'
E         got='http://r.ru/uhhphhhpuhruruhhpruhhphruhhru'
E       assert 'http://r.ru/...pruhhphruhhru' == 'http://ruhhp...pruhhphruhhru'
E         - http://ruhhphhhpuh.ru/ruhhpruhhphruhhru
E         ?                   -  -
E         + http://r.ru/uhhphhhpuhruruhhpruhhphruhhru
E         ?         ++++

tmp_8szm6jk.py:27: AssertionError
_______________________________ test_case[case6] _______________________________

i = 6, inp = 'httpftprftprutprururftruruftptp\n'
expected = 'http://ftprftp.ru/tprururftruruftptp\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='httpftprftprutprururftruruftptp\n'
E         expected='http://ftprftp.ru/tprururftruruftptp'
E         got='http://f.ru/tprftprutprururftruruftptp'
E       assert 'http://f.ru/...urftruruftptp' == 'http://ftprf...urftruruftptp'
E         - http://ftprftp.ru/tprururftruruftptp
E         ?               -  -
E         + http://f.ru/tprftprutprururftruruftptp
E         ?         ++++

tmp_8szm6jk.py:27: AssertionError
_______________________________ test_case[case7] _______________________________

i = 7, inp = 'httpfttpftpfttftpftpftppfrurururu\n'
expected = 'http://fttpftpfttftpftpftppf.ru/rururu\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='httpfttpftpfttftpftpftppfrurururu\n'
E         expected='http://fttpftpfttftpftpftppf.ru/rururu'
E         got='http://f.ru/ttpftpfttftpftpftppfrurururu'
E       assert 'http://f.ru/...ftppfrurururu' == 'http://fttpf...ppf.ru/rururu'
E         - http://fttpftpfttftpftpftppf.ru/rururu
E         ?                             ----
E         + http://f.ru/ttpftpfttftpftpftppfrurururu
E         ?         ++++                          ++

tmp_8szm6jk.py:27: AssertionError
_______________________________ test_case[case8] _______________________________

i = 8, inp = 'httpruhttttpruhttprupruhttpruhtturuhttphtruuru\n'
expected = 'http://ruhttttp.ru/httprupruhttpruhtturuhttphtruuru\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='httpruhttttpruhttprupruhttpruhtturuhttphtruuru\n'
E         expected='http://ruhttttp.ru/httprupruhttpruhtturuhttphtruuru'
E         got='http://r.ru/uhttttpruhttprupruhttpruhtturuhttphtruuru'
E       assert 'http://r.ru/...ruhttphtruuru' == 'http://ruhtt...ruhttphtruuru'
E         - http://ruhttttp.ru/httprupruhttpruhtturuhttphtruuru
E         ?                -  -
E         + http://r.ru/uhttttpruhttprupruhttpruhtturuhttphtruuru
E         ?         ++++

tmp_8szm6jk.py:27: AssertionError
_______________________________ test_case[case9] _______________________________

i = 9, inp = 'httpsjkazaaghasjkasjkabruru\n'
expected = 'http://sjkazaaghasjkasjkab.ru/ru\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='httpsjkazaaghasjkasjkabruru\n'
E         expected='http://sjkazaaghasjkasjkab.ru/ru'
E         got='http://s.ru/jkazaaghasjkasjkabruru'
E       assert 'http://s.ru/...sjkasjkabruru' == 'http://sjkaz...kasjkab.ru/ru'
E         - http://sjkazaaghasjkasjkab.ru/ru
E         ?                           -  -
E         + http://s.ru/jkazaaghasjkasjkabruru
E         ?         ++++

tmp_8szm6jk.py:27: AssertionError
______________________________ test_case[case10] _______________________________

i = 10, inp = 'httpftphttptphttphrururuhpftphtpftphtpftphtptpft\n'
expected = 'http://ftphttptphttph.ru/ruruhpftphtpftphtpftphtptpft\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='httpftphttptphttphrururuhpftphtpftphtpftphtptpft\n'
E         expected='http://ftphttptphttph.ru/ruruhpftphtpftphtpftphtptpft'
E         got='http://f.ru/tphttptphttphrururuhpftphtpftphtpftphtptpft'
E       assert 'http://f.ru/...htpftphtptpft' == 'http://ftpht...htpftphtptpft'
E         - http://ftphttptphttph.ru/ruruhpftphtpftphtpftphtptpft
E         ?                      -  -
E         + http://f.ru/tphttptphttphrururuhpftphtpftphtpftphtptpft
E         ?         ++++

tmp_8szm6jk.py:27: AssertionError
______________________________ test_case[case11] _______________________________

i = 11, inp = 'httpppppru\n', expected = 'http://pppp.ru\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='httpppppru\n'
E         expected='http://pppp.ru'
E         got='http://p.ru/pppru'
E       assert 'http://p.ru/pppru' == 'http://pppp.ru'
E         - http://pppp.ru
E         ?            -
E         + http://p.ru/pppru
E         ?         ++++

tmp_8szm6jk.py:27: AssertionError
______________________________ test_case[case12] _______________________________

i = 12, inp = 'ftprrurururrurururuurrururruuru\n'
expected = 'ftp://r.ru/rururrurururuurrururruuru\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='ftprrurururrurururuurrururruuru\n'
E         expected='ftp://r.ru/rururrurururuurrururruuru'
E         got='ftp://r.ru/rurururrurururuurrururruuru'
E       assert 'ftp://r.ru/r...uurrururruuru' == 'ftp://r.ru/r...uurrururruuru'
E         - ftp://r.ru/rururrurururuurrururruuru
E         + ftp://r.ru/rurururrurururuurrururruuru
E         ?            ++

tmp_8szm6jk.py:27: AssertionError
______________________________ test_case[case13] _______________________________

i = 13, inp = 'ftpabaruru\n', expected = 'ftp://aba.ru/ru\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='ftpabaruru\n'
E         expected='ftp://aba.ru/ru'
E         got='ftp://a.ru/baruru'
E       assert 'ftp://a.ru/baruru' == 'ftp://aba.ru/ru'
E         - ftp://aba.ru/ru
E         ?        --
E         + ftp://a.ru/baruru
E         ?            ++  ++

tmp_8szm6jk.py:27: AssertionError
______________________________ test_case[case14] _______________________________

i = 14, inp = 'ftpruurruurururururuuruuur\n'
expected = 'ftp://ruur.ru/urururururuuruuur\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='ftpruurruurururururuuruuur\n'
E         expected='ftp://ruur.ru/urururururuuruuur'
E         got='ftp://r.ru/uurruurururururuuruuur'
E       assert 'ftp://r.ru/u...urururuuruuur' == 'ftp://ruur.r...urururuuruuur'
E         - ftp://ruur.ru/urururururuuruuur
E         ?        ---
E         + ftp://r.ru/uurruurururururuuruuur
E         ?            +++++

tmp_8szm6jk.py:27: AssertionError
______________________________ test_case[case15] _______________________________

i = 15, inp = 'ftphhphruhhpruhhpuhhpuruhhphruhhruhhpuhhru\n'
expected = 'ftp://hhph.ru/hhpruhhpuhhpuruhhphruhhruhhpuhhru\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='ftphhphruhhpruhhpuhhpuruhhphruhhruhhpuhhru\n'
E         expected='ftp://hhph.ru/hhpruhhpuhhpuruhhphruhhruhhpuhhru'
E         got='ftp://h.ru/hphruhhpruhhpuhhpuruhhphruhhruhhpuhhru'
E       assert 'ftp://h.ru/h...uhhruhhpuhhru' == 'ftp://hhph.r...uhhruhhpuhhru'
E         - ftp://hhph.ru/hhpruhhpuhhpuruhhphruhhruhhpuhhru
E         ?        ---
E         + ftp://h.ru/hphruhhpruhhpuhhpuruhhphruhhruhhpuhhru
E         ?            +++++

tmp_8szm6jk.py:27: AssertionError
______________________________ test_case[case16] _______________________________

i = 16, inp = 'ftparua\n', expected = 'ftp://a.ru/a\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='ftparua\n'
E         expected='ftp://a.ru/a'
E         got='ftp://a.ru/rua'
E       assert 'ftp://a.ru/rua' == 'ftp://a.ru/a'
E         - ftp://a.ru/a
E         + ftp://a.ru/rua
E         ?            ++

tmp_8szm6jk.py:27: AssertionError
______________________________ test_case[case17] _______________________________

i = 17, inp = 'httpzru\n', expected = 'http://z.ru\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='httpzru\n'
E         expected='http://z.ru'
E         got=''
E       assert '' == 'http://z.ru'
E         - http://z.ru

tmp_8szm6jk.py:27: AssertionError
______________________________ test_case[case18] _______________________________

i = 18, inp = 'httprrur\n', expected = 'http://r.ru/r\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='httprrur\n'
E         expected='http://r.ru/r'
E         got='http://r.ru/rur'
E       assert 'http://r.ru/rur' == 'http://r.ru/r'
E         - http://r.ru/r
E         + http://r.ru/rur
E         ?              ++

tmp_8szm6jk.py:27: AssertionError
______________________________ test_case[case19] _______________________________

i = 19, inp = 'ftprru\n', expected = 'ftp://r.ru\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='ftprru\n'
E         expected='ftp://r.ru'
E         got=''
E       assert '' == 'ftp://r.ru'
E         - ftp://r.ru

tmp_8szm6jk.py:27: AssertionError
=========================== short test summary info ============================
FAILED tmp_8szm6jk.py::test_case[case0] - AssertionError: input='httpsunrux\n'
FAILED tmp_8szm6jk.py::test_case[case1] - AssertionError: input='ftphttprurur...
FAILED tmp_8szm6jk.py::test_case[case2] - AssertionError: input='httpuururrur...
FAILED tmp_8szm6jk.py::test_case[case3] - AssertionError: input='httpabuaruau...
FAILED tmp_8szm6jk.py::test_case[case4] - AssertionError: input='httpuurrruur...
FAILED tmp_8szm6jk.py::test_case[case5] - AssertionError: input='httpruhhphhh...
FAILED tmp_8szm6jk.py::test_case[case6] - AssertionError: input='httpftprftpr...
FAILED tmp_8szm6jk.py::test_case[case7] - AssertionError: input='httpfttpftpf...
FAILED tmp_8szm6jk.py::test_case[case8] - AssertionError: input='httpruhttttp...
FAILED tmp_8szm6jk.py::test_case[case9] - AssertionError: input='httpsjkazaag...
FAILED tmp_8szm6jk.py::test_case[case10] - AssertionError: input='httpftphttp...
FAILED tmp_8szm6jk.py::test_case[case11] - AssertionError: input='httpppppru\n'
FAILED tmp_8szm6jk.py::test_case[case12] - AssertionError: input='ftprrururur...
FAILED tmp_8szm6jk.py::test_case[case13] - AssertionError: input='ftpabaruru\n'
FAILED tmp_8szm6jk.py::test_case[case14] - AssertionError: input='ftpruurruur...
FAILED tmp_8szm6jk.py::test_case[case15] - AssertionError: input='ftphhphruhh...
FAILED tmp_8szm6jk.py::test_case[case16] - AssertionError: input='ftparua\n'
FAILED tmp_8szm6jk.py::test_case[case17] - AssertionError: input='httpzru\n'
FAILED tmp_8szm6jk.py::test_case[case18] - AssertionError: input='httprrur\n'
FAILED tmp_8szm6jk.py::test_case[case19] - AssertionError: input='ftprru\n'
============================== 20 failed in 3.97s ==============================
```
