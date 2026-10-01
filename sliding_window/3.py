'''
When facing a sliding window problem, always ask:
What invariant must the window maintain?
Here, the window must contain no duplicate characters

'''
def lengthOfLongestSubstring(s: str) -> int:
    maxLength = 0
    window = set()
    left = 0
    for right in range(len(s)):

        while s[right] in window:
            window.remove(s[left])
            left += 1
        
        window.add(s[right])
        maxLength = max(maxLength, right - left + 1)

    return maxLength


if __name__=='__main__':
    print(lengthOfLongestSubstring('abc'))
    print(lengthOfLongestSubstring('abccbcbb'))