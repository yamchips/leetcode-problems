def fastPow(x: float, n: int) -> float:
    if n == 0:
        return 1
    if n % 2 == 0:
        half = fastPow(x, n // 2)
        return half * half
    else:
        half = fastPow(x, n // 2)
        return half * half * x

def myPow(x: float, n: int) -> float:
    if n < 0:
        x = 1 / x
        n = -n
    return fastPow(x, n)

def myPowIterative(x: float, n: int) -> float:
    if n < 0:
        x = 1 / x
        n = -n
    res = 1
    while n:
        if n % 2:
            res *= x
        x = x ** 2
        n = n // 2
    return res

if __name__=='__main__':
    myPowIterative(2.0, 5)