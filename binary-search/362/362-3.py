from collections import deque

# get in O(log n) using binary search
class HitCounter():
    def __init__(self):
        self.hits = []
    
    def hit(self, t:int) -> None:
        self.hits.append(t)
        # clean the list
        while t - self.hits[0] >= 300:
            self.hits.pop(0)

    def getHits(self, t:int) -> int:
        target = t - 300 + 1
        # find the number of elements >= target
        left, right = 0, len(self.hits) - 1
        while left < right:
            mid = (left + right) // 2
            if self.hits[mid] < target:
                left = mid + 1
            else:
                right = mid
        # left is the index of first occurrence of element >= target
        return len(self.hits) - left