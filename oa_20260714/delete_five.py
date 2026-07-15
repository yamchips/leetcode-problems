'''
Given an integer, return the maximum possible value obtainable by deleting one
'5' digit from the decimal representation of N. It is guaranteed that N will
contain at least one '5' digit.

N consists of at least two digits in its decimal representation.
'''

def solution(N: int) -> int:
    maxVal = float('-inf')
    digits = str(N)
    for i in range(len(digits)):
        if digits[i] == '5':
            result = int(digits[0:i] + digits[i + 1:])
            maxVal = max(maxVal, result)
    return maxVal

if __name__=="__main__":
    print(solution(15958)) # 1958
    print(solution(-5859)) # -589
    print(solution(-5000)) # 0