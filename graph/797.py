

'''
Use (node, current_path) in stack
'''
def allPathsSourceTarget(graph: list[list[int]]) -> list[list[int]]:
    n = len(graph)

    stack = [(0, [0])] # (node, current_path)
    paths = []
    while stack:
        node, current_path = stack.pop()
        for neighbor in graph[node]:
            new_path = current_path.copy()
            new_path.append(neighbor)
            if neighbor != n - 1:
                stack.append((neighbor, new_path))
            else:
                paths.append(new_path)
    return paths

    

if __name__=="__main__":
    # [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]
    print(allPathsSourceTarget([[4,3,1],[3,2,4],[3],[4],[]]))

    # [[0,1,3],[0,2,3]]
    print(allPathsSourceTarget([[1,2],[3],[3],[]]))