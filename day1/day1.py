def getLists():
    left = []
    right = []

    file = open("input.txt", "r")
    lines = file.readlines()

    for line in lines:
        splits = line.split("   ")

        left.append(int(splits[0]))
        right.append(int(splits[1]))

    left.sort()
    right.sort()

    return left, right


def sumDistances(left, right):
    count = 0

    for i in range(len(left)):
        count += abs(left[i] - right[i])

    return count


if __name__ == '__main__':
    lList, rList = getLists()
    distances = sumDistances(lList, rList)

    print(f"Part 1: {distances}")