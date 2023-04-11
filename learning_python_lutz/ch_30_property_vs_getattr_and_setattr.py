class Proper:

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def __repr__(self):
        res = f'Instance of class: {self.__class__.__name__}'
        for attr in self.__dict__:
            res += f'\n{attr} --> {getattr(self, attr)}'
        return res

    # def __getattr__(self, item):
    #     if item == 'name':
    #         return self.__dict__['__name']
    #     if item == 'age':
    #         return self.__dict__['__age']
    #     else:
    #         raise AttributeError('Attr does not exist')
    #
    # def __setattr__(self, key, value):
    #     if key == 'name' or key == '_Proper__name':
    #         self.__dict__['__name'] = value
    #     elif key == 'age' or key == '_Proper__age':
    #         self.__dict__['__age'] = value
    #     else:
    #         raise AttributeError('Attr does not exist')

    # setting with property
    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__age = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        print('from set name')
        self.__name = value


p = Proper('Bob', 25)
if __name__ == '__main__':
    print(p)
    print(p.age)
    p.age = 30
    print(p.age)

