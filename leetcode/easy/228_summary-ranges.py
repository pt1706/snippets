from typing import List


def summaryRanges(nums: List[int]) -> List[str]:
    if not nums:
        return []
    if len(nums) == 1:
        return [str(nums[0])]
    res = []
    l, r = 0, 1
    while r < len(nums):
        while r <= len(nums) - 1 and nums[r] == nums[l] + r - l:
            r += 1
        if r - l == 1:
            res.append(str(nums[l]))
            l = r
        else:
            res.append(f'{str(nums[l])}->{str(nums[r - 1])}')
            l = r
    return res


def summaryRanges_first_att(nums: List[int]) -> List[str]:
    if not nums:
        return []
    res = []
    cur = nums[0]
    rng = ''
    for i in range(1, len(nums)):
        nxt = nums[i]
        if nxt - cur > 1:
            if not rng:
                res.append(str(cur))
            else:
                rng = rng + '->' + str(cur)
                res.append(rng)
                rng = ''
        else:
            if not rng:
                rng += str(cur)
        cur = nxt
    if not rng:
        res.append(str(cur))
    else:
        rng = rng + '->' + str(cur)
        res.append(rng)
    return res


if __name__ == '__main__':
    nums = [0, 2, 3, 4, 6, 8, 9]
    output = ['0', '2->4', '6', '8->9']
    assert output == summaryRanges(nums)

    nums = [-1]
    output = ['-1']
    assert output == summaryRanges(nums)
