from typing import List


class BaseIter:
    def __init__(self, data: List[str]):
        self.data = data

    def __repr__(self):
        return str(self.data)


class IterAndNext(BaseIter):
    def __iter__(self):
        self.iter = 0
        return self

    def __next__(self):
        if self.iter == len(self.data):
            raise StopIteration
        else:
            step_value = self.data[self.iter]
            self.iter += 1
            return step_value


class GetItem(BaseIter):
    def __getitem__(self, item):
        return self.data[item]

    def __setitem__(self, key, value):
        self.data[key] = value


class IterYield(BaseIter):
    def __iter__(self):
        for item in self.data:
            yield item


def test(res):
    for klass in (IterAndNext, GetItem, IterYield):
        assert res == [x for x in klass(res)]
    print('all tests passed')


def test_stop_iter(res, *klasses):
    for klass in klasses:
        d = klass(res)
        it_d = iter(d)
        try:
            for _ in range(len(res) + 1):
                if klass == IterAndNext:
                    next(d)
                else:
                    next(it_d)
            assert False, 'StopIteration not achieved'
        except StopIteration:
            assert True


if __name__ == '__main__':
    res = ['Bob', 'Sue', 'Pasha', 'Misha']
    test(res)
    test_stop_iter(res, IterAndNext, GetItem, IterYield)
