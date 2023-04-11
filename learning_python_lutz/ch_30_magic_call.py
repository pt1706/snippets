from typing import List


class BaseMagic:
    def __init__(self, data: List[str]):
        self.data = data

    def __repr__(self):
        return f'{self.data}'


class Caller(BaseMagic):
    def __init__(self, data, func):
        self.func = func
        super().__init__(data)

    def __call__(self, *args, **kwargs):
        return self.func(self, *args, **kwargs)


def f(*args):
    return args[1] ** 2


def f_self(self, x):
    self.data = [item * x for item in self.data]
    return self.data


if __name__ == '__main__':
    c = Caller(['Bob', 'Sue', 'Pasha', 'Misha'], f)
    assert 16 == c(4)

    c = Caller(['Bob', 'Sue', 'Pasha', 'Misha'], f_self)
    assert ['BobBob', 'SueSue', 'PashaPasha', 'MishaMisha'] == c(2)

