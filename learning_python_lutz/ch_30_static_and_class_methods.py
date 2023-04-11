class Main:
    counter = 0

    @classmethod
    def count(cls):
        cls.counter += 1

    def __init__(self):
        self.count()

    @classmethod
    def show_count(cls):
        return cls.counter


class Sub(Main):
    counter = 0


class DoubleSub(Main):
    counter = 0


if __name__ == '__main__':
    a = Main()
    b, c = Sub(), Sub()
    d, e, f = DoubleSub(), DoubleSub(), DoubleSub()
    print(Main.show_count())
    print(Sub.show_count())
    print(DoubleSub.show_count())


# ------------------------


class BaseCount:
    counter = 0

    def __init__(self):
        BaseCount.counter += 1

    @staticmethod
    def show_count():
        return BaseCount.counter


class SubCount_1(BaseCount):
    counter = 0

    def __init__(self):
        BaseCount.__init__(self)
        SubCount_1.counter += 1

    @classmethod
    def show_count(cls):
        return cls.counter


if __name__ == '__main__':
    bc = BaseCount()
    print(bc.show_count())
    bc = BaseCount()
    print(bc.show_count())
    sc = SubCount_1()
    print(sc.show_count())
    sc = SubCount_1()
    print(sc.show_count())
    print(f'Base number of instces: {BaseCount.show_count()}')
    print(f'Sub number of instces: {SubCount_1.show_count()}')