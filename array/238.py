from typing import List


def productExceptSelf(nums: List[int]) -> List[int]:
    n = len(nums)
    # prefix[i] = a[0]* a[1] * ... a[i-1] 
    res = [1] * n
    for i in range(1, n):
        res[i] = res[i - 1] * nums[i - 1]
    # suffix[i] = a[i+1] * ... a[n-1]
    suffix = 1
    for i in range(n-2, -1, -1):
        suffix *= nums[i + 1]
        res[i] *= suffix
    
    return res