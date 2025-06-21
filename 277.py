def knows(a, b) -> bool:
    return True

# O(n^2)
def findCelebrity(n: int) -> int:
    for start in range(n):
        flag = True
        for end in range(n):
            if start != end and knows(start, end):
                flag = False
                break
        if flag: # found one line's sum is 1
            break
    # start is the possible person
    for i in range(n):
        if i == start:
            continue
        if not knows(i, start):
            return -1
    return start

def findCelebrity(n: int) -> int:
    candidate = 0
    for i in range(1, n):
        if knows(candidate, i):
            candidate = i
    # now we find the candidate who doesn't know anyone after him/her
    # next we check whether:
    # 1. candidate knows 0 to candidate-1
    # 2. every one knows candidate
    for i in range(0, n):
        if i == candidate:
            continue
        if knows(candidate, i) or not knows(i, candidate):
            return -1
    return candidate