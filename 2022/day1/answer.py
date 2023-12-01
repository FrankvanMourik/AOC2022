def read_file():
    data = []
    for x in open("input.txt"):
        data.append(x[:-1])
    return data


def result1():
    data = read_file()
    sums = []
    som = 0
    for x in data:
        if x:
            som += int(x)
        else:
            sums.append(som)
            som = 0
    print(max(sums))


def result2():
    data = read_file()
    sums = []
    som = 0
    for x in data:
        if x:
            som += int(x)
        else:
            sums.append(som)
            som = 0
    sums.sort(reverse=True)
    print(sums[0]+sums[1]+sums[2])


if __name__ == "__main__":
    result1()
    result2()
