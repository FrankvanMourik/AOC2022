def read_file():
    data = []
    for x in open("input.txt"):
        data.append(x[:-1])
    return data


def answer1():
    data = read_file()[0]
    # data = "bvwbjplbgvbhsrlpgdmjqwftvncz"
    for i in range(len(data)-3):
        if len(set(data[i:i+4])) == 4:
            print(i+4)
            return


def answer2():
    data = read_file()[0]
    # data = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"
    for i in range(len(data) - 13):
        if len(set(data[i:i + 14])) == 14:
            print(i + 14)
            return


if __name__ == "__main__":
    print("Answer 1:")
    answer1()
    print("Answer 2:")
    answer2()
