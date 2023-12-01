def read_file():
    data = []
    for x in open("input.txt"):
        data.append(x[:-1])
    return data


def answer1():
    data = read_file()
    overlap = 0
    for line in data:
        line = line.split(',')
        first = line[0].split('-')
        second = line[1].split('-')
        first = [int(x) for x in first]
        second = [int(x) for x in second]
        if first[0] >= second[0] and first[1] <= second[1] or first[0] <= second[0] and first[1] >= second[1]:
            overlap += 1
    print(overlap)


def answer2():
    data = read_file()
    overlap = 0
    for line in data:
        line = line.split(',')
        first = line[0].split('-')
        second = line[1].split('-')
        first = [int(x) for x in first]
        second = [int(x) for x in second]
        if first[0] <= second[0] <= first[1] or second[0] <= first[0] <= second[1]:
            overlap += 1
    print(overlap)


if __name__ == "__main__":
    answer1()
    answer2()
