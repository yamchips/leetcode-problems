def threeSum(nums:list[int], target: int, res, first) -> list[list[int]]:
    for i in range(len(nums) - 2):
        if i - 1 >= 0 and nums[i] == nums[i - 1]:
            continue
        j = i + 1
        k = len(nums) - 1
        while j < k:
            total = nums[i] + nums[j] + nums[k]
            if total > target:
                k -= 1
            elif total < target:
                j += 1
            else:
                res.append([first, nums[i], nums[j], nums[k]])
                while j < k and nums[j] == nums[j + 1]:
                    j += 1
                while j < k and nums[k] == nums[k - 1]:
                    k -= 1
                j += 1
                k -= 1
    return res

def fourSum(nums:list[int], target: int) -> list[list[int]]:
    nums.sort()
    res = []
    for a in range(len(nums) - 3):
        if a - 1 >= 0 and nums[a] == nums[a - 1]:
            continue
        res = threeSum(nums[a + 1:], target - nums[a], res, nums[a])                
    return res

if __name__=='__main__':
    print(fourSum([1,0,-1,0,-2,2], 0))
    print(fourSum([2,2,2,2,2,2,2], 8))
    print(fourSum([-1,0,1,2,-1,-4], -1))
    print(fourSum([1,-2,-5,-4,-3,3,3,5], -11))