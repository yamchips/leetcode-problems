


def maxProfit(prices: list[int]) -> int:
    profit = 0
    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            if (prices[j] - prices[i] > profit):
                profit = prices[j] - prices[i]
    return profit

def maxProfit2(prices: list[int]) -> int:
    n = len(prices)
    dp = [0]*n
    for i in range(1, n):
        if (prices[i] > prices[i - 1]):
            profit = 0
            for j in range(0, i):
                profit = max(profit, prices[i] -prices[j])
            dp[i] = max(dp[i - 1], profit)
        else:
            dp[i] = dp[i - 1]
    return dp[n - 1]

def maxProfit3(prices:list[int]) -> int:
    # [value, index]
    low = [prices[0], 0]
    high = [0, 0] 
    n = len(prices)
    profit = 0
    for i in range(n):
        if prices[i] < low[0]:
            low[0] = prices[i]
            low[1] = i
            high[0] = low[0]
            high[1] = low[1]
        if prices[i] > high[0]:
            high[0] = prices[i]
            high[1] = i
        if high[1] > low[1]:
            profit = max(high[0] - low[0], profit)
    return profit
    
