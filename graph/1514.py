import heapq

'''
time complexity:
    build graph O(E) because we use a default dict not a list of list
    build arrive time array O(V)
    Dijkstra:
        examine edges O(E) : for neighbor, time in graph[node]
        heap push O(E), heap pop O(E) times, each push or pop costs O(log E)
        for a graph, E <= V**2, so overall Dijkstra is O(E * logV)
    max scan: O(V)

    overall O(V + E * log V)

space complexity
    build graph O(V + E)
    build probs array O(V)
    heap O(V)
    overall O(V + E)
'''
def maxProbability(n: int, edges: list[list[int]], succProb: list[float], start_node: int, end_node: int) -> float:
    # build the graph
    graph = [[] for _ in range(n)]
    for (u, v), prob in zip(edges, succProb):
        graph[u].append((v, prob))
        graph[v].append((u, prob))
    # probs stores the possibility of arriving this node
    probs = [0] * n
    probs[start_node] = 1
    maxHeap = [(-1,start_node)] # weight, node
    while maxHeap:
        nodeProb, node = heapq.heappop(maxHeap)
        nodeProb = - nodeProb
        if nodeProb < probs[node]:
            continue
        if node == end_node:
            return nodeProb
        for neighbor, neighborProb in graph[node]:
            newProb = nodeProb * neighborProb
            if newProb > probs[neighbor]:
                probs[neighbor] = newProb
                heapq.heappush(maxHeap, (-newProb, neighbor))
    return probs[end_node] 

if __name__ == "__main__":
    print(maxProbability(3, [[0,1],[1,2],[0,2]], [0.5,0.5,0.2], 0, 2))