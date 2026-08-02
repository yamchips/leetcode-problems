from collections import defaultdict

def containsNearbyDuplicate3(nums: list[int], k: int) -> bool:
    seen = set()
    for i, num in enumerate(nums):
        if num in seen:
            return True
        seen.add(num)
        if i >= k:
            seen.remove(nums[i - k])
    return False


def containsNearbyDuplicate2(nums: list[int], k: int) -> bool:
    n = len(nums)
    if n == 1: return False
    # initialize map of size k + 1
    record = dict() # key: content, value: index
    for i in range(n):
        if nums[i] in record and i - record[nums[i]] <= k:
            return True
        record[nums[i]] = i
        if i >= k and nums[i - (k)] != nums[i]:
            del record[nums[i - (k)]]
    return False

# before optimization
def containsNearbyDuplicate1(nums: list[int], k: int) -> bool:
    n = len(nums)
    if n == 1: return False
    # initialize map of size k + 1
    record = dict() # key: content, value: index
    for i in range(min(k + 1, n)):
        if nums[i] in record and i - record[nums[i]] <= k:
            return True
        record[nums[i]] = i

    # iterate through the array
    for i in range(k + 1, n):
        if nums[i] in record and i - record[nums[i]] <= k:
            return True
        record[nums[i]] = i
        if nums[i - (k + 1)] != nums[i]:
            del record[nums[i - (k + 1)]]
    
    return False

'''
dict solution
time: O(n)
space: O(n)
'''
def containsNearbyDuplicate(nums: list[int], k: int) -> bool:
    if k == 0: return False
    seen = {}
    for i in range(len(nums)):
        if nums[i] not in seen:
            seen[nums[i]] = i
        else:
            latestIndex = seen[nums[i]]
            if abs(i - latestIndex) <= k:
                return True
            else:
                seen[nums[i]] = i
    return False

def containsNearbyDuplicate(nums: list[int], k: int) -> bool:
    seen = set()
    for i, num in enumerate(nums):
        if num in seen:
            return True
        seen.add(num)
        if i >= k:
            seen.remove(nums[i - k])
    return False

def containsNearbyDuplicate(nums: list[int], k: int) -> bool:
    seen = set()
    start, end = 0, 0
    while end < len(nums):
        if nums[end] in seen:
            return True
        seen.add(nums[end])
        end += 1
        if end - start > k:
            seen.remove(nums[start])
            start += 1
    return False

if __name__=='__main__':
    print(containsNearbyDuplicate([1,0,1,1], 1)) # True
    print(containsNearbyDuplicate([1,2,3,1], 3)) # True
    print(containsNearbyDuplicate([1,2,3,1,2,3], 2)) # False
