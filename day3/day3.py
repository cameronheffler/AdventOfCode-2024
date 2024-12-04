import re

def get_input():
    in_string = ""
    file = open("input.txt", "r")

    for line in file:
        in_string += line

    return in_string

def decode_input(input_string):
    count = 0

    # use regex to find patterns of mul(<1-3 digit number>,<1-3 digit number>)
    # then multiply the two numbers and add to count

    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

    for match in re.finditer(pattern, input_string):
        count += int(match.group(1)) * int(match.group(2))

    return count



if __name__ == "__main__":
    memory = get_input()
    ans = decode_input(memory)

    print(f'Part 1: {ans}')