'''
Standard solution, use color array.

Time complexity: O(V+E)
    Each vertex is colored and added to the stack at most once. When we process
    a vertex, we check all of its neighbors, so every edge is examined at most 
    twice. 
Space complexity: O(V)
    The color array, the DFS stack can store up to V vertices.
'''
def isBipartite(graph: list[list[int]]) -> bool:
    color = [None] * len(graph)
    for start in range(len(graph)):
        if color[start] is not None:
            continue
        color[start] = True
        stack = [start]
        while stack:
            node = stack.pop()
            for neighbor in graph[node]:
                if color[neighbor] is None:
                    color[neighbor] = not color[node]
                    stack.append(neighbor)
                elif color[neighbor] == color[node]:
                    return False
    return True

'''
We don't need processed set, we can use color array.
'''
def isBipartite(graph: list[list[int]]) -> bool:
    processed = set()
    color = [None] * len(graph)
    for start in range(len(graph)):
        if start in processed:
            continue
        stack = [start]

        color[start] = True
    
        while stack:
            node = stack.pop()
            processed.add(node)
            for neighbor in graph[node]:
                if neighbor in processed:
                    continue
                if color[neighbor] is None:
                    color[neighbor] = not color[node]
                    stack.append(neighbor)
                else:
                    if color[neighbor] == color[node]:
                        return False
    return True

if __name__=="__main__":
    print(isBipartite([[1,2,3],[0,2],[0,1,3],[0,2]])) # False
    print(isBipartite([[1,3],[0,2],[1,3],[0,2]])) # True
    print(isBipartite([[],[2,4,6],[1,4,8,9],[7,8],[1,2,8,9],[6,9],[1,5,7,8,9],[3,6,9],[2,3,4,6,9],[2,4,5,6,7,8]]))