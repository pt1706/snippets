from typing import List, Any


class BaseMagic:
    def __init__(self, data: List[str]):
        self.data = data

    def __repr__(self):
        return f'{self.data}'


class Adder(BaseMagic):
    def __add__(self, other):
        return Adder(self.data + [other])


if __name__ == '__main__':
    res = Adder(['Bob', 'Sue', 'Pasha', 'Misha'])
    assert ['Bob', 'Sue', 'Pasha', 'Misha'] == res.__repr__()
    new_res = res + 'Max'
    assert ['Bob', 'Sue', 'Pasha', 'Misha', 'Max'] == new_res.__repr__()

