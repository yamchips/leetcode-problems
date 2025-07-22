import heapq


def getMinOperations(queryTimes:list) -> int:
    # initialize all even numbers in a heap
    maxHeap = [] # contain -query
    for query in queryTimes:
        if query % 2 == 0:
            heapq.heappush(maxHeap, -query)
    seen = set()
    operations = 0
    while maxHeap:
        query = - heapq.heappop(maxHeap)
        if query in seen:
            continue
        seen.add(query)
        next = query / 2
        operations += 1
        if next % 2 == 0:
            heapq.heappush(maxHeap, - next)
    return operations

if __name__=='__main__':
    print(getMinOperations([3, 24])) # expected 3
    print(getMinOperations([1, 9, 5])) # expected 0
    print(getMinOperations([2, 6, 8, 16])) # expected 5