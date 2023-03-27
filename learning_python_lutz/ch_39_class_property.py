class Tester:
    def __init__(self, name="Bob", age=40):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        print('getter() called')
        return self.__name

    @name.setter
    def name(self, name):
        print('setter() called')
        self.__name = name

    @name.deleter
    def name(self):
        del self.__name
