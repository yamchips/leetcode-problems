import heapq


def findKthLargest(nums: list[int], k: int) -> int:
    minHeap = nums[:k]
    heapq.heapify(minHeap)
    for i in range(k, len(nums)):
        heapq.heappushpop(minHeap, nums[i])
    return heapq.heappop(minHeap)

if __name__=='__main__':
    print(findKthLargest([3,2,1,5,6,4], 2))