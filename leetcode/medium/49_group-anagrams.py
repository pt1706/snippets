from typing import List


def groupAnagrams(strs: List[str]) -> List[List[str]]:
    if not strs:
        return [['']]

    dp = {}
    while strs:
        w = strs.pop()
        w_s = ''.join(sorted(w))
        if not dp.get(w_s):
            dp[w_s] = [w]
        else:
            dp[w_s].append(w)
    return list(dp.values())


def groupAnagrams_simple(strs: List[str]) -> List[List[str]]:
    def is_ana(w_1, w_2):
        w_1 = list(w_1)
        w_2 = list(w_2)
        w_1.sort()
        w_2.sort()
        return w_1 == w_2

    if not strs:
        return [['']]
    res = [[strs.pop()]]
    while strs:
        w_1 = strs.pop()
        for sub_res in res:
            if is_ana(w_1, sub_res[0]):
                sub_res.append(w_1)
                break
        else:
            res.append([w_1])
    return res


if __name__ == '__main__':
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    res = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
    print(groupAnagrams(strs))
    # assert res == groupAnagrams(strs), 'test 1'