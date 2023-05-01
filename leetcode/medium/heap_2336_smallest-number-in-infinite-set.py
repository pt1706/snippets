import heapq


class SmallestInfiniteSet:

    def __init__(self):
        self.heap = []
        self.small = 1

    def popSmallest(self) -> int:
        if not self.heap:
            self.small += 1
            return self.small - 1
        return heapq.heappop(self.heap)

    def addBack(self, num: int) -> None:
        if num < self.small and num not in self.heap:
            heapq.heappush(self.heap, num)


if __name__ == '__main__':
    obj = SmallestInfiniteSet()
    obj.addBack(2)
    assert 1 == obj.popSmallest(), 'test 1'
    assert 2 == obj.popSmallest(), 'test 2'
    assert 3 == obj.popSmallest(), 'test 3'
    obj.addBack(1)
    assert 1 == obj.popSmallest(), 'test 4'
    assert 4 == obj.popSmallest(), 'test 5'
    assert 5 == obj.popSmallest(), 'test 6'
