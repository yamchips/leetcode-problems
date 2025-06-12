def maxProfit(prices: list[int]) -> int:
    n = len(prices)
    if n == 1 : return 0
    profit = 0
    low, high = prices[0], prices[0]
    for i, price in enumerate(prices, start=1):
        if price < low:
            low = price
            high = price
        if price > high:
            high = price
        profit += high - low
        low = high
    return profit

def maxProfit2(prices:list[int]) -> int:
    profit = 0
    for i in range(1, len(prices)):
        if (prices[i] - prices[i - 1] > 0):
            profit += prices[i] - prices[i - 1]
    return profit
        