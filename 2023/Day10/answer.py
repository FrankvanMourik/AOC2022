import numpy as np

def read_file():
    data = []
    for x in open("sample.txt"):
        data.append(x[:-1])
    return data


def answer1():
    data = read_file()
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == 'S':
                S = (i,j)
    print(S)
    i = S[0]
    j = S[1]
    top = data[i-1][j]
    left = data[i][j-1]
    bottom = data[i+1][j]
    right = data[i][j+1]
    if top in "F|7":
        top = True
    else:
        top = False
    if left in "FL-":
        left = True
    else:
        left = False
    if right in "-J7":
        right = True
    else:
        right = False
    if bottom in "|LJ":
        bottom = True
    else:
        bottom = False
    steps = 0
    next_step = 'b'
    while True:
        directions = get_directions_dict()
        opposite = get_opposite()

        steps += 1
        if next_step == 'b':
            i += 1
        if next_step == 't':
            i -= 1
        if next_step == 'l':
            j -= 1
        if next_step == 'r':
            j += 1
        if i == S[0] and j == S[1]:
            break
        print(f'New location ({i},{j}), with value {data[i][j]}')
        next = directions[data[i][j]]
        next.remove(opposite[next_step])
        next_step = next[0]

    print(steps)
    print(steps//2)


def get_directions_dict():
    directions = dict()
    directions['F'] = ['r','b']
    directions['|'] = ['t','b']
    directions['7'] = ['l','b']
    directions['L'] = ['t','r']
    directions['J'] = ['t','l']
    directions['-'] = ['l','r']
    return directions

def get_opposite():
    opposite = dict()
    opposite['t'] = 'b'
    opposite['b'] = 't'
    opposite['l'] = 'r'
    opposite['r'] = 'l'
    return opposite

def answer2():
    data = read_file()
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == 'S':
                S = (i,j)
    print(S)
    i = S[0]
    j = S[1]
    top = data[i-1][j]
    left = data[i][j-1]
    bottom = data[i+1][j]
    right = data[i][j+1]
    if top in "F|7":
        top = True
    else:
        top = False
    if left in "FL-":
        left = True
    else:
        left = False
    if right in "-J7":
        right = True
    else:
        right = False
    if bottom in "|LJ":
        bottom = True
    else:
        bottom = False
    steps = 0
    # Next step is bottom for both
    next_step = 'b'
    loop = [S]
    while True:
        directions = get_directions_dict()
        opposite = get_opposite()

        steps += 1
        if next_step == 'b':
            i += 1
        if next_step == 't':
            i -= 1
        if next_step == 'l':
            j -= 1
        if next_step == 'r':
            j += 1
        if i == S[0] and j == S[1]:
            break
        next = directions[data[i][j]]
        loop.append((i,j))
        next.remove(opposite[next_step])
        # print(next)
        next_step = next[0]
    cells_in_loop = []
    for i in range(1,len(data)-1):
        for j in range(1,len(data[0])-1):
            if (i,j) not in loop:
                nr_of_crosses = 0
                for y in range(0,j):
                    if (i,y) in loop:
                        nr_of_crosses += 1
                if nr_of_crosses % 2 == 1:
                    cells_in_loop.append((i,j))
    print(cells_in_loop)
    
    

if __name__ == "__main__":
    print("Answer 1:")
    answer1()
    print("Answer 2:")
    answer2()
