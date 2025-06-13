# using greedy approach is not correct
def maxProfit3(prices:list[int], fee:int) -> int:
    n = len(prices)
    if (n == 1): return 0
    profit = 0
    low, high = prices[0], prices[0]
    for i, price in enumerate(prices):
        if price < low:
            low = price
            high = price
        if price > high:
            high = price
        if i <= n - 2 and prices[i + 1] < price:
            if high - low > fee:
                profit += high - low - fee
                low = price
                high = price
        else:
            if i == n - 1:
                if high - low > fee:
                    profit += high - low - fee
            elif prices[i + 1] > price:
                continue
            
    return profit

# dp[i] = max(dp[i-1], dp[i-2]+p[i]-p[i-1]-fee, .. , dp[0]+p[i]-p[1]-fee,0+p[i]-p[0]-fee )
def maxProfit3(prices:list[int], fee:int) -> int:
    n = len(prices)
    if (n == 1): return 0
    dp = [0] * n
    for i in range(1, n):
        for j in range(i):
            index = j-1 if j-1 >=0 else 0
            if (prices[i]-prices[j]-fee > 0):
                dp[i] = max(dp[i], prices[i]-prices[j]-fee+dp[index])
            else:
                dp[i] = max(dp[i], dp[index])
        dp[i] = max(dp[i], dp[i-1])
    return dp[-1]

def maxProfit3(prices:list[int], fee:int) -> int:
    n = len(prices)
    s0 = [0] * n
    s1 = [0] * n
    s1[0] = -prices[0]
    for i in range(1, n):
        s0[i] = max(s0[i-1], s1[i-1]+prices[i]-fee)
        s1[i] = max(s1[i-1], s0[i-1]-prices[i])
    return s0[-1]
