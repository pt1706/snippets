class Tester:
    def __init__(self, start=0):
        self.counter = start

    def __call__(self, step=1):
        self.counter += step
        return self.counter


if __name__ == '__main__':
    t = Tester()
    assert t() == 1
    assert t(2) == 3
    assert t() == 4
    assert t(6) == 10
    t1 = Tester(10)
    assert t1() == 11
    assert t1() == 12
    assert t1(10) == 22
    assert t1(0) == 22
    assert t1(-12) == 10
    print('all tests passed')


# ------------------2 exercice-----------------------------------


class TestDecor:
    def __init__(self, func):
        self.__func = func

    def __call__(self, *args, **kwargs):
        return self.__func(*args, **kwargs)


def get_summ(x, y):
    return x + y


if __name__ == '__main__':
    t = TestDecor(get_summ)
    assert t(5, 4) == 9
    assert t(-100, -99) == -199
    print('all tests passed')


# ------------------2 exercice-----------------------------------


class MyDecor:
    def __init__(self, func):
        self.func = func
        self.counter = 0

    def method(self, *args, **kwargs):
        return self.func(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        self.counter += 1
        x, y = args
        x *= 2
        y *= 2
        return self.func(x, y, **kwargs)


def test(x, y):
    return x * y


@MyDecor
def test1(x, y):
    return x * y


if __name__ == "__main__":
    m = MyDecor(test)
    assert m.method(5, 4) == 20
    assert m.method(0, 4) == 0
    assert m.method(10, 10) == 100
    assert m(5, 4) == 80
    assert m(0, 4) == 0
    assert m(10, 10) == 400
    assert m.counter == 3
    assert test1(10, 10) == 400
    assert test1(2, 3) == 24
    assert test1.counter == 2

# ------------------3 exercice-----------------------------------


class MyClass:
    counter = 0

    def __init__(self, name, age, job):
        self.name = name
        self.__age = age
        self.__job = job
        self.counter = MyClass.counter
        MyClass.counter += 1

    def __repr__(self):
        return f"instance N: {self.counter}, " \
               f"name: {self.name}, age: {self.__age}, " \
               f"job: {self.__job}"

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    @staticmethod
    def method():
        print(f'created {MyClass.counter} instances')


class Child(MyClass):
    counter = 0

    def __init__(self, *args, **kwargs):
        Child.counter += 1
        super().__init__(*args, **kwargs)

    @classmethod
    def class_method(cls):
        print(f'created {cls.counter} instances of class {cls.__name__}')


if __name__ == "__main__":
    I = MyClass("Pavel", 35, "Programmer")
    I1 = MyClass("Bob", 25, "Haker")
    I2 = Child("Mira", 5, "child")

# ------------------3 exercice-----------------------------------


class MyDecor:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        kwargs['y'] = 100
        return self.func(*args, **kwargs)


@MyDecor
def adder(x, y):
    return x + y


if __name__ == '__main__':
    assert adder(x=2, y=2) == 102
    print('all tests passed')


# ------------------with decor params-----------------------------------


def decor(*args_1, **kwargs_1):
    def wrapper_1(func):
        def wrapper_2(*args_2, **kwargs_2):
            print(*args_1, *kwargs_1)
            return func(*args_2, **kwargs_2) * kwargs_1.get('z', 2)
        return wrapper_2
    return wrapper_1


@decor('test', z=10)
def my_func(x, y):
    return x + y


if __name__ == '__main__':
    assert 40 == my_func(2, 2)
    print('all tests passed')