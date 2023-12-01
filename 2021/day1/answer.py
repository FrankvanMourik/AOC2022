def result1():
    list = []
    f = open("data/data.txt", "r").read().splitlines()
    for x in f:
        list.append(int(x))
    print(list)
    result = 0
    for i in range(len(list)-1):
        if list[i] < list[i+1]:
            result += 1
    print(result)


def result2():
    lijst = []
    f = open("data/data.txt", "r").read().splitlines()
    for x in f:
        lijst.append(int(x))
    print(lijst)
    result = 0
    for i in range(len(lijst)-3):
        sum = lijst[i]+lijst[i+1]+lijst[i+2]
        next_sum = lijst[i+1]+lijst[i+2]+lijst[i+3]
        if sum < next_sum:
            result += 1
    print(result)


if __name__ == "__main__":
    result2()