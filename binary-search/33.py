def search(nums: list[int], target: int) -> int:
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left  + right) // 2
        if nums[mid] == target:
            return mid

        if nums[left] <= nums[mid]:
            # left part is sorted
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            # right part is sorted
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1

if __name__=="__main__":
    print(search([4,5,6,7,0,1,2], 0)) # 4
    print(search([4,5,6,7,0,1,2], 3)) # -1
    print(search([3,1],1))
    
