from collections import defaultdict, deque


def findOrder(numCourses: int, prerequisites: list[list[int]]) -> list[int]:
    # use adjacent list and indegree array
    adj = defaultdict(list)
    indegree = [0] * numCourses
    # populate them
    for src, pre in prerequisites:
        adj[pre].append(src)
        indegree[src] += 1

    # initialize queue with nodes having 0 indegree
    queue = deque([node for node in range(numCourses) if indegree[node] == 0])
    completed = 0
    path = []
    while queue:
        course = queue.popleft()
        completed += 1
        path.append(course)
        for neighbor in adj[course]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    return path if completed == numCourses else []
