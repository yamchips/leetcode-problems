from collections import deque
from typing import List

def orangesRotting(grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    fresh, steps  = 0, 0
    queue = deque()
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                fresh += 1
            elif grid[i][j] == 2:
                queue.append((i,j))
    if fresh == 0:
        return 0
    while queue:
        size = len(queue)
        for _ in range(size):
            x, y = queue.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and grid[x+dx][y+dy] == 1:
                    grid[nx][ny] = 2
                    queue.append((x+dx, y+dy))
                    fresh -= 1                        
        steps += 1
    return steps - 1 if fresh == 0 else -1

def orangesRotting2(grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    fresh, steps  = 0, 0
    queue = deque()
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                fresh += 1
            elif grid[i][j] == 2:
                queue.append((i,j))
    seen = set()
    while queue:
        rotten = False
        size = len(queue)
        turnRotten = set()
        for _ in range(size):
            x, y = queue.popleft()
            seen.add((x, y))
            for dx, dy in directions:
                if 0 <= x + dx < m and 0 <= y + dy < n\
                    and (x+dx, y+dy) not in seen \
                    and grid[x+dx][y+dy] == 1:
                    queue.append((x+dx, y+dy))
                    seen.add((x+dx, y+dy))
                    if (x+dx, y+dy) not in turnRotten:
                        turnRotten.add((x+dx, y+dy))
                        fresh -= 1                        
                    rotten = True
        if rotten: steps += 1
    return steps if fresh == 0 else -1


def orangesRotting1(grid: List[List[int]]) -> int:
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

if __name__=='__main__':
    print(orangesRotting([[1,2,1,1,2,1,1]]))