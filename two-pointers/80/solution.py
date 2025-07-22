def removeDuplicates(nums: list[int]) -> int:
    if len(nums) < 3: return len(nums)
    slow = 2
    for fast in range(2, len(nums)):
        if (nums[fast] != nums[slow - 2]):
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1

    return slow
    



