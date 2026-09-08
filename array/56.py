def merge(intervals: list[list[int]]) -> list[list[int]]:
    intervals.sort()
    result = [intervals[0]]
    for start, end in intervals[1:]:
        if result[-1][1] >= start:
            result[-1][1] = max(result[-1][1], end)
        else:
            result.append([start, end])
    return result

if __name__=='__main__':
    print(merge([[1,3],[2,6],[8,10],[15,18]]))
    print(merge([[1,3],[3,6]]))
    print(merge([[1,3],[3,6],[6,6],[6,9]]))
    print(merge([[1,4],[2,3]]))
