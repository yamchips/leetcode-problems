def combinationSum(candidates: list[int], target: int) -> list[list[int]]:
    res = []
    backtrack(candidates, res, [], target, 0)
    return res

def backtrack(candidates: list[int], res:list[list[int]], temp: list[int], target: int, index: int):
    if target == 0:
        res.append(temp[:])
        return 
    if target < 0:
        return
    for i in range(index, len(candidates)):
        temp.append(candidates[i])
        backtrack(candidates, res, temp, target - candidates[i], i)
        temp.pop()

if __name__=='__main__':
    print(combinationSum([2,3,6,7], 7))
    print(combinationSum([2,3,5], 8))
    print(combinationSum([2,3,6,7], 1))
