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
        # True: exiting after processing all descendants
        stack = [(start, False)]
        while stack:
            node, exiting = stack.pop()

            if exiting:
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
    

if __name__=="__main__":
    print(has_cycle_undirected(3, [[0,1],[0,2],[1,2]])) #