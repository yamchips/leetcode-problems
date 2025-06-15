valueMap = {
    1: 'I',
    5: 'V',
    10: 'X',
    50: 'L',
    100: 'C',
    500: 'D',
    1000: 'M'
    }

def convert(num:int) -> str:
    if num in valueMap.keys():
        return valueMap[num]
    result = ''
    if str(num)[0] == '4' or str(num)[0] == '9':
        larger = 0
        for value in sorted(valueMap.keys(), reverse=True):
            if value > num:
                larger = value
                continue
            else:
                prefix = valueMap[larger - num]
                suffix = valueMap[larger]
                return prefix + suffix
    else:
        for value in sorted(valueMap.keys(), reverse=True):
            while num >= value:
                result += valueMap[value]
                num -= value
    return result

def intToRoman(num:int) -> str:
    input = str(num)
    n = len(input)
    result = ''
    for i in range(n):
        digit = int(input[i])
        power = n - 1 - i
        value = digit * 10 ** power
        result += convert(value)
    return result

def intToRoman2(num: int) -> str:
    valueMap = [
        (1000, 'M'),
        (900, 'CM'),
        (500, 'D'),
        (400, 'CD'),
        (100, 'C'),
        (90, 'XC'),
        (50, 'L'),
        (40, 'XL'),
        (10, 'X'),
        (9, 'IX'),
        (5, 'V'),
        (4, 'IV'),
        (1, 'I')
    ]

    result = ''
    for value, symbol in valueMap:
        while num >= value:
            result += symbol
            num -= value
    return result


if __name__=='__main__':
    print(intToRoman2(3749))
    print(intToRoman2(58))
    print(intToRoman2(1))
    print(intToRoman2(3999))