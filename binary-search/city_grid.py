from collections import deque

def getMinInconvenience(grid):
    # scan grid and build a queue of delivery center
    queue = deque()
    n, m = len(grid), len(grid[0])
    for r in range(n):
        for c in range(m):
            if grid[r][c] == 1:
                queue.append((r, c))

    # no delivery center
    if not queue:
        return max(n//2, m//2)

    # calculate incovenience of each slot in the grid
    dist = [[0] * m for _ in range(n)]
    directions = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
    seen = set(queue)
    while queue:
        r, c = queue.popleft()
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if (0 <= nr < n) and (0 <= nc < m) and ((nr, nc) not in seen):
                dist[nr][nc] = dist[r][c] + 1
                seen.add((nr, nc))
                queue.append((nr, nc))
    
    def canAchieve(k):
        min_r, max_r = n, -1
        min_c, max_c = m, -1
        for r in range(n):
            for c in range(m):
                if dist[r][c] > k:
                    min_r = min(min_r, r)
                    max_r = max(max_r, r)
                    min_c = min(min_c, c)
                    max_c = max(max_c, c)
        if max_r == -1:
            return True
        return (max_r - min_r <= 2*k and max_c - min_c <= 2*k)

    left = 0
    right = max(max(row) for row in dist)
    while left <= right:
        mid = (left + right) // 2
        if canAchieve(mid):
            right = mid - 1
        else:
            left = mid + 1

    return left
