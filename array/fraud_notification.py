# Hacker rank
import bisect
from collections import defaultdict
import heapq

'''
Priority Queue solution

'''
def activityNotifications3(expenditure: list[int], d: int) -> int:
    if len(expenditure) <= d or d == 0:
        return 0

    # small is a max-heap (store negatives), large is a min-heap
    small = []   # max-heap via negatives: contains the smaller half
    large = []   # min-heap: contains the larger half
    delayed = defaultdict(int)  # value -> count of lazy deletions

    smallSize = 0  # number of valid elements in small
    largeSize = 0  # number of valid elements in large

    def prune(heap, is_small):
        """Remove heap top elements that are marked for deletion."""
        while heap:
            val = -heap[0] if is_small else heap[0]
            if delayed[val] > 0:
                delayed[val] -= 1
                heapq.heappop(heap)
            else:
                break

    def rebalance():
        nonlocal smallSize, largeSize
        # Ensure small has either same size as large or one more element
        if smallSize > largeSize + 1:
            prune(small, True)
            v = -heapq.heappop(small)
            smallSize -= 1
            heapq.heappush(large, v)
            largeSize += 1
        elif largeSize > smallSize:
            prune(large, False)
            v = heapq.heappop(large)
            largeSize -= 1
            heapq.heappush(small, -v)
            smallSize += 1

    def add(num: int):
        nonlocal smallSize, largeSize
        # Before comparing with tops, prune to ensure tops are valid
        prune(small, True)
        prune(large, False)
        if not small or num <= -small[0]:
            heapq.heappush(small, -num)
            smallSize += 1
        else:
            heapq.heappush(large, num)
            largeSize += 1
        rebalance()

    def remove(num: int):
        nonlocal smallSize, largeSize
        # prune tops first so comparisons are correct
        prune(small, True)
        prune(large, False)
        # Decide which logical heap num belongs to and decrement that size
        if small and num <= -small[0]:
            smallSize -= 1
        else:
            largeSize -= 1
        # mark for lazy deletion
        delayed[num] += 1
        # actually remove from top if it sits at the top
        prune(small, True)
        prune(large, False)
        rebalance()

    def get_median() -> float:
        prune(small, True)
        prune(large, False)
        if d % 2 == 1:
            return float(-small[0])
        return (-small[0] + large[0]) / 2.0

    # Build initial window
    for x in expenditure[:d]:
        add(x)

    warns = 0
    for i in range(d, len(expenditure)):
        med = get_median()
        if expenditure[i] >= 2 * med:
            warns += 1
        # slide: remove outgoing, add incoming
        remove(expenditure[i - d])
        add(expenditure[i])

    return warns

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
Improved solution based on original solution 

Use binary search to delete, no TLE
'''
def activityNotifications2(expenditure: list[int], d: int) -> int:
    warns = 0

    trailing = sorted(expenditure[:d])

    for today in range(d, len(expenditure)):
        if d % 2 == 1:
            mid = trailing[d // 2]
        else:
            mid = (trailing[d // 2] + trailing[d // 2 - 1]) / 2
        if expenditure[d] > 2 * mid:
            warns += 1
        # update the window
        old_value = expenditure[today - d]
        del trailing[bisect.bisect_left(trailing, old_value)]
        index = bisect.bisect_left(trailing, expenditure[today])
        trailing.insert(index, expenditure[today])


'''
Original solution, TLE

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
    activityNotifications3([1,2,3,4,5],3)

    binary_insert([1,3,5,7], 6)
    # print(bisect.bisect_left([1,3,5,7], 6))
    print(bisect.bisect_right([1,3,5,7], 6))

    binary_insert([1,3,5,7], 4)
    # print(bisect.bisect_left([1,3,5,7], 4))
    print(bisect.bisect_right([1,3,5,7], 4))

    binary_insert([1,3,5,7], 2)
    # print(bisect.bisect_left([1,3,5,7], 2))
    print(bisect.bisect_right([1,3,5,7], 2))

    binary_insert([1,3,5,7], 3)
    # print(bisect.bisect_left([1,3,5,7], 3))
    print(bisect.bisect_right([1,3,5,7], 3))