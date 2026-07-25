def findRedundantConnection(edges: list[list[int]]) -> list[int]:
    # cycle detect function, n is the number of nodes
    def has_cycle(edges, n):
        graph = [[] for _ in range(n+1)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        seen = set()
        for start in range(1, n+1):
            if start in seen:
                continue
            stack = [(start, -1)]
            seen.add(start)
            while stack:
                node, parent = stack.pop()
                for neighbor in graph[node]:
                    if neighbor not in seen:
                        stack.append((neighbor, node))
                        seen.add(neighbor)
                    else:
                        if neighbor != parent:
                            return True
        return False                
        

    n = len(edges)
    for i in range(n-1, -1, -1):
        copied = edges.copy()
        copied.pop(i)
        if not has_cycle(copied, n):
            return edges[i]

'''
Solution given by AI
'''
def findRedundantConnection(edges: list[list[int]]) -> list[int]:
    n = len(edges)

    parent = list(range(n + 1))
    size = [1] * (n + 1)

    def find(node: int) -> int:
        while node != parent[node]:
            # Path compression
            parent[node] = parent[parent[node]]
            node = parent[node]

        return node

    def union(u: int, v: int) -> bool:
        root_u = find(u)
        root_v = find(v)

        if root_u == root_v:
            return False  # They are already connected

        # Union by size
        if size[root_u] < size[root_v]:
            root_u, root_v = root_v, root_u

        parent[root_v] = root_u
        size[root_u] += size[root_v]

        return True

    for u, v in edges:
        if not union(u, v):
            return [u, v]

    return []

'''
Someone's solution on Leetcode
'''
def findRedundantConnection2(edges: list[list[int]]) -> list[int]:
    parent = list(range(len(edges) + 1)) # each node is root of own subtree

    def find_parent(node):
        if parent[node] != node:
            parent[node] = find_parent(parent[node]) # set root for node as root of subtree
        return parent[node] # found root of subtree

    for node1, node2 in edges: 
        parent1, parent2 = find_parent(node1), find_parent(node2)

        if parent1 == parent2:
            return [node1, node2] # both nodes are already in same subtree

        parent[parent2] = parent1 # found new connection between nodes / subtrees
        # root[root1] = root2 also works            


def findRedundantConnection(edges: list[list[int]]) -> list[int]:
    pass

if __name__=="__main__":
    print(findRedundantConnection([[1,2],[2,3],[3,4],[1,4],[1,5]]))
