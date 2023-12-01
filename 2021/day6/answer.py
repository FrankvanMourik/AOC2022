def result1():
    fish = []
    for x in open("input.txt"):
        fish.extend([int(b) for b in x.split(',')])
    print(fish)
    for x in range(80):
        copy = fish.copy()
        for i, vis in enumerate(copy):
            if vis > 0:
                fish[i] -= 1
            elif vis == 0:
                fish[i] = 6
                fish.append(8)
        print(fish)
    print(len(fish))



def result2():
    fish = []
    for x in open("input.txt"):
        fish.extend([int(b) for b in x.split(',')])
    for x in range(256):
        copy = fish.copy()
        for i, vis in enumerate(copy):
            if vis > 0:
                fish[i] -= 1
            elif vis == 0:
                fish[i] = 6
                fish.append(8)
        print(x)
    print(len(fish))


def result2_golf():
    a = [0] * 9
    for m in map(int, open('input.txt').read().split(',')): a[m] += 1
    exec("z=a.pop(0);a[6]+=z;a.append(z);" * 256)
    print(sum(a))


if __name__ == "__main__":
    print(result2_golf())
