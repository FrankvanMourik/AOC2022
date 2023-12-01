def result1():
    data = []
    for x in map(int, open('input.txt').read().split(',')):
        data.append(x)
    print(max(data))
    best_option = 0
    least_fuel = 10000000000
    for x in range(max(data)):
        fuel = 0
        for b in data:
            fuel += abs(x-b)
        if fuel<least_fuel:
            least_fuel = fuel
            best_option = x
    print(best_option, least_fuel)



def result2():
    data = []
    for x in map(int, open('input.txt').read().split(',')):
        data.append(x)
    print(max(data))
    best_option = 0
    least_fuel = 10000000000
    for x in range(max(data)):
        fuel = 0
        for b in data:
            diff = abs(x - b)
            fuel += diff * (diff + 1) / 2
        if fuel < least_fuel:
            least_fuel = fuel
            best_option = x
    print(best_option, least_fuel)


def result2_golf():
    print("")


if __name__ == "__main__":
    print(result2())
