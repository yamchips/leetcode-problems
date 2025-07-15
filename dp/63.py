def uniquePathsWithObstacles1(obstacleGrid: list[list[int]]) -> int:
    m, n = len(obstacleGrid), len(obstacleGrid[0])
    dp = [[0] * n for _ in range(m)]
    for i in range(n):
        if obstacleGrid[0][i] != 1:
            dp[0][i] = 1
        else:
            break
    for i in range(m):
        if obstacleGrid[i][0] != 1:
            dp[i][0] = 1
        else:
            break
    for i in range(1, m):
        for j in range(1, n):
            if obstacleGrid[i][j] == 1:
                continue
            else:
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    return dp[-1][-1]

def uniquePathsWithObstacles(obstacleGrid: list[list[int]]) -> int:
    m, n = len(obstacleGrid), len(obstacleGrid[0])
    dp = [[0] * n for _ in range(m)]
    dp[0][0] = 1 if obstacleGrid[0][0] != 1 else 0
    for i in range(0, m):
        for j in range(0, n):
            if i == 0 and j == 0: continue
            if obstacleGrid[i][j] == 1:
                continue
            else:
                dp[i][j] = (dp[i - 1][j] if i - 1 >= 0 else 0) \
                    + (dp[i][j - 1] if j - 1 >= 0 else 0)
    return dp[-1][-1]

if __name__=='__main__':
    uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]])