def maxVowels(s: str, k: int) -> int:
    v = ['a', 'e', 'i', 'o', 'u']
    res = 0
    tmp = 0
    r = 0
    for l in range(len(s)):
        if l - r < k:
            if s[l] in v:
                tmp += 1
                res = max(res, tmp)
        else:
            if s[l] in v:
                tmp += 1
            if s[r] in v:
                tmp -= 1
            r += 1
            res = max(res, tmp)
    return res


# simple doesn't pass time limit
def maxVowels_s1(s: str, k: int) -> int:
    v = ['a', 'e', 'i', 'o', 'u']
    res = 0
    for i in range(len(s)):
        tmp = 0
        ss = s[i: i + k]
        if len(ss) > res:
            for j in ss:
                if j in v:
                    tmp += 1
            res = max(res, tmp)
    return res


# simple doesn't pass time limit
def maxVowels_s(s: str, k: int) -> int:
    v = ['a', 'e', 'i', 'o', 'u']
    res = 0
    for i in range(len(s)):
        p = i
        tmp = 0
        while p < len(s) and p - i + 1 <= k:
            if s[p] in v:
                tmp += 1
            res = max(res, tmp)
            p += 1
    return res


if __name__ == '__main__':
    s = 'aeiou'
    k = 2
    assert 2 == maxVowels(s, k), 'test 1'

    s = 'gpeuomvssuudnucpowlniufzncauggxcnabigzeefcfsywmpmviqkqeel' \
        'quatdbtpzqcnffisciqbmksfwkibrscfqmwquruknpmgnztrxmivfdplhkdoyz' \
        'fzrkxdjhkhmagiinlfgzymxeecngrcspcgnnaqcwlrimurrokjpiupoadyjyb' \
        'ikfgxbxcdgytrmjsbtgpuryddhgczpeakybbmbjzmuglvjstwozyhfmvcwlrn' \
        'uwjpaktwzzryczgamzfulyffhqbzgudylttkwwbfeyzuhhaoqnzkpzgtscvdx' \
        'kdtwgthxhewipieerpbjcljgjbvxuuqtrjfwuyqwzzvpatxjxwxykicedxgotrh' \
        'svkuceneehafoaxwaglhtepcdswaifvujiqzrfdvoiwwgdfxfomthxtunumlub' \
        'wbcppodqeqapsgthbdeepjoblufuecjdtgxtfpjpvzywijfxyrsnnvfozipi' \
        'diejpivgglagdsovevphnmjqgkzkiiuwkbtebzigcxgsqllgzvnutgedyskqsf' \
        'tsbxjrrgoujecyphuhprhfxqgfcmvpxqdvdgnlwivyrspnbbnfrmiqtnqvcott' \
        'rtckmsvfzuahfccfgzzqemabfwabeyesxkadtodrcvwhwiidbmwljwgbvrxwsj' \
        'rjajtqdcghtrawvkiionohkjlwjgiqncsehssvuzcgipxxnxpzwlnxxvfxfvtgu' \
        'rdyosrruiawaairccwbweromikeolbuvxzvdztwmoezdegqyexoaozmfsbanh' \
        'qjysaeukzsrggrfczypusslhsjxjidhttylxcwowfldedtaganslgkhcpleyi' \
        'xsdnpelokdsachqvkjqovjzcuxuyefteuztmgqcyythwyhnrarekuhnflekuyy' \
        'tsatymjmyxriusvqfnvxrbteynwtpfkgztibydoyjnfoyyvccjdeqxunciqo' \
        'tkvhopzqusurdovraxrukisjtnuyhtvwluehecmfrewzijrfruyjzbpggbldgw' \
        'vykrnbeszmksyaxistovyvqjmtwxtfbkmrubuwqonnlakrlgbufxkodurjdlnx' \
        'ssakkuwkjzctaajrfovrfxnslyozvfnwjnndpoeoptmogvyfapxacbqaookuv' \
        'mcbmhmiigtaokceqymkygxhqmiasncgyllrbnxgilfknvxfwtphrmnqpjcaf' \
        'dufzojiygybnuyrtvclgsbwurgulyoskztudlhrljasjsbpxafyqyhpdmotlf' \
        'ngrjajofovtuhludyykiysukryfejeecsqaogxmieqrhzulyiabenrnbbveot' \
        'nvvhuimkbobqgtigalyhtditwsfjiwhyvcftmropycidxnwkyybmghchowdw' \
        'fbndkuzzkpcevpemujgtwdhamhbxzvwtqqhmircqeiacslgedxboligihex' \
        'eathdjwehkjsqrcykyrttolztvttycydinqaobipcolkdadhdcomatzpcki' \
        'bwldbjxkifzxcfuqkfsuzispwnprbdomlypmxvogoqqtvxclkxfwmyspabiayh' \
        'mfldzcwhhdwuuxwvkhywjkiiohrqeeatsyrqfctjsmkcypwqfkwrkosqgjbymsi' \
        'higeyxpvplikqxeiblqhxbsffbfddpnzmjwnczvvzflhnuoxfoplyeqztxscley' \
        'kcvztyexkowgmofvzwmcddeddxqraugnscfaqlhufqhklruobxjvrzzsergzgle' \
        'kcarmlipwgnzstvwqrorjtbtdedclmmljbwxrefqndkkfjksephvndkrjxzgati' \
        'jwuanrszgywwchamhmstomginrplyeddtxfjndcztghbctikbqgcswrkatpmuoh' \
        'qfausnzdsauubbnwmfipxeigpsyaxcibclhcmxebwjylapkdabuqblcqznglkqm' \
        'slpwdlnhkyvuascuwwjykvxitccbrfrgcrxldcddrwsltcbresplcaamchhfon' \
        'wvubujexvqquprefofocgajzttfkmhwpcpwdsrolienomwyglcsqwhizosaqpu' \
        'lythkqfyxjuekqawwfuxlphghotuqqkmvpftcdexvrbaeygvgkarpkecbybuujl' \
        'cpczcxvqpryvfezzlrtalfzzheupnyhlnvncnjchyucglvrbolfeqfytqojstgw' \
        'btbejdgajnzwmkjhnawletgkzudirjixmdnuuelkvygitfqbctcwjepfuuinkxe' \
        'mvctthihxbwnaombcdhyyxyfucjglhuehqxcvtjpqaypqrgnunncwadnhyuduhhb' \
        'spcwhjeyclkdacwhgmkpveyvwphqywkkcgheohomlqyfypikdkbxmoplkzlpurdc' \
        'mwglfhijfpewxjycqarpinmhpdkvflzdbvapztwxftcojyqwqdhrywrfanveukqc' \
        'zvjzajqsmdzztnwtrinbjzcxczodczdouvhvjmshfcvkoihofoqyspcegtnbgvxe' \
        'ehndzfzcbrqscvkdctccdsiepsvjoydcbircdhgrsxjzqcesggmsoqdiovxlklp' \
        'pkvkjtdzaybtudjrbnstwwmcnewghngejxwdnoisxjeeshopcnjpylkszejetlz' \
        'nlwditrvniczxvtcpxtevlivuwpifwililkqoymbznxtcauuimwmnnsywyxoprs' \
        'gpqopxujsmtntqbriythktgqlwheqpyejyufrvnwzaortobxvoidqsckdfwecggi' \
        'gjlrrngkkrbpxsmmqgnvrsqofugjaisclmgondkofdxrcaletvmxmufcqqqgrph' \
        'dvaenhmxpmhwytfyuffuylmqqqqxpuumdkhalbyuzqodivwkrjrotptzviuriwr' \
        'wlkgqvvgnqczigzzefxmmvyttcknheeklknvfxfakkogomnlxheschgivrkqqut' \
        'kszpglxedgrfojeetwgmoyprydilmspoosuzlaexivqlvltckjwunqzdpndzfi' \
        'nssjxbffqogxtmgwkiuxflxsozwrgdwbnbwoqmbpfgecgtfmnjdzpfltumixxi' \
        'ygthuqihikgmbmyyqmmkfvqzztgekojrgrarrnzciczusebdhphatdzackfqyx' \
        'zzvnlxupbdwcxgqyautlhtxtglwmupgcxiowkgnnkcdbcihwmvofqsioviwhcl' \
        'gqjzeunypxsayuuiaknvhsvixkfiuctnctjqokdovqshurwlhpykvmhjdcmcwx' \
        'gjncuwfygmgbujyrxnrqbzcefmnlpuhntkbxhykphrpjuxocsomziszymjlfrs' \
        'vybdoywrycoxsawiqrzkzhgefzmmrxstskwfwejasmyjsjwvkukdpwhkpvghop' \
        'amhegffnwyvadydpmtlvlssidbovoscnfaavoltqiqicogzvpcizxwneacupsl' \
        'jzclnxqoirjlrikoobjmsqvkavhvazmffebvcaubodvatyttpwsuaxsfbrxhyr' \
        'rkwdsdipybouprojcivxdgxoggcggllysymtuumapxpfqnhgotzuqhvkcxhesf' \
        'sypkcycfbrjuxiacvoxycvocszpcukjwqyqxyugabcgiyvffvpdcfaybwohggs' \
        'rcdtseendbtkzjwrhwrffbttemrxnrnhikbeylfovmezjrfetgxcgvbmmllsyu' \
        'tuszaotyhqdqnokdmeymkwttyzqlnjvefxknzbggjjyfulguwtocgruvxbedxz' \
        'zvgrkhjegfaqdmkbehziducbgrgbnbloyxyazsmyijujfuigqmvxrjxckdewwe' \
        'nnwmyigjlbvgwtrdricaxtaepzyvrofqfmjjestjbmrtwtfxhanfptjnopbfpj' \
        'xsujmizgeqqlvinpaxkmrnwyymouirlgpmfzuvdpgqnimehtfhgwcvradklekw' \
        'bjhftbhhrfjemrloqyceqkqdiqmwbpxeclymbysevepifxazbdulmltyuqvsjc' \
        'reccxfxbsqnznfcngchctpxanqsfldpeaslbbibvrpexowptbnjqgojqazxgsp' \
        'yveqiqlglmlutepidtjrrucqqwaenphyzefovhuceslknvfzasiegmedkxdmcg' \
        'jtsboyzynddomlccygxzuytuecfbdwfhbtoelrihogffqpkahpwutbdhzvkbxn' \
        'cvvnjyjiqjujxdaamsmilfxewlqeshiwdegqytphtbqbcxfiavzoldumbjahlq' \
        'vxpqatisxefhfsdktjrlfxgodrdomzdnahlbggbrgchiwvnveptflozemxipxf' \
        'ujagkficqqmawtmetbaiflfykrrumegxuvomqduiamiuqpxifbmgtyossqxqlp' \
        'jausfardpmelhtmusvppyfcseozzkvxgrbncsmljjfuzpmeggymmxpvpgwqdvl' \
        'pxdruscnikbpcppwnyxwsflucxjnkzhwpjukxwnxolrwjlptltatgjxcaswhqf' \
        'jqoygawfggypkzzwzrjepmlmwapydapbyxvvwtsnixvvjfvctomtxtwivxtiwv' \
        'sdlgoaeomsgwulhromiirgdtceluklfuhwlacjckylexxeauetsosokrfewsog' \
        'elkisripvkxkemrtieaedvbxwrjxswltpjnjroahmblanhkbhulufplvbomzqr' \
        'tcxiouvqmzlijsbcpqshpehnbmupcxvypxwuagwayopyhdgsfbxjunomocnpzn' \
        'dhkurrpvayftwnnkqkohbycxudfazztunpanmhxfhuoiisfwooihpddqeoxao' \
        'fkzrfwzfsmfryixoogkqyfxymmyksnmdexfkmwluexagwbnmajpphnmxoopgc' \
        'kxqjqcvqcflcpfufrfdcvsvgjhdazzmictidjulhxhomnprngmjeiueueqzci' \
        'whnvsfmowuwvouqbpdsxhmjfftaqvybyjvjunxeiczxnklqcjqzjkmpdifypa' \
        'clebjqznhnznzzsodezvefpgqfiagokipgdrmwnkmiezbvxdpktiplqxeepkr' \
        'bwhyomxhepynqedufaxavrijsvpuqwhlymxkcpzqzizqqzkwitrcsodkrxoqz' \
        'azzcimzubgfcbmwlbzgamezlcwfntpimxlbsepyldidnbcxmsubshyhfzvmlw' \
        'qqoyfitowgpcfqawxhpazabmsdgfgxwdefdadcfiovkyfjunnekbdxhkncvwpb' \
        'dshrhfvbyarlamiawpmtcsfjrapumlhgnsghxblfyykfqyoypejcwgyhxzasgxp' \
        'wbxweokcrwlggbzgmwthkhkhcbvptcpezfmwydznypirsbdbfryomhxumiawpd' \
        'vvrumdzpyjdnvyjncunwxtpsckyevqddojaslnszzclsvapjglinekmkfblqyg' \
        'tszqpnrfcgnyjobdaqvfjzrzdszqkatrblhxjfujvvkbcbzzqslyiiahnnions' \
        'oygqaowwramxozvqeghcjntchjyuepkrsctbxpsmzbluhjmrktzwptbrvtojlu' \
        'zmsoukftfuxdpugmqouhtiqnpzuqrhjixbaohawzouulfzmarmsmexkfghtxsn' \
        'qafphxosoztkdzuknmtubobuhnejmfuyeudkttpxbwaowipaiizuothqmvusuj' \
        'amzhpjpvlblqkiplbtntsdpcxdguhnmbpsusuwwzmfhenvmbktoaejhgqlnr' \
        'tvmqkbcywxmuujsttqygwmbkdkeeiofzsrzofvhrfzovtlomokrnkulbtbuh' \
        'dfxyrhqbvuavcmmngovbkhophlfgxaqeoslrmjvrteujbpcdyoqkaulmmhvyvz' \
        'zbczjwlskotyaxvpkfljhkrhdwophcbhgkxwlvdhcdtpfsdkoxlpvhdqbbewph' \
        'cbgspbtjlehbahcomkjeyrdcsvibvgbaokakleamzlykrzofnwjdftagalhksa' \
        'ogcxrzoudikyvogziolreyjbjjpyzbjxygmctvjqdrupzgzzggusikykobwqv' \
        'lxvjjxqqtmwsvfqqhzaurtxbqynpzvgafwnzidkyamxfcxpmwyfyejzbjecws' \
        'haqslesczcvgbevglodvqmirfalcklrogpffvhuegjquhijvrlgvcsrdwwgce' \
        'jbwiwwxhqilakdokdrmraiucnlayytomspyfpoeckjmhwpafboywitcekngid' \
        'rupyxhxjnljauouevcwkmooezfcebhgnjdjwjuexlvslbbtotbohvxrqsgerl' \
        'yqmqlmremkzeavgkkpskgcbtpnufpcuzmppaufgsguwpmphjvuzgkeyjwifnu' \
        'cncexzhwpourphjlrbzlldwmkumsvugpnfegyefyxreghwpcekxyqxehkrsfu' \
        'clnilxzclysdmbynaaxpbktrpokunjenmwgopqeilmyjouqaftuisvzvnonct' \
        'tcmyfvlfttpuacsqdragdngwthpmtkbthtehvqtjwustmwlveynbnxyftkopl' \
        'kbmsrocaaysnclpc'
    k = 6118
    assert 1181 == maxVowels(s, k), 'test 2'