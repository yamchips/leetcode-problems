# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def smallestFromLeaf(root: Optional[TreeNode]) -> str:
    def compare(path1, path2) -> list:
        for a, b in zip(reversed(path1), reversed(path2)):
            if a.val < b.val:
                return path1
            elif a.val > b.val:
                return path2
        return path1 if len(path1) < len(path2) else path2
    def transfer(arr):
        res = []
        for node in reversed(arr):
            res.append(chr(ord('a') + node.val))
        return ''.join(res)
    # use dfs to traverse the tree
    if not root:
        return ''
    stack = [(root, [])]
    smallest = None
    while stack:
        node, path = stack.pop()
        path = path + [node]
        if not node.left and not node.right:
            if smallest is None:
                smallest = path
            else:
                smallest = compare(path, smallest)
        if node.right:
            stack.append((node.right, path))
        if node.left:
            stack.append((node.left, path))
    return transfer(smallest)

if __name__=='__main__':
    node1 = TreeNode(1, TreeNode(3), TreeNode(4))
    node2 = TreeNode(2, TreeNode(3), TreeNode(4))
    root = TreeNode(0, node1, node2)
    print(smallestFromLeaf(root)) # expected dba