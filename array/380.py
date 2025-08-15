# Insert Delete GetRandom O(1)

import random

class RandomizedSet:

    def __init__(self):
        self.arr = []
        self.indexMap = {}

    def insert(self, val: int) -> bool:
        if val in self.indexMap:
            return False
        self.arr.append(val)
        self.indexMap[val] = len(self.arr) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.indexMap:
            return False
        index = self.indexMap[val]
        lastIndex = len(self.arr) - 1
        if index != lastIndex:
            self.arr[index], self.arr[lastIndex] = self.arr[lastIndex], self.arr[index] 
            self.indexMap[self.arr[index]] = index
        self.arr.pop()
        del self.indexMap[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.arr)

