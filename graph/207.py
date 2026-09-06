from collections import defaultdict, deque

'''
Kahn's algorithm
Indegree array
'''
def canFinishKahn(numCourses: int, prerequisites: list[list[int]]) -> bool:
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

'''
Use two sets: visited and visiting + a boolean flag to check whether we are exiting this node
'''
def canFinish(numCourses: int, prerequisites: list[list[int]]) -> bool:
    adj = defaultdict(list)
    for dest, src in prerequisites:
        adj[src].append(dest)

    visited = set()     # permanently visited (no cycle)
    visiting = set()    # nodes in current DFS path

    for course in range(numCourses):
        if course in visited:
            continue

        stack = [(course, False)]  # (node, exiting_flag)

        while stack:
            node, exiting = stack.pop()

            if exiting:
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

'''
Use a state array to record states. 0 means unvisited, 1 means visiting, 2 means
this node and its children are processed.

Use (node, bool) in stack. False means entering the node, True means this node
and its children are processed and we leave this node.
'''
def canFinish(numCourses: int, prerequisites: list[list[int]]) -> bool:
    # build the graph
    graph = [[] for _ in range(numCourses)]
    for end, start in prerequisites:
        graph[start].append(end)
    
    # build the state array
    state = [0] * numCourses

    # iterate the graph
    for course in range(numCourses):
        if state[course] == 2:
            continue

        stack = [(course, False)] 

        while stack:
            node, processed = stack.pop()

            # exit node
            if processed:
                state[node] = 2
                continue
            # stale entry
            if state[node] == 2:
                continue

            state[node] = 1
            stack.append((node, True))

            for neighbor in graph[node]:
                if state[neighbor] == 1:
                    return False # loop
                elif state[neighbor] == 2:
                    continue
                else:
                    stack.append((neighbor, False))
    return True


if __name__=='__main__':
    print(canFinish(7,[[1,0],[2,0],[3,1],[3,2],[5,4],[6,5],[4,6]])) # False
    print(canFinishKahn(3, [[1,0],[1,2],[0,1]])) # False
    print(canFinishKahn(3, [[1,0],[1,2]])) # True
    print(canFinishKahn(4, [[1,0],[2,0],[3,1],[3,2]])) # True
    print(canFinishKahn(6, [[1,0],[2,0],[3,1],[3,2],[5,4]])) # True
    print(canFinishKahn(6, [[1,0],[2,0],[3,1],[3,2],[0,3],[5,4]])) # False
    print(canFinish(5, [[1,4],[2,4],[3,1],[3,2]])) # True
    print(canFinish(4, [[3,1],[2,3],[1,2]])) # False
    print(canFinish(2, [[1,0],[0,1]])) # False
    print(canFinish(2, [[1,0]])) # True
    