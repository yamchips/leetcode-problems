def minSubArrayLen(target: int, nums: list[int]) -> int:
    start, end = 0, 0
    sum = 0
    n = len(nums)
    minLength = n + 1
    while end < n:
        sum += nums[end]
        while sum >= target:
            minLength = min(minLength, end - start + 1)
            sum -= nums[start]
            start += 1
        end += 1
    return minLength if minLength < n + 1 else 0