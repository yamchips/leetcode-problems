import bisect

'''
Priority Queue solution

'''

'''
Optimal solution

Use an occurrence array for the trailing array.

O(1) space
O(n) time
'''
def findMid(arr, d): 
    total = 0
    if d % 2 == 1:
        m = d // 2 + 1
        for i in range(len(arr)):
            total += arr[i]
            if total >= m:
                return i
    else:
        m1, m2 = d // 2, d // 2 + 1
        a = b = 0
        for i in range(len(arr)):
            total += arr[i]
            if not a and total >= m1:
                a = i 
            if total >= m2:
                b = i
                return (a + b) / 2 

def activityNotifications(expenditure: list[int], d: int) -> int:
    n = len(expenditure)
    trailing = [0] * 201
    notification = 0
    for i in range(d):
        trailing[expenditure[i]] += 1
    for i in range(d, n):
        mid = findMid(trailing, d)
        if expenditure[i] >= 2 * mid:
            notification += 1
        trailing[expenditure[i - d]] -= 1
        trailing[expenditure[i]] += 1
    return notification


'''
Original solution

O(nd) time
O(d) space
'''

def binary_insert(prev: list[int], x: int) -> None:
    left, right = 0, len(prev) - 1
    while left <= right:
        mid = (left + right) // 2
        if prev[mid] > x:
            right = mid - 1
        else:
            left = mid + 1
    prev.insert(left, x)

def activityNotifications1(expenditure: list[int], d: int) -> int:
    n = len(expenditure)
    res = 0
    prev = expenditure[:d]
    prev.sort()
    for end in range(d, n):
        if d % 2 == 0:
            mid = (prev[d//2] + prev[d//2 - 1]) / 2
        else:
            mid = prev[d//2]
        if expenditure[end] >= 2 * mid:
            res += 1
        prev.remove(expenditure[end - d])
        binary_insert(prev, expenditure[end])    
    return res

if __name__=='__main__':
    activityNotifications([1,2,3,4,4],4)
    