def minStartValue(nums: list[int]) -> int:
    total = 0
    val = 1
    for num in nums:
        total += num
        val = max(val, 1 - total)
    return val
