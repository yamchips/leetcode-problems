def merge(intervals: list[list[int]]) -> list[list[int]]:
    result = []
    sorted_intervals = sorted(intervals, key=lambda x:x[0])
    for interval in sorted_intervals:            
        if result and interval[0] <= result[-1][1]:
            result[-1] = [result[-1][0], max(result[-1][1], interval[1])]
        else:
            result.append(interval)
    return result

if __name__=='__main__':
    print(merge([[1,3],[2,6],[8,10],[15,18]]))
    print(merge([[1,3],[3,6]]))
    print(merge([[1,3],[3,6],[6,6],[6,9]]))
    print(merge([[1,4],[2,3]]))
