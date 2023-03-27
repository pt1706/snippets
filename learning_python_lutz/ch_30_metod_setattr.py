class MyTest:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def __repr__(self):
        attr = [(k, v) for k, v in self.__dict__.items()]
        return f'{attr}'


if __name__ == '__main__':
    mt = MyTest(age=40, name='Bob', job='Dev')
    assert mt.age == 40, 'value age steed'

