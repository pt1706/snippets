class RecentCounter:

    def __init__(self):
        self.calls = []

    def ping(self, t: int) -> int:
        self.calls.append(t)
        new_calls = []
        for call in self.calls:
            if call >= t - 3000:
                new_calls.append(call)
        self.calls = new_calls
        return len(self.calls)


if __name__ == '__main__':
    r = RecentCounter()
    assert 1 == r.ping(1), 'test 1.1'
    assert 2 == r.ping(100), 'test 1.2'
    assert 3 == r.ping(3001), 'test 1.3'
    assert 3 == r.ping(3002), 'test 1.1'