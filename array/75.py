def sortColors(nums: list[int]) -> None:
    red, white, blue = 0, 0, 0
    for num in nums:
        if num == 0:
            red += 1
        elif num == 1:
            white += 1
        else:
            blue +=1
    for i in range(len(nums)):
        if i < red:
            nums[i] = 0
        elif i < red + white:
            nums[i] = 1
        else:
            nums[i] = 2
            