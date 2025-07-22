# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

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
    
if __name__=='__main__':
    node_6 = TreeNode(6)
    node_4 = TreeNode(4)
    node_2 = TreeNode(2, TreeNode(7), node_4)
    node_5 = TreeNode(5, node_6, node_2)
    node_1 = TreeNode(1, TreeNode(0), TreeNode(8))
    root = TreeNode(3, node_5, node_1)
    print(lowestCommonAncestor(root, node_6, node_4).val)