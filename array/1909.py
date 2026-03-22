from typing import List

def canBeIncreasing(self, nums: List[int]) -> bool:
    broken = False
    for i in range(1, len(nums)):
        if nums[i - 1] >= nums[i]:
            if broken:
                return False
            
            broken = True
            
            if i > 1 and nums[i] <= nums[i - 2]:
                nums[i] = nums[i - 1]
    return True

def isStrictlyIncreasing(arr):
    n = len(arr)
    for i in range(n - 1):
        if arr[i] >= arr[i + 1]:
            return False
    return True

def canBeIncreasing(self, nums: List[int]) -> bool:
    if isStrictlyIncreasing(nums): return True
    for i in range(len(nums)):
        temp = [nums[j] for j in range(len(nums)) if j != i]
        if isStrictlyIncreasing(nums):
            return True
    return False

