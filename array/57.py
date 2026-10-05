def insert(intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
    result = []
    left_bound, right_bound = newInterval
    i = 0
    n = len(intervals)
    while i < n and intervals[i][1] < left_bound:
        result.append(intervals[i])
        i += 1

    while i < n and intervals[i][0] <= right_bound:
        left_bound = min(left_bound, intervals[i][0])
        right_bound = max(right_bound, intervals[i][1])
        i += 1

    result.append([left_bound, right_bound])
    
    while i < n:
        result.append(intervals[i])
        i += 1

    return result

if __name__=='__main__':
    print(insert([[1,2],[3,5],[6,7],[8,10],[12,16]],[4,15]))
    print(insert([[1,2],[3,5],[6,7],[8,10],[12,16]],[4,8]))

    print(insert([[1,3],[6,9]],[2,5]))
    print(insert([[1,5]],[6,8]))