from abc import ABC, abstractmethod
import typing


class Adder(ABC):
    def __init__(self, value: typing.Union[list, str, tuple, dict]):
        self.data = value

    def __add__(self, other):
        return self.add(other)

    @abstractmethod
    def add(self, x):
        raise NotImplementedError


class ListAdder(Adder):
    def add(self, x: typing.Union[list, str, tuple]) \
            -> typing.Union[list, str, tuple]:
        return self.data + x


class DictAdder(Adder):
    def add(self, x: dict) -> dict:
        return {**self.data, **x}


if __name__ == '__main__':
    ins = ListAdder([1, 2, 3])
    assert ins.add([4, 5, 6]) == [1, 2, 3, 4, 5, 6]
    assert ins + [4, 5, 6] == [1, 2, 3, 4, 5, 6]
    ins = ListAdder('spam')
    assert ins.add('ham') == 'spamham'
    assert ins + 'ham' == 'spamham'
    ins = ListAdder((1, 2, 3),)
    assert ins.add((4, 5, 6),) == (1, 2, 3, 4, 5, 6)
    d1 = dict([(1, 'spam'), (2, 'ham')])
    ins = DictAdder(d1)
    d2 = {1: 'foo', 3: 'bar', 4: 'baz'}
    assert ins.add(d2) == {1: 'foo', 2: 'ham', 3: 'bar', 4: 'baz'}
    assert ins + d2 == {1: 'foo', 2: 'ham', 3: 'bar', 4: 'baz'}
    d3 = {}
    assert ins.add(d3) == {1: 'spam', 2: 'ham'}
    d4 = dict(spam=1, ham=2)
    assert ins.add(d4) == {1: 'spam', 2: 'ham', 'spam': 1, 'ham': 2}
    print('all test passed')


# ------------------------------------------------------------------


class MyList(list):
    def __init__(self, lst=[]):
        lst = lst[:]
        self.data = lst

    def __str__(self):
        return f'{self.data}'

    def __add__(self, other):
        return self.data + other

    def __radd__(self, other):
        return other + self.data

    def __getitem__(self, item):
        return self.data[item]

    def __iter__(self):
        self.ix = 0
        return self

    def __next__(self):
        if self.ix == len(self.data):
            raise StopIteration
        item = self.data[self.ix]
        self.ix += 1
        return item

    def __getattr__(self, name):
        print(name)
        return getattr(self.data, name)

    def append(self, item) -> list:
        self.data.append(item)


class MyListSub(MyList):
    counter = 0

    def __add__(self, other):
        MyListSub.counter += 1
        return super().__add__(other)

    @classmethod
    def print_counter(self):
        return MyListSub.counter


if __name__ == "__main__":
    I = MyList([1, 2, 3])
    assert I + [4, 5, 6] == [1, 2, 3, 4, 5, 6]
    assert [4, 5, 6] + I == [4, 5, 6, 1, 2, 3]
    assert I[0] == 1
    assert I[:] == [1, 2, 3]
    assert I[-1] == 3
    assert [i * 2 for i in I] == [2, 4, 6]
    assert list(map(str, I)) == ['1', '2', '3']
    assert sorted(I, reverse=True) == [3, 2, 1]
    I.append(4)
    I = MyListSub([1, 2, 3])
    I + [3, 4]
    I + [3, 4]
    I + [3, 4]
    B = MyListSub([1, 2, 3])
    B + [3, 4]
    B + [3, 4]
    assert MyListSub.print_counter() == 5
    assert I.print_counter() == 5
    assert B.print_counter() == 5
    print('all tests passed')


# ------------------------------------------------------------------


class Attrs:
    def __getattr__(self, name):
        print(name)

    def __setattr__(self, name, value):
        self.__dict__[name] = value
        print(self.__dict__[name])


def some_method(x):
    return x * 10


if __name__ == "__main__":
    A = Attrs()
    A.x = 5
    assert A.x == 5
    A.method = some_method
    assert A.method(5) == 50
    print('all tests passed')


