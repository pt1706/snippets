from typing import List


def suggestedProducts(products: List[str], searchWord: str) -> List[List[str]]:
    products.sort()
    res = []
    res_r = products
    res_new = []
    for i in range(len(searchWord)):
        for word in res_r:
            if word[:i + 1] == searchWord[:i + 1]:
                res_new.append(word)
        res.append(res_new[:3])
        res_r = res_new
        res_new = []
    return res


if __name__ == '__main__':
    products = ['mobile', 'mouse', 'moneypot', 'monitor', 'mousepad']
    searchWord = 'mouse'
    res = [["mobile", "moneypot", "monitor"], ["mobile", "moneypot", "monitor"], ["mouse", "mousepad"], ["mouse", "mousepad"], ["mouse", "mousepad"]]
    assert res == suggestedProducts(products, searchWord), 'test 1'