def minSubArrayLen(target: int, nums: list[int]) -> int:
    minLength = float('inf')
    left = 0
    total = 0
    for right in range(len(nums)):
        total += nums[right]
        while total >= target:
            minLength = min(minLength, right - left + 1)
            total -= nums[left]
            left += 1
    return 0 if minLength == float('inf') else minLength