import math
from typing import List


def successfulPairs(spells: List[int], potions: List[int], success: int) -> List[int]:
    res = []
    potions.sort()

    for s in spells:
        l, r = 0, len(potions) - 1
        idx = len(potions)

        while l <= r:
            m = (r + l) // 2
            if s * potions[m] >= success:
                r = m - 1
                idx = m
            else:
                l = m + 1
        res.append(len(potions) - idx)

    return res


def successfulPairs_my(spells: List[int], potions: List[int], success: int) -> List[int]:
    res = []
    potions.sort()
    potions = [math.ceil(success / x) for x in potions]
    for i in range(len(spells)):
        if spells[i] in spells[:i]:
            for j in range(len(spells)):
                if spells[i] == spells[j]:
                    res.append(res[j])
                    break
            continue

        l, r = 0, len(potions)
        while l < r:
            m = (r - l) // 2 + l
            if spells[i] >= potions[m]:
                r = m
            else:
                l = m + 1
        if len(potions[r:]) == 0:
            res.append(0)
        else:
            res.append(len(potions[r:]))
    return res


if __name__ == '__main__':
    spells = [5, 1, 3]
    potions = [1, 2, 3, 4, 5]
    success = 7
    assert [4, 0, 3] == successfulPairs(spells, potions, success), 'test 1'
