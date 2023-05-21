from typing import List


def topKFrequent(nums: List[int], k: int) -> List[int]:
    d = {}
    for i in nums:
        d[i] = d.get(i, 0) + 1

    values = [[] for _ in range(len(nums) + 1)]
    for key, v in d.items():
        values[v].append(key)
    res = []
    for i in range(len(values) - 1, -1, -1):
        for j in values[i]:
            res.append(j)
            if len(res) == k:
                return res


def topKFrequent_simple(nums: List[int], k: int) -> List[int]:
    """works"""
    d = {}
    for i in nums:
        d[i] = d.get(i, 0) + 1
    res = [(v, key) for key, v in d.items()]
    res = sorted(res, reverse=True)[:k]
    res = [key for v, key in res]
    return res


if __name__ == '__main__':
    nums = [3, 0, 1, 0]
    assert [0] == topKFrequent(nums, 1)