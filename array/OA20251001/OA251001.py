'''
OA problem 2
'''

def minLength(systemState, dist):
    n = len(systemState)
    INF = float('inf')
    right, left = [INF] * n, [INF] * n

    lastOnDist = -1
    for i in range(n - 1, -1, -1):
        if systemState[i] == 1:
            lastOnDist = dist[i]
        elif lastOnDist != -1:
            right[i] = lastOnDist - dist[i]
            lastOnDist = dist[i]

    lastOnDist = -1
    for i in range(n):
        if systemState[i] == 1:
            lastOnDist = dist[i]
        elif lastOnDist != -1: 
            left[i] = dist[i] - lastOnDist
            lastOnDist = dist[i]

    total = 0
    for i in range(n):
        if systemState[i] == 0:
            total += min(left[i], right[i])

    return total

if __name__=="__main__":
    print(minLength([0,1,0,0,1,1,0,0],[3,5,10,12,13,23,30,38]))
    print(minLength([1,0,1,1,0,1,1], [1,5,6,7,8,9,17]))
    