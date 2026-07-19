import heapq

'''
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.
'''

def findKthLargest(nums: list[int], k: int) -> int:
    minHeap = nums[:k]
    heapq.heapify(minHeap)
    for i in range(k, len(nums)):
        heapq.heappushpop(minHeap, nums[i])
    return minHeap[0]

def findKthLargest(nums: list[int], k: int) -> int:
    heap = []
    for num in nums:
        if len(heap) < k:
            heapq.heappush(heap, num)
        elif num > heap[0]:
            heapq.heappushpop(heap, num)
    return heap[0]

if __name__=='__main__':
    print(findKthLargest([3,2,1,5,6,4], 2))