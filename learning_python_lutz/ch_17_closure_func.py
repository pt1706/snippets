def counter(start=0):
    def steper():
        nonlocal start
        start += 1
        return start
    return steper


if __name__ == '__main__':
    C1 = counter()
    C2 = counter(10)
    print(C1(), C2())
    print(C1(), C2())
    print(C1(), C2())


def counter_add():
    def count(arg):
        return arg + 5
    return count


if __name__ == '__main__':
    cnt = counter_add()
    k = int(input())
    cnt(k)


def counter_add(n):
    def count(arg):
        return arg + n
    return count


if __name__ == '__main__':
    cnt = counter_add(2)
    k = int(input())
    print(cnt(k))


def outer_func(tp: str = 'list'):
    def get_collection(k):
        k = k.split(' ')
        if tp == 'list':
            return list(map(lambda x: int(x), k))
        return tuple(list(map(lambda x: int(x), k)))
    return get_collection


get_collection = outer_func('lis')
print(get_collection('-5 6 8 11 0 111 -456 3'))
