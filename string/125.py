import re

def isPalindrome(s: str) -> bool:
    s = s.lower()
    result = re.findall(r"[a-z]+", s)
    phrase = "".join(result)
    left, right = 0, len(phrase) - 1
    while left <= right:
        if phrase[left] == phrase[right]:
            left += 1
            right -= 1
        else:
            return False
    return True

if __name__=="__main__":
    print(isPalindrome("A man, a plan, a canal: Panama")) # true
    print(isPalindrome("a")) # true
    print(isPalindrome(" ")) # true
    print(isPalindrome("A man, a plan, a canal: Panamab")) # false

