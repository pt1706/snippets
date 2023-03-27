def get_sort(d):
    new_d = sorted(d, reverse=True)
    return [d[k] for k in new_d]


d = {
    'cat': 'кот',
    'horse': 'лошадь',
    'tree': 'дерево',
    'dog': 'собака',
    'book': 'книга'
}

if __name__ == '__main__':
    assert ['дерево', 'лошадь', 'собака', 'кот', 'книга'] == get_sort(d)


def get_sorted_2(s):
    lst = list(map(int, s.split()))
    lst = list(set(lst))
    return lst.sort(reverse=True)[:4]


s = '10 5 4 -3 2 0 5 10 3'

if __name__ == '__main__':
    assert [10, 5, 4, 3] == get_sorted_2(s)


# ------------------ 2 ---------------------

lst_in = [
    'смартфон:120000',
    'яблоко:2',
    'сумка:560',
    'брюки:2500',
    'линейка:10',
    'бумага:500'
]


def get_cheap(lst_in):
    d = dict([tuple(x.split(':')) for x in lst_in])
    d = {k: int(v) for (k, v) in d.items()}
    t = tuple(d.items())
    lst = [(x[1], x[0]) for x in t]
    lst.sort()
    return list(dict(lst[:3]).values())


if __name__ == '__main__':
    assert ['яблоко', 'линейка', 'бумага'] == get_cheap(lst_in)
    print(*get_cheap(lst_in))

lst_in = [
    'Номер;Имя;Оценка;Зачет',
    '1;Портос;5;Да',
    '2;Арамис;3;Да',
    '3;Атос;4;Да',
    "4;д'Артаньян;2;Нет",
    '5;Балакирев;1;Нет'
]

lst = [x.split(';') for x in lst_in]
a = [1, 3, 2, 0]
lst = [
    sorted(
        [i for i in enumerate(item)],
        key=lambda x: a.index(x[0])
    ) for item in lst
]
lst = tuple(
    tuple(
        int(i[1]) if i[1].isdigit() else i[1] for i in item
    ) for item in lst
)
print(*lst)