from collections import deque

def maxSlidingWindow(nums: list[int], k: int) -> list[int]:
    result = []
    # store the index
    # nums[window[0]] > nums[window[1]] > ...
    window = deque() 
    for i in range(len(nums)):
        if window and i - k + 1 > window[0]:
            # window size exceeds limit
            window.popleft()
        
        while window and nums[window[-1]] <= nums[i]:
            window.pop()
        window.append(i)

        if i >= k - 1:
            result.append(nums[window[0]])

    return result
    

if __name__=="__main__":
    print(maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3) == [3,3,5,5,6,7])