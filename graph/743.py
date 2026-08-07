from collections import defaultdict
import heapq
'''
Dijkstra algorithm

time complexity:
    build graph O(E) because we use a default dict not a list of list
    build arrive time array O(V)
    iterate all vertices and edges O(V + E), heap insertion and removal O(log V)
    overall O((V + E) * log V)
    assume the graph is connected, E >= V - 1, so V + E = O(E), then it's O(ElogV)
    for disconnected graph, we still use O((V + E) * log V)

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

if __name__=="__main__":
    print(networkDelayTime([[1,2,1],[2,1,3]],2, 2)) # 3
    print(networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2)) # 2
    print(networkDelayTime([[2,1,1],[2,3,2],[3,4,3],[3,5,1],[5,4,1]], 5, 2)) # 4