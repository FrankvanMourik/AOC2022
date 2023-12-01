from pprint import pprint


def result1(fileName):
    data = []
    for x in open(fileName):
        data.append([int(y) for y in x[:-1]])
    pprint(data)
    new_data = [[(0,False)]*10 for x in range(10)]
    # pre processing
    for j in range(len(data)):
        for h in range(len(data[0])):
            new_data[j][h] = (data[j][h],False)
    data = new_data
    steps = 100
    flashes = 0
    for i in range(steps):
        # part 1
        for j in range(len(data)):
            for h in range(len(data[0])):
                data[j][h] = (data[j][h][0]+1, False)

        # part 2
        octopusDidFlash = True
        while(octopusDidFlash):
            octopusDidFlash = False
            for j in range(len(data)):
                for h in range(len(data[0])):
                    if data[j][h][0] > 9 and not data[j][h][1]:
                        flashes += 1
                        data[j][h] = (data[j][h][0], True)
                        octopusDidFlash = True
                        # Update neighbour cells
                        if j==0:
                            if h==0:
                                data[j][h+1] = (data[j][h+1][0]+1, data[j][h+1][1])
                                data[j+1][h] = (data[j+1][h][0]+1, data[j+1][h][1])
                                data[j+1][h+1] = (data[j+1][h+1][0]+1, data[j+1][h+1][1])
                            elif h==len(data)-1:
                                data[j][h-1] = (data[j][h - 1][0] + 1, data[j][h - 1][1])
                                data[j + 1][h] = (data[j + 1][h][0] + 1, data[j + 1][h][1])
                                data[j + 1][h - 1] = (data[j + 1][h - 1][0] + 1, data[j + 1][h - 1][1])
                            else:
                                data[j][h + 1] = (data[j][h + 1][0] + 1, data[j][h + 1][1])
                                data[j + 1][h] = (data[j + 1][h][0] + 1, data[j + 1][h][1])
                                data[j + 1][h + 1] = (data[j + 1][h + 1][0] + 1, data[j + 1][h + 1][1])
                                data[j][h - 1] = (data[j][h - 1][0] + 1, data[j][h - 1][1])
                                data[j + 1][h - 1] = (data[j + 1][h - 1][0] + 1, data[j + 1][h - 1][1])
                        elif j==len(data)-1:
                            if h==0:
                                data[j][h+1] = (data[j][h+1][0]+1, data[j][h+1][1])
                                data[j-1][h] = (data[j-1][h][0]+1, data[j-1][h][1])
                                data[j-1][h+1] = (data[j-1][h+1][0]+1, data[j-1][h+1][1])
                            elif h==len(data)-1:
                                data[j][h-1] = (data[j][h - 1][0] + 1, data[j][h - 1][1])
                                data[j - 1][h] = (data[j - 1][h][0] + 1, data[j - 1][h][1])
                                data[j - 1][h - 1] = (data[j - 1][h - 1][0] + 1, data[j - 1][h - 1][1])
                            else:
                                data[j][h + 1] = (data[j][h + 1][0] + 1, data[j][h + 1][1])
                                data[j - 1][h] = (data[j - 1][h][0] + 1, data[j - 1][h][1])
                                data[j - 1][h + 1] = (data[j - 1][h + 1][0] + 1, data[j - 1][h + 1][1])
                                data[j][h - 1] = (data[j][h - 1][0] + 1, data[j][h - 1][1])
                                data[j - 1][h - 1] = (data[j - 1][h - 1][0] + 1, data[j - 1][h - 1][1])
                        else:
                            if h==0:
                                data[j - 1][h] = (data[j - 1][h][0] + 1, data[j - 1][h][1])
                                data[j + 1][h] = (data[j + 1][h][0] + 1, data[j + 1][h][1])
                                data[j][h + 1] = (data[j][h + 1][0] + 1, data[j][h + 1][1])
                                data[j + 1][h + 1] = (data[j + 1][h + 1][0] + 1, data[j + 1][h + 1][1])
                                data[j - 1][h + 1] = (data[j - 1][h + 1][0] + 1, data[j - 1][h + 1][1])
                            elif h==len(data)-1:
                                data[j - 1][h] = (data[j - 1][h][0] + 1, data[j - 1][h][1])
                                data[j + 1][h] = (data[j + 1][h][0] + 1, data[j + 1][h][1])
                                data[j][h - 1] = (data[j][h - 1][0] + 1, data[j][h - 1][1])
                                data[j + 1][h - 1] = (data[j + 1][h - 1][0] + 1, data[j + 1][h - 1][1])
                                data[j - 1][h - 1] = (data[j - 1][h - 1][0] + 1, data[j - 1][h - 1][1])
                            else:
                                data[j][h] = (data[j][h][0] + 1, data[j][h][1])
                                data[j][h+1] = (data[j][h+1][0] + 1, data[j][h+1][1])
                                data[j][h-1] = (data[j][h-1][0] + 1, data[j][h-1][1])
                                data[j+1][h] = (data[j+1][h][0] + 1, data[j+1][h][1])
                                data[j+1][h+1] = (data[j+1][h+1][0] + 1, data[j+1][h+1][1])
                                data[j+1][h-1] = (data[j+1][h-1][0] + 1, data[j+1][h-1][1])
                                data[j-1][h] = (data[j-1][h][0] + 1, data[j-1][h][1])
                                data[j-1][h+1] = (data[j-1][h+1][0] + 1, data[j-1][h+1][1])
                                data[j-1][h-1] = (data[j-1][h-1][0] + 1, data[j-1][h-1][1])


        # Part 3
        for j in range(len(data)):
            for h in range(len(data[0])):
                if data[j][h][1]:
                    data[j][h] = (0, False)
    return flashes


