# interview/437-a

**Status:** FAIL (exit code 1)

## stdout

```
============================= test session starts ==============================
platform linux -- Python 3.10.18, pytest-7.4.4, pluggy-1.6.0
PyQt5 5.15.10 -- Qt runtime 5.15.17 -- Qt compiled 5.15.2
rootdir: /tmp/tmprm7qlbz0
configfile: pytest.ini
plugins: Faker-25.1.0, anyio-4.9.0, cov-5.0.0, mock-3.12.0, qt-4.3.1
collected 35 items

tmpfhfdn43w.py::test_case[case0] PASSED
tmpfhfdn43w.py::test_case[case1] PASSED
tmpfhfdn43w.py::test_case[case2] PASSED
tmpfhfdn43w.py::test_case[case3] PASSED
tmpfhfdn43w.py::test_case[case4] PASSED
tmpfhfdn43w.py::test_case[case5] FAILED
tmpfhfdn43w.py::test_case[case6] PASSED
tmpfhfdn43w.py::test_case[case7] FAILED
tmpfhfdn43w.py::test_case[case8] FAILED
tmpfhfdn43w.py::test_case[case9] PASSED
tmpfhfdn43w.py::test_case[case10] PASSED
tmpfhfdn43w.py::test_case[case11] FAILED
tmpfhfdn43w.py::test_case[case12] PASSED
tmpfhfdn43w.py::test_case[case13] PASSED
tmpfhfdn43w.py::test_case[case14] PASSED
tmpfhfdn43w.py::test_case[case15] PASSED
tmpfhfdn43w.py::test_case[case16] FAILED
tmpfhfdn43w.py::test_case[case17] PASSED
tmpfhfdn43w.py::test_case[case18] PASSED
tmpfhfdn43w.py::test_case[case19] FAILED
tmpfhfdn43w.py::test_case[case20] PASSED
tmpfhfdn43w.py::test_case[case21] PASSED
tmpfhfdn43w.py::test_case[case22] PASSED
tmpfhfdn43w.py::test_case[case23] PASSED
tmpfhfdn43w.py::test_case[case24] PASSED
tmpfhfdn43w.py::test_case[case25] PASSED
tmpfhfdn43w.py::test_case[case26] PASSED
tmpfhfdn43w.py::test_case[case27] PASSED
tmpfhfdn43w.py::test_case[case28] PASSED
tmpfhfdn43w.py::test_case[case29] PASSED
tmpfhfdn43w.py::test_case[case30] PASSED
tmpfhfdn43w.py::test_case[case31] PASSED
tmpfhfdn43w.py::test_case[case32] PASSED
tmpfhfdn43w.py::test_case[case33] PASSED
tmpfhfdn43w.py::test_case[case34] PASSED

=================================== FAILURES ===================================
_______________________________ test_case[case5] _______________________________

i = 5
inp = 'A.G_R__iT_ow_Y__Sm_al__u_____l_ltK\nB.CWRe__h__cbCF\nC._QJ_dVHCL_g_WBsMO__LC____hMNE_DoO__xea_ec\nD.___Zh_\n'
expected = 'D\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='A.G_R__iT_ow_Y__Sm_al__u_____l_ltK\nB.CWRe__h__cbCF\nC._QJ_dVHCL_g_WBsMO__LC____hMNE_DoO__xea_ec\nD.___Zh_\n'
E         expected='D'
E         got='C'
E       assert 'C' == 'D'
E         - D
E         + C

tmpfhfdn43w.py:27: AssertionError
_______________________________ test_case[case7] _______________________________

i = 7
inp = 'A.G_R__iT_ow_Y__Sm_al__u_____l_ltK\nB.CWRe__h__cbCF\nC._QJ_dVHCL_g_WBsMO__LC____hMNE_DoO__xea_ec\nD.___Zh_\n'
expected = 'D\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='A.G_R__iT_ow_Y__Sm_al__u_____l_ltK\nB.CWRe__h__cbCF\nC._QJ_dVHCL_g_WBsMO__LC____hMNE_DoO__xea_ec\nD.___Zh_\n'
E         expected='D'
E         got='C'
E       assert 'C' == 'D'
E         - D
E         + C

tmpfhfdn43w.py:27: AssertionError
_______________________________ test_case[case8] _______________________________

i = 8
inp = 'A.ejQ_E_E_G_e_SDjZ__lh_f_K__Z_i_B_U__S__S_EMD_ZEU_Sq\nB.o_JpInEdsrAY_T__D_S\nC.E_Vp_s\nD.a_AU_h\n'
expected = 'A\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='A.ejQ_E_E_G_e_SDjZ__lh_f_K__Z_i_B_U__S__S_EMD_ZEU_Sq\nB.o_JpInEdsrAY_T__D_S\nC.E_Vp_s\nD.a_AU_h\n'
E         expected='A'
E         got='C'
E       assert 'C' == 'A'
E         - A
E         + C

tmpfhfdn43w.py:27: AssertionError
______________________________ test_case[case11] _______________________________

i = 11
inp = 'A.x_\nB.__RSiDT_\nC.Ci\nD.KLY_Hc_YN_xXg_DynydumheKTw_PFHo_vqXwm_DY_dA___OS_kG___\n'
expected = 'D\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='A.x_\nB.__RSiDT_\nC.Ci\nD.KLY_Hc_YN_xXg_DynydumheKTw_PFHo_vqXwm_DY_dA___OS_kG___\n'
E         expected='D'
E         got='C'
E       assert 'C' == 'D'
E         - D
E         + C

tmpfhfdn43w.py:27: AssertionError
______________________________ test_case[case16] _______________________________

i = 16
inp = 'A.ejQ_E_E_G_e_SDjZ__lh_f_K__Z_i_B_U__S__S_EMD_ZEU_Sq\nB.o_JpInEdsrAY_T__D_S\nC.E_Vp_s\nD.a_AU_h\n'
expected = 'A\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='A.ejQ_E_E_G_e_SDjZ__lh_f_K__Z_i_B_U__S__S_EMD_ZEU_Sq\nB.o_JpInEdsrAY_T__D_S\nC.E_Vp_s\nD.a_AU_h\n'
E         expected='A'
E         got='C'
E       assert 'C' == 'A'
E         - A
E         + C

tmpfhfdn43w.py:27: AssertionError
______________________________ test_case[case19] _______________________________

i = 19
inp = 'A.x_\nB.__RSiDT_\nC.Ci\nD.KLY_Hc_YN_xXg_DynydumheKTw_PFHo_vqXwm_DY_dA___OS_kG___\n'
expected = 'D\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='A.x_\nB.__RSiDT_\nC.Ci\nD.KLY_Hc_YN_xXg_DynydumheKTw_PFHo_vqXwm_DY_dA___OS_kG___\n'
E         expected='D'
E         got='C'
E       assert 'C' == 'D'
E         - D
E         + C

tmpfhfdn43w.py:27: AssertionError
=========================== short test summary info ============================
FAILED tmpfhfdn43w.py::test_case[case5] - AssertionError: input='A.G_R__iT_ow...
FAILED tmpfhfdn43w.py::test_case[case7] - AssertionError: input='A.G_R__iT_ow...
FAILED tmpfhfdn43w.py::test_case[case8] - AssertionError: input='A.ejQ_E_E_G_...
FAILED tmpfhfdn43w.py::test_case[case11] - AssertionError: input='A.x_\nB.__R...
FAILED tmpfhfdn43w.py::test_case[case16] - AssertionError: input='A.ejQ_E_E_G...
FAILED tmpfhfdn43w.py::test_case[case19] - AssertionError: input='A.x_\nB.__R...
========================= 6 failed, 29 passed in 6.68s =========================
```
