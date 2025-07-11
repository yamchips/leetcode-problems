from collections import deque

# Leetcode 2593
def findScore(nums):
    index_arr = list(enumerate(nums))
    sorted_arr = sorted(index_arr, key = lambda x : x[1])
    print(sorted_arr)
    reached = [False] * len(nums)
    score = 0
    for item in sorted_arr:
        index = item[0]
        value = item[1]
        if not reached[index]:
            reached[index] = True
            if index + 1 < len(nums):
                reached[index + 1] = True
            if index - 1 >= 0:
                reached[index - 1] = True
            score += value
    return score



input = [10,44,10,8,48,30,17,38,41,27,16,33,45,45,34,30,22,3,42,42]

print(findScore(input))
