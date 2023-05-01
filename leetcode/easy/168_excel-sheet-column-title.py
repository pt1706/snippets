import string

# don't know why (columnNumber - 1)
def convertToTitle(columnNumber: int) -> str:
    res = ''
    while columnNumber:
        letter = string.ascii_uppercase[(columnNumber - 1) % 26]
        columnNumber = (columnNumber - 1) // 26
        res += letter
    return res[::-1]

# # can't find solution to go through test 1.1
# def convertToTitle(columnNumber: int) -> str:
#     d = dict(enumerate(string.ascii_uppercase, 1))
#     res = ''
#     while columnNumber != 0:
#         mult = 0
#         while True:
#             tail = (columnNumber) // 26 ** mult
#             if tail <= 26:
#                 break
#             mult += 1
#         res += d[(columnNumber) // 26 ** mult]
#         columnNumber = (columnNumber) - tail * (26 ** mult)
#     return res


if __name__ == '__main__':
    # print(convertToTitle(52))
    columnNumber = 1
    assert 'A' == convertToTitle(columnNumber), 'test 1'

    columnNumber = 52
    assert 'AZ' == convertToTitle(columnNumber), 'test 1.1'

    columnNumber = 28
    assert 'AB' == convertToTitle(columnNumber), 'test 2'

    columnNumber = 701
    assert 'ZY' == convertToTitle(columnNumber), 'test 3'

    columnNumber = 2147483647
    assert 'FXSHRXW' == convertToTitle(columnNumber), 'test 4'