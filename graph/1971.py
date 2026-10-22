# find if path exists in graph

from collections import defaultdict
from typing import List


def validPath(n: int, edges: List[List[int]], source: int, destination: int) -> bool:
    if source == destination:
        return True
    # build adjacency list
    adj = [[] for _ in range(n)]            
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    stack = [source]
    seen = set([source])
    while stack:
        node = stack.pop()
        for neighbor in adj[node]:
            if neighbor not in seen:
                if neighbor == destination: return True
                seen.add(neighbor)
                stack.append(neighbor)
    return False

if __name__=="__main__":
    print(validPath(6, [[0,1],[0,2],[3,5],[5,4],[4,3]], 0, 5)) # False
    print(validPath(3, [[0,1],[1,2],[2,0]], 0, 2)) # true
