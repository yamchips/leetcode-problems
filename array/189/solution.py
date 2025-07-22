# O(n) space complexity
def rotate1(nums: list[int], k:int) -> None:
    n = len(nums)
    steps = k % n
    temp = [0] * n
    for i in range(n - steps):
        temp[i + steps] = nums[i]
    for j in range(n - steps, n):
        temp[j - (n - steps)] = nums[j]
    nums[:] = temp


def rotate2(nums: list[int], k:int) -> None:
    n = len(nums)
    steps = k % n
    count = 0
    for start in range(n):
        if (count >= n): break
        current = start
        prev = nums[start]
        while True:
            newIndex = (current + steps) % n
            nums[newIndex], prev = prev, nums[newIndex]
            current = newIndex
            count += 1
            if current == start:
                break

def rotate3(nums: list[int], k:int) -> None:
    n = len(nums)
    steps = k % n
    def reverse(array: list[int], left:int, right:int) -> None:
        while left < right:
            array[left], array[right] = array[right], array[left]
            left += 1
            right -= 1
    reverse(nums, 0, n - 1)
    reverse(nums, 0, steps - 1)
    reverse(nums, steps, n - 1)


    
  
    



