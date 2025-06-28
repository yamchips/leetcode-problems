def maxArea(height: list[int])->int:
    res = 0
    left, right = 0, len(height) - 1
    while left < right:
        res = max(res, (right - left) * min(height[right], height[left]))
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return res

if __name__=='__main__':
    print(maxArea([1,8,6,2,5,4,8,3,7])) # expected 49
    print(maxArea([1,1])) # expected 1