class MyList:

    def __init__(self, value):
        self.value = value

    def __repr__(self):
        print(self.value)

    def intersection(self, other):
        return MyList(*self.value, *other)


M = MyList([1, 2, 3])


# ------------------------------------------------------------------


class MyList:

    def __add__(self, other):
        return self.union(other)

    def __init__(self, value: list) -> None:
        self.value = value[:]

    def __repr__(self) -> str:
        return f'{self.value}'

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index == len(self.value):
            raise StopIteration
        item = self.value[self.index]
        self.index += 1
        return item

    def __getitem__(self, item):
        return self.value[item]

    def union(self, *args):
        item = []
        for i in args:
            item.extend(i)
        return MyList([*self.value, *item])

    def intersection(self, *args):
        res = []
        for i in self.value:
            for arg in args:
                if i in arg:
                    res.append(i)
                break
        return MyList(res)

    def concat(self):
        new_lst = []
        for i in range(len(self.value)):
            item = self.value.pop()
            if item not in new_lst:
                new_lst += [item]
        return MyList(new_lst[::-1])


M = MyList([1, 2, 3])
M.union([4, 5])
M.intersection([1, 2])
M1 = MyList([1, 2, 3, 4, 4])
print(M.union([1, 4], [5, 6]))
print(M.intersection([1, 2, 4, 6], [5, 6, 1, 2]))


# ------------------7 exercices-----------------------------------


class Lunch:
    def __init__(self, customer_name):
        self.employee = Employee()
        self.customer = Customer(customer_name)

    def order(self, foodName):
        print(f"Ordering food: {foodName}, customer: {self.customer.name}")
        self.customer.placeOrder(foodName, self.employee)

    def result(self):
        print(f'Result: {self.customer.dish} '
              f'is cooking and soon be dispatched to {self.customer.name}')


class Employee:
    def __init__(self):
        self.name = 'Bob'

    def takeOrder(self, foodName, customer):
        print(f'{self.name} successfully took order')
        Food(foodName, customer)


class Customer:
    def __init__(self, name, dish=None):
        self.name = name
        self.dish = dish

    def placeOrder(self, foodName, employee):
        print(f'Customer {self.name} is served by waiter {employee.name}')
        employee.takeOrder(foodName, self)


class Food:
    def __init__(self, nameFood, customer):
        customer.dish = nameFood
        print(f'{str(nameFood).capitalize()} preparing')


if __name__ == '__main__':
    lunch = Lunch("Semen")
    lunch.order("pizza")
    lunch.result()

# ------------------8 exercice-----------------------------------


class Animal:
    def reply(self):
        return self.speak()

    def speak(self):
        raise NotImplementedError


class Mammal(Animal):
    pass


class Cat(Mammal):
    def speak(self):
        return 'meow-meow'


class Dog(Mammal):
    def speak(self):
        return 'gav-gav'


class Primate(Mammal):
    def speak(self):
        return 'u-u-u-u...aaaaa'


class Hacker(Primate):
    def speak(self):
        return 'Hello world'


if __name__ == "__main__":
    A = Animal()
    C = Cat()
    D = Dog()
    P = Primate()
    H = Hacker()
    print(C.reply())
    print(P.reply())
    print(H.reply())
    print(H.speak())


# ------------------9 exercice-----------------------------------


class Annimal:
    def line(self):
        print(f'{self}: {self.say()}')


class Customer(Annimal):
    name = "customer"

    def __repr__(self):
        return f'{self.name}'

    def say(self):
        return "that's one ex-bird!"


class Clerk(Annimal):
    name = "clerk"

    def __repr__(self):
        return f'{self.name}'

    def say(self):
        return "no it isn't..."


class Parrot(Annimal):
    name = "parrot"

    def __repr__(self):
        return f'{self.name}'

    def say(self):
        return None


class Scene:
    def __init__(self):
        self.customer = Customer()
        self.clerk = Clerk()
        self.parrot = Parrot()

    def action(self):
        self.customer.line()
        self.clerk.line()
        self.parrot.line()


if __name__ == '__main__':
    Scene().action()
