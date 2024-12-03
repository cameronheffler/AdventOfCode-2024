def increasing(numbers):
    return all(numbers[i] < numbers[i + 1] for i in range(len(numbers) - 1))


def decreasing(numbers):
    return all(numbers[i] > numbers[i + 1] for i in range(len(numbers) - 1))


def is_safe(intList):
    if not increasing(intList) and not decreasing(intList):
        return False

    safe = True
    
    for i in range(len(intList) - 1):
        diff = abs(intList[i] - intList[i + 1])

        if diff > 3 or diff < 1:
            safe = False
            break
    
    return safe


def red_nosed_reactor():
    file = open("input.txt", "r")
    lines = file.readlines()

    count = 0

    for line in lines:
        chars = []

        for i in line.split(" "):
            chars.append(i)

        intList = list(map(int, chars))
        safe = is_safe(intList)

        if safe:
            count += 1

        else:
            for i in range(len(intList) - 1):
                # newList = intList[:intList[i]] + intList[intList[i] + 1:]
                nlist = [x for y, x in enumerate(intList) if y != i]
                # print(nlist)

                if is_safe(nlist):
                    count += 1
                    break


    return count


if __name__ == "__main__":
    print(f'Part 1: {red_nosed_reactor()}')