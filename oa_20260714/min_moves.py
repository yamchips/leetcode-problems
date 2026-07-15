'''
Given a string S representing a sequence of N arrows. Each arrow points in one 
of the four directions: up, down, left, right. In one move, we can rotate an 
arrow anti-clockwise. For example, up arrow to left arrow. 

^ < v >

Write a function, given the string S, return the min number of movements
required to make all of the arrows point in the same direction.
'''

'''
This method is correct, but not scalable. If we have 100 states, we need to 
calculate 100 results, each formula involves other 99 states.
'''
def solution(S: str) -> int:
    # build the freq map
    freq = {"^": 0,
        "<": 0,
        "v": 0,
        ">": 0,}
    for char in S:
        freq[char] += 1
    # calculate four options: all up, all down, all left, all right
    all_up_steps = (
        freq["<"] * 3
        + freq["v"] * 2
        + freq[">"] * 1
    )

    all_left_steps = (
        freq["^"] * 1
        + freq["v"] * 3
        + freq[">"] * 2
    )

    all_down_steps = (
        freq["^"] * 2
        + freq["<"] * 1
        + freq[">"] * 3
    )

    all_right_steps = (
        freq["^"] * 3
        + freq["<"] * 2
        + freq["v"] * 1
    )
    return min(all_down_steps, all_right_steps, all_left_steps, all_up_steps)

'''
This solution combines freq map with modulo

The tricky part is (target - current + 4) % 4
Here is how we come up with it:
    If target is larger than current, steps are (target - current)
    If target is less than current, (target - current) is negative
    We can make it positive by adding 4, which is the length of states to it
    After that, first condition is not right, so we modulo the length of states

'''
def solution(S: str) -> int:
    position = {"^":0, "<":1, "v":2, ">":3}
    freq = {"^":0, "<":0, "v":0, ">":0}
    # get freq map
    for char in S:
        freq[char] += 1
    min_moves = float('inf')
    for target in range(4):
        moves = 0

        for state, count in freq.items():
            current = position[state]
            steps = (target - current + 4) % 4
            moves += steps * count
        
        min_moves = min(min_moves, moves)
    return min_moves

if __name__=="__main__":
    print(solution("^vv<")) # 3
    print(solution("vv>>vv")) # 4
    print(solution("<<<")) # 0

