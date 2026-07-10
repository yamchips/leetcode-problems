# given an integer, return it as a string
# get each digit and return them

def int_to_str(n: int) -> str:
    if n == 0:
        return '0'
    result = []
    number = abs(n)
    while number != 0:
        digit = number % 10
        result.append(str(digit))
        number = number // 10
    if n < 0 :
        result.append('-')
    result.reverse()
    return ''.join(result)


if __name__=="__main__":
    print(int_to_str(123)) 
    print(int_to_str(-456))