def combinationSum2(candidates: list[int], target: int) -> list[list[int]]:
    temp = []
    res = []
    backtrack(candidates, target, temp, res, 0)
    return res

def backtrack(candidates: list[int], target: int, temp: list[int], res: list[list[int]], index: int) -> None:
    if target == 0:
        res.append(temp[:])
        return
    if target < 0:
        return
    for i in range(index, len(candidates)):
        temp.append(candidates[i])
        backtrack(candidates, target - candidates[i], temp, res, i)
        temp.pop()