# use a dp matrix,  O(n^2) time and O(n^2) space
# even if we turn matrix to two arrays, we still have O(n) space
def longestPalindrome1(s:str) -> str:
    n = len(s)
    dp = [[False] * n for _ in range(n)] # dp[i][j]: whether s[i:j+1] is a palindrome
    start = 0
    end = 0
    maxLength = 0
    for i in range(n - 1, -1, -1):
        for j in range(i, n):
            if j - i <= 2 and s[i] == s[j]:
                dp[i][j] = True
            elif s[i] == s[j] and dp[i+1][j-1]:
                dp[i][j] = True
            if dp[i][j] and j - i + 1 > maxLength:
                maxLength = j - i + 1
                start = i
                end = j
    return s[start : end + 1]

# use expand method, O(n^2) time and O(1) space
def expand(s: str, left: int, right: int, n: int) -> str:
    while left >= 0 and right <= n - 1 and s[left] == s[right]:
        left -= 1
        right += 1
    return s[left + 1: right]

def longestPalindrome(s:str) -> str:
    n = len(s)
    if n == 1: return s
    result = s[0]
    for i in range(n):
        odd = expand(s, i, i, n)
        even = expand(s, i, i + 1, n)
        if len(odd) > len(result):
            result = odd
        if len(even) > len(result):
            result = even
    return result

if __name__=='__main__':
    print(longestPalindrome('babad')) # expected bab or aba
    print(longestPalindrome('cbbd')) # expected bb
    print(longestPalindrome('abc')) # expected a or b or c