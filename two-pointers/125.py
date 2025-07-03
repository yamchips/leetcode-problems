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

