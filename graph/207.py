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

def canFinish(numCourses: int, prerequisites: list[list[int]]) -> bool:
    graph = [[] for _ in range(numCourses)]
    for end, start in prerequisites:
        graph[start].append(end)

    # the node in it and everything reachable have been fully checked and are cycle-free
    processed = set() 
    visiting = set() # current path
    for start in range(numCourses):
        if start in processed:
            continue

        stack = [(start, False)]

        while stack:
            node, exiting = stack.pop()

            if exiting:
                visiting.remove(node)
                processed.add(node)
                continue

            if node in processed:
                continue

            visiting.add(node)
            stack.append((node, True))

            for neighbor in graph[node]:
                if neighbor in visiting:
                    return False
                if neighbor not in processed:
                    stack.append((neighbor, False))

    return True

def canFinishRecursive(numCourses: int, prerequisites: list[list[int]]) -> bool:
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
    print(canFinish(7,[[1,0],[2,0],[3,1],[3,2],[5,4],[6,5],[4,6]]))

    print(canFinishKahn(3, [[1,0],[1,2],[0,1]])) # False
    print(canFinishKahn(3, [[1,0],[1,2]])) # True
    print(canFinishKahn(4, [[1,0],[2,0],[3,1],[3,2]])) # True
    print(canFinishKahn(6, [[1,0],[2,0],[3,1],[3,2],[5,4]])) # True
    print(canFinishKahn(6, [[1,0],[2,0],[3,1],[3,2],[0,3],[5,4]])) # False
    print(canFinish(5, [[1,4],[2,4],[3,1],[3,2]])) # True
    print(canFinish(4, [[3,1],[2,3],[1,2]])) # False
    print(canFinish(2, [[1,0],[0,1]])) # False
    print(canFinish(2, [[1,0]])) # True
    