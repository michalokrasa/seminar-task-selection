# introductory/1203-d1

**Status:** FAIL (exit code 1)

## stdout

```
============================= test session starts ==============================
platform linux -- Python 3.10.18, pytest-7.4.4, pluggy-1.6.0
PyQt5 5.15.10 -- Qt runtime 5.15.17 -- Qt compiled 5.15.2
rootdir: /tmp/tmpx373zoxa
configfile: pytest.ini
plugins: Faker-25.1.0, anyio-4.9.0, cov-5.0.0, mock-3.12.0, qt-4.3.1
collected 44 items

tmpj7bldfqd.py::test_case[case0] PASSED
tmpj7bldfqd.py::test_case[case1] FAILED
tmpj7bldfqd.py::test_case[case2] PASSED
tmpj7bldfqd.py::test_case[case3] FAILED
tmpj7bldfqd.py::test_case[case4] FAILED
tmpj7bldfqd.py::test_case[case5] FAILED
tmpj7bldfqd.py::test_case[case6] PASSED
tmpj7bldfqd.py::test_case[case7] FAILED
tmpj7bldfqd.py::test_case[case8] FAILED
tmpj7bldfqd.py::test_case[case9] FAILED
tmpj7bldfqd.py::test_case[case10] FAILED
tmpj7bldfqd.py::test_case[case11] PASSED
tmpj7bldfqd.py::test_case[case12] PASSED
tmpj7bldfqd.py::test_case[case13] PASSED
tmpj7bldfqd.py::test_case[case14] PASSED
tmpj7bldfqd.py::test_case[case15] PASSED
tmpj7bldfqd.py::test_case[case16] FAILED
tmpj7bldfqd.py::test_case[case17] FAILED
tmpj7bldfqd.py::test_case[case18] PASSED
tmpj7bldfqd.py::test_case[case19] FAILED
tmpj7bldfqd.py::test_case[case20] FAILED
tmpj7bldfqd.py::test_case[case21] FAILED
tmpj7bldfqd.py::test_case[case22] FAILED
tmpj7bldfqd.py::test_case[case23] PASSED
tmpj7bldfqd.py::test_case[case24] FAILED
tmpj7bldfqd.py::test_case[case25] FAILED
tmpj7bldfqd.py::test_case[case26] PASSED
tmpj7bldfqd.py::test_case[case27] FAILED
tmpj7bldfqd.py::test_case[case28] FAILED
tmpj7bldfqd.py::test_case[case29] FAILED
tmpj7bldfqd.py::test_case[case30] FAILED
tmpj7bldfqd.py::test_case[case31] PASSED
tmpj7bldfqd.py::test_case[case32] PASSED
tmpj7bldfqd.py::test_case[case33] PASSED
tmpj7bldfqd.py::test_case[case34] PASSED
tmpj7bldfqd.py::test_case[case35] PASSED
tmpj7bldfqd.py::test_case[case36] PASSED
tmpj7bldfqd.py::test_case[case37] PASSED
tmpj7bldfqd.py::test_case[case38] FAILED
tmpj7bldfqd.py::test_case[case39] FAILED
tmpj7bldfqd.py::test_case[case40] PASSED
tmpj7bldfqd.py::test_case[case41] PASSED
tmpj7bldfqd.py::test_case[case42] PASSED
tmpj7bldfqd.py::test_case[case43] PASSED

=================================== FAILURES ===================================
_______________________________ test_case[case1] _______________________________

i = 1, inp = 'baaba\nab\n', expected = '2\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='baaba\nab\n'
E         expected='2'
E         got='3'
E       assert '3' == '2'
E         - 2
E         + 3

tmpj7bldfqd.py:27: AssertionError
_______________________________ test_case[case3] _______________________________

i = 3, inp = 'asdfasdf\nfasd\n', expected = '3\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='asdfasdf\nfasd\n'
E         expected='3'
E         got='4'
E       assert '4' == '3'
E         - 3
E         + 4

tmpj7bldfqd.py:27: AssertionError
_______________________________ test_case[case4] _______________________________

i = 4
inp = 'zywmerhahxlqsjekpqsdqxnjiduyjrytswiweohctztgpiorwimhjmdfofqynyggcrtzslbyvkuvqrsgwyacyvcuathplliwwshusluiqwuhutnzwvuch...qsdqjidytswwztgiowimhmffqygctzslbykurwacyvcuaplwshsluiqwuhutnwchfewwfdizttcpnqestgkfvsjylkksumaljmmkcjwwdkolmcgodcle\n'
expected = '5\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='zywmerhahxlqsjekpqsdqxnjiduyjrytswiweohctztgpiorwimhjmdfofqynyggcrtzslbyvkuvqrsgwyacyvcuathplliwwshusluiqwuhutnzwvuchfedhwwfdzizltdxibtsaocpnqezstblgkfdcvfsjjyzwalkksumsaljqljmmkcyejwwdkolmcgmodoiclte\nzywmehahxlqjekqsdqjidytswwztgiowimhmffqygctzslbykurwacyvcuaplwshsluiqwuhutnwchfewwfdizttcpnqestgkfvsjylkksumaljmmkcjwwdkolmcgodcle\n'
E         expected='5'
E         got='70'
E       assert '70' == '5'
E         - 5
E         + 70

tmpj7bldfqd.py:27: AssertionError
_______________________________ test_case[case5] _______________________________

i = 5
inp = 'nqlswpkupyawfzygzjfntqpivmudprpmtkhwjcoabkkxfemjekxvnjikbvtbzgrxyacflvausuwgqfxvfcgxphzeiwpitswykvcsyspvimmynlyeldkqj...rypyzjhjhsntegsuryjgpknwvnjxplztmjszidqkihuxgzc\nnlwkupywfzgzftqpiudprmkhwcozenmjdhacygryjhhntgugpkwvnjxplztszikihgc\n'
expected = '101\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='nqlswpkupyawfzygzjfntqpivmudprpmtkhwjcoabkkxfemjekxvnjikbvtbzgrxyacflvausuwgqfxvfcgxphzeiwpitswykvcsyspvimmynlyeldkqjsogjhszcqtvteiefdcissquzeynmjdhazcygrypyzjhjhsntegsuryjgpknwvnjxplztmjszidqkihuxgzc\nnlwkupywfzgzftqpiudprmkhwcozenmjdhacygryjhhntgugpkwvnjxplztszikihgc\n'
E         expected='101'
E         got='133'
E       assert '133' == '101'
E         - 101
E         + 133

tmpj7bldfqd.py:27: AssertionError
_______________________________ test_case[case7] _______________________________

i = 7
inp = 'kbuwmzldbajqgbdyeqqyuvdwsdzvjicqgsadjgruebcsxuhgftlykvuevsldvapqoxkrwjbwjjqquogxkpradzauxxlhrayprgnwxwumabxdojztankeq...ggrltdvcpiozbrvwhxhjpurwachimqrxrplcavtpaqzemxhrvagbngyqhacuxfbpkwqxyixdfmrj\nkbmrxrplcavtpaqemxhagbghacuxbpkwqxidmj\n'
expected = '150\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='kbuwmzldbajqgbdyeqqyuvdwsdzvjicqgsadjgruebcsxuhgftlykvuevsldvapqoxkrwjbwjjqquogxkpradzauxxlhrayprgnwxwumabxdojztankeqmraeqbbggrltdvcpiozbrvwhxhjpurwachimqrxrplcavtpaqzemxhrvagbngyqhacuxfbpkwqxyixdfmrj\nkbmrxrplcavtpaqemxhagbghacuxbpkwqxidmj\n'
E         expected='150'
E         got='162'
E       assert '162' == '150'
E         - 150
E         + 162

tmpj7bldfqd.py:27: AssertionError
_______________________________ test_case[case8] _______________________________

i = 8
inp = 'aplxwwvctglkkvfdyfpegleljcjtaxhdjnfonpedzeyvqprewgqwalqafebjvbjmpimoujgcfcnycugvdmgkjeaeggmnrspkydplacliklknqifoenxwx...opdzevqpregwqafejvbjpmoujgccncumgkjeaeggnspdplclknifenxxmakekewgligiphingoczheheioiocustuzkodlyeesinfrpuonnobldvagmx\n'
expected = '21\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='aplxwwvctglkkvfdyfpegleljcjtaxhdjnfonpedzeyvqprewgqwalqafebjvbjmpimoujgcfcnycugvdmgkjeaeggmnrspkydplacliklknqifoenxwxmtxsmakekewtkglligipuhpicngocrzhehelimoiocusgtuzkodlyqeetsiionfrphuoznnnobldhvjagmx\naplxwvctgdjfopdzevqpregwqafejvbjpmoujgccncumgkjeaeggnspdplclknifenxxmakekewgligiphingoczheheioiocustuzkodlyeesinfrpuonnobldvagmx\n'
E         expected='21'
E         got='72'
E       assert '72' == '21'
E         - 21
E         + 72

tmpj7bldfqd.py:27: AssertionError
_______________________________ test_case[case9] _______________________________

i = 9
inp = 'toimpgygoklxroowdhpacrtrrwmkhcgcpidapeyxrjmiqgilveimnazyydvnujtqpenfkeqdbylfdinompxupfwvirxohaampqihjueasygkucweptgco...npgygkxrowdpcrmkcgciapxjmiqgveimnazydvnujteqdblinmpxpvxoaampesygucweptgcignwytgurgnhjtfovwusqavdtnppcxgdxyalksgkxtid\n'
expected = '6\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='toimpgygoklxroowdhpacrtrrwmkhcgcpidapeyxrjmiqgilveimnazyydvnujtqpenfkeqdbylfdinompxupfwvirxohaampqihjueasygkucweptgcowjibgnwyqetynykgoujeargnhjbmntfovwusqavpdwtpnpqpkcgaxbhgdxloyealksmgkxprtpfugixdyfn\npgygkxrowdpcrmkcgciapxjmiqgveimnazydvnujteqdblinmpxpvxoaampesygucweptgcignwytgurgnhjtfovwusqavdtnppcxgdxyalksgkxtid\n'
E         expected='6'
E         got='85'
E       assert '85' == '6'
E         - 6
E         + 85

tmpj7bldfqd.py:27: AssertionError
______________________________ test_case[case10] _______________________________

i = 10
inp = 'ziurxtzxixmsmewfuffsqdkpphssdcgybwtmzavkosqtmcntspzvftqybaldjllvgttblectspqinfdhhnpvkcbwjlqlquajueqsgymyekuswjctumsbn...wmzavkosqtmctspvftybaljlgtltsqinfdhhpvkcwjlqlqymykusctumsbnvvainxjlcyxfykokeguvvhategjfxinuwihjznkhepjznzftmmqtlihpn\n'
expected = '8\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='ziurxtzxixmsmewfuffsqdkpphssdcgybwtmzavkosqtmcntspzvftqybaldjllvgttblectspqinfdhhnpvkcbwjlqlquajueqsgymyekuswjctumsbnvvaiinxjlzcnyixfaykolkeogufvzvhnatqtelgjkqfvexghiznwubwihjkznkhepjzrnyzftmimqtlihpn\nzurzximmewfuffskppsdcybwmzavkosqtmctspvftybaljlgtltsqinfdhhpvkcwjlqlqymykusctumsbnvvainxjlcyxfykokeguvvhategjfxinuwihjznkhepjznzftmmqtlihpn\n'
E         expected='8'
E         got='61'
E       assert '61' == '8'
E         - 8
E         + 61

tmpj7bldfqd.py:27: AssertionError
______________________________ test_case[case16] _______________________________

i = 16
inp = 'xmxcpstetnnyxqbdbfsqhyjpdihhcpbxfugnmwhjadphwsialqafdvunwjqpifdqdwoxrkyetoyafjiyaosahwxfoxejwtvtousuailafdlukqfyealda...bxfgmaphialqdvunwjqpifdqdwoxketofjyaohxfoejwtousuaiaukqfyaldakjfgtxgeasiclcldtxokotgabqbrstcffxrfopyrmnvvhoppbcnlkdz\n'
expected = '4\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='xmxcpstetnnyxqbdbfsqhyjpdihhcpbxfugnmwhjadphwsialqafdvunwjqpifdqdwoxrkyetoyafjiyaosahwxfoxejwtvtousuailafdlukqfyealdakjxgfagdltxgteasiclclbdutzdxokclotgabcqbytryszetctfvfmxrfouepwyrmvnvvvhoppbcnlkdzio\npstnnyxqbfqhdipbxfgmaphialqdvunwjqpifdqdwoxketofjyaohxfoejwtousuaiaukqfyaldakjfgtxgeasiclcldtxokotgabqbrstcffxrfopyrmnvvhoppbcnlkdz\n'
E         expected='4'
E         got='69'
E       assert '69' == '4'
E         - 4
E         + 69

tmpj7bldfqd.py:27: AssertionError
______________________________ test_case[case17] _______________________________

i = 17
inp = 'pibvxshjediuehnmfyvprhjtghzadeavjgnlvjwaqzlbexrlrnijokvqirbgfpnwwgnuptzotcdoooorqyqipbfawdslkvqrscnguydrywwzazwohlufb...amfaugfmluuidnkmxbrzfzvmchopukbrlkuinxgridioo\npdrwwzzwohlurfvoblvygeonmpoyvjdxscjmcqsmfauguikmxbzfzmchopukbrluidioo\n'
expected = '101\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='pibvxshjediuehnmfyvprhjtghzadeavjgnlvjwaqzlbexrlrnijokvqirbgfpnwwgnuptzotcdoooorqyqipbfawdslkvqrscnguydrywwzazwohlufbverfvoblvygevornmproyvsnjdxscgyrjmcqsmamfaugfmluuidnkmxbrzfzvmchopukbrlkuinxgridioo\npdrwwzzwohlurfvoblvygeonmpoyvjdxscjmcqsmfauguikmxbzfzmchopukbrluidioo\n'
E         expected='101'
E         got='131'
E       assert '131' == '101'
E         - 101
E         + 131

tmpj7bldfqd.py:27: AssertionError
______________________________ test_case[case19] _______________________________

i = 19
inp = 'eseflxqdffomkoxxhdicryombxleqlvckmqfxxpwipivffhoozteiinpelbaukuifsoygjwyxjlqtazufqrafadzulucrgbtqfsxlnrvauxpojwbpgyzwentjokrkvkepazivjvtxsepruqorgmhvjfnjintftbvnqfwmapmcuilsbkmjgdulgirtpfpywawfpjpbxhy\nfnntftvnqwmmulbkmdgifpywfpjpxhy\n'
expected = '150\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='eseflxqdffomkoxxhdicryombxleqlvckmqfxxpwipivffhoozteiinpelbaukuifsoygjwyxjlqtazufqrafadzulucrgbtqfsxlnrvauxpojwbpgyzwentjokrkvkepazivjvtxsepruqorgmhvjfnjintftbvnqfwmapmcuilsbkmjgdulgirtpfpywawfpjpbxhy\nfnntftvnqwmmulbkmdgifpywfpjpxhy\n'
E         expected='150'
E         got='169'
E       assert '169' == '150'
E         - 150
E         + 169

tmpj7bldfqd.py:27: AssertionError
______________________________ test_case[case20] _______________________________

i = 20
inp = 'ppneeasyjzorefvertisgxykuoqsugzppvfoubkybksuwtmmepnauteyemvtwwweftteccshepmnoxoglvpinlcduflxybdkvmjrwxcedsfjskiuxizwl...foubkybksuwtmmepnauteemvtwweftcsepmnooglvplcuxybdkvjrxcesfskiuzckchsycmwlaomxwkpahmabcmhanlknsnjzbwhudbupwdwdbhebyhg\n'
expected = '21\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='ppneeasyjzorefvertisgxykuoqsugzppvfoubkybksuwtmmepnauteyemvtwwweftteccshepmnoxoglvpinlcduflxybdkvmjrwxcedsfjskiuxizwlckchsycmbwnlasriohmxwkkqdrpahmeuabdchfmyhbanluynzaaknssnjzbqwhudbupwhqfdvwdbhebykhg\nppnuqsppvfoubkybksuwtmmepnauteemvtwweftcsepmnooglvplcuxybdkvjrxcesfskiuzckchsycmwlaomxwkpahmabcmhanlknsnjzbwhudbupwdwdbhebyhg\n'
E         expected='21'
E         got='75'
E       assert '75' == '21'
E         - 21
E         + 75

tmpj7bldfqd.py:27: AssertionError
______________________________ test_case[case21] _______________________________

i = 21
inp = 'izoiweukqszkkhwapzxyotbaarpqxbybsjxilhylbbjbvoedrezyluaabsfzvtxxvncdwxrlfdtfvbfoqwlzqwneimwzpoygfdcldmxdhoxzensxlspit...xlylbbjbrezlasfzvtxvcdxrltffoqwlzqwneizpoygfdcmdxzesxlsitozzrfomhggrwrcfoorvhyzdpjhakuoxdjhzaalanzwqlrtmmraleyjyxutc\n'
expected = '4\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='izoiweukqszkkhwapzxyotbaarpqxbybsjxilhylbbjbvoedrezyluaabsfzvtxxvncdwxrlfdtfvbfoqwlzqwneimwzpoygfdcldmxdhoxzensxlspituzocvzzrfomhggrwurdccgfoorvhyzsdkpjhwakuoxwdjhzaalanyzwuuqwlrtmvmdraleyusjqdyxuztvc\noukzkkhwazxbaarpbybsjxlylbbjbrezlasfzvtxvcdxrltffoqwlzqwneizpoygfdcmdxzesxlsitozzrfomhggrwrcfoorvhyzdpjhakuoxdjhzaalanzwqlrtmmraleyjyxutc\n'
E         expected='4'
E         got='63'
E       assert '63' == '4'
E         - 4
E         + 63

tmpj7bldfqd.py:27: AssertionError
______________________________ test_case[case22] _______________________________

i = 22
inp = 'qmrzsrvfllfraflralrwlcfjxupnlomnbeuvipcyxxmksztljxqaoqnptwwemhgswpovpnvoqajaqzxpmtqarpgdrgwuuferbhjjowmljtaoiidzkrcaa...mevipcyxxmkstljaoqnptweswpovpnvoqajaxptarpgdgwufbhjjoljtiidcawzorugpwzgskgddbrazdwreyztdctcujgxvjqlewvjpfpmbbcjtndis\n'
expected = '7\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='qmrzsrvfllfraflralrwlcfjxupnlomnbeuvipcyxxmksztljxqaoqnptwwemhgswpovpnvoqajaqzxpmtqarpgdrgwuuferbhjjowmljtaoiidzkrcaawzomruigpwzgsksgdkbdbrjwaszgdwreyztdctwacfmujdgxvjqoclueiwdgvjcfpfbpmbbmcufjiitndis\nqmrzsrflrrwlfjxupnlmevipcyxxmkstljaoqnptweswpovpnvoqajaxptarpgdgwufbhjjoljtiidcawzorugpwzgskgddbrazdwreyztdctcujgxvjqlewvjpfpmbbcjtndis\n'
E         expected='7'
E         got='65'
E       assert '65' == '7'
E         - 7
E         + 65

tmpj7bldfqd.py:27: AssertionError
______________________________ test_case[case24] _______________________________

i = 24
inp = 'dexradrxekhwsmctzdqyrqctyrduvazzfybzlwdrhjdxawojhilywadneuijwuuwjbnhdjitjekszqjmnhrxulxcwfrwfzjlkzagaygllqzbehxdyiazt...vzzyblwhdaojhilwanijuuwbnhjitjeksqjmnhrulxwfwflkgagllbhxyiaztcpjvrvmzkhvnnsaadvxwectdpevjsgodxdefwhwcdospyjziiwoogxz\n'
expected = '4\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='dexradrxekhwsmctzdqyrqctyrduvazzfybzlwdrhjdxawojhilywadneuijwuuwjbnhdjitjekszqjmnhrxulxcwfrwfzjlkzagaygllqzbehxdyiaztrcpjtvrvtmzkhvgnopwdnssyvaagatdvxgwectdpelvjmsgovdxrdeffawhwcdkospyjziiyiwyoofgnxzq\ndexrdekhwczqrqtyduvzzyblwhdaojhilwanijuuwbnhjitjeksqjmnhrulxwfwflkgagllbhxyiaztcpjvrvmzkhvnnsaadvxwectdpevjsgodxdefwhwcdospyjziiwoogxz\n'
E         expected='4'
E         got='66'
E       assert '66' == '4'
E         - 4
E         + 66

tmpj7bldfqd.py:27: AssertionError
______________________________ test_case[case25] _______________________________

i = 25
inp = 'lyvutlpllxxqnttfihibqdntcxbmnzpyfcpfmcqiazztsesrumkfaksqieruntdgptwgzgsuwezxnzouiyducrcksnxjfnlhiekbnqxdakumkwgunlliw...jozprcmxcqvxvjqvjfdljvhvjyrissqopfdcbsajaolxiy\nlvuplxntihiqdncbmpyfcfqazztsrumkfasqieuntgtgzguwxnzouiydccksnxjfhieb\n'
expected = '100\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='lyvutlpllxxqnttfihibqdntcxbmnzpyfcpfmcqiazztsesrumkfaksqieruntdgptwgzgsuwezxnzouiyducrcksnxjfnlhiekbnqxdakumkwgunlliwtnkdsletbyeqfxqeitljzgmnqqccuhasbcrarjozprcmxcqvxvjqvjfdljvhvjyrissqopfdcbsajaolxiy\nlvuplxntihiqdncbmpyfcfqazztsrumkfasqieuntgtgzguwxnzouiydccksnxjfhieb\n'
E         expected='100'
E         got='132'
E       assert '132' == '100'
E         - 100
E         + 132

tmpj7bldfqd.py:27: AssertionError
______________________________ test_case[case27] _______________________________

i = 27
inp = 'pofvbxtueyzxgzcrthooeacytrsysourmdvkfhebuqpoofbixkxrveqijcluhgaqbeljezhpeiffpeaejkvvuhbhrlhlwuwpkbmgejmrelsnzlrubrgmqowtfucbjzvqoqcbvrqqljzvlscrrulfahdijkzosggdocqmhpbszktbucsfnfurklmlnxcshtdjhrherwxr\npofvbxtuezgrtooacytrssoumdvkuobxr\n'
expected = '151\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='pofvbxtueyzxgzcrthooeacytrsysourmdvkfhebuqpoofbixkxrveqijcluhgaqbeljezhpeiffpeaejkvvuhbhrlhlwuwpkbmgejmrelsnzlrubrgmqowtfucbjzvqoqcbvrqqljzvlscrrulfahdijkzosggdocqmhpbszktbucsfnfurklmlnxcshtdjhrherwxr\npofvbxtuezgrtooacytrssoumdvkuobxr\n'
E         expected='151'
E         got='167'
E       assert '167' == '151'
E         - 151
E         + 167

tmpj7bldfqd.py:27: AssertionError
______________________________ test_case[case28] _______________________________

i = 28
inp = 'rycgapxwyctxltrpateousbjtijdfsrxxgexpbiwyijynvomwanlrqbzqbkoaikqyblojwamoqlgoxxtvqatcrmhulzcubrtaguxysvepnrvtppeuzgnn...ycgpxwytxltrpaeusbjijdxxgexpbiwyjynvoalrbzqaikqywamoloxxtvqrmhulcubtgxysvepnrpzgnunucncuedvequfgtcyhltdtdaiodtmazfov\n'
expected = '20\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='rycgapxwyctxltrpateousbjtijdfsrxxgexpbiwyijynvomwanlrqbzqbkoaikqyblojwamoqlgoxxtvqatcrmhulzcubrtaguxysvepnrvtppeuzgnncusougnuzcayncuedvadkezhtkqucmfvgtdzcyhlztdtdkaiocdmtmoawzvfojvkdfzlaudxxchpnbbgtkp\nrycgpxwytxltrpaeusbjijdxxgexpbiwyjynvoalrbzqaikqywamoloxxtvqrmhulcubtgxysvepnrpzgnunucncuedvequfgtcyhltdtdaiodtmazfov\n'
E         expected='20'
E         got='83'
E       assert '83' == '20'
E         - 20
E         + 83

tmpj7bldfqd.py:27: AssertionError
______________________________ test_case[case29] _______________________________

i = 29
inp = 'grkhejdykjmieztowpjdazxmjqlccvlwjjspiupkmhbpuvjfkncwoiastztyekhrpsfwkqwmtrznggbkfwzrtuwswbgowsemwpmssbkzorkmjauqzpsdy...lclwjspiupkmhbufknciatzterpsfkmtrznggbkfwzrtwswgowsempsbkzokmauzpsdynhapjpgswibljvaakslncnbjxtjddnnvxyevszspztbpqstf\n'
expected = '5\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='grkhejdykjmieztowpjdazxmjqlccvlwjjspiupkmhbpuvjfkncwoiastztyekhrpsfwkqwmtrznggbkfwzrtuwswbgowsemwpmssbkzorkmjauqzpsdylnhapjopgiswihierbluojvarvrakdslncrhinbjxyxptiojddnnvxsedklyjehbvsinezsppztbpqswutf\nrkhjdykjitopjdxmqlclwjspiupkmhbufknciatzterpsfkmtrznggbkfwzrtwswgowsempsbkzokmauzpsdynhapjpgswibljvaakslncnbjxtjddnnvxyevszspztbpqstf\n'
E         expected='5'
E         got='67'
E       assert '67' == '5'
E         - 5
E         + 67

tmpj7bldfqd.py:27: AssertionError
______________________________ test_case[case30] _______________________________

i = 30
inp = 'kxzkueqzheeolprfncwxyxgqqlocajzkusopvpwowdxubsvvtfvnrkyijoxqjawzkvfkainowbxdzcxbgrywttplukaorxvtimqxonumuvsqyfobzorqq...zkqeeolprcxyxgqqloazkuspwouvvvnkyoxjzvkinowxdzbrytluaorximxnmvfoboqqsozjvschtlgbetizhcjipirccvffgkzyxbeozgctkzpsheus\n'
expected = '5\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='kxzkueqzheeolprfncwxyxgqqlocajzkusopvpwowdxubsvvtfvnrkyijoxqjawzkvfkainowbxdzcxbgrywttplukaorxvtimqxonumuvsqyfobzorqqsohazhjyvscjhtlgbmetpigfzhtcjipiorcrcsvvdofflgkqzymdxbeaozrgcjxrgtkxrzpshjesucdwhds\nkzkqeeolprcxyxgqqloazkuspwouvvvnkyoxjzvkinowxdzbrytluaorximxnmvfoboqqsozjvschtlgbetizhcjipirccvffgkzyxbeozgctkzpsheus\n'
E         expected='5'
E         got='83'
E       assert '83' == '5'
E         - 5
E         + 83

tmpj7bldfqd.py:27: AssertionError
______________________________ test_case[case38] _______________________________

i = 38
inp = 'kbuwmzldbajqgbdyeqqyuvdwsdzvjicqgsadjgruebcsxuhgftlykvuevsldvapqoxkrwjbwjjqquogxkpradzauxxlhrayprgnwxwumabxdojztankeq...ggrltdvcpiozbrvwhxhjpurwachimqrxrplcavtpaqzemxhrvagbngyqhacuxfbpkwqxyixdfmrj\nkbmrxrplcavtpaqemxhagbghacuxbpkwqxidmj\n'
expected = '150\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='kbuwmzldbajqgbdyeqqyuvdwsdzvjicqgsadjgruebcsxuhgftlykvuevsldvapqoxkrwjbwjjqquogxkpradzauxxlhrayprgnwxwumabxdojztankeqmraeqbbggrltdvcpiozbrvwhxhjpurwachimqrxrplcavtpaqzemxhrvagbngyqhacuxfbpkwqxyixdfmrj\nkbmrxrplcavtpaqemxhagbghacuxbpkwqxidmj\n'
E         expected='150'
E         got='162'
E       assert '162' == '150'
E         - 150
E         + 162

tmpj7bldfqd.py:27: AssertionError
______________________________ test_case[case39] _______________________________

i = 39
inp = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa...aaaaaaaaaaaaaa\naaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\n'
expected = '99\n'

    @pytest.mark.parametrize(
        "i,inp,expected",
        [(i, inp, out) for i, (inp, out) in _cases],
        ids=[f"case{i}" for i in range(len(_cases))],
    )
    def test_case(i, inp, expected):
        result = subprocess.run(
            [sys.executable, "/app/solution.py"],
            input=inp,
            capture_output=True,
            text=True,
            timeout=10,
        )
        actual = result.stdout.strip()
        exp = expected.strip()
>       assert actual == exp, f"input={inp!r}\nexpected={exp!r}\ngot={actual!r}"
E       AssertionError: input='aaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\naaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\n'
E         expected='99'
E         got='100'
E       assert '100' == '99'
E         - 99
E         + 100

tmpj7bldfqd.py:27: AssertionError
=========================== short test summary info ============================
FAILED tmpj7bldfqd.py::test_case[case1] - AssertionError: input='baaba\nab\n'
FAILED tmpj7bldfqd.py::test_case[case3] - AssertionError: input='asdfasdf\nfa...
FAILED tmpj7bldfqd.py::test_case[case4] - AssertionError: input='zywmerhahxlq...
FAILED tmpj7bldfqd.py::test_case[case5] - AssertionError: input='nqlswpkupyaw...
FAILED tmpj7bldfqd.py::test_case[case7] - AssertionError: input='kbuwmzldbajq...
FAILED tmpj7bldfqd.py::test_case[case8] - AssertionError: input='aplxwwvctglk...
FAILED tmpj7bldfqd.py::test_case[case9] - AssertionError: input='toimpgygoklx...
FAILED tmpj7bldfqd.py::test_case[case10] - AssertionError: input='ziurxtzxixm...
FAILED tmpj7bldfqd.py::test_case[case16] - AssertionError: input='xmxcpstetnn...
FAILED tmpj7bldfqd.py::test_case[case17] - AssertionError: input='pibvxshjedi...
FAILED tmpj7bldfqd.py::test_case[case19] - AssertionError: input='eseflxqdffo...
FAILED tmpj7bldfqd.py::test_case[case20] - AssertionError: input='ppneeasyjzo...
FAILED tmpj7bldfqd.py::test_case[case21] - AssertionError: input='izoiweukqsz...
FAILED tmpj7bldfqd.py::test_case[case22] - AssertionError: input='qmrzsrvfllf...
FAILED tmpj7bldfqd.py::test_case[case24] - AssertionError: input='dexradrxekh...
FAILED tmpj7bldfqd.py::test_case[case25] - AssertionError: input='lyvutlpllxx...
FAILED tmpj7bldfqd.py::test_case[case27] - AssertionError: input='pofvbxtueyz...
FAILED tmpj7bldfqd.py::test_case[case28] - AssertionError: input='rycgapxwyct...
FAILED tmpj7bldfqd.py::test_case[case29] - AssertionError: input='grkhejdykjm...
FAILED tmpj7bldfqd.py::test_case[case30] - AssertionError: input='kxzkueqzhee...
FAILED tmpj7bldfqd.py::test_case[case38] - AssertionError: input='kbuwmzldbaj...
FAILED tmpj7bldfqd.py::test_case[case39] - AssertionError: input='aaaaaaaaaaa...
======================== 22 failed, 22 passed in 7.59s =========================
```
