class Decor:
    def __init__(self, mult=1):
        self.mult = mult

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            print('from decor: before call')
            res = func(*args, **kwargs) * self.mult
            print('from decor: after call')
            return res
        return wrapper


@Decor(mult=5)
def multiple(x):
    return x * 2


if __name__ == '__main__':
    assert 20 == multiple(2)