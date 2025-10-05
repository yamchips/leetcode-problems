'''
Given an array of strings, find the relevant pairs where one element is the prefix of the other or they are the same. 

Example: 
titles: ['abc', 'a', 'a', 'b', 'ab', 'ac']
relevant pairs:
1. titles[0] 'abc' and titles[1] 'a'
2. titles[0] 'abc' and titles[2] 'a'
3. titles[1] 'a' and titles[2] 'a'
4. titles[1] 'a' and titles[4] 'ab'
5. titles[1] 'a' and titles[5] 'ac'
6. titles[2] 'a' and titles[4] 'ab'
7. titles[2] 'a' and titles[5] 'ac'
8. titles[4] 'ab' and titles[0] 'abc'
'''

def countPrefixPairs(titles: list[str]) -> int:
    n = len(titles)
    count = 0
    titles.sort()
    for i in range(n):
        j = i + 1
        while j < n and titles[j].startswith(titles[i]):
            count += 1
            j += 1
    return count
