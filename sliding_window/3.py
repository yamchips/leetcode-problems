'''
When facing a sliding window problem, always ask:
What invariant must the window maintain?
Here, the window must contain no duplicate characters

'''
def lengthOfLongestSubstring(s: str) -> int:
    maxLength = 0
    left = 0
    seen = set()
    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        seen.add(s[right])
        maxLength = max(maxLength, right - left + 1)
    return maxLength


# this is two-pointer mindset, not sliding window 
def lengthOfLongestSubstring(s: str) -> int:
    maxLength = 0
    if len(s) == 0: return maxLength
    if len(s) == 1: return 1
    seen = set(s[0])
    left, right = 0, 1
    while left < len(s) and right < len(s):
        while right < len(s) and s[right] not in seen:
            seen.add(s[right])
            right += 1
        
        maxLength = max(maxLength, right - left)

        while right < len(s) and s[right] in seen:
            seen.remove(s[left])    
            left += 1
    return maxLength

def lengthOfLongestSubstring(s: str) -> int:
    max_length = 0
    seen = set()
    start, end = 0, 0
    while end < len(s):
        while s[end] in seen:
            max_length = max(end - start, max_length)
            seen.remove(s[start])
            start += 1
        seen.add(s[end])
        end += 1
    return max(max_length, end - start)

if __name__=='__main__':
    print(lengthOfLongestSubstring('abc'))
    print(lengthOfLongestSubstring('abccbcbb'))