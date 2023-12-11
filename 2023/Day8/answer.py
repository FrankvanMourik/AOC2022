import numpy as np

def read_file():
    data = []
    for x in open("input.txt"):
        data.append(x[:-1])
    return data


def answer1():
    data = read_file()
    intructions = data[0]
    tree = dict()
    for line in data[2:]:
        key = line[0:3]
        left = line[7:10]
        right = line[12:15]
        tree[key] = [left, right]
    position = 'AAA'
    counter = 0
    while True:
        inst = intructions[counter % len(intructions)]
        # print(position)
        if inst == 'L':
            position = tree[position][0]
        else:
            position = tree[position][1]
        counter += 1
        if position == 'ZZZ':
            break
    print(counter)
        

def answer2():
    data = read_file()
    intructions = data[0]
    tree = dict()
    for line in data[2:]:
        key = line[0:3]
        left = line[7:10]
        right = line[12:15]
        tree[key] = [left, right]
    positions = [key for key in tree.keys() if key[2] == 'A']
    og_positions = positions.copy()
    print(positions)
    all_results = []
    for i in range(len(positions)):
        results = []
        counter = 0
        while len(results) < 1:
            inst = intructions[counter % len(intructions)]
            # print(positions)
            if inst == 'L':
                positions[i] = tree[positions[i]][0]
            else:
                positions[i] = tree[positions[i]][1]
            counter += 1
            if positions[i][2] == 'Z':
                print(f"Found end for OG {og_positions[i]} at position {positions[i]} at counter {counter}")
                results.append(counter)
        all_results.append(results)
    print(all_results)
    arr = np.array(all_results)
    print(arr)
    lcm = np.lcm.reduce(arr)
    print(lcm)
    for x in all_results:
        print(lcm/x)


if __name__ == "__main__":
    print("Answer 1:")
    # answer1()
    print("Answer 2:")
    answer2()

