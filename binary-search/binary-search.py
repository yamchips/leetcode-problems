# find exact match, return -1 if not found
def search(nums: list[int], target) -> int:
    n = len(nums)
    left, right = 0, n - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1

# find exact match if exists, otherwise return insert position
# arr.insert(1, val) means putting val at index 1 and move previous index 1 to 2
def searchInsert(nums: list[int], target) -> int:
    n = len(nums)
    left, right = 0, n - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return left


if __name__=='__main__':
    print(search([0,1,2,3], 0))
    print(search([0,1,2,3], 3))
    print(search([0,1,2,3], 2))


