from typing import List


class BaseMagic:
    def __init__(self, data: List[str]):
        self.data = data

    def __repr__(self):
        return str(self.data)


class Contains(BaseMagic):
    def __contains__(self, item):
        return item in self.data


class GetItem(BaseMagic):
    def __getitem__(self, item):
        return self.data[item]

    def __setitem__(self, key, value):
        self.data[key] = value


if __name__ == '__main__':
    data = ['Bob', 'Sue', 'Pasha', 'Misha']
    assert True is ('Bob' in Contains(data))
    assert False is ('Max' in Contains(data))

    try:
        assert True is ('Bob' in BaseMagic(data)), 'should not work'
    except TypeError:
        assert True

    assert True is ('Bob' in GetItem(data))
    assert False is ('Max' in GetItem(data))
