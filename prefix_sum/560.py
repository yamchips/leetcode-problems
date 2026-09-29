from typing import List

'''

'''
def subarraySum(nums: List[int], k: int) -> int:
    count = 0

    # prefix = sum of nums[0:i]
    prefix = 0
    # we define prefix[0] to 0, so we need to add that key-value pair to dictionary
    prefix_count = {0:1}

    for num in nums:
        prefix += num
        target = prefix - k
        count += prefix_count.get(target, 0)
        prefix_count[prefix] = prefix_count.get(prefix, 0) + 1
    
    return count

if __name__=='__main__':
    print(subarraySum([1,1,1],2))
    print(subarraySum([-1,1,0],0))
    print(subarraySum([1,2,3],3))