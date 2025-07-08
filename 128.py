def longestConsecutive(nums: list[int]) -> int:
    numSet = set(nums) # O(n) time
    maxLength = 0
    for num in numSet: # iterate in set help skip duplicates
        if num - 1 not in numSet: # this help skip elements
            length = 0
            while num + length in numSet:
                length += 1
                maxLength = max(maxLength, length)
            
    return maxLength

if __name__=='__main__':
    print(longestConsecutive([100, 4, 200, 1, 3, 2]))