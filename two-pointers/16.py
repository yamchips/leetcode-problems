def threeSumClosest(nums: list[int], target: int) -> int:
    nums.sort()
    diff = 20001
    res = 0
    for i in range(len(nums) - 2):

        if i - 1 >= 0 and nums[i] == nums[i - 1]:
            continue
        j = i + 1
        k = len(nums) - 1
        while j < k:
            
            sum = nums[i] + nums[j] + nums[k]
            curr_diff = abs(sum - target)

            if curr_diff == 0:
                return sum
        
            if j < k and sum > target:
                k -= 1
                
            if j < k and sum < target:
                j += 1
                

            if curr_diff < diff:
                diff = curr_diff
                res = sum

    return res

if __name__=='__main__':
    print(threeSumClosest([10,20,30,40,50,60,70,80,90], 1))