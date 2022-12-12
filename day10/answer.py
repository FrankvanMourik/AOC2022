def read_file():
    data = []
    for x in open("input.txt"):
        data.append(x[:-1])
    return data


def answer1():
    data = read_file()
    x = 1
    cycle = 1
    sum = 0
    for line in data:
        if line[0] == 'a':
            if cycle in [20, 60, 100, 140, 180, 220]:
                print("Added at cycle " + str(cycle) + ":\t" + str(cycle * x))
                sum += cycle * x
            cycle += 1
            if cycle in [20, 60, 100, 140, 180, 220]:
                print("Added at cycle " + str(cycle) + ":\t" + str(cycle * x))
                sum += cycle * x
            line = line.split()
            nr = int(line[1])
            x += nr
        else:
            if cycle in [20, 60, 100, 140, 180, 220]:
                print("Added at cycle " + str(cycle) + ":\t" + str(cycle * x))
                sum += cycle * x
        cycle += 1
    print("Total sum:\t" + str(sum))


def answer2():
    data = read_file()
    x = 1
    cycle = 1
    result_string = ""
    for line in data:
        if cycle == 9:
            print("breakpoint")
        if x+1 == cycle % 40 or x == cycle % 40 or x+2 == cycle % 40:
            result_string += "#"
        else:
            result_string += "."
        if line[0] == 'a':
            cycle += 1
            if x + 1 == cycle % 40 or x == cycle % 40 or x + 2 == cycle % 40:
                result_string += "#"
            else:
                result_string += "."
            line = line.split()
            nr = int(line[1])
            x += nr
        cycle += 1
    print("Total string:\t" + result_string)
    print("Length string:\t" + str(len(result_string)))
    for x in range(0, len(result_string),40):
        print(result_string[x:x+40])


if __name__ == "__main__":
    print("Answer 1:")
    answer1()
    print("Answer 2:")
    answer2()
