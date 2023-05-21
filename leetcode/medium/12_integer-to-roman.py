def intToRoman(num: int) -> str:
    d = {1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX', 10: 'X', 20: 'XX',
         30: 'XXX', 40: 'XL', 50: 'L', 60: 'LX', 70: 'LXX', 80: 'LXXX', 90: 'XC', 100: 'C', 200: 'CC', 300: 'CCC',
         400: 'CD', 500: 'D', 600: 'DC', 700: 'DCC', 800: 'DCCC', 900: 'CM', 1000: 'M', 2000: 'MM', 3000: 'MMM'}
    res = ''
    m = 1000
    while num:
        item = num // m
        res += d.get(item * m, '')
        num = num % m
        m /= 10
    return res


if __name__ == '__main__':
    assert 'III' == intToRoman(3), 'test 1'
    assert 'LVIII' == intToRoman(58), 'test 2'
    assert 'MCMXCIV' == intToRoman(1994), 'test 3'
    assert 'X' == intToRoman(10), 'test 4'
    assert 'XL' == intToRoman(40), 'test 5'