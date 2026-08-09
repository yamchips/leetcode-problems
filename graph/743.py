from collections import defaultdict
import heapq
'''
Dijkstra algorithm

time complexity:
    build graph O(E) because we use a default dict not a list of list
    build arrive time array O(V)
    Dijkstra:
        examine edges O(E) : for neighbor, time in graph[node]
        heap push O(E), heap pop O(E) times, each push or pop costs O(log E)
        for a graph, E <= V**2, so overall Dijkstra is O(E * logV)
    max scan: O(V)

    overall O(V + E * log V)
    
    assume all V nodes are reachable from k, E >= V - 1, so it's O(E * logV)
    for disconnected graph, some nodes are not reachable,
    we still use O(V + E * log V)

space complexity:
    build graph O(V + E)
    build arrive time array O(V)
    build the heap O(E)
    overall O(V + E)
'''
def networkDelayTime(times: list[list[int]], n: int, k: int) -> int:
    # build the graph
    graph = defaultdict(list)
    for start, end, time in times:
        graph[start].append((end, time))

    # start from k, traverse the graph
    arriveTime = [float('inf')] * (n + 1)
    arriveTime[k] = 0

    minHeap = [(0, k)] # (arriveTime from k, node)

    while minHeap:
        currentTime, node = heapq.heappop(minHeap)
        if currentTime > arriveTime[node]:
            continue
        for neighbor, time in graph[node]:
            newTime = currentTime + time
            if newTime < arriveTime[neighbor]:
                arriveTime[neighbor] = newTime
                heapq.heappush(minHeap, (newTime, neighbor))

    answer = max(arriveTime[1:])
    return answer if answer != float('inf') else -1

def networkDelayTime(times: list[list[int]], n: int, k: int) -> int:
    # build the graph
    graph = defaultdict(list)
    for u, v, weight in times:
        graph[u].append((v, weight))

    # arriveTime stores min time arriving the node
    arriveTime = [float('inf')] * (n + 1)
    arriveTime[k] = 0
    minHeap = [(0, k)] # (min time to node k, node k)

    while minHeap:
        timeToNode, node = heapq.heappop(minHeap)
        # if node was reached before and previous reach time is shorter, we
        # don't update the node
        if timeToNode > arriveTime[node]:
            continue

        for neighbor, timeToNeighbor in graph[node]:
            newTime = timeToNode + timeToNeighbor
            # if current path leads to a shorter arrive time to neighbor node
            # update the neighbor's arrive time and the heap
            if newTime < arriveTime[neighbor]:
                arriveTime[neighbor] = newTime
                heapq.heappush(minHeap, (newTime, neighbor))

    result = max(arriveTime[1:])
    return result if result != float('inf') else -1

if __name__=="__main__":
    print(networkDelayTime([[1,2,3],[1,3,1],[2,3,1],[3,2,1],[2,4,2],[3,5,1],[3,4,2],[2,5,1],[5,4,2],[4,6,3],[5,6,2]], 6, 1)) 
    print(networkDelayTime([[1,2,1],[2,1,3]],2, 2)) # 3
    print(networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2)) # 2
    print(networkDelayTime([[2,1,1],[2,3,2],[3,4,3],[3,5,1],[5,4,1]], 5, 2)) # 4