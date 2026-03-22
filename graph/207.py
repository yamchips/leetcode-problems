from collections import defaultdict, deque

# Kahn's algorithm
def canFinish(numCourses: int, prerequisites: list[list[int]]) -> bool:
    adj = defaultdict(list)
    indegree = [0] * numCourses

    # Build the graph and indegree array
    for dest, src in prerequisites:
        adj[src].append(dest)
        indegree[dest] += 1

    # Initialize queue with courses having no prerequisites
    queue = deque([i for i in range(numCourses) if indegree[i] == 0])
    completed = 0

    while queue:
        course = queue.popleft()
        completed += 1
        for neighbor in adj[course]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    # If we could process all courses, no cycle exists
    return completed == numCourses


def canFinishIterative(numCourses: int, prerequisites: list[list[int]]) -> bool:
    adj = defaultdict(list)
    for dest, src in prerequisites:
        adj[src].append(dest)

    visited = set()     # permanently visited (no cycle)
    visiting = set()    # nodes in current DFS path

    for course in range(numCourses):
        if course in visited:
            continue

        stack = [(course, False)]  # (node, expanded_flag)

        while stack:
            node, expanded = stack.pop()

            if expanded:
                visiting.remove(node)
                visited.add(node)
                continue

            if node in visited:
                continue

            if node in visiting:
                return False  # cycle detected

            visiting.add(node)
            stack.append((node, True))  # post-order mark

            for neighbor in adj[node]:
                stack.append((neighbor, False))

    return True

def canFinish(numCourses: int, prerequisites: list[list[int]]) -> bool:
    # build the adjacent list
    graph = defaultdict(list)
    for dest, src in prerequisites:
        graph[src].append(dest)
    # set state array
    # 0=unvisited, 1=visiting, 2=visited
    state = [0] * numCourses
    # define dfs function
    # return True means there is no cycle
    # return False means there is a cycle
    def dfs(node):
        if state[node] == 1:
            return False # cycle
        if state[node] == 2:
            return True
        state[node] = 1
        for neighbor in graph[node]:
            if not dfs(neighbor):
                return False
        state[node] = 2
        return True
    
    for i in range(numCourses):
        if not dfs(i):
            return False
    
    return True

if __name__=='__main__':
    print(canFinish(5, [[1,4],[2,4],[3,1],[3,2]]))
    print(canFinish(4, [[3,1],[2,3],[1,2]]))
    print(canFinish(2, [[1,0],[0,1]]))
    print(canFinish(2, [[1,0]]))
    