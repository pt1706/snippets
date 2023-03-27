import time
result = {2: 1024}


def decor(func):
    def wrapper(arg):
        start_time = time.time()
        if arg in result.keys():
            print(
                "from memory -> --- %07.3f ms ---" %
                ((time.time() - start_time) * 1000))
            return result[arg]
        else:
            result[arg] = func(arg)
            print(
                "calculate -> --- %07.3f ms ---" %
                ((time.time() - start_time) * 1000))
            return result[arg]

    wrapper.__doc__ = func.__doc__
    wrapper.__name__ = func.__name__
    return wrapper


@decor
def my_pow(value):
    return value ** 10


if __name__ == '__main__':
    print(f'Function {my_pow.__name__}')
    print(my_pow(2), '\n')


def show_menu(func):
    def wrapper(arg):
        for i, item in enumerate(func(arg), 1):
            print(f'{i}. {item}')

    wrapper.__doc__ = func.__doc__
    wrapper.__name__ = func.__name__
    return wrapper


@show_menu
def get_menu(s: str) -> list:
    return s.split(' ')


if __name__ == '__main__':
    s = 'Главная Добавить Удалить Выйти'
    print(f'Function {get_menu.__name__}')
    get_menu(s)
    print('\n')


def get_sorted(func):
    def wrapper(arg):
        lst = sorted([int(i) for i in func(arg)])
        print(*lst)
    return wrapper


def get_list(s: str) -> list:
    return s.split(' ')


if __name__ == "__main__":
    s = '8 11 -5 4 3 10'

    get_list = get_sorted(get_list)
    get_list(s)


from typing import List, Callable


def get_dict(func: Callable):
    def wrapper(*args: str):
        return dict(tuple(zip(func(*args)[0], func(*args)[1])))
    return wrapper


def get_lists(*args: str) -> List[list]:
    return [i.split(' ') for i in args]


if __name__ == "__main__":
    s = 'house river tree car'
    s1 = 'дом река дерево машина'

    get_lists = get_dict(get_lists)
    print(get_lists(s, s1))


t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd',
     'е': 'e', 'ж': 'zh', 'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k',
     'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r',
     'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c',
     'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '',
     'э': 'e', 'ю': 'yu', 'я': 'ya'}


def replacer(f):
    def wrapper(arg: str):
        arg = (arg.replace(' ', '-').replace(':', '-').
               replace(';', '-').replace('.', '-').
               replace(',', '-').replace('_', '-').lower())
        translation = f(arg)
        translation = translation.replace('---', '-')
        translation = translation.replace('--', '-')
        return translation

    wrapper.__doc__ = f.__doc__
    wrapper.__name__ = f.__name__
    return wrapper


def translater(word: str):
    translation = ''
    for i in word:
        if i in t.keys():
            translation += t[i]
        else:
            translation += i
    return translation


word = 'Python это круто'
x = replacer(translater)
print(x(word))
