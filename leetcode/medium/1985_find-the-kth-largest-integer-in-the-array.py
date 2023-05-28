import heapq
from typing import List


def kthLargestNumber(nums: List[str], k: int) -> str:
    nums = [-int(i) for i in nums]
    heapq.heapify(nums)
    item = ''
    while k:
        item = heapq.heappop(nums)
        k -= 1
    return str(-item)


if __name__ == '__main__':
    nums = ["3", "6", "7", "10"]
    k = 4
    assert "3" == kthLargestNumber(nums, k), 'test 1'