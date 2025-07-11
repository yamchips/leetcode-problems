# O(nlogn) time and O(n) space
def findMinArrowShots1(points: list[list[int]]) -> int:
    # sort the array by end
    points.sort(key = lambda x : x[1])
    n = len(points)
    # dp[i]: (min, pos) means the min number of arrows when there are i+1 intervals, and pos is the position of the rightmost arrow
    dp = [(0,0)] * n 
    # first arrow is the rightmost position of the interval
    dp[0] = (1, points[0][1])
    for i in range(1, n):
        start, end = points[i]
        if start > dp[i - 1][1]: 
            # no overlapping, add an arrow at rightmost position
            dp[i] = (dp[i - 1][0] + 1, end)
        else:
            # if there is overlapping, no need for an arrow
            dp[i] = dp[i - 1]
    return dp[-1][0]

# O(nlogn) time and O(1) space
def findMinArrowShots(points: list[list[int]]) -> int:
    # sort the array by end
    points.sort(key = lambda x : x[1])
    n = len(points)
    minShots, latestArrow = 1, points[0][1]
    for i in range(1, n):
        start, end = points[i]
        if start > latestArrow: 
            # no overlapping, add an arrow, update latest arrow
            minShots += 1
            latestArrow = end
    return minShots

if __name__=='__main__':
    print(findMinArrowShots([[10,16],[2,8],[1,6],[7,12]]))
    print(findMinArrowShots([[1,2],[3,4],[5,6],[7,8]]))
    print(findMinArrowShots([[1,2],[2,3],[3,4],[4,5]]))