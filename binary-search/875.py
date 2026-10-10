import math

def minEatingSpeed(piles: list[int], h: int) -> int:
    right = max(piles)
    left = 1

    def finishTime(k):
        total = 0
        for pile in piles:
            total += math.ceil(pile / k)
        return total

    while left <= right:
        mid = (left + right) // 2
        time = finishTime(mid)
        if time <= h:
            right = mid - 1
        elif time > h:
            left = mid + 1
    return left

if __name__=="__main__":
    print(minEatingSpeed([3,6,7,11],8))