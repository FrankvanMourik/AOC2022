def result1():
    data = []
    for x in open("t.txt"):
        data.append(x.split(' | '))
    for i in range(len(data)):
        data[i][1] = data[i][1][:-1]
        data[i][0] = data[i][0].split()
        data[i][1] = data[i][1].split()
    data_for_1 = [x[1] for x in data]
    count = 0
    for x in data_for_1:
        for y in x:
            if len(y) == 2 or len(y) == 3 or len(y) == 4 or len(y) == 7:
                count += 1
                print(y)
    return count


def result2():
    print("")

def result2_golf():
    print("")


if __name__ == "__main__":
    print(result1())
