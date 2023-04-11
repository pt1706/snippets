from typing import List


def maxProfit_n2(prices: List[int]) -> int:
    max_price = 0
    for min_index in range(len(prices)):
        price = max(set(prices[min_index:])) - prices[min_index]
        if price > max_price:
            max_price = price
    return max_price


def maxProfit(prices: List[int]) -> int:
    l, r = 0, 1
    max_price = 0
    while r < len(prices):
        if prices[r] - prices[l] > max_price:
            max_price = prices[r] - prices[l]
        if prices[r] < prices[l]:
            l = r
        r += 1
    return max_price


if __name__ == '__main__':
    prices = [7, 1, 5, 3, 6, 4]
    assert 5 == maxProfit(prices)