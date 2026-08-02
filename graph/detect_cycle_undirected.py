'''
node: n nodes, from 0 to n - 1

We use (node, parent) to store nodes in stack
If a node's neighbor is in visited, and it's not parent, then we find a loop
'''
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

from collections import defaultdict
def has_cycle_undirected(n: int, edges: list[list]) -> bool:
    # build the graph
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    # use dfs to detect
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
                    stack.append((neighbor, node))
                    visited.add(neighbor)
                else:
                    if neighbor == parent:
                        continue
                    else:
                        return True
    return False

if __name__=="__main__":
    edges_0 = [[0,1],[0,2]] 
    edges_1 = [[0,1],[0,2],[1,2]] 
    edges_2 = [[0,1],[0,2],[1,3],[1,4],[2,4],[2,5]] 
    edges_3 = [[0,1],[0,2],[1,3],[1,4],[2,6],[2,5]] 
    print(has_cycle_undirected(3, edges_0)) # False
    print(has_cycle_undirected(3, edges_1)) # True
    print(has_cycle_undirected(6, edges_2)) # True
    print(has_cycle_undirected(7, edges_3)) # False

