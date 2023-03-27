def timer(func):
    import time

    def wrapper(arg):
        start_time = time.time()
        result = func(arg)
        print("--- %07.3f ms ---" % ((time.time() - start_time) * 1000))
        return result

    wrapper.__doc__ = func.__doc__
    wrapper.__name__ = func.__name__
    return wrapper


@timer
def factor(value):
    if value > 1:
        return value * factor(value - 1)
    else:
        return 1


print(factor(50))


# ------------------3 exercice-----------------------------------


def get_rec_N(N):
    if N:
        get_rec_N(N - 1)
        print(N)
        return N
    print('start')
    return 'start'


get_rec_N(8)


# ------------------3 exercice-----------------------------------

s = '8 11 -5 4 3'


def recur(s: str) -> int:
    if len(s) == 0:
        return 0
    line = s.strip(' ').split(' ')
    last = int(line.pop())
    return last + recur(' '.join(line))


print(recur(s))


# ------------------3 exercice-----------------------------------


d = [1, 2, [True, False],
     ["Москва", "Уфа", [100, 101],
      ['True', [-2, -1]]], 7.89]


def get_line_list(d, a=[]):
    for item in d:
        if type(item) != list:
            a.append(item)
            continue
        get_line_list(item, a)
    return a


print(get_line_list(d))


# ------------------3 exercice-----------------------------------


def get_path(N):
    if N == 1:
        return 1
    if N == 2:
        return 2
    return get_path(N - 1) + get_path(N - 2)


if __name__ == '__main__':
    assert get_path(1) == 1
    assert get_path(2) == 2
    assert get_path(3) == 3
    assert get_path(4) == 5
    print('all tests passed')


# ------------------search by merge-----------------------------------


def merge_lists(l1, l2):
    res = []
    i = j = 0
    while i < len(l1) and j < len(l2):
        if l1[i] <= l2[j]:
            res.append(l1[i])
            i += 1
        else:
            res.append(l2[j])
            j += 1
    if i < len(l1):
        res += (l1[i:])
    if j < len(l2):
        res += l2[j:]
    return res


def get_sorted(s):
    if len(s) == 2:
        return [s[0], s[1]] if s[0] < s[1] else [s[1], s[0]]
    if len(s) < 2:
        return s
    return merge_lists(get_sorted(s[0:len(s) // 2]),
                       get_sorted(s[len(s) // 2:]))


if __name__ == '__main__':
    assert get_sorted([3, 4, 5, -1, 0]) == [-1, 0, 3, 4, 5]
    assert get_sorted([-9, -9, -81, -81, -90, 0]) == [-90, -81, -81, -9, -9, 0]
    print('all tests passed')
