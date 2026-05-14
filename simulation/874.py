# walking robot simulation

def robotSim(commands: list[int], obstacles: list[list[int]]) -> int:
    max_len = 0
    # key is (x, y, command), value is (new_x, new_y)
    change_dir = {
        (0, 1, -1): (1, 0),
        (0, 1, -2): (-1, 0),
        (1, 0, -1): (0, -1),
        (1, 0, -2): (0, 1),
        (0, -1, -1): (-1, 0),
        (0, -1, -2): (1, 0),
        (-1, 0, -1): (0, 1),
        (-1, 0, -2): (0, -1)
    }
    dir = (0, 1)
    pos = [0, 0]
    obs = set(tuple(x) for x in obstacles)

    for command in commands:
        if command <0:
            dir = change_dir[tuple([dir[0], dir[1], command])]
        else:
            for _ in range(command):
                nx, ny = pos[0] + dir[0], pos[1] + dir[1]
                if (nx, ny) in obs:
                    break
                pos[0], pos[1] = nx, ny
                max_len = max(max_len, nx ** 2 + ny ** 2)
    return max_len

# walking robot simulation

def robotSim(commands: list[int], obstacles: list[list[int]]) -> int:
    max_len = 0
    directions = [
        (0, 1),
        (1, 0),
        (0, -1),
        (-1, 0)
    ]
    direction_index = 0
    x, y = 0, 0
    obs = set(tuple(x) for x in obstacles)

    for command in commands:
        if command == -1:
            direction_index = (direction_index + 1) % 4
        elif command == -2:
            direction_index = (direction_index - 1) % 4
        else:
            dx, dy = directions[direction_index]
            for _ in range(command):
                nx, ny = x + dx, y + dy
                if (nx, ny) in obs:
                    break
                x, y = nx, ny
                max_len = max(max_len, nx ** 2 + ny ** 2)
    return max_len

if __name__=="__main__":
    commands = [4, -1 , 3]
    obstacles = []
    print(robotSim(commands, obstacles)) # 25

    commands = [4, -1, 4, -2, 4]
    obstacles = [[2,4]]
    print(robotSim(commands, obstacles)) # 65

    commands = [6, -1, -1, 6]
    obstacles = [[0, 0]]
    print(robotSim(commands, obstacles)) # 36
