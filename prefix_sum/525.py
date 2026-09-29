def findMaxLength(nums: list[int]) -> int:
    # prefix[0] = 0, prefix[i] = arr[0]+...+arr[i-1]
    prefix = 0
    # key: prefix value, value: first index that sees this value
    prefix_index = {0:0} 

    max_length = 0
    for i in range(1, len(nums)+1):
        prefix += 1 if nums[i - 1] == 1 else -1
        
        if prefix in prefix_index:
            curr_length = i - prefix_index[prefix]
            max_length = max(max_length, curr_length)
        else:
            prefix_index[prefix] = i 

    return max_length
    

if __name__=="__main__":
    print(findMaxLength([0,1]) ) # 2
    print(findMaxLength([0,1,0,1]) ) # 4 
    print(findMaxLength([0,1,1,1,1,1,0,0,0]) ) # 6