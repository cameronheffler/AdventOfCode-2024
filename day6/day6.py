def get_input():
    map = open("input.txt", "r")
    mapList = []

    for line in map.readlines():
        mapList.append(list(line.strip()))

    return mapList


def get_start(map):
    for i in range(len(map)):
        for j in range(len(map)):
            if map[i][j] == "^":
                return j, i


def print_map(map):
    for line in map:
        print("".join(line))

    print("\n")


def move_guard(map, guard, move, dir, last):
    map[last[1]][last[0]] = "X"

    if move < 0 or move >= len(map) or guard < 0 or guard >= len(map):
        return True

    map[move][guard] = dir
    return False


def rotate_dir(dir, x, y):
    nx = x
    ny = y
    ndir = dir

    if dir == "^":
        ndir = ">"
        ny = y + 1
        nx = x + 1

    if dir == ">":
        ndir = "v"
        ny = y + 1
        nx = x - 1

    if dir == "v":
        ndir = "<"
        ny = y - 1
        nx = x - 1

    if dir == "<":
        ndir = "^"
        ny = y - 1
        nx = x + 1

    return ndir, nx, ny

def run_route(map):
    outside = False
    
    visited = set()

    x, y = get_start(map)
    line = map[y]
    dir = map[y][x]

    while not outside:
        last = (x, y)

        if dir == "^":
            y = y - 1

        elif dir == ">":
            x = x + 1

        elif dir == "v":
            y = y + 1

        elif dir == "<":
            x = x - 1

        if y >= 0 and y < len(map) and x >= 0 and x < len(line):
            position = (last[0], last[1], dir)

            if position in visited:
                return True

            visited.add(position)

            next = map[y][x]
                
            while next == "#" or next == "O":
                dir, x, y = rotate_dir(dir, x, y)
                next = map[y][x]

        outside = move_guard(map, x, y, dir, last)

    return False


def count(map):
    count = 0
    positions = []

    for y in range(len(map)):
        for x in range(len(map)):
            if map[y][x] == "X":
                positions.append((y, x))
                count += 1

    return count, positions


def obstacles(spots):
    count = 0
    first_map = get_input()
    # timer = 0
    sx, sy = get_start(first_map)

    base_map = [row.copy() for row in first_map]
    spots = list(set(spots))


    for spot in spots:
        # print(timer)

        map = [row.copy() for row in base_map]
        y, x = spot

        if (y, x) == (sy, sx):
            continue

        if map[y][x] == "#" or map[y][x] == "^":
            continue

        map[y][x] = "O"
        loop = run_route(map)

        if loop:
            count += 1

        # timer += 1

    return count


if __name__ == "__main__": 
    map = get_input()
    run_route(map)
    num, path = count(map)

    print(f"Part 1: {num}")

    print(f"Part 2: {obstacles(path)}")