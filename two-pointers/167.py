def twoSum1(numbers: list[int], target: int) -> list[int]:
    result = []
    for i, num in enumerate(numbers):
        num2 = target - num
        # binary search in numbers[i + 1, n], return the index
        index = search(numbers, i + 1, num2)
        if index > 0:
            result = [i + 1, index + 1]
            break
    return result

def search(numbers, start, num):
    n = len(numbers)
    left, right = start, n - 1
    while left <= right:
        mid = (left + right) // 2
        if numbers[mid] == num:
            return mid
        elif numbers[mid] < num:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def twoSum(numbers: list[int], target: int) -> list[int]:
    left, right = 0, len(numbers) - 1
    while left < right:
        sum = numbers[left] + numbers[right]
        if sum == target:
            return [left + 1, right + 1]
        elif sum < target:
            left += 1
        else:
            right -= 1
    return []

if __name__=='__main__':
    print(twoSum([2,7,11,15], 9) )
    print(twoSum([2,3,4], 6) )
    print(twoSum([-1,0], -1) )