def isPalindrome(s: str) -> bool:
    s = ''.join(c.lower() for c in s if c.isalnum())
    n = len(s)
    left, right = 0, n - 1
    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            return False
    return True

import re

def isPalindrome(s: str) -> bool:
    chars = re.findall(r"[A-Za-z0-9]", s)
    word = "".join(chars).lower()
    start = 0
    end = len(word) - 1
    while start < end:
        if word[start] != word[end]:
            return False
        start += 1
        end -= 1
    return True