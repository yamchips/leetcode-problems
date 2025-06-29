from copy import deepcopy


def permute(nums: list[int]) -> list[list[int]]:
    res = []
    backtrack(res, [], nums)
    return res

def backtrack(res: list[list[int]], temp: list[int], nums: list[int]):
    if len(temp) == len(nums):
        res.append(temp[:])
    else:
        for i in range(len(nums)):
            if nums[i] in temp:
                continue
            else:
                temp.append(nums[i])
                backtrack(res, temp, nums)
                temp.remove(nums[i])

if __name__=='__main__':
    print(permute([1,2,3]))