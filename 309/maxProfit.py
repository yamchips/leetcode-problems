def maxProfit2(prices:list[int]) -> int:
    n = len(prices)
    if (n == 1): return 0
    dp = [0] * n
    if (prices[1] > prices[0]):
        dp[1] = prices[1] - prices[0]
    if (n == 2): return dp[1]
    
    for i in range(2, n):
        for j in range(i):
            index = 0 if j - 2 < 0 else j - 2
            if (prices[i] - prices[j] > 0): 
                dp[i] = max(prices[i] - prices[j] + dp[index], dp[i])
            else:
                dp[i] = max(dp[index], dp[i])        
        dp[i] = max(dp[i-1], dp[i])
    return dp[n - 1]

def maxProfit2(prices:list[int]) ->int:
    n = len(prices)
    if (n == 1): return 0
    s0 = [0] * n
    s1 = [0] * n
    s2 = [0] * n
    s1[0] = -prices[0]
    for i in range(1,n):
        s0[i] = max(s2[i-1], s0[i-1])
        s1[i] = max(s1[i-1], s0[i-1]-prices[i])
        s2[i] = s1[i-1] + prices[i]
    return max(s0[-1], s2[-1])
    