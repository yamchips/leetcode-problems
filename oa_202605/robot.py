def solution(directions):
    visited = {(0, 0)}
    revisited = set()
    steps = {"N": (0, 1),
             "S": (0, -1),
             "E": (1, 0),
             "W": (-1, 0)}
    x, y = 0, 0
    for direction in directions:
        if direction in steps:
            dx, dy = steps[direction]
            x, y = x + dx, y + dy
            if (x, y) in visited:
                revisited.add((x, y))
            else:
                visited.add((x, y))
    return len(revisited)

if __name__=="__main__":
    directions = ["", "NS", "WEWNES", "SxWxNxN"]
    outputs = [solution(direction) for direction in directions]
    print(outputs) # outputs should be [0, 1, 2, 0]
    