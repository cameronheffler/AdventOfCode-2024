import re

def get_input():
    all_lines = []
    file = open("input.txt", "r")

    for line in file:
        all_lines.append(line.strip())

    file.close()
    return all_lines


def diagonal_right(all_lines):
    diagonals = []
    j = 0

    while j < len(all_lines[0]):
        singular = ""
        singular += all_lines[0][j]

        i = j + 1
        y = 1

        while i < len(all_lines[0]):
            singular += all_lines[y][i]
            i += 1
            y += 1

        if len(singular) >= 4:
            diagonals.append(singular)

        j += 1

    j = 0

    j = int(len(all_lines) -2)
    firstindex = int(len(all_lines) -1)

    while j >= 0:

        singular = ""
        singular += all_lines[firstindex][j]

        i = j - 1
        index = firstindex - 1

        while i >= 0:
            singular += all_lines[index][i]
            i -= 1
            index -= 1

        if len(singular) >= 4:
            diagonals.append(singular)

        j -= 1

    return diagonals


def diagonal_left(all_lines):
    diagonals = []
    j = len(all_lines[0]) - 1

    while j >= 0:
        singular = ""
        singular += all_lines[0][j]

        i = j - 1
        y = 1

        while i >= 0:
            singular += all_lines[y][i]
            i -= 1
            y += 1

        if len(singular) >= 4:
            diagonals.append(singular)

        j -= 1

    j = 1
    firstindex = int(len(all_lines) - 1)

    while j < int(len(all_lines)):

        singular = ""
        singular += all_lines[firstindex][j]

        i = j + 1
        index = firstindex -  1

        while i < len(all_lines):
            # print(f'line[{index}][{i}]')
            singular += all_lines[index][i]
            i += 1
            index -= 1

        if len(singular) >= 4:
            diagonals.append(singular)

        j += 1

    return diagonals


def down(all_lines):
    lines = []
    j = 0

    while j < len(all_lines[0]):
        singular = ""

        for line in all_lines:
            singular += line[j]
        
        lines.append(singular)

        j += 1

    return lines


def x_mas(all_lines):
    count = 0
    row = 0

    while row < (len(all_lines) - 2):
        i = 0

        while i < len(all_lines[0]):
            x = row
            y = i

            one = all_lines[x][y]

            if one not in ('S', 'M'):
                i += 1  # Increment here to avoid infinite loop
                continue

            x += 1
            y += 1

            if x >= len(all_lines) or y >= len(all_lines[0]) or x < 0 or y < 0:
                i += 1
                continue

            two = all_lines[x][y]

            if two != 'A':
                i += 1
                continue

            x += 1
            y += 1

            if x >= len(all_lines) or y >= len(all_lines[0]) or x < 0 or y < 0:
                i += 1
                continue

            three = all_lines[x][y]

            if three not in ('S', 'M') or three == one:
                i += 1
                continue

            x -= 2

            if x >= len(all_lines) or x < 0:
                i += 1
                continue

            four = all_lines[x][y]

            if four not in ('S', 'M'):
                i += 1
                continue

            x += 2
            y -= 2

            if x >= len(all_lines) or y >= len(all_lines[0]) or x < 0 or y < 0:
                i += 1
                continue

            five = all_lines[x][y]

            if five not in ('S', 'M') or five == four:
                i += 1
                continue

            count += 1
            i += 1  # Ensure i increments after a successful match

        row += 1

    return count



def count(all_lines):
    count = 0
    match = r"(?=(XMAS|SAMX))"  # Lookahead to allow overlaps

    # Assuming these functions return lists of strings for different patterns
    check = [all_lines, diagonal_left(all_lines), diagonal_right(all_lines), down(all_lines)]

    for pattern in check:
        for line in pattern:
            # print(line)  # Debug: print the line being processed
            count += sum(1 for _ in re.finditer(match, line))  # Count overlapping matches
            # print(sum(1 for _ in re.finditer(match, line)))  # Debug: print count of matches

    return count




if __name__ == "__main__":
    print(f"Part 1: {count(get_input())}")
    print(f"Part 2: {x_mas(get_input())}")