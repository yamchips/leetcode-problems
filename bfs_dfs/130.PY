from collections import deque

def solve(board: list[list[str]]) -> None:
    m, n = len(board), len(board[0])
    visited = set()
    for i in range(m):
        for j in range(n):
            if board[i][j] == 'X':
                visited.add((i,j))
                continue
            if (i,j) in visited:
                continue
            visited.add((i,j))
            region = [(i,j)]
            isSurrounded = True
            queue = deque([(i,j)])
            if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                isSurrounded = False
            while queue:
                size = len(queue)
                for _ in range(size):
                    x, y = queue.popleft()
                    for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx <= m - 1 and 0 <= ny <= n - 1:
                            if (nx, ny) in visited:
                                continue
                            visited.add((nx, ny))
                            if board[nx][ny] == 'O':
                                queue.append((nx, ny))
                                region.append((nx, ny))
                                if x + dx == 0 or x + dx == m - 1\
                                    or y + dy == 0 or y + dy == n - 1:
                                    isSurrounded = False
            if isSurrounded:
                while region:
                    x, y = region.pop()
                    board[x][y] = 'X'

def solve2(board:list[list[str]]) -> None:
    m, n = len(board), len(board[0])
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    def bfs(i: int, j: int):
        queue = deque([(i, j)])
        board[i][j] = 'S'  # mark as safe
        while queue:
            x, y = queue.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and board[nx][ny] == 'O':
                    board[nx][ny] = 'S'
                    queue.append((nx, ny))

    # start from boarder O, mark them as S (safe)
    for i in range(m):
        if board[i][0] == 'O':
            bfs(i, 0)
        if board[i][n - 1] == 'O':
            bfs(i, n - 1)
    for j in range(n):
        if board[0][j] == 'O':
            bfs(0, j)
        if board[m - 1][j] == 'O':
            bfs(m - 1, j)
    # change all O into X and all S into O
    for i in range(m):
        for j in range(n):
            if board[i][j] == 'O':
                board[i][j] = 'X'
            if board[i][j] == 'S':
                board[i][j] = 'O'