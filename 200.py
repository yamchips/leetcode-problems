from collections import deque

# bfs
# originally, we change visited after we pop the element, and it causes a MLE. If we move the code to each if clause, we won't have this error. That's because in the old way, we might add one position multiple times, that leads to MLE.
def numIslands(grid) -> int:
    m = len(grid)
    n = len(grid[0])
    visited = set()
    count = 0
    while len(visited) < m * n:
        for i in range(m):
            for j in range(n):
                if (i,j) in visited:
                    continue
                visited.add((i,j))
                if grid[i][j] == "0":
                    continue
                count += 1
                queue = deque([(i,j)])
                while queue:
                    x, y = queue.popleft()
                    
                    if x + 1 < m and (x+1, y) not in visited and grid[x+1][y] == "1":
                        visited.add((x+1, y))
                        queue.append((x+1, y))
                    if x - 1 >= 0 and (x-1, y) not in visited and grid[x-1][y] == "1":
                        visited.add((x-1, y))
                        queue.append((x-1, y))
                    if y + 1 < n and (x, y+1) not in visited and grid[x][y+1] == "1":
                        visited.add((x, y+1))
                        queue.append((x, y+1))
                    if y - 1 >=0 and (x, y-1) not in visited and grid[x][y-1] == "1":
                        visited.add((x, y-1))
                        queue.append((x, y-1))
    return count

# bfs without set, modify grid
def numIslands(grid) -> int:
    m = len(grid)
    n = len(grid[0])
    count = 0
    
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 'v':
                continue
            if grid[i][j] == "0":
                grid[i][j] = 'v'
                continue
            count += 1
            grid[i][j] = 'v'
            queue = deque([(i,j)])
            while queue:
                x, y = queue.popleft()
                for dx, dy in [(1,0), (-1, 0), (0, 1), (0, -1)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == '1':
                        grid[nx][ny] = 'v'
                        queue.append((nx, ny))
    return count

# dfs using a stack
def numIslands(grid) -> int:
    m = len(grid)
    n = len(grid[0])
    count = 0
    stack = []
    visited = set()
    for i in range(m):
        for j in range(n):
            if (i, j) not in visited and grid[i][j] == '1':
                visited.add((i, j))
                stack.append((i, j))
                count += 1
                while stack:
                    x, y = stack.pop()
                    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited and grid[nx][ny] == '1':
                            visited.add((nx, ny))
                            stack.append((nx, ny))
    return count

def numIslands(grid) -> int:
    count = 0
    m = len(grid)
    n = len(grid[0])
    def dfs(grid, i, j, m, n):
        if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] == '0':
            return
        grid[i][j] = '0'
        dfs(grid, i, j + 1, m, n)
        dfs(grid, i, j - 1, m, n)
        dfs(grid, i + 1, j, m, n)
        dfs(grid, i - 1, j, m, n)
 
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '1':
                dfs(grid, i, j, m, n)
                count += 1

    return count

if __name__=='__main__':
    print(numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]])) # expected 1
    print(numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]])) # expected 3
    print(numIslands([['1']])) # expected 1
    print(numIslands([['0']])) # expected 0
    print(numIslands([['1', '0', '1']])) # expected 2
    print(numIslands([['1'], ['0'], ['1']])) # expected 2
    