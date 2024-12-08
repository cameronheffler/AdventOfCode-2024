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
        
        orders.append([line])

    file.close()

    return rules, orders


if __name__ == "__main__":
    print(get_input())