def read_file():
    data = []
    for x in open("input.txt"):
        data.append(x[:-1])
    return data


def answer1():
    data = read_file()
    line1 = data[0].split(':')
    race_times = line1[1].split()
    line2 = data[1].split(':')
    race_records = line2[1].split()
    total = 1
    print(race_times)
    print(race_records)
    for i in range(len(race_times)):
        total_better = 0
        for j in range(1,int(race_times[i])):
            speed = j
            travel_time = int(race_times[i])-j
            distance = speed * travel_time
            if distance > int(race_records[i]):
                total_better += 1
        total *= total_better
        print(i)
    print(total)


def answer2():
    data = read_file()
    line1 = data[0].split(':')
    race_times = line1[1].split()
    line2 = data[1].split(':')
    race_records = line2[1].split()
    total = 1
    print(race_times)
    print(race_records)
    for i in range(len(race_times)):
        total_better = 0
        for j in range(1,int(race_times[i])):
            speed = j
            travel_time = int(race_times[i])-j
            distance = speed * travel_time
            if distance > int(race_records[i]):
                total_better += 1
        total *= total_better
        print(i)
    print(total)


if __name__ == "__main__":
    print("Answer 1:")
    answer1()
    print("Answer 2:")
    answer2()
