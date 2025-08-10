'''
String compression

convert string abaasass to aba2sas2
'''

def compression(s: str) -> str:
    res = []
    n = len(s)
    if n < 2:
        return s
    left, right = 0, 1
    while left < n:
        if right < n and s[left] == s[right]:
            right += 1
        else:
            res.append(s[left])
            if right - left > 1:
                res.append(str(right - left))
            left = right
            right += 1
    return ''.join(res)
            
if __name__=='__main__':
    print(compression('abaasass'))
    print(compression('aaabbbbc'))