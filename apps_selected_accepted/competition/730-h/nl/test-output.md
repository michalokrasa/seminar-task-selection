# competition/730-h

**Status:** FAIL (exit code 1)

## stdout

```
============================= test session starts ==============================
platform linux -- Python 3.10.18, pytest-7.4.4, pluggy-1.6.0
PyQt5 5.15.10 -- Qt runtime 5.15.17 -- Qt compiled 5.15.2
rootdir: /tmp/tmp6vkkfza5
configfile: pytest.ini
plugins: Faker-25.1.0, anyio-4.9.0, cov-5.0.0, mock-3.12.0, qt-4.3.1
collected 34 items

tmp_2fi8fae.py::test_case[case0] FAILED
tmp_2fi8fae.py::test_case[case1] FAILED
tmp_2fi8fae.py::test_case[case2] FAILED
tmp_2fi8fae.py::test_case[case3] FAILED
tmp_2fi8fae.py::test_case[case4] FAILED
tmp_2fi8fae.py::test_case[case5] FAILED
tmp_2fi8fae.py::test_case[case6] FAILED
tmp_2fi8fae.py::test_case[case7] FAILED
tmp_2fi8fae.py::test_case[case8] FAILED
tmp_2fi8fae.py::test_case[case9] FAILED
tmp_2fi8fae.py::test_case[case10] FAILED
tmp_2fi8fae.py::test_case[case11] FAILED
tmp_2fi8fae.py::test_case[case12] FAILED
tmp_2fi8fae.py::test_case[case13] FAILED
tmp_2fi8fae.py::test_case[case14] FAILED
tmp_2fi8fae.py::test_case[case15] FAILED
tmp_2fi8fae.py::test_case[case16] FAILED
tmp_2fi8fae.py::test_case[case17] FAILED
tmp_2fi8fae.py::test_case[case18] FAILED
tmp_2fi8fae.py::test_case[case19] FAILED
tmp_2fi8fae.py::test_case[case20] FAILED
tmp_2fi8fae.py::test_case[case21] FAILED
tmp_2fi8fae.py::test_case[case22] FAILED
tmp_2fi8fae.py::test_case[case23] FAILED
tmp_2fi8fae.py::test_case[case24] FAILED
tmp_2fi8fae.py::test_case[case25] FAILED
tmp_2fi8fae.py::test_case[case26] FAILED
tmp_2fi8fae.py::test_case[case27] FAILED
tmp_2fi8fae.py::test_case[case28] FAILED
tmp_2fi8fae.py::test_case[case29] FAILED
tmp_2fi8fae.py::test_case[case30] FAILED
tmp_2fi8fae.py::test_case[case31] FAILED
tmp_2fi8fae.py::test_case[case32] FAILED
tmp_2fi8fae.py::test_case[case33] FAILED

=================================== FAILURES ===================================
_______________________________ test_case[case0] _______________________________

i = 0, inp = '3 2\nab\nac\ncd\n1 2\n', expected = 'Yes\na?\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='3 2\nab\nac\ncd\n1 2\n'
E         expected='Yes\na?'
E         got=''
E       assert '' == 'Yes\na?'
E         - Yes
E         - a?

tmp_2fi8fae.py:27: AssertionError
_______________________________ test_case[case1] _______________________________

i = 1, inp = '5 3\ntest\ntezt\ntest.\n.est\ntes.\n1 4 5\n'
expected = 'Yes\n?es?\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='5 3\ntest\ntezt\ntest.\n.est\ntes.\n1 4 5\n'
E         expected='Yes\n?es?'
E         got=''
E       assert '' == 'Yes\n?es?'
E         - Yes
E         - ?es?

tmp_2fi8fae.py:27: AssertionError
_______________________________ test_case[case2] _______________________________

i = 2, inp = '4 4\na\nb\nc\ndd\n1 2 3 4\n', expected = 'No\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='4 4\na\nb\nc\ndd\n1 2 3 4\n'
E         expected='No'
E         got=''
E       assert '' == 'No'
E         - No

tmp_2fi8fae.py:27: AssertionError
_______________________________ test_case[case3] _______________________________

i = 3, inp = '6 3\n.svn\n.git\n....\n...\n..\n.\n1 2 3\n'
expected = 'Yes\n.???\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='6 3\n.svn\n.git\n....\n...\n..\n.\n1 2 3\n'
E         expected='Yes\n.???'
E         got=''
E       assert '' == 'Yes\n.???'
E         - Yes
E         - .???

tmp_2fi8fae.py:27: AssertionError
_______________________________ test_case[case4] _______________________________

i = 4, inp = '4 2\n.b\n.c\ndbt\ne.\n2 4\n', expected = 'No\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='4 2\n.b\n.c\ndbt\ne.\n2 4\n'
E         expected='No'
E         got=''
E       assert '' == 'No'
E         - No

tmp_2fi8fae.py:27: AssertionError
_______________________________ test_case[case5] _______________________________

i = 5
inp = '27 27\na\nb\nc\nd\ne\nf\ng\nh\ni\nj\nk\nl\nm\nn\no\np\nq\nr\ns\nt\nu\nv\nw\nx\ny\nz\n.\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27\n'
expected = 'Yes\n?\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='27 27\na\nb\nc\nd\ne\nf\ng\nh\ni\nj\nk\nl\nm\nn\no\np\nq\nr\ns\nt\nu\nv\nw\nx\ny\nz\n.\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27\n'
E         expected='Yes\n?'
E         got=''
E       assert '' == 'Yes\n?'
E         - Yes
E         - ?

tmp_2fi8fae.py:27: AssertionError
_______________________________ test_case[case6] _______________________________

i = 6
inp = '27 26\na\nb\nc\nd\nee\nf\ng\nh\ni\nj\nk\nl\nm\nn\no\np\nq\nr\ns\nt\nu\nv\nw\nx\ny\nz\n.\n1 2 3 4 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27\n'
expected = 'Yes\n?\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='27 26\na\nb\nc\nd\nee\nf\ng\nh\ni\nj\nk\nl\nm\nn\no\np\nq\nr\ns\nt\nu\nv\nw\nx\ny\nz\n.\n1 2 3 4 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27\n'
E         expected='Yes\n?'
E         got=''
E       assert '' == 'Yes\n?'
E         - Yes
E         - ?

tmp_2fi8fae.py:27: AssertionError
_______________________________ test_case[case7] _______________________________

i = 7
inp = '27 26\na\nb\nc\nd\ne\nf\ng\nh\ni\nj\nkq\nl\nm\nn\no\np\nq\nr\ns\nt\nu\nv\nw\nx\ny\nz\n.\n1 2 3 4 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27\n'
expected = 'No\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='27 26\na\nb\nc\nd\ne\nf\ng\nh\ni\nj\nkq\nl\nm\nn\no\np\nq\nr\ns\nt\nu\nv\nw\nx\ny\nz\n.\n1 2 3 4 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27\n'
E         expected='No'
E         got=''
E       assert '' == 'No'
E         - No

tmp_2fi8fae.py:27: AssertionError
_______________________________ test_case[case8] _______________________________

i = 8, inp = '1 1\nuevim.mrr\n1\n', expected = 'Yes\nuevim.mrr\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='1 1\nuevim.mrr\n1\n'
E         expected='Yes\nuevim.mrr'
E         got=''
E       assert '' == 'Yes\nuevim.mrr'
E         - Yes
E         - uevim.mrr

tmp_2fi8fae.py:27: AssertionError
_______________________________ test_case[case9] _______________________________

i = 9, inp = '2 1\nkbfyvezmy\nsbfammwcy\n1\n', expected = 'Yes\nkbfyvezmy\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='2 1\nkbfyvezmy\nsbfammwcy\n1\n'
E         expected='Yes\nkbfyvezmy'
E         got=''
E       assert '' == 'Yes\nkbfyvezmy'
E         - Yes
E         - kbfyvezmy

tmp_2fi8fae.py:27: AssertionError
______________________________ test_case[case10] _______________________________

i = 10
inp = '5 3\nlmljeqklg\nlclydkkxj\nuylscbk.g\neplpqakme\nablibhkfg\n1 3 5\n'
expected = 'Yes\n??l???k?g\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='5 3\nlmljeqklg\nlclydkkxj\nuylscbk.g\neplpqakme\nablibhkfg\n1 3 5\n'
E         expected='Yes\n??l???k?g'
E         got=''
E       assert '' == 'Yes\n??l???k?g'
E         - Yes
E         - ??l???k?g

tmp_2fi8fae.py:27: AssertionError
______________________________ test_case[case11] _______________________________

i = 11, inp = '5 4\nabacaba\naaaaaaa\naaaaaab\naaaaaac\naaaaaad\n2 3 4 5\n'
expected = 'Yes\naaaaaa?\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='5 4\nabacaba\naaaaaaa\naaaaaab\naaaaaac\naaaaaad\n2 3 4 5\n'
E         expected='Yes\naaaaaa?'
E         got=''
E       assert '' == 'Yes\naaaaaa?'
E         - Yes
E         - aaaaaa?

tmp_2fi8fae.py:27: AssertionError
______________________________ test_case[case12] _______________________________

i = 12, inp = '5 4\nabacaba\naaaaaaa\nbaaaaab\ncaaaaac\ndaaaaad\n2 3 4 5\n'
expected = 'Yes\n?aaaaa?\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='5 4\nabacaba\naaaaaaa\nbaaaaab\ncaaaaac\ndaaaaad\n2 3 4 5\n'
E         expected='Yes\n?aaaaa?'
E         got=''
E       assert '' == 'Yes\n?aaaaa?'
E         - Yes
E         - ?aaaaa?

tmp_2fi8fae.py:27: AssertionError
______________________________ test_case[case13] _______________________________

i = 13, inp = '5 5\nabacaba\naaaaaaa\nbaaaaab\ncaaaaac\ndaaaaad\n1 2 3 4 5\n'
expected = 'Yes\n??a?a??\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='5 5\nabacaba\naaaaaaa\nbaaaaab\ncaaaaac\ndaaaaad\n1 2 3 4 5\n'
E         expected='Yes\n??a?a??'
E         got=''
E       assert '' == 'Yes\n??a?a??'
E         - Yes
E         - ??a?a??

tmp_2fi8fae.py:27: AssertionError
______________________________ test_case[case14] _______________________________

i = 14, inp = '5 3\nabacaba\naaaaaaa\nbaaaaab\ncaaaaac\ndaaaaad\n2 3 4\n'
expected = 'No\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='5 3\nabacaba\naaaaaaa\nbaaaaab\ncaaaaac\ndaaaaad\n2 3 4\n'
E         expected='No'
E         got=''
E       assert '' == 'No'
E         - No

tmp_2fi8fae.py:27: AssertionError
______________________________ test_case[case15] _______________________________

i = 15, inp = '5 4\naaaaaaa\nbaaaaab\ncaaaaac\ndaaaaad\nabacaba\n1 2 3 4\n'
expected = 'Yes\n?aaaaa?\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='5 4\naaaaaaa\nbaaaaab\ncaaaaac\ndaaaaad\nabacaba\n1 2 3 4\n'
E         expected='Yes\n?aaaaa?'
E         got=''
E       assert '' == 'Yes\n?aaaaa?'
E         - Yes
E         - ?aaaaa?

tmp_2fi8fae.py:27: AssertionError
______________________________ test_case[case16] _______________________________

i = 16
inp = '5 3\naaaaaaaaaa\nbbbbbbbbbb\ncccccccccc\ndddddddddd\neeeeeeeeee\n1 3 5\n'
expected = 'No\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='5 3\naaaaaaaaaa\nbbbbbbbbbb\ncccccccccc\ndddddddddd\neeeeeeeeee\n1 3 5\n'
E         expected='No'
E         got=''
E       assert '' == 'No'
E         - No

tmp_2fi8fae.py:27: AssertionError
______________________________ test_case[case17] _______________________________

i = 17
inp = '5 4\naaaaaaaaaa\nbbbbbbbbbb\ncccccccccc\ndddddddddd\neeeeeeeeee\n1 3 4 5\n'
expected = 'No\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='5 4\naaaaaaaaaa\nbbbbbbbbbb\ncccccccccc\ndddddddddd\neeeeeeeeee\n1 3 4 5\n'
E         expected='No'
E         got=''
E       assert '' == 'No'
E         - No

tmp_2fi8fae.py:27: AssertionError
______________________________ test_case[case18] _______________________________

i = 18
inp = '5 5\naaaaaaaaaa\nbbbbbbbbbb\ncccccccccc\ndddddddddd\neeeeeeeeee\n1 2 3 4 5\n'
expected = 'Yes\n??????????\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='5 5\naaaaaaaaaa\nbbbbbbbbbb\ncccccccccc\ndddddddddd\neeeeeeeeee\n1 2 3 4 5\n'
E         expected='Yes\n??????????'
E         got=''
E       assert '' == 'Yes\n??????????'
E         - Yes
E         - ??????????

tmp_2fi8fae.py:27: AssertionError
______________________________ test_case[case19] _______________________________

i = 19
inp = '5 4\naaaaaaaaaa\nbbbbbbbbbb\ncccccccccc\ndddddddddd\neeeeeeeee\n1 2 3 4\n'
expected = 'Yes\n??????????\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='5 4\naaaaaaaaaa\nbbbbbbbbbb\ncccccccccc\ndddddddddd\neeeeeeeee\n1 2 3 4\n'
E         expected='Yes\n??????????'
E         got=''
E       assert '' == 'Yes\n??????????'
E         - Yes
E         - ??????????

tmp_2fi8fae.py:27: AssertionError
______________________________ test_case[case20] _______________________________

i = 20
inp = '5 4\naaaaaaaaaa\nbbbbbbbbbb\ncccccccccc\neeeeeeeee\ndddddddddd\n1 2 3 5\n'
expected = 'Yes\n??????????\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='5 4\naaaaaaaaaa\nbbbbbbbbbb\ncccccccccc\neeeeeeeee\ndddddddddd\n1 2 3 5\n'
E         expected='Yes\n??????????'
E         got=''
E       assert '' == 'Yes\n??????????'
E         - Yes
E         - ??????????

tmp_2fi8fae.py:27: AssertionError
______________________________ test_case[case21] _______________________________

i = 21
inp = '5 4\naaaaaaaaaa\nbbbbbbbbbb\neeeeeeeee\ncccccccccc\ndddddddddd\n1 2 4 5\n'
expected = 'Yes\n??????????\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='5 4\naaaaaaaaaa\nbbbbbbbbbb\neeeeeeeee\ncccccccccc\ndddddddddd\n1 2 4 5\n'
E         expected='Yes\n??????????'
E         got=''
E       assert '' == 'Yes\n??????????'
E         - Yes
E         - ??????????

tmp_2fi8fae.py:27: AssertionError
______________________________ test_case[case22] _______________________________

i = 22
inp = '5 4\naaaaaaaaaa\neeeeeeeee\nbbbbbbbbbb\ncccccccccc\ndddddddddd\n1 3 4 5\n'
expected = 'Yes\n??????????\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='5 4\naaaaaaaaaa\neeeeeeeee\nbbbbbbbbbb\ncccccccccc\ndddddddddd\n1 3 4 5\n'
E         expected='Yes\n??????????'
E         got=''
E       assert '' == 'Yes\n??????????'
E         - Yes
E         - ??????????

tmp_2fi8fae.py:27: AssertionError
______________________________ test_case[case23] _______________________________

i = 23
inp = '5 4\neeeeeeeee\naaaaaaaaaa\nbbbbbbbbbb\ncccccccccc\ndddddddddd\n2 3 4 5\n'
expected = 'Yes\n??????????\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='5 4\neeeeeeeee\naaaaaaaaaa\nbbbbbbbbbb\ncccccccccc\ndddddddddd\n2 3 4 5\n'
E         expected='Yes\n??????????'
E         got=''
E       assert '' == 'Yes\n??????????'
E         - Yes
E         - ??????????

tmp_2fi8fae.py:27: AssertionError
______________________________ test_case[case24] _______________________________

i = 24, inp = '2 1\na\nb\n1\n', expected = 'Yes\na\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='2 1\na\nb\n1\n'
E         expected='Yes\na'
E         got=''
E       assert '' == 'Yes\na'
E         - Yes
E         - a

tmp_2fi8fae.py:27: AssertionError
______________________________ test_case[case25] _______________________________

i = 25, inp = '2 1\na\nb\n2\n', expected = 'Yes\nb\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='2 1\na\nb\n2\n'
E         expected='Yes\nb'
E         got=''
E       assert '' == 'Yes\nb'
E         - Yes
E         - b

tmp_2fi8fae.py:27: AssertionError
______________________________ test_case[case26] _______________________________

i = 26, inp = '2 2\na\nb\n1 2\n', expected = 'Yes\n?\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='2 2\na\nb\n1 2\n'
E         expected='Yes\n?'
E         got=''
E       assert '' == 'Yes\n?'
E         - Yes
E         - ?

tmp_2fi8fae.py:27: AssertionError
______________________________ test_case[case27] _______________________________

i = 27, inp = '2 1\naa\nb\n1\n', expected = 'Yes\naa\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='2 1\naa\nb\n1\n'
E         expected='Yes\naa'
E         got=''
E       assert '' == 'Yes\naa'
E         - Yes
E         - aa

tmp_2fi8fae.py:27: AssertionError
______________________________ test_case[case28] _______________________________

i = 28, inp = '2 1\naa\nb\n2\n', expected = 'Yes\nb\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='2 1\naa\nb\n2\n'
E         expected='Yes\nb'
E         got=''
E       assert '' == 'Yes\nb'
E         - Yes
E         - b

tmp_2fi8fae.py:27: AssertionError
______________________________ test_case[case29] _______________________________

i = 29, inp = '2 2\naa\nb\n1 2\n', expected = 'No\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='2 2\naa\nb\n1 2\n'
E         expected='No'
E         got=''
E       assert '' == 'No'
E         - No

tmp_2fi8fae.py:27: AssertionError
______________________________ test_case[case30] _______________________________

i = 30, inp = '2 1\nb\naa\n1\n', expected = 'Yes\nb\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='2 1\nb\naa\n1\n'
E         expected='Yes\nb'
E         got=''
E       assert '' == 'Yes\nb'
E         - Yes
E         - b

tmp_2fi8fae.py:27: AssertionError
______________________________ test_case[case31] _______________________________

i = 31, inp = '2 1\nb\naa\n2\n', expected = 'Yes\naa\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='2 1\nb\naa\n2\n'
E         expected='Yes\naa'
E         got=''
E       assert '' == 'Yes\naa'
E         - Yes
E         - aa

tmp_2fi8fae.py:27: AssertionError
______________________________ test_case[case32] _______________________________

i = 32, inp = '2 2\nb\naa\n1 2\n', expected = 'No\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='2 2\nb\naa\n1 2\n'
E         expected='No'
E         got=''
E       assert '' == 'No'
E         - No

tmp_2fi8fae.py:27: AssertionError
______________________________ test_case[case33] _______________________________

i = 33
inp = '2 1\naaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab\naaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaac\n1\n'
expected = 'Yes\naaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='2 1\naaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab\naaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaac\n1\n'
E         expected='Yes\naaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab'
E         got=''
E       assert '' == 'Yes\naaaaaaa...aaaaaaaaaaaab'
E         - Yes
E         - aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab

tmp_2fi8fae.py:27: AssertionError
=========================== short test summary info ============================
FAILED tmp_2fi8fae.py::test_case[case0] - AssertionError: input='3 2\nab\nac\...
FAILED tmp_2fi8fae.py::test_case[case1] - AssertionError: input='5 3\ntest\nt...
FAILED tmp_2fi8fae.py::test_case[case2] - AssertionError: input='4 4\na\nb\nc...
FAILED tmp_2fi8fae.py::test_case[case3] - AssertionError: input='6 3\n.svn\n....
FAILED tmp_2fi8fae.py::test_case[case4] - AssertionError: input='4 2\n.b\n.c\...
FAILED tmp_2fi8fae.py::test_case[case5] - AssertionError: input='27 27\na\nb\...
FAILED tmp_2fi8fae.py::test_case[case6] - AssertionError: input='27 26\na\nb\...
FAILED tmp_2fi8fae.py::test_case[case7] - AssertionError: input='27 26\na\nb\...
FAILED tmp_2fi8fae.py::test_case[case8] - AssertionError: input='1 1\nuevim.m...
FAILED tmp_2fi8fae.py::test_case[case9] - AssertionError: input='2 1\nkbfyvez...
FAILED tmp_2fi8fae.py::test_case[case10] - AssertionError: input='5 3\nlmljeq...
FAILED tmp_2fi8fae.py::test_case[case11] - AssertionError: input='5 4\nabacab...
FAILED tmp_2fi8fae.py::test_case[case12] - AssertionError: input='5 4\nabacab...
FAILED tmp_2fi8fae.py::test_case[case13] - AssertionError: input='5 5\nabacab...
FAILED tmp_2fi8fae.py::test_case[case14] - AssertionError: input='5 3\nabacab...
FAILED tmp_2fi8fae.py::test_case[case15] - AssertionError: input='5 4\naaaaaa...
FAILED tmp_2fi8fae.py::test_case[case16] - AssertionError: input='5 3\naaaaaa...
FAILED tmp_2fi8fae.py::test_case[case17] - AssertionError: input='5 4\naaaaaa...
FAILED tmp_2fi8fae.py::test_case[case18] - AssertionError: input='5 5\naaaaaa...
FAILED tmp_2fi8fae.py::test_case[case19] - AssertionError: input='5 4\naaaaaa...
FAILED tmp_2fi8fae.py::test_case[case20] - AssertionError: input='5 4\naaaaaa...
FAILED tmp_2fi8fae.py::test_case[case21] - AssertionError: input='5 4\naaaaaa...
FAILED tmp_2fi8fae.py::test_case[case22] - AssertionError: input='5 4\naaaaaa...
FAILED tmp_2fi8fae.py::test_case[case23] - AssertionError: input='5 4\neeeeee...
FAILED tmp_2fi8fae.py::test_case[case24] - AssertionError: input='2 1\na\nb\n...
FAILED tmp_2fi8fae.py::test_case[case25] - AssertionError: input='2 1\na\nb\n...
FAILED tmp_2fi8fae.py::test_case[case26] - AssertionError: input='2 2\na\nb\n...
FAILED tmp_2fi8fae.py::test_case[case27] - AssertionError: input='2 1\naa\nb\...
FAILED tmp_2fi8fae.py::test_case[case28] - AssertionError: input='2 1\naa\nb\...
FAILED tmp_2fi8fae.py::test_case[case29] - AssertionError: input='2 2\naa\nb\...
FAILED tmp_2fi8fae.py::test_case[case30] - AssertionError: input='2 1\nb\naa\...
FAILED tmp_2fi8fae.py::test_case[case31] - AssertionError: input='2 1\nb\naa\...
FAILED tmp_2fi8fae.py::test_case[case32] - AssertionError: input='2 2\nb\naa\...
FAILED tmp_2fi8fae.py::test_case[case33] - AssertionError: input='2 1\naaaaaa...
============================== 34 failed in 6.59s ==============================
```
