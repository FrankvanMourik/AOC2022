def read_file():
    data = []
    for x in open("input.txt"):
        data.append(x[:-1])
    return data


def answer1():
    data = read_file()
    sum = 0
    for line in data:
        digits = [x for x in line if str.isdigit(x)]
        number = digits[0] + digits[-1]
        sum += int(number)
    print(sum)


def answer2():
    data = read_file()
    sum = 0
    options3 = ["one", "two", "six"]
    options4 = ["four", "five", "nine"]
    options5 = ["three", "seven", "eight"]
    for line in data:
        first_occ = 0
        last_occ = 0
        for i in range(len(line)):
            if str.isdigit(line[i]):
                if first_occ == 0:
                    first_occ = line[i]
                last_occ = line[i]
            if line[i:i+3] in options3 or line[i:i+4] in options4 or line[i:i+5] in options5:
                if first_occ == 0:
                    first_occ = convert_to_digit(line, i)
                last_occ = convert_to_digit(line, i)
        value = int(first_occ + last_occ)
        print(line + ": " + str(value))
        sum += value

    print(sum)

def convert_to_digit(line, index):
    convert = {
        "on": "1",
        "tw": "2",
        "th": "3",
        "fo": "4",
        "fi": "5",
        "si": "6",
        "se": "7",
        "ei": "8",
        "ni": "9",
    }
    return convert[line[index:index+2]]

if __name__ == "__main__":
    print("Answer 1:")
    answer1()
    print("Answer 2:")
    answer2()
