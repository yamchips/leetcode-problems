import bisect

# find exact match, return -1 if not found
# if there are duplicates, the index is a random one
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

'''
The difference between bisect_left and bisect_right is how they deal with equal situation

In bisect_left, if a[mid] = x, h = mid

In bisect_right, if a[mid] = x, l = mid + 1
'''

if __name__=='__main__':
    print(search([1,3,3,5,7], 3))
    print(bisect.bisect_left([1,3,3,5,7], 3))
    print(bisect.bisect_right([1,3,3,5,7], 3))

    # print(search([0,1,2,3], 0))
    # print(search([0,1,2,3], 3))
    # print(search([0,1,2,3], 2))


