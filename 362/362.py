# clean in O(n), delete element in array is O(n)
# get in O(n)
class HitCounter():

    def __init__(self):
        self.hits = []
    
    def hit(self, t:int)->None:
        self.hits.append(t)
        # clean the array
        while self.hits and t - self.hits[0] > 300:
            del self.hits[0]
            # self.hits.pop(0)

    def getHits(self, t:int)->int:
        count = 0
        for i in range(len(self.hits) -1, -1, -1):
            if t - self.hits[i] < 300:
                count += 1
            else:
                break
        return count