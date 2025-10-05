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

if __name__=='__main__':
    print(containsNearbyDuplicate3([1,0,1,1], 1))