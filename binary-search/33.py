from typing import List

'''
Use two pointers: start and end.

Calculate mid.

If nums[mid] == target, return the index directly.

Determine which half is sorted:

If nums[mid] > nums[end], left half is sorted.
Else, right half is sorted.
Check if the target lies inside the sorted half:

If yes → move towards that side.
Else → move towards the other side.
Continue until start > end.

If not found, return -1.

'''

def search(self, nums: List[int], target: int) -> int:
    n = len(nums)
    left, right = 0, n - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target: return mid
        elif nums[mid] > nums[right]:
            # left half is sorted
            if nums[left] < target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            # right half is sorted
            if nums[mid] < target < nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1