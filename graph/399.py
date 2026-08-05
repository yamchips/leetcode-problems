from collections import defaultdict, deque

# recursive dfs
def calcEquationDFS(equations: list[list[str]], values: list[float], queries: list[list[str]]) -> list[float]:
    adj = defaultdict(list)
    for equation, value in zip(equations, values):
        adj[equation[0]].append((equation[1], value))
        adj[equation[1]].append((equation[0], 1 / value))

    def dfs(curr, end, prod, visited):
        if curr == end:
            return prod
        visited.add(curr)
        for neighbor, value in adj[curr]:
            if neighbor not in visited:
                result = dfs(neighbor, end, prod * value, visited)
                if result != -1.0:
                    return result
        return -1.0

    res = []
    for start, end in queries:
        if start not in adj or end not in adj:
            res.append(-1.0)
        elif start == end:
            res.append(1.0)
        else:
            visited = set()
            res.append(dfs(start, end, 1.0, visited))
    return res

# bfs
def calcEquation(equations: list[list[str]], values: list[float], queries: list[list[str]]) -> list[float]:
    adj = defaultdict(list)
    for equation, value in zip(equations, values):
        adj[equation[0]].append((equation[1], value))
        adj[equation[1]].append((equation[0], 1 / value))
    res = []
    for query in queries:
        start, end = query
        if start not in adj or end not in adj:
            res.append(-1.0)
            continue
        if start == end:
            res.append(1.0)
            continue

        queue = deque(adj[start])
        visited = set()
        reachEnd = False
        while queue:
            node, prod = queue.popleft()
            if node == end:
                res.append(prod)
                reachEnd = True
                break
            visited.add(node)
            for neighbor, value in adj[node]:
                if neighbor not in visited:
                    queue.append((neighbor, prod * value))
        if not reachEnd:
            res.append(-1.0)
    return res

'''
time complexity:
    build graph O(E)
    iterate K queries, in each query, O(V + E)
    overall, O(K(V + E))

space complexity:
    build graph O(V + E)
    in one query DFS uses O(V)
    result array O(K)
    overall O(K + V + E)
'''
def calcEquation(equations: list[list[str]], values: list[float], queries: list[list[str]]) -> list[float]:
    # build the graph
    graph = defaultdict(list)
    for (u, v), value in zip(equations, values):
        graph[u].append((v, value))
        graph[v].append((u, 1 / value))

    result = []
    for start, end in queries:
        # check whether the queries are valid: both nodes in graph
        if start not in graph or end not in graph :
            result.append(-1.0)
            continue
        if start == end:
            result.append(1.0)
            continue
        # if valid, find the path from A to B and calculate the value
        stack = [(start, 1.0)]
        seen = {start}
        found_end = False
        while stack:
            node, node_value = stack.pop()
            for neighbor, neighbor_value in graph[node]:
                if neighbor in seen:
                    continue
                if neighbor == end:
                    # found the end
                    result.append(node_value * neighbor_value)
                    found_end = True
                    break
                stack.append((neighbor, node_value * neighbor_value))
                seen.add(neighbor)
            if found_end:
                break
        if not found_end:
            result.append(-1.0)

    return result

# Test case
if __name__=='__main__':
    print(calcEquation([["a","b"],["c","d"]], [1.0, 1.0], [["a","c"],["b","d"],["b","a"],["d","c"]]))
    print(calcEquation([["x1","x2"],["x2","x3"],["x3","x4"],["x4","x5"]], [3.0,4.0,5.0,6.0], [["x1","x5"],["x5","x2"],["x2","x4"],["x2","x2"],["x2","x9"],["x9","x9"]]))
    print(calcEquation([["a","b"]], [0.5], [["a","b"],["b","a"],["a","c"],["x","y"]]))
    print(calcEquation([["a","b"],["b","c"],["bc","cd"]], [1.5,2.5,5.0], [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]))
    print(calcEquation([["a","b"],["b","c"]], [2.0,3.0],[["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]))