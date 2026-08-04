def possibleBipartition(n: int, dislikes: list[list[int]]) -> bool:
    graph = [[] for _ in range(n)]
    for u, v in dislikes:
        graph[u-1].append(v)
        graph[v-1].append(u)

    colors = [None] * n
    for start in range(1, n+1):
        if colors[start - 1] is not None:
            continue
        stack = [start]
        while stack:
            node = stack.pop()
            for neighbor in graph[node - 1] :
                if colors[neighbor - 1] is None:
                    stack.append(neighbor)
                    colors[neighbor - 1] = not colors[node - 1]
                else:
                    if colors[neighbor - 1] == colors[node - 1]:
                        return False
    return True


if __name__=="__main__":
    print(possibleBipartition(4,[[1,2],[1,3],[2,4]])) # True
    print(possibleBipartition(3,[[1,2],[1,3],[2,3]])) # False