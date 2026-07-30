from collections import defaultdict
def has_cycle_undirected(n, edges) -> bool:
    graph = [[] for _ in range(n)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    visited = set()
    for start in range(n):
        if start in visited:
            continue
        stack = [(start, -1)]
        visited.add(start)
        while stack:
            node, parent = stack.pop()
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.append([neighbor, node])
                elif neighbor != parent:
                    return True
    return False

def has_cycle_directed(n, edges):
    graph = [[] for _ in range(n)]
    for start, end in edges:
        graph[start].append(end)

    # 0: unvisited
    # 1: visiting
    # 2: processed, this node and all its descendants are processed
    state = [0] * n

    for start in range(n):
        if state[start] == 2:
            continue
        # False: entering the node
        # True: processed this node and all descendants
        stack = [(start, False)]
        while stack:
            node, processed = stack.pop()

            if processed:
                state[node] = 2
                continue
            if state[node] == 1:
                return True
            if state[node] == 2:
                continue
            state[node] = 1
            stack.append((node, True))
            for neighbor in graph[node]:
                if state[neighbor] == 1:
                    return True # cycle found
                elif state[neighbor] == 2:
                    continue
                else:
                    stack.append((neighbor, False))
    return False
   
# check whether a directed graph has cycle
def solution(n, edges):
    # build adjacent list
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
    # iterate each node
    # 0 means initial state
    # 1 means visiting
    # 2 means this node and its children are processed
    state = [0] * n
    for node in range(n):
        if state[node] == 2:
            continue
        # False means this node is not processed
        # True means this node and its children are processed
        stack = [(node, False)] 
        while stack:
            curr, processed = stack.pop()

            if processed:
                state[curr] = 2
                continue
            if state[curr] == 2:
                continue

            stack.append((curr, True))
            state[curr] = 1
            for neighbor in graph[curr]:
                if state[neighbor] == 1:
                    return True
                elif state[neighbor] == 2:
                    continue
                else:
                    stack.append((neighbor, False))
                    
    return False
  
def solution(n, edges):
    # build adjacent list
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
    # processed: node and its children are processed
    processed_set = set()
    for node in range(n):
        if node in processed_set:
            continue

        # False means the node is not processed
        # True means the node and its children are processed
        stack = [(node, False)]
        visiting = set()
        while stack:
            curr, processed = stack.pop()

            if processed:
                processed_set.add(curr)
                visiting.remove(curr)
                continue

            if curr in processed:
                continue
            
            stack.append((curr, True))
            visiting.add(curr)

            for neighbor in graph[curr]:
                if neighbor in visiting:
                    return True
                elif neighbor in processed_set:
                    continue
                else:
                    stack.append((neighbor, False))

    return False




if __name__=="__main__":
    edges_0 = [[0,1],[0,2]]
    edges_1 = [[1,2],[1,3],[2,4],[2,5],[3,6],[3,5]]
    edges_2 = [[1,2],[1,3],[2,4],[2,5],[3,6],[3,5],[6,1]]
    print(solution(3, edges_0)) # False
    print(solution(7, edges_1)) # False
    print(solution(7, edges_2)) # True