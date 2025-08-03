from collections import defaultdict, deque


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
    # detect whether there is a cycle, if yes, return false
    adj = defaultdict(list)
    for dest, src in prerequisites:
        adj[src].append(dest)
    # find whether there is a cycle
    visited = set()
    for num in range(numCourses):
        if num in visited:
            continue
        stack = [num]
        path = set()
        while stack:
            node = stack[-1]
            if node in visited:
                stack.pop()
                continue
            if node in path:
                return False  # cycle detected
            path.add(node)
            all_done = True
            for neighbor in adj[node]:
                if neighbor in path:
                    return False  # back edge → cycle
                if neighbor not in visited:
                    stack.append(neighbor)
                    all_done = False
            if all_done:
                visited.add(node)
                path.remove(node)
                stack.pop()
    return True

if __name__=='__main__':
    print(canFinish(5, [[1,4],[2,4],[3,1],[3,2]]))
    print(canFinish(2, [[1,0],[0,1]]))
    print(canFinish(2, [[1,0]]))
    