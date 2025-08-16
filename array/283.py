def productExceptSelf1(nums: list[int]) -> list[int]:
    n = len(nums)
    res = [1] * n
    prod = 1
    for i in range(n):
        res[i] = prod
        prod *= nums[i] 
    prod = 1
    for i in range(n - 1, -1, -1):
        res[i] *= prod
        prod *= nums[i]
    return res

def productExceptSelf(nums: list[int]) -> list[int]:
    res = []
    n = len(nums)
    prod = 1
    for i in range(n):
        for j in range(0, i):
            prod *= nums[i]
        if i + 1 <= n - 1:
            for j in range(i + 1, n):
                prod *= nums[j]
        res.append(prod)
        prod = 1
    return res

if __name__=='__main__':
    productExceptSelf([1,2,3,4])
    print([1 for _ in range(4)])
    