def result2(fileName):
    data = []
    for x in open(fileName):
        data.append([int(y) for y in x[:-1]])
    pprint(data)
    new_data = [[(0, False)] * 10 for x in range(10)]
    # pre processing
    for j in range(len(data)):
        for h in range(len(data[0])):
            new_data[j][h] = (data[j][h], False)
    data = new_data
    for i in range(1000000):
        # part 1
        for j in range(len(data)):
            for h in range(len(data[0])):
                data[j][h] = (data[j][h][0] + 1, False)

        # part 2
        flashes_this_round = 0
        octopusDidFlash = True
        while (octopusDidFlash):
            octopusDidFlash = False
            for j in range(len(data)):
                for h in range(len(data[0])):
                    if data[j][h][0] > 9 and not data[j][h][1]:
                        flashes_this_round += 1
                        data[j][h] = (data[j][h][0], True)
                        octopusDidFlash = True
                        # Update neighbour cells
                        if j == 0:
                            if h == 0:
                                data[j][h + 1] = (data[j][h + 1][0] + 1, data[j][h + 1][1])
                                data[j + 1][h] = (data[j + 1][h][0] + 1, data[j + 1][h][1])
                                data[j + 1][h + 1] = (data[j + 1][h + 1][0] + 1, data[j + 1][h + 1][1])
                            elif h == len(data) - 1:
                                data[j][h - 1] = (data[j][h - 1][0] + 1, data[j][h - 1][1])
                                data[j + 1][h] = (data[j + 1][h][0] + 1, data[j + 1][h][1])
                                data[j + 1][h - 1] = (data[j + 1][h - 1][0] + 1, data[j + 1][h - 1][1])
                            else:
                                data[j][h + 1] = (data[j][h + 1][0] + 1, data[j][h + 1][1])
                                data[j + 1][h] = (data[j + 1][h][0] + 1, data[j + 1][h][1])
                                data[j + 1][h + 1] = (data[j + 1][h + 1][0] + 1, data[j + 1][h + 1][1])
                                data[j][h - 1] = (data[j][h - 1][0] + 1, data[j][h - 1][1])
                                data[j + 1][h - 1] = (data[j + 1][h - 1][0] + 1, data[j + 1][h - 1][1])
                        elif j == len(data) - 1:
                            if h == 0:
                                data[j][h + 1] = (data[j][h + 1][0] + 1, data[j][h + 1][1])
                                data[j - 1][h] = (data[j - 1][h][0] + 1, data[j - 1][h][1])
                                data[j - 1][h + 1] = (data[j - 1][h + 1][0] + 1, data[j - 1][h + 1][1])
                            elif h == len(data) - 1:
                                data[j][h - 1] = (data[j][h - 1][0] + 1, data[j][h - 1][1])
                                data[j - 1][h] = (data[j - 1][h][0] + 1, data[j - 1][h][1])
                                data[j - 1][h - 1] = (data[j - 1][h - 1][0] + 1, data[j - 1][h - 1][1])
                            else:
                                data[j][h + 1] = (data[j][h + 1][0] + 1, data[j][h + 1][1])
                                data[j - 1][h] = (data[j - 1][h][0] + 1, data[j - 1][h][1])
                                data[j - 1][h + 1] = (data[j - 1][h + 1][0] + 1, data[j - 1][h + 1][1])
                                data[j][h - 1] = (data[j][h - 1][0] + 1, data[j][h - 1][1])
                                data[j - 1][h - 1] = (data[j - 1][h - 1][0] + 1, data[j - 1][h - 1][1])
                        else:
                            if h == 0:
                                data[j - 1][h] = (data[j - 1][h][0] + 1, data[j - 1][h][1])
                                data[j + 1][h] = (data[j + 1][h][0] + 1, data[j + 1][h][1])
                                data[j][h + 1] = (data[j][h + 1][0] + 1, data[j][h + 1][1])
                                data[j + 1][h + 1] = (data[j + 1][h + 1][0] + 1, data[j + 1][h + 1][1])
                                data[j - 1][h + 1] = (data[j - 1][h + 1][0] + 1, data[j - 1][h + 1][1])
                            elif h == len(data) - 1:
                                data[j - 1][h] = (data[j - 1][h][0] + 1, data[j - 1][h][1])
                                data[j + 1][h] = (data[j + 1][h][0] + 1, data[j + 1][h][1])
                                data[j][h - 1] = (data[j][h - 1][0] + 1, data[j][h - 1][1])
                                data[j + 1][h - 1] = (data[j + 1][h - 1][0] + 1, data[j + 1][h - 1][1])
                                data[j - 1][h - 1] = (data[j - 1][h - 1][0] + 1, data[j - 1][h - 1][1])
                            else:
                                data[j][h] = (data[j][h][0] + 1, data[j][h][1])
                                data[j][h + 1] = (data[j][h + 1][0] + 1, data[j][h + 1][1])
                                data[j][h - 1] = (data[j][h - 1][0] + 1, data[j][h - 1][1])
                                data[j + 1][h] = (data[j + 1][h][0] + 1, data[j + 1][h][1])
                                data[j + 1][h + 1] = (data[j + 1][h + 1][0] + 1, data[j + 1][h + 1][1])
                                data[j + 1][h - 1] = (data[j + 1][h - 1][0] + 1, data[j + 1][h - 1][1])
                                data[j - 1][h] = (data[j - 1][h][0] + 1, data[j - 1][h][1])
                                data[j - 1][h + 1] = (data[j - 1][h + 1][0] + 1, data[j - 1][h + 1][1])
                                data[j - 1][h - 1] = (data[j - 1][h - 1][0] + 1, data[j - 1][h - 1][1])

        # Part 3
        for j in range(len(data)):
            for h in range(len(data[0])):
                if data[j][h][1]:
                    data[j][h] = (0, False)
        if flashes_this_round == 100:
            pprint(data)
            return i+1
    return 0


def test():
    print(result2("sample.txt"))


def result2_golf():
    print("No way")


if __name__ == "__main__":
    # print(test())
    # print(result1("input.txt"))
    print(result2("input.txt"))
