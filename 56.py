def merge(intervals: list[list[int]]) -> list[list[int]]:
    intervals.sort(key= lambda x : x[0])
    res = [intervals[0]]
    curr = res[-1]
    index = 1
    while index < len(intervals):
        if curr[1] >= intervals[index][0]:
            res[-1][1] = max(intervals[index][1], res[-1][-1])
            index += 1
        else:
            res.append(intervals[index])
            index += 1
            curr = res[-1]
    return res

if __name__=='__main__':
    print(merge([[1,3],[2,6],[8,10],[15,18]]))
    print(merge([[1,3],[3,6]]))
    print(merge([[1,3],[3,6],[6,6],[6,9]]))
    print(merge([[1,4],[2,3]]))
