import math


def read_file():
    data = []
    for x in open("input.txt"):
        data.append(x[:-1])
    return data


def answer1():
    data = read_file()
    total_points = 0
    for line in data:
        parts = line.split(' | ')
        your_numbers = parts[1].split()
        start_part = parts[0].split(': ')
        winning_numbers = start_part[1].split()
        print(your_numbers)
        print(winning_numbers)
        points_array = [1 for x in your_numbers if x in winning_numbers]
        points = sum(points_array)
        total_points += math.floor(pow(2,points-1))
    print(total_points)


def answer2():
    data = read_file()
    total_cards = [1]*len(data)
    for i in range(len(data)):
        parts = data[i].split(' | ')
        your_numbers = parts[1].split()
        start_part = parts[0].split(': ')
        winning_numbers = start_part[1].split()
        print(your_numbers)
        print(winning_numbers)
        points_array = [1 for x in your_numbers if x in winning_numbers]
        points = sum(points_array)
        for j in range(points):
            if i+j < len(data):
                total_cards[i+j+1] += total_cards[i]
    print(sum(total_cards))


if __name__ == "__main__":
    print("Answer 1:")
    answer1()
    print("Answer 2:")
    answer2()
