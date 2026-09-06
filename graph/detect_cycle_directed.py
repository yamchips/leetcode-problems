from collections import defaultdict
'''
We have n nodes from 0 to n-1

Use a state array, 0 means unvisited, 1 means visiting, 2 means this node and all its children are processed

Store (node, bool) in stack, True means exiting this node and its children are processed, False means entering the node

Time complexity: O(V + E)
    Let V be the number of vertices and E the number of edges. 
    Building the adjacency list takes O(V + E). During DFS, each course is fully processed at most once, and when we process a course, we scan its outgoing edges. Across the whole graph, each directed edge is examined once, so the DFS is O(V + E).
    There can be some stale duplicate stack entries in this iterative implementation, but each of those entries is created while examining an edge, so they do not change the asymptotic complexity.

Space complexity: O(V + E)
    The adjacency list uses O(V + E), the state array uses O(V), and the stack may contain O(V + E) entries in the worst case because the same unprocessed node can be pushed by multiple parents.
'''
def has_cycle_directed(n, edges):
    graph = [[] for _ in range(n)]
    for start, end in edges:
        graph[start].append(end)

    state = [0] * n

    for start in range(n):
        if state[start] == 2:
            continue
        
        stack = [(start, False)]
        while stack:
            node, processed = stack.pop()

            if processed:
                state[node] = 2
                continue
            if state[node] == 1:
                return True
            if state[node] == 2:
                continue
            state[node] = 1
            stack.append((node, True))
            for neighbor in graph[node]:
                if state[neighbor] == 1:
                    return True # cycle found
                elif state[neighbor] == 2:
                    continue
                else:
                    stack.append((neighbor, False))
    return False
   


'''
Use two sets: processed_set and visiting. 
Processed_set means the nodes inside and its children are processed. 
Visiting means the nodes inside is currently processing.

Time complexity: O(V + E)
    Building the adjacency list takes O(V + E). Each node is fully processed at most once, and each outgoing edge is examined when its source node is expanded. Duplicate pending stack entries are bounded by the number of edges, so the total time is O(V + E).

Space complexity: O(V + E)
    The adjacency list uses O(V + E). The processed_set and visiting sets use O(V), while the stack may use O(V + E) space because a node can be pushed through multiple incoming edges before it is processed.
'''
def has_cycle_directed(n, edges):
    # build adjacent list
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
    # processed: node and its children are processed
    processed_set = set()
    for node in range(n):
        if node in processed_set:
            continue

        # False means the node is not processed
        # True means its children are processed
        stack = [(node, False)]
        visiting = set()
        while stack:
            curr, processed = stack.pop()

            if processed:
                processed_set.add(curr)
                visiting.remove(curr)
                continue

            if curr in processed_set:
                continue
            
            stack.append((curr, True))
            visiting.add(curr)

            for neighbor in graph[curr]:
                if neighbor in visiting:
                    return True
                elif neighbor in processed_set:
                    continue
                else:
                    stack.append((neighbor, False))

    return False

'''
Detect a loop in a directed graph
If there exists one, return it in any order
0 -> 1 -> 3 -> 6 -> 1
return [1,3,6] or [3,6,1] or [6,1,3]

If no loop, return an empty array

Time complexity: O(V + E)
    Building the adjacency list takes O(V + E). The DFS processes each node and examines each edge at most a constant number of times. Reconstructing the detected loop follows at most V parent pointers, so the total time remains O(V + E).

Space complexity: O(V + E)
    The adjacency list uses O(V + E). The visited and visiting sets, parent dictionary, and returned loop use O(V). The stack may use O(V + E) space because duplicate pending entries can be created by multiple incoming edges.
'''
def get_loop(n: int, edges:list[list]) -> list:
    # build the graph
    graph = defaultdict(list)
    for start, end in edges:
        graph[start].append(end)

    def get_loop_elements(start: int, end: int):
        loop = [end]
        while loop[-1] != start:
            loop.append(parent[loop[-1]])
        loop.reverse()
        return loop

    visited = set()
    parent = {} # key: node, value: node's parent
    for start in range(n):
        if start in visited:
            continue
        stack = [(start, False)]
        visiting = set()
        while stack:
            node, processed = stack.pop()
            if processed:
                visited.add(node)
                visiting.remove(node)
                continue
            if node in visited:
                continue
            stack.append((node, True))
            visiting.add(node)
            for neighbor in graph[node]:
                if neighbor in visiting:
                    return get_loop_elements(neighbor, node)
                elif neighbor in visited:
                    continue
                else:
                    stack.append((neighbor, False))  
                    parent[neighbor] = node
    return []


if __name__=="__main__":
    edges_0 = [[0,1],[0,2]]
    edges_1 = [[1,2],[1,3],[2,4],[2,5],[3,6],[3,5]]
    edges_2 = [[1,2],[1,3],[2,4],[2,5],[3,6],[3,5],[6,1]]
    print(has_cycle_directed(3, edges_0)) # False
    print(has_cycle_directed(7, edges_1)) # False
    print(has_cycle_directed(7, edges_2)) # True

    edges_3 = [[0,1],[1,2],[1,3],[2,4],[2,5],[3,6],[3,5],[6,1]]
    edges_4 = [[0,1],[1,2],[1,3],[2,4],[2,5],[3,6],[3,5],[5,1]]
    print(get_loop(7, edges_3)) # [1,3,6]
    print(get_loop(7, edges_4)) # [1,3,6]

