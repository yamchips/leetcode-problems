
'''
We modify grid so no need for a visited set.
Mark the node as visited when we add it to the stack.
'''
def numIslands(grid) -> int:
    number = 0
    m = len(grid)
    n = len(grid[0])
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '1':
                # use dfs to modify all neighbors to 0
                number += 1
                stack = [(i,j)]
                grid[i][j] = '0' # mark it as visited right now
                while stack:
                    x, y = stack.pop()
                    for dx, dy in [(0,1),(1,0),(-1,0),(0,-1)]:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == '1':
                            stack.append((nx, ny))       
                            grid[nx][ny] = '0' # mark it as visited
    return number

'''
If we cannot modify the grid, then we use a visited set to record.
'''
def numIslands(grid: list[list[str]]) -> int:
    number = 0
    m = len(grid)
    n = len(grid[0])

    visited = set()

    for i in range(m):
        for j in range(n):
            if grid[i][j] == '1' and (i,j) not in visited:
                number += 1

                stack = [(i,j)]
                visited.add((i,j))

                while stack:
                    x, y = stack.pop()

                    for dx, dy in [(0,1),(1,0),(-1,0),(0,-1)]:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < m and 0 <= ny < n \
                            and grid[nx][ny] == '1' \
                            and (nx, ny) not in visited:
                            stack.append((nx, ny))
                            visited.add((nx, ny))
    return number


if __name__=='__main__':
    print(numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]])) # expected 1
    print(numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]])) # expected 3
    print(numIslands([['1']])) # expected 1
    print(numIslands([['0']])) # expected 0
    print(numIslands([['1', '0', '1']])) # expected 2
    print(numIslands([['1'], ['0'], ['1']])) # expected 2
    