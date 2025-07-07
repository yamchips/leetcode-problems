def updateBoard(board, i, j):
    m, n = len(board), len(board[0])
    count = 0
    for dx, dy in [(1, 1), (1, 0), (1, -1), (0, 1), (0,- 1), (-1, 1), (-1, 0), (-1, -1)]:
        nx, ny = i + dx, j + dy
        if 0 <= nx <= m - 1 and 0 <= ny <= n - 1:
            if (isinstance(board[nx][ny], int) and board[nx][ny] == 1) \
            or (isinstance(board[nx][ny], tuple) and board[nx][ny][0] == 1):
                count += 1
    if board[i][j] == 1:
        if count == 2 or count == 3:
            board[i][j] = (board[i][j], 1)            
        else:
            board[i][j] = (board[i][j], 0)
    else:
        if count == 3:
            board[i][j] = (board[i][j], 1)
        else:
            board[i][j] = (board[i][j], 0)


def gameOfLife(board: list[list[int]]) -> None:
    m, n = len(board), len(board[0])
    for i in range(m):
        for j in range(n):
            updateBoard(board, i, j)
    # modify each element
    for i in range(m):
        for j in range(n):
            board[i][j] = board[i][j][1] # type: ignore
    print(board)

if __name__=='__main__':
    gameOfLife([[0,1,0],[0,0,1],[1,1,1],[0,0,0]])