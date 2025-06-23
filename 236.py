# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def lowestCommonAncestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    dict = {} # child: parent
    # BFS, traverse the tree 
    queue = deque([root])
    while queue:
        size = len(queue)
        for _ in range(size):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
                dict[node.left] = node
            if node.right:
                queue.append(node.right)
                dict[node.right] = node
    # dict contains all child-parent pair
    # find all parents of node p
    pParent = {p}
    while p.val != root.val:
        parent = dict[p]
        pParent.add(parent)
        p = parent
    while q.val != root.val:
        if q in pParent:
            break
        q = dict[q]
    return q

def lowestCommonAncestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    if root is None or root == p or root == q:
        return root
    left = lowestCommonAncestor(root.left, p, q)
    right = lowestCommonAncestor(root.right, p, q)
    if left and right:
        return root
    elif left:
        return left
    else:
        return right