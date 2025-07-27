# Clone graph
from collections import defaultdict, deque
from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def cloneGraphDfsRecursive(node: Optional['Node']) -> Optional['Node']:
    if not node: return node
    oldToNew = {}
    def dfs(curr: Node) -> Node:
        # base case
        if curr in oldToNew:
            return oldToNew[curr]
        # copy current node
        copied = Node(curr.val)
        oldToNew[curr] = copied
        # copy its all neighbors
        for neighbor in curr.neighbors:
            copied.neighbors.append(dfs(neighbor))
        return copied
    return dfs(node)


def cloneGraphDfsIterative(node: Optional['Node']) -> Optional['Node']:
    if not node: return node
    oldToNew = {node: Node(node.val)}
    stack = [node]
    while stack:
        curr = stack.pop()
        for neighbor in curr.neighbors:
            if neighbor not in oldToNew:
                oldToNew[neighbor] = Node(neighbor.val)
                stack.append(neighbor)
            oldToNew[curr].neighbors.append(oldToNew[neighbor])
    return oldToNew[node]

def cloneGraph(node: Optional['Node']) -> Optional['Node']:
    if not node: return node
    oldToNew = {node: Node(node.val)}
    queue = deque([node])
    while queue:
        curr = queue.popleft()
        for neighbor in curr.neighbors:
            if neighbor not in oldToNew:
                oldToNew[neighbor] = Node(neighbor.val)
                queue.append(neighbor)
            oldToNew[curr].neighbors.append(oldToNew[neighbor])
    return oldToNew[node]

'''
Following code is not correct
'''
# adjacent list
def cloneGraph2(node: Optional['Node']) -> Optional['Node']:
    if not node: return node
    adj = defaultdict(list)
    queue = deque([node])
    start = node.val
    visited = set()
    while queue:
        size = len(queue)
        for _ in range(size):
            curr = queue.popleft()
            visited.add(curr)
            for neighbor in curr.neighbors:
                if neighbor in visited:
                    continue
                adj[curr.val].append(neighbor.val)
                adj[neighbor.val].append(curr.val)
                queue.append(neighbor)
    head = Node(start)
    stack = [head]
    visited.clear()
    while stack:
        curr = stack.pop()
        visited.add(curr.val)
        for val in adj[curr.val]:
            newNode = Node(val)
            curr.neighbors.append(newNode)
            if val not in visited:
                stack.append(newNode)
    return head


# bfs
def cloneGraph1(node: Optional['Node']) -> Optional['Node']:
    if not node: return node
    queue = deque([node])
    dummy = Node(0)
    flag = True
    visited = set()
    while queue:
        size = len(queue)
        for _ in range(size):
            curr = queue.popleft()
            visited.add(curr.val)
            newNode = Node(curr.val)
            if flag:
                dummy.neighbors.append(newNode)
                flag = False
            for neighbor in curr.neighbors:
                if neighbor.val in visited:
                    continue
                newNeighbor = Node(neighbor.val)
                newNode.neighbors.append(newNeighbor)
            queue.extend(curr.neighbors)
    return dummy.neighbors[0]

        
if __name__=='__main__':
    leaves = []
    for num in [3,6,8,7,9]:
        leaves.append(Node(num))
    node2 = Node(2)
    for i in range(3):
        node2.neighbors.append(leaves[i])
    node4 = Node(4)
    for i in range(3,5):
        node4.neighbors.append(leaves[i])
    node1 = Node(1, [node2, node4])
    node2.neighbors.append(node1)
    node4.neighbors.append(node1)


    cloneGraph(node1)