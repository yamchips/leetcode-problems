def isInterleave(s1: str, s2: str, s3: str) -> bool:
    if len(s1) + len(s2) != len(s3): 
        return False
    m, n = len(s1), len(s2)
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    dp[0][0] = True
    for i in range(m + 1):
        for j in range(n + 1):
            if (i - 1 >= 0 and dp[i - 1][j] and s1[i - 1] == s3[i + j - 1])\
                or (j - 1 >= 0 and dp[i][j - 1] and s2[j - 1] == s3[i + j - 1]):
                dp[i][j] = True
    return dp[-1][-1]