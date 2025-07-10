def insert1(intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
    n = len(intervals)
    if n == 0: return [newInterval]
    res = []
    i = 0
    while i < n and intervals[i][1] < newInterval[0]:
        res.append(intervals[i])
        i += 1
    
    start = 0
    if i < n and intervals[i][0] <= newInterval[0] <= intervals[i][1]:
        start = intervals[i][0]
    else:
        start = newInterval[0]

    end = newInterval[1]
    while i < n and newInterval[1] >= intervals[i][0]:
        end = max(intervals[i][1], newInterval[1])
        i += 1

    res.append([start, end])

    while i < len(intervals):
        res.append(intervals[i])
        i += 1

    return res

def insert(intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
    n = len(intervals)
    startIndex = findPosition(intervals, newInterval[0], True)
    endIndex = findPosition(intervals, newInterval[1], False)
    

    
    return intervals

def findPosition(intervals, target, start):
    left, right = 0, len(intervals)
    while left < right:
        mid = (left + right) // 2
        val = intervals[mid][0] if start else intervals[mid][1]
        if (start and val < target) or (not start and val <= target):
            left = mid + 1
        else:
            right = mid
    return left


# when finding insertion position, only find according to start, and then merge
# when traversing the array, don't have to use binary search to find end's position
def insertSolution(intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
     # If the intervals vector is empty, return a vector containing the newInterval
    if not intervals:
        return [newInterval]

    n = len(intervals)
    target = newInterval[0]
    left, right = 0, n - 1

    # Binary search to find the position to insert newInterval
    while left <= right:
        mid = (left + right) // 2
        if intervals[mid][0] < target:
            left = mid + 1
        else:
            right = mid - 1

    # Insert newInterval at the found position
    intervals.insert(left, newInterval)

    # Merge overlapping intervals
    res = []
    for interval in intervals:
        # If res is empty or there is no overlap, add the interval to the result
        if not res or res[-1][1] < interval[0]:
            res.append(interval)
        # If there is an overlap, merge the intervals by updating the end of the last interval in res
        else:
            res[-1][1] = max(res[-1][1], interval[1])
    return res

if __name__=='__main__':
    print(insertSolution([[1,2],[3,5],[6,7],[8,10],[12,16]],[4,15]))
    print(insertSolution([[1,3],[6,9]],[2,5]))
    print(insertSolution([[1,5]],[6,8]))