from collections import defaultdict, deque

'''
Kahan's algorithm
'''
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

def findOrder(numCourses: int, prerequisites: list[list[int]]) -> list[int]:
    # build graph
    graph = [[] for _ in range(numCourses)]
    for end, start in prerequisites:
        graph[start].append(end)

    processed = set() # all processed nodes
    visiting = set() # current DFS path nodes
    path = []
    # iterate all courses
    for start in range(numCourses):
        if start in processed:
            continue

        stack = [(start, False)] # False means entering this node, True means exiting this node, and all its descendants are processed

        while stack:
            node, exiting = stack.pop()

            if exiting:
                processed.add(node)
                path.append(node)
                visiting.remove(node)
                continue

            if node in processed:
                continue

            stack.append((node, True))
            visiting.add(node)

            for neighbor in graph[node]:
                if neighbor in visiting:
                    return [] # cycle detected
                elif neighbor in processed:
                    continue
                else:
                    stack.append((neighbor, False))
    return path[::-1]

if __name__=="__main__":
    pass

