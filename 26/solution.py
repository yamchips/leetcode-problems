def removeDuplicates(nums: list[int]) -> int:
    slow, fast = 0, 0
    while fast < len(nums):
        while not (nums[fast] > nums[slow]):
            fast += 1
            if fast == len(nums):
                return slow + 1
        if fast - slow == 1: 
            slow = fast
            continue
        slow += 1
        nums[slow], nums[fast] = nums[fast], nums[slow]
    return slow + 1