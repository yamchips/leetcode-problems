from collections import deque

# cleaning in O(1)
# get in O(n)
class HitCounter():
    def __init__(self):
        self.hits = deque()
    
    def hit(self, t:int) -> None:
        self.hits.append(t)
        # clean the deque
        while t - self.hits[0] >= 300:
            self.hits.popleft()
        

    def getHits(self, t:int) -> int:
        count = 0
        for i in range(len(self.hits) - 1, -1, -1):
            if t - self.hits[i] < 300:
                count += 1
        return count