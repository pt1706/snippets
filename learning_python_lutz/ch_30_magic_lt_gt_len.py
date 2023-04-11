from typing import List, Any


class BaseMagic:
    def __init__(self, data: List[str]):
        self.data = data

    def __repr__(self):
        return str(self.data)


class LtAndGt(BaseMagic):
    def __init__(self, value: int, data: List[Any] = []):
        self.value = value
        BaseMagic.__init__(self, data)

    def __lt__(self, other):
        print('lt')
        return self.value < other

    def __gt__(self, other):
        print('gt')
        return self.value > other


class LenMagic(BaseMagic):
    def __len__(self):
        return len(self.data)


if __name__ == '__main__':
    res = LtAndGt(5) < 6
    assert True is res

    res = LtAndGt(5) > 4
    assert True is res

    res = LenMagic(['Bob', 'Sue', 'Pasha', 'Misha'])
    assert 4 == len(res)
