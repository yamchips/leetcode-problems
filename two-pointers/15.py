from typing import List


def search(target: int, sortedNums: list[int]) -> int:
    # return index of target in sortedNums, if not found, return -1
    left, right = 0, len(sortedNums) - 1
    while left <= right:
        mid = (left + right) // 2
        if sortedNums[mid] > target:
            right = mid - 1
        elif sortedNums[mid] < target:
            left = mid + 1
        else:
            return mid
    return -1

def threeSum1(nums:list[int]) -> list[list[int]]:
    res = []
    sortedNums = sorted(nums)
    left, right = 0, len(nums) - 1
    while left < right:
        target = -(sortedNums[left] + sortedNums[right])
        index = search(target, sortedNums)
        if index == -1:
            if target > 0:
                left += 1
            else:
                right -= 1
        else:
            if index != left and index != right:
                triplet = sorted([sortedNums[left], sortedNums[right], sortedNums[index]])
                if triplet not in res:
                    res.append(triplet)
                left += 1
                right -= 1
            else:
                if index == left:
                    right -=1
                if index == right:
                    left += 1
    return res

def threeSum2(nums:list[int]) -> list[list[int]]:
    nums.sort()
    res = []
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left, right = i + 1, len(nums) - 1
        while left < right:
            sum = nums[i] + nums[left] + nums[right]
            if sum > 0:
                right -= 1
            elif sum < 0:
                left += 1
            else:
                res.append([nums[i], nums[left], nums[right]])
                # skip duplicate for left and right
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
    return res

def threeSum(nums: list[int]) -> list[list[int]]:
    res = []
    nums.sort()
    for i in range(len(nums) - 2):
        if nums[i] > 0:
            break
        if i - 1 >= 0 and nums[i] == nums[i - 1]:
            continue
        j = i + 1
        k = len(nums) - 1
        while j < k:
            total = nums[i] + nums[j] + nums[k]
            if total > 0:
                k -= 1
            elif total < 0:
                j += 1
            else:
                res.append([nums[i], nums[j], nums[k]])
                while j < k and nums[j] == nums[j + 1]:
                    j += 1
                while j < k and nums[k] == nums[k - 1]:
                    k -= 1
                j += 1
                k -= 1
    return res 

def threeSum(self, nums: List[int]) -> List[List[int]]:
    nums.sort()
    res = [] 
    for i in range(len(nums) - 2):
        k = len(nums) - 1
        j = i + 1
        while j < k:
            total = nums[i] + nums[j] + nums[k]
            if total < 0:
                j += 1
            elif total > 0:
                k -= 1
            else:
                res.append([nums[i], nums[j], nums[k]])
                while j < k and nums[j] == nums[j + 1]:
                    j += 1
                while j < k and nums[k] == nums[k - 1]:
                    k -= 1
                j += 1
                k -= 1

    return res

if __name__=='__main__':
    print(threeSum([-1,0,1,2,-1,-4]))
    print(threeSum([0,1,1]))
    print(threeSum([0,0,0]))
    print(threeSum([-2,0,1,1,2]))
    print(threeSum([0,1,-1,-1]))
