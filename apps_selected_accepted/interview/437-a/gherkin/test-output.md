# interview/437-a

**Status:** FAIL (exit code 1)

## stdout

```
============================= test session starts ==============================
platform linux -- Python 3.10.18, pytest-7.4.4, pluggy-1.6.0
PyQt5 5.15.10 -- Qt runtime 5.15.17 -- Qt compiled 5.15.2
rootdir: /tmp/tmpycnwxqs6
configfile: pytest.ini
plugins: Faker-25.1.0, anyio-4.9.0, cov-5.0.0, mock-3.12.0, qt-4.3.1
collected 35 items

tmp56hchxz8.py::test_case[case0] FAILED
tmp56hchxz8.py::test_case[case1] FAILED
tmp56hchxz8.py::test_case[case2] FAILED
tmp56hchxz8.py::test_case[case3] FAILED
tmp56hchxz8.py::test_case[case4] FAILED
tmp56hchxz8.py::test_case[case5] FAILED
tmp56hchxz8.py::test_case[case6] FAILED
tmp56hchxz8.py::test_case[case7] FAILED
tmp56hchxz8.py::test_case[case8] FAILED
tmp56hchxz8.py::test_case[case9] FAILED
tmp56hchxz8.py::test_case[case10] FAILED
tmp56hchxz8.py::test_case[case11] FAILED
tmp56hchxz8.py::test_case[case12] FAILED
tmp56hchxz8.py::test_case[case13] FAILED
tmp56hchxz8.py::test_case[case14] FAILED
tmp56hchxz8.py::test_case[case15] FAILED
tmp56hchxz8.py::test_case[case16] FAILED
tmp56hchxz8.py::test_case[case17] FAILED
tmp56hchxz8.py::test_case[case18] FAILED
tmp56hchxz8.py::test_case[case19] FAILED
tmp56hchxz8.py::test_case[case20] FAILED
tmp56hchxz8.py::test_case[case21] FAILED
tmp56hchxz8.py::test_case[case22] FAILED
tmp56hchxz8.py::test_case[case23] FAILED
tmp56hchxz8.py::test_case[case24] FAILED
tmp56hchxz8.py::test_case[case25] FAILED
tmp56hchxz8.py::test_case[case26] FAILED
tmp56hchxz8.py::test_case[case27] FAILED
tmp56hchxz8.py::test_case[case28] FAILED
tmp56hchxz8.py::test_case[case29] FAILED
tmp56hchxz8.py::test_case[case30] FAILED
tmp56hchxz8.py::test_case[case31] FAILED
tmp56hchxz8.py::test_case[case32] FAILED
tmp56hchxz8.py::test_case[case33] FAILED
tmp56hchxz8.py::test_case[case34] FAILED

=================================== FAILURES ===================================
_______________________________ test_case[case0] _______________________________

i = 0
inp = 'A.VFleaKing_is_the_author_of_this_problem\nB.Picks_is_the_author_of_this_problem\nC.Picking_is_the_author_of_this_problem\nD.Ftiasch_is_cute\n'
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
E       AssertionError: input='A.VFleaKing_is_the_author_of_this_problem\nB.Picks_is_the_author_of_this_problem\nC.Picking_is_the_author_of_this_problem\nD.Ftiasch_is_cute\n'
E         expected='D'
E         got=''
E       assert '' == 'D'
E         - D

tmp56hchxz8.py:27: AssertionError
_______________________________ test_case[case1] _______________________________

i = 1, inp = 'A.ab\nB.abcde\nC.ab\nD.abc\n', expected = 'C\n'

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
E       AssertionError: input='A.ab\nB.abcde\nC.ab\nD.abc\n'
E         expected='C'
E         got=''
E       assert '' == 'C'
E         - C

tmp56hchxz8.py:27: AssertionError
_______________________________ test_case[case2] _______________________________

i = 2, inp = 'A.c\nB.cc\nC.c\nD.c\n', expected = 'B\n'

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
E       AssertionError: input='A.c\nB.cc\nC.c\nD.c\n'
E         expected='B'
E         got=''
E       assert '' == 'B'
E         - B

tmp56hchxz8.py:27: AssertionError
_______________________________ test_case[case3] _______________________________

i = 3
inp = 'A.He_nan_de_yang_guang_zhao_yao_zhe_wo_men_mei_guo_ren_lian_shang_dou_xiao_kai_yan_wahaaaaaaaaaaaaaaaa\nB.Li_bai_li_b..._shen_le_a_a\nD.Wo_huo_le_si_shi_er_nian_zhen_de_shi_cong_lai_ye_mei_you_jian_guo_zhe_me_biao_zhun_de_yi_bai_ge_zi_a\n'
expected = 'C\n'

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
E       AssertionError: input='A.He_nan_de_yang_guang_zhao_yao_zhe_wo_men_mei_guo_ren_lian_shang_dou_xiao_kai_yan_wahaaaaaaaaaaaaaaaa\nB.Li_bai_li_bai_fei_liu_zhi_xia_san_qian_chi_yi_si_yin_he_luo_jiu_tian_li_bai_li_bai_li_bai_li_bai_shi\nC.Peng_yu_xiang_shi_zai_tai_shen_le_jian_zhi_jiu_shi_ye_jie_du_liu_a_si_mi_da_zhen_shi_tai_shen_le_a_a\nD.Wo_huo_le_si_shi_er_nian_zhen_de_shi_cong_lai_ye_mei_you_jian_guo_zhe_me_biao_zhun_de_yi_bai_ge_zi_a\n'
E         expected='C'
E         got=''
E       assert '' == 'C'
E         - C

tmp56hchxz8.py:27: AssertionError
_______________________________ test_case[case4] _______________________________

i = 4
inp = 'A.a___FXIcs_gB____dxFFzst_p_P_Xp_vS__cS_C_ei_\nB.fmnmkS_SeZYx_tSys_d__Exbojv_a_YPEL_BPj__I_aYH\nC._nrPx_j\nD.o_A_UwmNbC_sZ_AXk_Y___i_SN_U_UxrBN_qo_____\n'
expected = 'C\n'

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
E       AssertionError: input='A.a___FXIcs_gB____dxFFzst_p_P_Xp_vS__cS_C_ei_\nB.fmnmkS_SeZYx_tSys_d__Exbojv_a_YPEL_BPj__I_aYH\nC._nrPx_j\nD.o_A_UwmNbC_sZ_AXk_Y___i_SN_U_UxrBN_qo_____\n'
E         expected='C'
E         got=''
E       assert '' == 'C'
E         - C

tmp56hchxz8.py:27: AssertionError
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
E         got=''
E       assert '' == 'D'
E         - D

tmp56hchxz8.py:27: AssertionError
_______________________________ test_case[case6] _______________________________

i = 6
inp = 'A.a___FXIcs_gB____dxFFzst_p_P_Xp_vS__cS_C_ei_\nB.fmnmkS_SeZYx_tSys_d__Exbojv_a_YPEL_BPj__I_aYH\nC._nrPx_j\nD.o_A_UwmNbC_sZ_AXk_Y___i_SN_U_UxrBN_qo_____\n'
expected = 'C\n'

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
E       AssertionError: input='A.a___FXIcs_gB____dxFFzst_p_P_Xp_vS__cS_C_ei_\nB.fmnmkS_SeZYx_tSys_d__Exbojv_a_YPEL_BPj__I_aYH\nC._nrPx_j\nD.o_A_UwmNbC_sZ_AXk_Y___i_SN_U_UxrBN_qo_____\n'
E         expected='C'
E         got=''
E       assert '' == 'C'
E         - C

tmp56hchxz8.py:27: AssertionError
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
E         got=''
E       assert '' == 'D'
E         - D

tmp56hchxz8.py:27: AssertionError
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
E         got=''
E       assert '' == 'A'
E         - A

tmp56hchxz8.py:27: AssertionError
_______________________________ test_case[case9] _______________________________

i = 9
inp = 'A.PN_m_P_qgOAMwDyxtbH__Yc__bPOh_wYH___n_Fv_qlZp_\nB._gLeDU__rr_vjrm__O_jl_R__DG___u_XqJjW_\nC.___sHLQzdTzT_tZ_Gs\nD.sZNcVa__M_To_bz_clFi_mH_\n'
expected = 'C\n'

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
E       AssertionError: input='A.PN_m_P_qgOAMwDyxtbH__Yc__bPOh_wYH___n_Fv_qlZp_\nB._gLeDU__rr_vjrm__O_jl_R__DG___u_XqJjW_\nC.___sHLQzdTzT_tZ_Gs\nD.sZNcVa__M_To_bz_clFi_mH_\n'
E         expected='C'
E         got=''
E       assert '' == 'C'
E         - C

tmp56hchxz8.py:27: AssertionError
______________________________ test_case[case10] _______________________________

i = 10
inp = 'A.bR___cCYJg_Wbt____cxfXfC____c_O_\nB.guM\nC.__bzsH_Of__RjG__u_w_i__PXQL_U_Ow_U_n\nD._nHIuZsu_uU_stRC_k___vD_ZOD_u_z_c_Zf__p_iF_uD_Hdg\n'
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
E       AssertionError: input='A.bR___cCYJg_Wbt____cxfXfC____c_O_\nB.guM\nC.__bzsH_Of__RjG__u_w_i__PXQL_U_Ow_U_n\nD._nHIuZsu_uU_stRC_k___vD_ZOD_u_z_c_Zf__p_iF_uD_Hdg\n'
E         expected='B'
E         got=''
E       assert '' == 'B'
E         - B

tmp56hchxz8.py:27: AssertionError
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
E         got=''
E       assert '' == 'D'
E         - D

tmp56hchxz8.py:27: AssertionError
______________________________ test_case[case12] _______________________________

i = 12
inp = 'A.yYGJ_C__NYq_\nB.ozMUZ_cKKk_zVUPR_b_g_ygv_HoM__yAxvh__iE\nC.sgHJ___MYP__AWejchRvjSD_o\nD.gkfF_GiOqW_psMT_eS\n'
expected = 'C\n'

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
E       AssertionError: input='A.yYGJ_C__NYq_\nB.ozMUZ_cKKk_zVUPR_b_g_ygv_HoM__yAxvh__iE\nC.sgHJ___MYP__AWejchRvjSD_o\nD.gkfF_GiOqW_psMT_eS\n'
E         expected='C'
E         got=''
E       assert '' == 'C'
E         - C

tmp56hchxz8.py:27: AssertionError
______________________________ test_case[case13] _______________________________

i = 13
inp = 'A._LYm_nvl_E__RCFZ_IdO\nB.k__qIPO_ivvZyIG__L_\nC.D_SabLm_R___j_HS_t__\nD._adj_R_ngix____GSe_aw__SbOOl_\n'
expected = 'C\n'

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
E       AssertionError: input='A._LYm_nvl_E__RCFZ_IdO\nB.k__qIPO_ivvZyIG__L_\nC.D_SabLm_R___j_HS_t__\nD._adj_R_ngix____GSe_aw__SbOOl_\n'
E         expected='C'
E         got=''
E       assert '' == 'C'
E         - C

tmp56hchxz8.py:27: AssertionError
______________________________ test_case[case14] _______________________________

i = 14
inp = 'A.h_WiYTD_C_h___z_Gn_Th_uNh__g___jm\nB.__HeQaudCJcYfVi__Eg_vryuQrDkb_g__oy_BwX_Mu_\nC._MChdMhQA_UKrf_LGZk_ALTo_mnry_GNNza_X_D_u____ueJb__Y_h__CNUNDfmZATck_ad_XTbG\nD.NV___OoL__GfP_CqhD__RB_____v_T_xi\n'
expected = 'C\n'

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
E       AssertionError: input='A.h_WiYTD_C_h___z_Gn_Th_uNh__g___jm\nB.__HeQaudCJcYfVi__Eg_vryuQrDkb_g__oy_BwX_Mu_\nC._MChdMhQA_UKrf_LGZk_ALTo_mnry_GNNza_X_D_u____ueJb__Y_h__CNUNDfmZATck_ad_XTbG\nD.NV___OoL__GfP_CqhD__RB_____v_T_xi\n'
E         expected='C'
E         got=''
E       assert '' == 'C'
E         - C

tmp56hchxz8.py:27: AssertionError
______________________________ test_case[case15] _______________________________

i = 15
inp = 'A.____JGWsfiU\nB.S_LMq__MpE_oFBs_P\nC.U_Rph_VHpUr____X_jWXbk__ElJTu_Z_wlBpKLTD\nD.p_ysvPNmbrF__\n'
expected = 'C\n'

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
E       AssertionError: input='A.____JGWsfiU\nB.S_LMq__MpE_oFBs_P\nC.U_Rph_VHpUr____X_jWXbk__ElJTu_Z_wlBpKLTD\nD.p_ysvPNmbrF__\n'
E         expected='C'
E         got=''
E       assert '' == 'C'
E         - C

tmp56hchxz8.py:27: AssertionError
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
E         got=''
E       assert '' == 'A'
E         - A

tmp56hchxz8.py:27: AssertionError
______________________________ test_case[case17] _______________________________

i = 17
inp = 'A.PN_m_P_qgOAMwDyxtbH__Yc__bPOh_wYH___n_Fv_qlZp_\nB._gLeDU__rr_vjrm__O_jl_R__DG___u_XqJjW_\nC.___sHLQzdTzT_tZ_Gs\nD.sZNcVa__M_To_bz_clFi_mH_\n'
expected = 'C\n'

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
E       AssertionError: input='A.PN_m_P_qgOAMwDyxtbH__Yc__bPOh_wYH___n_Fv_qlZp_\nB._gLeDU__rr_vjrm__O_jl_R__DG___u_XqJjW_\nC.___sHLQzdTzT_tZ_Gs\nD.sZNcVa__M_To_bz_clFi_mH_\n'
E         expected='C'
E         got=''
E       assert '' == 'C'
E         - C

tmp56hchxz8.py:27: AssertionError
______________________________ test_case[case18] _______________________________

i = 18
inp = 'A.bR___cCYJg_Wbt____cxfXfC____c_O_\nB.guM\nC.__bzsH_Of__RjG__u_w_i__PXQL_U_Ow_U_n\nD._nHIuZsu_uU_stRC_k___vD_ZOD_u_z_c_Zf__p_iF_uD_Hdg\n'
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
E       AssertionError: input='A.bR___cCYJg_Wbt____cxfXfC____c_O_\nB.guM\nC.__bzsH_Of__RjG__u_w_i__PXQL_U_Ow_U_n\nD._nHIuZsu_uU_stRC_k___vD_ZOD_u_z_c_Zf__p_iF_uD_Hdg\n'
E         expected='B'
E         got=''
E       assert '' == 'B'
E         - B

tmp56hchxz8.py:27: AssertionError
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
E         got=''
E       assert '' == 'D'
E         - D

tmp56hchxz8.py:27: AssertionError
______________________________ test_case[case20] _______________________________

i = 20
inp = 'A.yYGJ_C__NYq_\nB.ozMUZ_cKKk_zVUPR_b_g_ygv_HoM__yAxvh__iE\nC.sgHJ___MYP__AWejchRvjSD_o\nD.gkfF_GiOqW_psMT_eS\n'
expected = 'C\n'

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
E       AssertionError: input='A.yYGJ_C__NYq_\nB.ozMUZ_cKKk_zVUPR_b_g_ygv_HoM__yAxvh__iE\nC.sgHJ___MYP__AWejchRvjSD_o\nD.gkfF_GiOqW_psMT_eS\n'
E         expected='C'
E         got=''
E       assert '' == 'C'
E         - C

tmp56hchxz8.py:27: AssertionError
______________________________ test_case[case21] _______________________________

i = 21
inp = 'A._LYm_nvl_E__RCFZ_IdO\nB.k__qIPO_ivvZyIG__L_\nC.D_SabLm_R___j_HS_t__\nD._adj_R_ngix____GSe_aw__SbOOl_\n'
expected = 'C\n'

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
E       AssertionError: input='A._LYm_nvl_E__RCFZ_IdO\nB.k__qIPO_ivvZyIG__L_\nC.D_SabLm_R___j_HS_t__\nD._adj_R_ngix____GSe_aw__SbOOl_\n'
E         expected='C'
E         got=''
E       assert '' == 'C'
E         - C

tmp56hchxz8.py:27: AssertionError
______________________________ test_case[case22] _______________________________

i = 22
inp = 'A.h_WiYTD_C_h___z_Gn_Th_uNh__g___jm\nB.__HeQaudCJcYfVi__Eg_vryuQrDkb_g__oy_BwX_Mu_\nC._MChdMhQA_UKrf_LGZk_ALTo_mnry_GNNza_X_D_u____ueJb__Y_h__CNUNDfmZATck_ad_XTbG\nD.NV___OoL__GfP_CqhD__RB_____v_T_xi\n'
expected = 'C\n'

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
E       AssertionError: input='A.h_WiYTD_C_h___z_Gn_Th_uNh__g___jm\nB.__HeQaudCJcYfVi__Eg_vryuQrDkb_g__oy_BwX_Mu_\nC._MChdMhQA_UKrf_LGZk_ALTo_mnry_GNNza_X_D_u____ueJb__Y_h__CNUNDfmZATck_ad_XTbG\nD.NV___OoL__GfP_CqhD__RB_____v_T_xi\n'
E         expected='C'
E         got=''
E       assert '' == 'C'
E         - C

tmp56hchxz8.py:27: AssertionError
______________________________ test_case[case23] _______________________________

i = 23
inp = 'A.____JGWsfiU\nB.S_LMq__MpE_oFBs_P\nC.U_Rph_VHpUr____X_jWXbk__ElJTu_Z_wlBpKLTD\nD.p_ysvPNmbrF__\n'
expected = 'C\n'

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
E       AssertionError: input='A.____JGWsfiU\nB.S_LMq__MpE_oFBs_P\nC.U_Rph_VHpUr____X_jWXbk__ElJTu_Z_wlBpKLTD\nD.p_ysvPNmbrF__\n'
E         expected='C'
E         got=''
E       assert '' == 'C'
E         - C

tmp56hchxz8.py:27: AssertionError
______________________________ test_case[case24] _______________________________

i = 24, inp = 'A.aaaaaa\nB.aaa\nC.aaa\nD.aaa\n', expected = 'A\n'

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
E       AssertionError: input='A.aaaaaa\nB.aaa\nC.aaa\nD.aaa\n'
E         expected='A'
E         got=''
E       assert '' == 'A'
E         - A

tmp56hchxz8.py:27: AssertionError
______________________________ test_case[case25] _______________________________

i = 25, inp = 'A.aaa\nB.aaaaaa\nC.aaaaaa\nD.aaaaaa\n', expected = 'A\n'

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
E       AssertionError: input='A.aaa\nB.aaaaaa\nC.aaaaaa\nD.aaaaaa\n'
E         expected='A'
E         got=''
E       assert '' == 'A'
E         - A

tmp56hchxz8.py:27: AssertionError
______________________________ test_case[case26] _______________________________

i = 26, inp = 'A.a\nB.b\nC.c\nD.d\n', expected = 'C\n'

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
E       AssertionError: input='A.a\nB.b\nC.c\nD.d\n'
E         expected='C'
E         got=''
E       assert '' == 'C'
E         - C

tmp56hchxz8.py:27: AssertionError
______________________________ test_case[case27] _______________________________

i = 27, inp = 'A._\nB.__\nC.____\nD.________\n', expected = 'C\n'

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
E       AssertionError: input='A._\nB.__\nC.____\nD.________\n'
E         expected='C'
E         got=''
E       assert '' == 'C'
E         - C

tmp56hchxz8.py:27: AssertionError
______________________________ test_case[case28] _______________________________

i = 28, inp = 'A.____\nB.________\nC.________\nD._______\n', expected = 'C\n'

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
E       AssertionError: input='A.____\nB.________\nC.________\nD._______\n'
E         expected='C'
E         got=''
E       assert '' == 'C'
E         - C

tmp56hchxz8.py:27: AssertionError
______________________________ test_case[case29] _______________________________

i = 29, inp = 'A.h\nB.asdf\nC.asqw\nD.qwertasdfg\n', expected = 'C\n'

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
E       AssertionError: input='A.h\nB.asdf\nC.asqw\nD.qwertasdfg\n'
E         expected='C'
E         got=''
E       assert '' == 'C'
E         - C

tmp56hchxz8.py:27: AssertionError
______________________________ test_case[case30] _______________________________

i = 30, inp = 'A.aa\nB.aaaaa\nC.aaaaaa\nD.aaaaaaaaaaaaa\n', expected = 'C\n'

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
E       AssertionError: input='A.aa\nB.aaaaa\nC.aaaaaa\nD.aaaaaaaaaaaaa\n'
E         expected='C'
E         got=''
E       assert '' == 'C'
E         - C

tmp56hchxz8.py:27: AssertionError
______________________________ test_case[case31] _______________________________

i = 31, inp = 'A.ccc\nB.ccccccc\nC.ccc\nD.c\n', expected = 'C\n'

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
E       AssertionError: input='A.ccc\nB.ccccccc\nC.ccc\nD.c\n'
E         expected='C'
E         got=''
E       assert '' == 'C'
E         - C

tmp56hchxz8.py:27: AssertionError
______________________________ test_case[case32] _______________________________

i = 32, inp = 'A.c\nB.ccc\nC.cccccccccccccccccc\nD.cccccc\n', expected = 'C\n'

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
E       AssertionError: input='A.c\nB.ccc\nC.cccccccccccccccccc\nD.cccccc\n'
E         expected='C'
E         got=''
E       assert '' == 'C'
E         - C

tmp56hchxz8.py:27: AssertionError
______________________________ test_case[case33] _______________________________

i = 33, inp = 'A.aa\nB.bb\nC.cc\nD.ddd\n', expected = 'C\n'

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
E       AssertionError: input='A.aa\nB.bb\nC.cc\nD.ddd\n'
E         expected='C'
E         got=''
E       assert '' == 'C'
E         - C

tmp56hchxz8.py:27: AssertionError
______________________________ test_case[case34] _______________________________

i = 34, inp = 'A.QW\nB.WERT\nC.QWER\nD.QWERTYUI\n', expected = 'C\n'

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
E       AssertionError: input='A.QW\nB.WERT\nC.QWER\nD.QWERTYUI\n'
E         expected='C'
E         got=''
E       assert '' == 'C'
E         - C

tmp56hchxz8.py:27: AssertionError
=========================== short test summary info ============================
FAILED tmp56hchxz8.py::test_case[case0] - AssertionError: input='A.VFleaKing_...
FAILED tmp56hchxz8.py::test_case[case1] - AssertionError: input='A.ab\nB.abcd...
FAILED tmp56hchxz8.py::test_case[case2] - AssertionError: input='A.c\nB.cc\nC...
FAILED tmp56hchxz8.py::test_case[case3] - AssertionError: input='A.He_nan_de_...
FAILED tmp56hchxz8.py::test_case[case4] - AssertionError: input='A.a___FXIcs_...
FAILED tmp56hchxz8.py::test_case[case5] - AssertionError: input='A.G_R__iT_ow...
FAILED tmp56hchxz8.py::test_case[case6] - AssertionError: input='A.a___FXIcs_...
FAILED tmp56hchxz8.py::test_case[case7] - AssertionError: input='A.G_R__iT_ow...
FAILED tmp56hchxz8.py::test_case[case8] - AssertionError: input='A.ejQ_E_E_G_...
FAILED tmp56hchxz8.py::test_case[case9] - AssertionError: input='A.PN_m_P_qgO...
FAILED tmp56hchxz8.py::test_case[case10] - AssertionError: input='A.bR___cCYJ...
FAILED tmp56hchxz8.py::test_case[case11] - AssertionError: input='A.x_\nB.__R...
FAILED tmp56hchxz8.py::test_case[case12] - AssertionError: input='A.yYGJ_C__N...
FAILED tmp56hchxz8.py::test_case[case13] - AssertionError: input='A._LYm_nvl_...
FAILED tmp56hchxz8.py::test_case[case14] - AssertionError: input='A.h_WiYTD_C...
FAILED tmp56hchxz8.py::test_case[case15] - AssertionError: input='A.____JGWsf...
FAILED tmp56hchxz8.py::test_case[case16] - AssertionError: input='A.ejQ_E_E_G...
FAILED tmp56hchxz8.py::test_case[case17] - AssertionError: input='A.PN_m_P_qg...
FAILED tmp56hchxz8.py::test_case[case18] - AssertionError: input='A.bR___cCYJ...
FAILED tmp56hchxz8.py::test_case[case19] - AssertionError: input='A.x_\nB.__R...
FAILED tmp56hchxz8.py::test_case[case20] - AssertionError: input='A.yYGJ_C__N...
FAILED tmp56hchxz8.py::test_case[case21] - AssertionError: input='A._LYm_nvl_...
FAILED tmp56hchxz8.py::test_case[case22] - AssertionError: input='A.h_WiYTD_C...
FAILED tmp56hchxz8.py::test_case[case23] - AssertionError: input='A.____JGWsf...
FAILED tmp56hchxz8.py::test_case[case24] - AssertionError: input='A.aaaaaa\nB...
FAILED tmp56hchxz8.py::test_case[case25] - AssertionError: input='A.aaa\nB.aa...
FAILED tmp56hchxz8.py::test_case[case26] - AssertionError: input='A.a\nB.b\nC...
FAILED tmp56hchxz8.py::test_case[case27] - AssertionError: input='A._\nB.__\n...
FAILED tmp56hchxz8.py::test_case[case28] - AssertionError: input='A.____\nB._...
FAILED tmp56hchxz8.py::test_case[case29] - AssertionError: input='A.h\nB.asdf...
FAILED tmp56hchxz8.py::test_case[case30] - AssertionError: input='A.aa\nB.aaa...
FAILED tmp56hchxz8.py::test_case[case31] - AssertionError: input='A.ccc\nB.cc...
FAILED tmp56hchxz8.py::test_case[case32] - AssertionError: input='A.c\nB.ccc\...
FAILED tmp56hchxz8.py::test_case[case33] - AssertionError: input='A.aa\nB.bb\...
FAILED tmp56hchxz8.py::test_case[case34] - AssertionError: input='A.QW\nB.WER...
============================== 35 failed in 6.35s ==============================
```
