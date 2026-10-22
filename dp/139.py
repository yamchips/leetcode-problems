def wordBreak(s: str, wordDict: list[str]) -> bool:
    n = len(s)
    wordDictionary = set(wordDict)
    dp = [False] * (n + 1)
    dp[0] = True

    maxLen = max(map(len, wordDict))
    for i in range(1, n + 1):
        for j in range(max(0, i - maxLen), i):
            if dp[j] == True and s[j:i] in wordDictionary:
                dp[i] = True
                break
    return dp[-1]
