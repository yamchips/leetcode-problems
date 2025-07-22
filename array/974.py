from collections import defaultdict

# O(n^2) time complexity
def subarrayDivByK1(nums:list[int], k:int) -> int:
    n = len(nums)
    summation = [0 for _ in range(n)]
    count = 0
    for start in range(n):
        for i in range(start, n):
            if i == start: 
                summation[i] = nums[i]
            else:
                summation[i] = summation[i - 1] + nums[i]
            if summation[i] % k == 0:
                count += 1
    return count

def subarrayDivByK(nums:list[int], k:int) -> int:
    remainderMap = defaultdict(int)
    remainderMap[0] = 1
    prefixSum = 0
    count = 0
    for num in nums:
        prefixSum += num
        mod = prefixSum % k
        count += remainderMap[mod]
        remainderMap[mod] += 1
    return count

    

if __name__=='__main__':
    print(subarrayDivByK([4,5,0,-2,-3,1], 5))
    print(subarrayDivByK([2], 9))
    print(subarrayDivByK([9], 9))
