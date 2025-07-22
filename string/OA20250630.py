# given a string s, return the max length of substring that has no duplicate characters

from collections import defaultdict


def getMaxLength(s: str) -> int:
  n = len(s)
  if n == 0:
    return 0
  if n == 1:
    return 1
  
  chars = set()
  start, end = 0, 0
  maxLength = 0
  
  while end < n:
    if s[end] not in chars:
      chars.add(s[end])
      end += 1
      maxLength = max(maxLength, len(chars))
    else:
      chars.remove(s[start])
      start += 1

  return maxLength

if __name__=='__main__':
  print(getMaxLength('abcabcbb') == 3) 
  print(getMaxLength('') == 0)
  print(getMaxLength('bb') == 1)
  print(getMaxLength('abba') == 2)
  print(getMaxLength('abcd') == 4)
  print(getMaxLength('abcc') == 3)
  print(getMaxLength('dvdf') == 3)
  print(getMaxLength('aab') == 2)
  print(getMaxLength("tmmzuxt") == 5)
  print(getMaxLength("abcdecfgh") == 6)

  

