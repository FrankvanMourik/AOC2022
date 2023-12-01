def result1():
    data = []
    for b in open('input.txt'):
        data.append(b)
    data = [''.join(s) for s in zip(*data)][:-1]
    print(data)
    gamma = ""
    epsilon = ""
    for b in data:
        if b.count('1') > b.count('0'):
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"
    print(gamma)
    print(epsilon)
    print(int(gamma, 2) * int(epsilon, 2))


def result2():
    data = []
    for b in open('input.txt'):
        data.append(b)
    nr_of_bits = len(data[0])
    oxygen_numbers = data.copy()
    co2_numbers = data.copy()
    for i in range(nr_of_bits):
        print("Length of oxygen numbers at start loop:", len(oxygen_numbers))
        zeroes = 0
        ones = 0
        for b in oxygen_numbers:
            if b[i] == '0':
                zeroes += 1
            else:
                ones += 1
        print(zeroes, ", ", ones)
        if ones >= zeroes:
            if len(oxygen_numbers) > 1:
                copy = oxygen_numbers.copy()
                [oxygen_numbers.remove(x) for x in copy if x[i] == "0"]
                print("Length of oxygen number after removing", len(oxygen_numbers))
        elif ones < zeroes:
            if len(oxygen_numbers) > 1:
                copy = oxygen_numbers.copy()
                [oxygen_numbers.remove(x) for x in copy if x[i] == "1"]
                print("Length of oxygen number after removing",len(oxygen_numbers))
    for i in range(nr_of_bits):
        print("Length of co2 numbers at start loop:", len(co2_numbers))
        zeroes = 0
        ones = 0
        for b in co2_numbers:
            if b[i] == '0':
                zeroes += 1
            else:
                ones += 1
        if ones >= zeroes:
            if len(co2_numbers) > 1:
                copy = co2_numbers.copy()
                [co2_numbers.remove(x) for x in copy if x[i] == "1"]
                print("Length of co2 number after removing", len(co2_numbers))
        elif ones < zeroes:
            if len(co2_numbers) > 1:
                copy = co2_numbers.copy()
                [co2_numbers.remove(x) for x in copy if x[i] == "0"]
                print("Length of co2 number after removing",len(co2_numbers))
    print(int(oxygen_numbers[0], 2) * int(co2_numbers[0], 2))


def result2_golf():
    print("Nee")


if __name__ == "__main__":
    result2()
