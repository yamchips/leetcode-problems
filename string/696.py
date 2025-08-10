def countBinarySubstrings(s: str) -> int:
    groups = []
    count = 1
    n = len(s)
    for i in range(1, n):
        if s[i] == s[i - 1]:
            count += 1
        else:
            groups.append(count)
            count = 1
    groups.append(count)
    res = 0
    for i in range(1, len(groups)):
        res += min(groups[i - 1], groups[i])
    return res
