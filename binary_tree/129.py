from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sumNumbers(root: Optional[TreeNode]) -> int:
    if not root: return 0
    stack = [(root, str(root.val))]
    res = 0
    while stack:
        node, val = stack.pop()
        if node.left:
            stack.append((node.left, val + str(node.left.val)))
        if node.right:
            stack.append((node.right, val + str(node.right.val)))
        if (not node.left) and (not node.right):
            res += int(val)
    return res

if __name__=='__main__':
    root = TreeNode(1,TreeNode(5), TreeNode(1,None, TreeNode(6)))
    sumNumbers(root)