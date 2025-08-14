# H-Index
def hIndex1(citations: list[int]) -> int:
    n = len(citations)
    arr = [0] * (n + 1)
    # arr[i]: number of papers whose citation is exact i
    # if citation is larger than n, then we consider it is n
    for citation in citations:
        arr[min(citation, n)] += 1
    res = 0
    for i in range(n, -1, -1):
        res += arr[i]
        if res >= i:
            return i
    

def hIndex(citations: list[int]) -> int:
    n = len(citations)
    arr = [0] * (n + 1)
    # arr[i]: number of papers whose citation is at least i
    for citation in citations:
        for i in range(min(n + 1, citation + 1)):
            arr[i] += 1
    res = 0
    for i in range(len(arr)):
        if arr[i] >= i:
            res = i
        else:
            return res
    return res



if __name__=='__main__':
    hIndex([3,0,6,1,5])