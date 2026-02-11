from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    # create the map
    map = {}
    for i in range(len(nums)):
        map[i] = nums[i]
    # iterate and find the solution
    res = []
    for i in range(len(nums)):
        if target - nums[i] in map.values():
            for key in map.keys():
                if key != i and map[key] == target - nums[i]:
                    res.append(key)
                    res.append(i)
            if res:
                return res

def twoSum(nums: List[int], target: int) -> List[int]:
    # create the map, key is element, value is index
    # seen = {}
    # for i in range(len(nums)):
    #     seen[nums[i]] = i
    seen = {num : i for i , num in enumerate(nums)}
    # iterate and find the solution
    for index, num in enumerate(nums):
        if target - num in seen and seen[target - num] != index:
            return [index, seen[target - num]]
        
def twoSum(nums: List[int], target: int) -> List[int]:
    seen = {}
    for index, num in enumerate(nums):
        if target - num in seen:
            return [index, seen[target - num]]
        seen[num] = index