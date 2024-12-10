def get_input():
    map = open("input.txt", "r")
    mapList = []

    for line in map.readlines():
        mapList.append(list(line.strip()))

    return mapList


def print_map(map):
    for line in map:
        print("".join(line))

    print("\n")


def move_guard(map, line, guard, move, dir, last):
    if move < 0 or move >= len(map) or guard < 0 or guard >= len(line):
        line[last] = "X"
        print_map(map)
        return True

    # print(f"guard: {guard}, move: {move}")

    map[move][guard] = dir
    line[last] = "X"

    print_map(map)
    return False


def rotate_dir(dir, x, y):
    nx = x
    ny = y
    ndir = dir

    if dir == "^":
        ndir = ">"
        ny = y + 1
        nx = x + 1

        # print(f"changing x: {x}, y: {y}")

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

    while not outside:
        for i in range(len(map)):
            line = map[i]
            x = 0
            y = 0
            dir = "^"
            last = ""

            if "^" in line:
                x = line.index("^")
                y = i - 1
                dir = "^"
                last = line.index("^")

                if y >= 0 and y < len(map) and x >= 0 and x < len(line):
                    next = map[y][x]
                    
                    while next == "#":
                        dir, x, y = rotate_dir(dir, x, y)
                        next = map[y][x]

            elif ">" in line:
                x = line.index(">") + 1
                y = i
                dir = ">"
                last = line.index(">")

                if y >= 0 and y < len(map) and x >= 0 and x < len(line):
                    next = map[y][x]
                    
                    while next == "#":
                        dir, x, y = rotate_dir(dir, x, y)
                        next = map[y][x]


            elif "v" in line:
                x = line.index("v")
                y = i + 1
                dir = "v"
                last = line.index("v")

                if y >= 0 and y < len(map) and x >= 0 and x < len(line):
                    next = map[y][x]
                    
                    while next == "#":
                        dir, x, y = rotate_dir(dir, x, y)
                        next = map[y][x]

            
            elif "<" in line:
                x = line.index("<") - 1
                y = i
                dir = "<"
                last = line.index("<")

                if y >= 0 and y < len(map) and x >= 0 and x < len(line):
                    next = map[y][x]
                    
                    while next == "#":
                        dir, x, y = rotate_dir(dir, x, y)
                        next = map[y][x]


            else:
                continue

            outside = move_guard(map, line, x, y, dir, last)
            i += 1


if __name__ == "__main__":
    map = get_input()
    run_route(map)