def subsets(nums:list[int]) -> list[list[int]]:
    res = [[]]
    for num in nums:
        size = len(res)
        for i in range(size):
            curr = res[i][:]
            curr.append(num)
            res.append(curr)
            
    return res
    

if __name__=='__main__':
    print(subsets([1,2,3]))
    print(subsets([0]))