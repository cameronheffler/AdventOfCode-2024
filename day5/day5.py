def get_input():
    file = open("input.txt", "r")
    read_rules = True

    rules = {}
    orders = []

    for line in file.readlines():
        if line == "\n":
            read_rules = False
            continue

        line = line.strip()

        if read_rules:
            if line.split("|")[0] in rules:
                rules[line.split("|")[0]].append(line.split("|")[1])
                continue

            rules[line.split("|")[0]] = [line.split("|")[1]]
            continue
        
        orders.append(line.split(","))

    file.close()

    return rules, orders


def get_correct(rules, orders):
    result = []

    for print_list in orders:
        skip = False
        i = 1

        while i < len(print_list):
            current = print_list[i]
            j = i - 1

            while j >= 0:
                behind = print_list[j]

                if current in rules and behind in rules[current]:
                    skip = True
                    break

                j -= 1

            if skip:
                break

            i += 1
        
        if skip:
            continue

        result.append(print_list)

    return result


def get_middles(correct):
    result = 0

    for sublist in correct:
        index = (len(sublist) -1 ) // 2
        result += int(sublist[index])

    return result
            


if __name__ == "__main__":
    rules, orders = get_input()
    correct = get_correct(rules, orders)

    print(f"Part 1: {get_middles(correct)}")