from collections import deque

'''
HackerRank Red Knight's Shortest Path

Start node and end node is guaranteed to be different.
Important Notice: (0,0) is on the top left

We can use len(path) to get the total steps, so we don't need to count BFS levels.
We then can delete the size = len(queue) and for _ in range(size) part.
'''

def printShortestPath(n, i_start, j_start, i_end, j_end):
    directions = [(-2,-1),(-2,1),(0,2),(2,1),(2,-1),(0,-2)]
    moves = ['UL','UR','R','LR','LL','L']
    queue = deque([(i_start, j_start)])
    seen = {(i_start, j_start)}

    # each cell stores (i_parent, j_parent, move)
    board = [[None for _ in range(n)] for _ in range(n)] 
    board[i_start][j_start] = (-1, -1, 'Start')
    
    def find_path():
        path = []
        x, y = i_end, j_end
        while x != -1 and y != -1:
            x_parent, y_parent, move = board[x][y]
            path.append(move)
            x = x_parent
            y = y_parent
        path.reverse()
        return path[1:]
    
    while queue:
        x, y = queue.popleft()
        for (dx, dy), move in zip(directions, moves):
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n:
                if (nx, ny) in seen:
                    continue
                board[nx][ny] = (x, y, move)
                if nx == i_end and ny == j_end:
                    # find end 
                    path = find_path()
                    print(len(path))
                    print(' '.join(path))
                    return
                queue.append((nx, ny))
                seen.add((nx, ny))
    print("Impossible")


'''
Simplify the reachable check

row_diff should always be even, which means 2 * n
col_diff could be odd or even
if n is odd, then col_diff should be odd
if n is even, then col_diff should be even
'''
def check_reachable(i_start, j_start, i_end, j_end):
    # check whether the destination is reachable
    reachable = False
    row_diff = abs(i_end - i_start)
    col_diff = abs(j_start - j_end)
    if row_diff % 2 == 0 and (col_diff % 2 == (row_diff // 2) % 2):
        reachable = True
    if not reachable:
        print("Impossible")
        return
    

'''
Original solution. Correct. But reachable check can be simplified

time complexity: O(n**2)

space complexity: O(n**2)

In the worst case it may explore a number of positions proportional to the size of the board. There are n² positions, and each checks six moves, so BFS takes O(n²) time. Also, creating the n × n parent board takes O(n²) time and space by itself. The queue and visited set can also contain up to O(n²) positions.
'''
def printShortestPath(n, i_start, j_start, i_end, j_end):

    # check whether the destination is reachable
    reachable = False
    if i_start == i_end and abs(j_start - j_end) % 2 == 0:
        reachable = True
    if j_start == j_end and abs(i_end - i_start) % 4 == 0:
        reachable = True
    if i_start != i_end and j_end != j_start:
        if (abs(i_end - i_start) % 4 == 0 and abs(j_start - j_end) % 2 == 0)\
            or (abs(i_end - i_start) % 4 == 2 and abs(j_start - j_end) % 2 == 1):
            reachable = True
    if not reachable:
        print("Impossible")
        return
    # When it's reachable
    directions = [(-2,-1),(-2,1),(0,2),(2,1),(2,-1),(0,-2)]
    moves = ['UL','UR','R','LR','LL','L']
    queue = deque([(i_start, j_start)])
    steps = 0
    seen = set([(i_start, j_start)])
    board = [[None for _ in range(n)] for _ in range(n)] # each slot store (i_parent, j_parent, move)
    board[i_start][j_start] = (-1, -1, 'Start')
    
    def find_path():
        path = []
        x, y = i_end, j_end
        move = ''
        while x != -1 and y != -1:
            x_parent, y_parent, move = board[x][y]
            path.append(move)
            x = x_parent
            y = y_parent
        path.reverse()
        return path[1:]
    
    while queue:
        size = len(queue)
        steps += 1
        for _ in range(size):
            x, y = queue.popleft()
            for i in range(6):
                nx, ny = x + directions[i][0], y + directions[i][1]
                if 0 <= nx < n and 0 <= ny < n:
                    if (nx, ny) in seen:
                        continue
                    board[nx][ny] = (x, y, moves[i])
                    if nx == i_end and ny == j_end:
                        print(steps) # find end 
                        path = find_path()
                        print(' '.join(path))
                    queue.append((nx, ny))
                    seen.add((nx, ny))
                    
    

if __name__ == '__main__':
    print(printShortestPath(5, 4, 1, 0, 3)) # 2 UR UR