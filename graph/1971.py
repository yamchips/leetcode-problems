# find if path exists in graph

from collections import defaultdict
from typing import List


def validPath(n: int, edges: List[List[int]], source: int, destination: int) -> bool:
    # build the adjacent list
    adj_list = defaultdict(list)
    for edge in edges:
        u, v = edge
        adj_list[u].append(v)
        adj_list[v].append(u)
    # start from source, find destination
    if source == destination: return True
    stack = [source]
    seen = set([source])
    while stack:
        node = stack.pop()
        if node == destination: return True
        for neighbor in adj_list[node]:
            if neighbor == destination: return True
            if neighbor not in seen:
                seen.add(neighbor)
                stack.append(neighbor)           
    return False

if __name__=="__main__":
    print(validPath(6, [[0,1],[0,2],[3,5],[5,4],[4,3]], 0, 5)) # False
    print(validPath(3, [[0,1],[1,2],[2,0]], 0, 2)) # true
