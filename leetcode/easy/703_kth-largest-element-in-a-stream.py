import heapq
from typing import List


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = sorted(nums)[-self.k:]

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        if len(self.nums) > self.k:
            heapq.heappop(self.nums)
        return self.nums[0]


class KthLargest_simple:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums

    def add(self, val: int) -> int:
        self.nums.append(val)
        nums = self._sorted()
        return nums[self.k - 1]

    def _sorted(self):
        self.nums.sort(reverse=True)
        return self.nums


if __name__ == '__main__':
    obj = KthLargest(3, [4, 5, 8, 2])
    assert 4 == obj.add(3), 'test 1.0'
    obj.add(5)
    obj.add(10)
    obj.add(9)
    assert 8 == obj.add(4), 'test 1.1'

    obj = KthLargest(1, [])
    assert -3 == obj.add(-3), 'test 2.0'
    obj.add(-2)
    obj.add(-4)
    obj.add(0)
    assert 4 == obj.add(4), 'test 2.1'
