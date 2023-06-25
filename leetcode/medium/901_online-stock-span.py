class StockSpanner:
    def __init__(self):
        self.prices = []

    def next(self, price: int) -> int:
        res = 1
        while self.prices:
            p, c = self.prices.pop()
            if p > price:
                self.prices.append([p, c])
                break
            res += c
        self.prices.append([price, res])
        return res


class StockSpanner_simple:
    def __init__(self):
        self.prices = []

    def next(self, price: int) -> int:
        self.prices.append(price)
        res = 0
        for p in self.prices[::-1]:
            if p > price:
                return res
            res += 1
        return res


if __name__ == '__main__':
    s = StockSpanner()
    s.next(100)
    s.next(80)
    assert 1 == s.next(60), 'test 1.1'
    assert 2 == s.next(70), 'test 1.2'
    assert 1 == s.next(60), 'test 1.3'
    assert 4 == s.next(75), 'test 1.4'
    assert 6 == s.next(85), 'test 1.5'

    s = StockSpanner()
    s.next(2)
    s.next(3)
    assert 3 == s.next(5), 'test 2.1'
    assert 4 == s.next(5), 'test 2.2'
    assert 5 == s.next(6), 'test 2.3'
    assert 6 == s.next(6), 'test 2.4'
    assert 7 == s.next(7), 'test 2.5'
