def searchRange(nums: list[int], target: int) -> list[int]:
    def searchHelper(arr, direction):
        result = -1
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] < target:
                left = mid + 1
            elif arr[mid] > target:
                right = mid - 1
            else:
                result = mid
                if direction == "left":
                    right = mid - 1
                elif direction == "right":
                    left = mid + 1
        return result
    leftIndex = searchHelper(nums, "left")
    rightIndex = searchHelper(nums, "right")
    return [leftIndex, rightIndex]

    
    

