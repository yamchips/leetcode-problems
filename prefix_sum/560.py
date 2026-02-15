from typing import List


def subarraySum(nums: List[int], k: int) -> int:
    result = 0
    sumFreq = {0:1}
    total = 0
    for num in nums:
        total += num
        if total - k in sumFreq:
            result += sumFreq[total - k]
        sumFreq[total] = sumFreq.get(total, 0) + 1
    print(sumFreq)
    return result

if __name__=='__main__':
    print(subarraySum([1,1,1],2))
    print(subarraySum([-1,1,0],0))
    print(subarraySum([1,2,3],3))