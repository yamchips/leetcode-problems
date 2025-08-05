# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def zigzagLevelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
    if not root: return []
    res = []
    queue = deque([root])
    reverse = False
    while queue:
        size = len(queue)
        temp = []
        for _ in range(size):
            curr = queue.popleft()
            temp.append(curr)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        if reverse:
            temp.reverse()
        res.append(temp)
        reverse = not reverse
    return res