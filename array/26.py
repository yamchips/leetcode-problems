# Remove duplicates from sorted array

def removeDuplicates(nums: list[int]) -> int:
    if len(nums) == 1:
        return 1
    left, right = 0, 1
    for right in range(1, len(nums)):
        if nums[right] > nums[left]:
            nums[left + 1] = nums[right]
            left += 1
    return left + 1