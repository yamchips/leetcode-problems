def firstUniqChar(s: str) -> int:
    occurrence = [0] * 26
    for ch in s:
        occurrence[ord(ch) - ord('a')] += 1
    for i in range(len(s)):
        if occurrence[ord(s[i]) - ord('a')] == 1:
            return i
    return -1