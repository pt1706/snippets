from decimal import Decimal


def my_pow(star, end):
    res = []
    while star <= end:
        res.append(pow(star, 2))
        star += 1
    print(*res)


n, m = map(int, input().split())
my_pow(n, m)

# ------------------2 exercice-----------------------------------


def price_book(price, quantity=10):
    counter = 1
    while counter <= quantity:
        print(Decimal(price) * counter, end=' ')
        counter += 1


n = input()
price_book(n)

# ------------------3 exercice-----------------------------------


def deviding(n):
    devider = 1
    res = 0
    while devider <= n:
        res += 1 / devider
        devider += 1
    return round(res, 3)


n = int(input())
print(deviding(n))

# ------------------4 exercice-----------------------------------


def summer():
    res = 0
    while True:
        n = int(input('Введите число: '))
        if n == 0:
            break
        res += n
    return res


print(summer())

# ------------------4 exercice-----------------------------------
