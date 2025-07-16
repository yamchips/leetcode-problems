import heapq

# brutal force, O(m * n * logk)
def kSmallestPairs1(nums1: list[int], nums2: list[int], k: int) -> list[list[int]]:
    maxheap = []
    for u in nums1:
        for v in nums2:
            if len(maxheap) < k:
                heapq.heappush(maxheap, (-(u+v), [u, v]))
            else:
                heapq.heappushpop(maxheap, (-(u+v), [u, v]))
    res = []
    while maxheap:
        res.append(heapq.heappop(maxheap)[1])
    return res

# imagine we have a matrix, add first k-th row and explore the top left part
# O(k * logk)
def kSmallestPairs(nums1: list[int], nums2: list[int], k: int) -> list[list[int]]:
    minheap = []
    res = []
    for i in range(min(k, len(nums1))):
        heapq.heappush(minheap, (nums1[i] + nums2[0], i, 0))
    while len(res) < k:
        _, i, j = heapq.heappop(minheap)
        res.append([nums1[i], nums2[j]])
        if j + 1 < len(nums2):
            heapq.heappush(minheap, (nums1[i] + nums2[j + 1], i, j + 1))

    return res