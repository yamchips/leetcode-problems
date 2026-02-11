from collections import defaultdict


def isAnagram(self, s: str, t: str) -> bool:
    # create a 26 digit array
    record = [0] * 26
    # record s
    for char in s:
        record[ord(char) - ord('a')] += 1
    # iterate t
    for char in t:
        record[ord(char) - ord('a')] -= 1
    # check whether all are 0
    for e in record:
        if e != 0:
            return False
    return True
    # O(n) time, O(1) space

def isAnagram(self, s: str, t: str) -> bool:
    # use a dict instead of an array
    # O(n) time, O(1) space
    if len(s) != len(t):
        return False
    record = defaultdict(int)
    for char in s:
        record[char] += 1
    for char in t:
        if char not in record or record[char] == 0:
            return False
        record[char] -= 1
    return True