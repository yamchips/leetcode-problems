from typing import List


def orangesRotting(grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    rotten = True
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    fresh, steps  = 0, 0
    while rotten:
        rotten = False
        fresh = 0
        changing = []
        # iterate all grids
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    for direction in directions:
                        newX = i + direction[0]
                        newY = j + direction[1]
                        if 0 <= newX < m and 0 <= newY < n and \
                            grid[newX][newY] == 1:
                            fresh -= 1
                            changing.append((newX, newY))
                            rotten = True
        # update grids
        for newX, newY in changing:
            grid[newX][newY] = 2                
        # update steps
        if rotten: steps += 1
    return steps if fresh == 0 else -1
