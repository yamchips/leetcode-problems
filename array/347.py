from collections import Counter, defaultdict
import heapq
from typing import List


def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    # create a freq dict
    freq = defaultdict(int)
    for num in nums:
        freq[num] += 1
    # create a min heap of size k
    heap = []
    for key, value in freq.items():
        heapq.heappush(heap, (value, key))
        if len(heap) > k:
            heapq.heappop(heap)
    return [key for count, key in heap]
    # time complexity O(n + mlogk)
    # m is the number of unique numbers

def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    # create a freq dict
    freq = Counter(nums)

    # bucket sort
    buckets = [[] for _ in range(len(nums) + 1)]
    for num, count in freq.items():
        buckets[count].append(num)
    
    result = []
    for i in range(len(buckets) - 1, 0, -1):
        for num in buckets[i]:
            result.append(num)
            if len(result) == k:
                return result

    pass
