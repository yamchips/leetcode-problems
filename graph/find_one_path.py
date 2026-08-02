from collections import defaultdict
'''
If our input guarantees that there is only 1 node that has no children and only 
one node that has no parent, which means the graph has one start and one end. 
And there is no loop, means we can definitely move from start to end.

We are given the number of nodes and the edges. Return one path from start node 
to end node. 
'''
def find_one_path(n: int, edges:list[list]):
    # build the graph, key: end, value: start
    # build the indegree and outdegree array to find start and end
    indegree = [0] * n
    outdegree = [0] * n
    reverse_graph = defaultdict(list)
    for start, end in edges:
        reverse_graph[end].append(start)
        indegree[end] += 1
        outdegree[start] += 1
    # start node: indegree is 0; end node: outdegree is 0
    start_node = -1
    end_node = -1
    for i in range(n):
        if indegree[i] == 0:
            start_node = i
        if outdegree[i] == 0:
            end_node = i
    # build the path from end to start
    path = [end_node]
    while path[-1] != start_node:
        path.append(reverse_graph[path[-1]][0])
    path.reverse()
    return path
    
if __name__=="__main__":
    edges_5 = [[0,1],[0,2],[1,3],[1,4],[3,5],[4,5],[2,6],[6,5]]
    print("start to end path is: ", find_one_path(7, edges_5))
