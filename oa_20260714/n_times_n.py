'''
Given an array A consisting of N integers, return the biggest value X, which 
occurs in A exactly X times. If there is no such value, return 0.
'''

def solution(A: list) -> int:
    n = len(A)
    freq = {}
    for num in A:
        if num <= n:
            freq[num] = freq.get(num, 0) + 1
    result = 0
    for num, frequency in freq.items():
        if num == frequency:
            result = max(result, num)
    return result


if __name__=="__main__":
    print(solution([3,8,2,3,3,2])) # 3
    print(solution([7,1,8,2,2])) # 2
    print(solution([3,1,4,1,5])) # 0
    print(solution([5,5,5,5,5])) # 5

