def read_file():
    data = []
    for x in open("input.txt"):
        data.append(x[:-1])
    return data


def answer1():
    data = read_file()
    print()


def answer2():
    data = read_file()
    print()

if __name__ == "__main__":
    print("Answer 1:")
    answer1()
    print("Answer 2:")
    answer2()
