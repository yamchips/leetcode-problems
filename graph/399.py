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

# Test case
if __name__=='__main__':
    print(calcEquation([["a","b"],["c","d"]], [1.0, 1.0], [["a","c"],["b","d"],["b","a"],["d","c"]]))
    print(calcEquation([["x1","x2"],["x2","x3"],["x3","x4"],["x4","x5"]], [3.0,4.0,5.0,6.0], [["x1","x5"],["x5","x2"],["x2","x4"],["x2","x2"],["x2","x9"],["x9","x9"]]))
    print(calcEquation([["a","b"]], [0.5], [["a","b"],["b","a"],["a","c"],["x","y"]]))
    print(calcEquation([["a","b"],["b","c"],["bc","cd"]], [1.5,2.5,5.0], [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]))
    print(calcEquation([["a","b"],["b","c"]], [2.0,3.0],[["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]))