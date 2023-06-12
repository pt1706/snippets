from typing import List


def canPlaceFlowers(flowerbed: List[int], n: int) -> bool:
    for i in range(len(flowerbed)):
        if flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 0) and (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0):
            flowerbed[i] = 1
            n -= 1
    return n <= 0


if __name__ == '__main__':
    flowerbed = [1, 0, 0, 0, 1]
    n = 1
    assert True is canPlaceFlowers(flowerbed, n), 'test 1'

    flowerbed = [1, 0, 0, 0, 1]
    n = 2
    assert False is canPlaceFlowers(flowerbed, n), 'test 2'

    flowerbed = [1, 0, 0, 0, 0, 1]
    n = 2
    assert False is canPlaceFlowers(flowerbed, n), 'test 3'

