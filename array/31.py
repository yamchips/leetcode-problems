# Next permutation

def nextPermutation(nums: list[int]) -> None:
    n = len(nums)
    # find the break point
    index = -1
    for i in range(n - 2, -1, -1):
        if nums[i] < nums[i + 1]:
            index = i
            break
    # if the array is in decreasing order
    if index == -1:
        return nums.reverse()
    # if the array is not in decreasing order
    # in [index + 1, n - 1], find smallest element > nums[index]
    targetIndex, val = n, 101
    for i in range(index + 1, n):
        if nums[i] > nums[index] and nums[i] <= val:
            val = nums[i]
            targetIndex = i
    nums[index], nums[targetIndex] = nums[targetIndex], nums[index]
    nums[index + 1:] = reversed(nums[index + 1:])
    print(nums)
    
if __name__=='__main__':
    nextPermutation([2,3,1,3,3])
    nextPermutation([1,3,2])
