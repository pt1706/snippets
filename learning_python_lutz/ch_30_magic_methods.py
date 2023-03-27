from typing import Union, Any


class Indexer:
    def __init__(self, value: Union[list, str]) -> None:
        self.data = value

    def __getitem__(self, item: int) -> Any:
        return self.data[item]


if __name__ == "__main__":
    input = ([1, 2, 3, 4, 5], 'spam', (1, 2, 3))

    def test(cls, seq: Union[list, str, tuple]) -> None:
        C = cls(seq)
        print(f'seq={seq}: C[0] = {C[0]}; len(seq)-1 = '
              f'{len(seq)-1}; list(map(lambda x: x*2, C)) = '
              f'{list(map(lambda x: x*2, C))}')

    for seq in input:
        test(Indexer, seq)


class Printer:
    def __init__(self, value):
        self.data = value

    def __str__(self):
        return f"from __str__: data = {self.data}"

    def __repr__(self):
        return f"from __repr__: data = {self.data}"


"""
Iterator toying
"""


class MyIter:
    def __init__(self, value):
        self.value = value

    def __getitem__(self, item):
        return self.value[item]

    def __iter__(self):
        self.iter = 0
        return self

    def __next__(self):
        if self.iter == len(self.value):
            raise StopIteration
        step_value = self.value[self.iter]
        self.iter += 1
        return step_value

    def __repr__(self):
        return str(self.value)


if __name__ == '__main__':
    m = MyIter([1, 2, 3, 4])
    assert list(m) == [1, 2, 3, 4]
    assert m[2] == 3
    try:
        m[4]
    except IndexError as error:
        assert error.args[0] == "list index out of range"


# ------------------ The same as above but only with iter ---------------


class MyIter:
    def __init__(self, value):
        self.value = value

    def __getitem__(self, item):
        return self.value[item]

    def __iter__(self):
        for x in self.value:
            yield x

    # def __next__(self):
    #     if self.iter == len(self.value):
    #         raise StopIteration
    #     step_value = self.value[self.iter]
    #     self.iter += 1
    #     return step_value

    def __repr__(self):
        return str(self.value)


if __name__ == '__main__':
    m = MyIter([1, 2, 3, 4])
    assert list(m) == [1, 2, 3, 4]
    assert m[2] == 3
    try:
        m[4]
    except IndexError as error:
        assert error.args[0] == "list index out of range"
    print(dir(iter(m)))


# ------------------2 exercise-----------------------------------


class MyIter:
    def __init__(self, value):
        self.value = value

    def __getitem__(self, item):
        return self.value[item]

    def __iter__(self):
        for x in self.value:
            yield x

    def __contains__(self, item):
        return item in self.value

    def __repr__(self):
        return str(self.value)

    def __getattr__(self, name):
        return f'There is no {name.upper()} attr'

    def __setattr__(self, name, value=0):
        self.__dict__[name] = value
        return f'Attr {name.upper()} setted, value is {value}'


def test(x):
    return True if x in m else False


if __name__ == '__main__':
    m = MyIter([1, 2, 3, 4])
    assert list(m) == [1, 2, 3, 4]
    assert m[2] == 3
    try:
        m[4]
    except IndexError as error:
        assert error.args[0] == "list index out of range"
    print(True if 1 in m else False)
    print(m.has)
    m.has = 4
    print(m.has)
