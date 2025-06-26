def trap(height: list[int]) -> int:
    n = len(height)
    leftMax = [0] * n
    rightMax = [0] * n
    # compute leftMax and rightMax for each slot
    leftMax[0] = height[0]
    for i in range(1, n):
        leftMax[i] = max(height[i], leftMax[i - 1])
    rightMax[-1] = height[-1]
    for i in range(n - 2, -1, -1):
        rightMax[i] = max(height[i], rightMax[i + 1])
    # compute water in each slot
    water = 0
    for i in range(1, n - 1):
        waterHere = min(leftMax[i], rightMax[i]) - height[i]
        water += waterHere if waterHere > 0 else 0
    return water

if __name__=='__main__':
    print(trap([0,1,0,2,1,0,1,3,2,1,2,1])) # expected 6
    print(trap([4,2,0,3,2,5])) # expected 9