def result1():
    fish = []
    for x in open("t.txt"):
        fish.extend([int(b) for b in x.split(',')])
    print(fish)
    for x in range(80):
        copy = fish.copy()
        for i,vis in enumerate(copy):
            if vis > 0:
                fish[i] -= 1
            elif vis == 0:
                fish[i] = 6
                fish.append(8)
        print(fish)
    print(len(fish))


def result2():
    print("")

def result2_golf():
    print("")


if __name__ == "__main__":
    result1()
