def read_file():
    data = []
    for x in open("input.txt"):
        data.append(x[:-1])
    return data


def ugly_operation_for_dummy(monkey_nr, worry_level):
    match monkey_nr:
        case 0:
            return 19 * worry_level
        case 1:
            return worry_level + 6
        case 2:
            return worry_level * worry_level
        case 3:
            return worry_level + 3


def ugly_operation_for_input(monkey_nr, worry_level):
    match monkey_nr:
        case 0:
            return 11 * worry_level
        case 1:
            return worry_level + 4
        case 2:
            return worry_level * 19
        case 3:
            return worry_level * worry_level
        case 4:
            return worry_level + 1
        case 5:
            return worry_level + 3
        case 6:
            return worry_level + 8
        case 7:
            return worry_level + 7


def parse_monkey(monkey_id, monkeys, data):
    monkeys[monkey_id] = {}
    starting_items = data[1].split(":")[1]
    starting_items = starting_items.split(", ")
    starting_items = [int(x) for x in starting_items]
    monkeys[monkey_id]["start"] = starting_items
    divide_number = data[3].split()
    divide_number = int(divide_number[len(divide_number) - 1])
    monkeys[monkey_id]["divide"] = divide_number
    true_monkey = data[4].split()
    true_monkey = int(true_monkey[len(true_monkey) - 1])
    monkeys[monkey_id]["true"] = true_monkey
    false_monkey = data[5].split()
    false_monkey = int(false_monkey[len(false_monkey) - 1])
    monkeys[monkey_id]["false"] = false_monkey


def parse_input(data):
    monkeys = {}
    for monkey_id in range(1 +len(data) // 7):
        parse_monkey(monkey_id, monkeys, data[7 * monkey_id: 7 * monkey_id + 7])
    return monkeys


def answer1():
    data = read_file()
    monkeys = parse_input(data)
    throws = [0]*len(monkeys)
    print(throws)
    nr_iter = 20
    for x in range(nr_iter):
        for monkey_id in monkeys:
            monkey = monkeys[monkey_id]
            for i, item in enumerate(monkey["start"]):
                # inspect
                monkey["start"][i] = ugly_operation_for_input(monkey_id, monkey["start"][i])
                # rest
                monkey["start"][i] = monkey["start"][i] // 3
                if monkey["start"][i] % monkey["divide"] == 0:
                    to_monkey = monkey["true"]
                    monkeys[to_monkey]["start"] = monkeys[to_monkey]["start"] + [monkey["start"][i]]
                else:
                    to_monkey = monkey["false"]
                    monkeys[to_monkey]["start"] = monkeys[to_monkey]["start"] + [monkey["start"][i]]
                throws[monkey_id] += 1
            monkey["start"] = []
    print(throws)
    throws.sort(reverse=True)
    print(throws)
    print(throws[0] * throws[1])
    return


def answer2():
    data = read_file()
    monkeys = parse_input(data)
    throws = [0] * len(monkeys)
    print(throws)
    nr_iter = 10000
    lcm = 1
    for monkey_id in monkeys:
        monkey = monkeys[monkey_id]
        lcm = lcm * monkey["divide"]
    print(lcm)
    for x in range(nr_iter):
        for monkey_id in monkeys:
            monkey = monkeys[monkey_id]
            for i, item in enumerate(monkey["start"]):
                # inspect
                monkey["start"][i] = ugly_operation_for_input(monkey_id, monkey["start"][i]) % lcm
                if monkey["start"][i] % monkey["divide"] == 0:
                    to_monkey = monkey["true"]
                    monkeys[to_monkey]["start"] = monkeys[to_monkey]["start"] + [monkey["start"][i]]
                else:
                    to_monkey = monkey["false"]
                    monkeys[to_monkey]["start"] = monkeys[to_monkey]["start"] + [monkey["start"][i]]
                throws[monkey_id] += 1
            monkey["start"] = []
    print(throws)
    throws.sort(reverse=True)
    print(throws)
    print(throws[0] * throws[1])
    return


if __name__ == "__main__":
    print("Answer 1:")
    answer1()
    print("Answer 2:")
    answer2()
