def maxProfit(prices:list[int]) -> int:
    n = len(prices)
    if (n == 1): return 0
    dp = [0] * n
    if (prices[1] > prices[0]):
        dp[1] = prices[1] - prices[0]
    if (n == 2): return dp[1]
    
    for i in range(2, n):
        for j in range(i):
            index = 0 if j - 2 < 0 else j - 2
            dp[i] = max(prices[i] - prices[j] + dp[index], dp[i])
        dp[i] = max(dp[i-1], dp[i])
    return dp[n - 1]
    