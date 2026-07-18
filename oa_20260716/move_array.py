'''
Given an array of length n. Its element are integers from 1 to n. 

We call this action as move it 1 step:
origin array [1,5,4,3,2]
move one step
result array [2,1,5,4,3]

So, for an array of length n, moving n steps makes it back to its original state.

Now find the number of steps that makes this array a decreasing array. If it cannot be changed into a decreasing array, return -1.
For example:
[1,5,4,3,2] moves 4 steps and become [5,4,3,2,1], return 4.
[1,4,5,3,2] cannot be changed into a decreasing array, return -1.
'''

'''
First, we simulate the process to get the desired step.
Time complexity: O(n ** 2)
Space complexity: O(n)
'''
def move_array(arr):
    n = len(arr)
    target = [n - i for i in range(n)]
    for step in range(n):
        temp_arr = arr[n - step:] + arr[:n - step]
        if temp_arr == target:
            return step
    return -1

'''
Find the element n, and check from it to the end, whether it's decreasing. and from start to it, whether it's decreasing. if so, we can get the right step.
Time: O(n)
Space: O(n)

This solution is not correct.
For example, [4,3,5,2,1] returns 3, but actually it should return -1.
Also, [5,4,3,2,1] returns 5, expected 0.
''' 
def is_decreasing(arr: list):
    return all(a > b for a, b in zip(arr, arr[1:]))

def move_array(arr: list):
    n = len(arr)
    position = arr.index(n)
    if is_decreasing(arr[:position]) and is_decreasing(arr[position:]):
        return n - position
    return -1

'''
Use modulo to calcuate all elements.
'''
def move_array(arr:list):
    n = len(arr)
    position = arr.index(n)
    for i in range(n - 1):
        current = arr[(position + i) % n]
        next = arr[(position + i + 1) % n]
        if current <= next:
            return -1
    return (n - position) % n

if __name__=="__main__":
    print(move_array([1,5,4,3,2])) # 4
    print(move_array([1,4,5,3,2])) # -1