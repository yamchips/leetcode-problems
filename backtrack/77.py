def backtrack1(nums, k, res, temp, lastIndex):
    if len(temp) == k:
        res.append(temp[:])
        return
    for i in range(len(nums)):
        if i > lastIndex:
            temp.append(nums[i])
            backtrack1(nums, k, res, temp, i)
            temp.pop()


def combine1(n: int, k: int) -> list[list[int]]:
    res = []
    nums = [i for i in range(1, n + 1)]
    backtrack1(nums, k, res, [], -1)
    return res

def backtrack(start, res, temp, n, k):
    if len(temp) == k:
        res.append(temp[:])
    for num in range(start, n + 1):
        temp.append(num)
        backtrack(num + 1, res, temp, n, k)
        temp.pop()

def combine(n: int, k: int) -> list[list[int]]:
    res, temp = [], []
    backtrack(1, res, temp, n, k)
    return res

if __name__=='__main__':
    print(combine(4, 2))