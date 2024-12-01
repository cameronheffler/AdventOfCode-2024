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

if __name__ == '__main__':
    lList, rList = getLists()
    print(lList, rList)