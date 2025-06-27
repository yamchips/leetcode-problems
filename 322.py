def coinChange(coins:list[int], amount:int) -> int:
    # dp[i] means min number of coins to reach amount i
    # initialize with large amount because we want min here
    dp = [amount + 10] * (amount + 1) 
    dp[0] = 0
    for i in range(1, amount + 1):
        minVal = amount + 10
        for coin in coins:
            if i - coin >= 0:
                minVal = min(minVal, dp[i - coin] + 1)
        dp[i] = minVal
    return dp[-1] if dp[-1] != amount + 10 else -1


if __name__=='__main__':
    print(coinChange([1,2,5], 11)) # expected 3
    print(coinChange([2], 3)) # expected -1
    print(coinChange([1], 0)) # expected 0
    print(coinChange([2], 3)) # expected -1
    print(coinChange([1], 2)) # expected 2