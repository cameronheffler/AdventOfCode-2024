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
    wrong = []

    for print_list in orders:
        skip = False
        i = 1

        while i < len(print_list):
            current = print_list[i]
            j = i - 1

            while j >= 0:
                behind = print_list[j]

                if current in rules and behind in rules[current]:
                    wrong.append(print_list)
                    skip = True
                    break

                j -= 1

            if skip:
                break

            i += 1
        
        if skip:
            continue

        result.append(print_list)

    return result, wrong


def get_middles(correct):
    result = 0

    for sublist in correct:
        index = (len(sublist) -1 ) // 2
        result += int(sublist[index])

    return result


def move_element(lst, old_index, new_index):
    element = lst.pop(old_index)
    lst.insert(new_index, element)



def fix(wrong):
    result = []
    restart = False

    for sublist in wrong:

        times = 0 

        while times < len(sublist):
            i = 1

            while i < len(sublist):
                current = sublist[i]
                j = i - 1

                while j >= 0:
                    behind = sublist[j]

                    if current in rules and behind in rules[current]:
                        move_element(sublist, j, i)
                        restart = True

                    if restart:
                        break


                    j -= 1

                i += 1

            times += 1

        result.append(sublist)

    return result
            


if __name__ == "__main__":
    rules, orders = get_input()
    correct, wrong = get_correct(rules, orders)

    print(f"Part 1: {get_middles(correct)}")

    fixed = fix(wrong)

    print(f"Part 2: {get_middles(fixed)}")