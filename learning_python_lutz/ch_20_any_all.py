lst = map(float, input().split(' '))  # 2 4 6 8 22 56
print(all(map(lambda x: True if x == round(x) else False, lst)))


# ------------------ 2 ---------------------


def is_string(lst):
    return all(map(lambda x: isinstance(x, str), lst))


def is_string_and_number(lst):
    return all(map(lambda x: isinstance(x, (str, int)), lst))


lst = ['a', 'spam', 'ham']
lst_1 = ['a', 'spam', 'ham', 1]

if __name__ == '__main__':
    assert True is is_string(lst)
    assert False is is_string(lst_1)
    assert True is is_string_and_number(lst)
    assert True is is_string_and_number(lst_1)


# ------------------ 3 ---------------------


def is_free(lst):
    return any(map(lambda x: True if '#' in x else False, lst))


def is_free_1(lst):
    return any('#' in i for i in lst)


lst = ['o x o', 'x o x', 'o o #']

if __name__ == '__main__':
    print(is_free_1(lst))
    print(*('#' not in i for i in lst))
