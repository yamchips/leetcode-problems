
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


def construct(grid: list[list[int]]) :
    n = len(grid)
    # base case
    if n == 1:
        if grid[0][0] == 1:
            return Node(1, 1, None, None, None, None)
        else:
            return Node(0, 1, None, None, None, None)
    # recursive 
    topleft = construct([row[:n//2] for row in grid[:n//2]])
    topright = construct([row[n//2:] for row in grid[:n//2]])
    bottomleft = construct([row[:n//2] for row in grid[n//2:]])
    bottomright = construct([row[n//2:] for row in grid[n//2:]])
    if (topleft.isLeaf and topright.isLeaf and bottomleft.isLeaf and \
        bottomright.isLeaf and \
        topleft.val == topright.val == bottomleft.val == bottomright.val):
        return Node(topleft.val, 1, None, None, None, None)
    else:
        return Node(1, 0, topleft, topright, bottomleft, bottomright)



if __name__=='__main__':
    construct([[1,1,0,0],[0,0,1,1],[1,1,0,0],[0,0,1,1]])
    construct([[0,1],[1,0]])
    construct([[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0]])