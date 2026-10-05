def eraseOverlapIntervals(intervals: list[list[int]]) -> int:
    intervals.sort(key=lambda x:x[1])
    last_end = intervals[0][1]
    count = 0
    for i in range(1, len(intervals)):
        if last_end<=intervals[i][0]:
            last_end = intervals[i][1]
        else:
            count += 1
    return count
