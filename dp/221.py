def maximalSquare1(matrix: list[list[str]]) -> int:
    m, n = len(matrix), len(matrix[0])
    # dp[i][j]: max side length at matrix[i][j]
    dp = [[0] * n for _ in range(m)]
    # initialize first row and column
    dp[0] = [int(e) for e in matrix[0]]
    for i in range(m):
        dp[i][0] = int(matrix[i][0])
    maxLength = 0
    for i in range(n):
        if matrix[0][i] == '1':
            maxLength = 1
            break
    for i in range(m):
        if matrix[i][0] == '1':
            maxLength = 1
            break
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][j] == '0':
                dp[i][j] = 0
            else:
                dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1
            maxLength = max(maxLength, dp[i][j])
    return maxLength ** 2

def maximalSquare(matrix: list[list[str]]) -> int:
    m, n = len(matrix), len(matrix[0])
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    maxLength = 0
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if matrix[i - 1][j - 1] == '0':
                dp[i][j] = 0
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
            maxLength = max(dp[i][j], maxLength)
    return maxLength ** 2

if __name__=='__main__':
    maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]])