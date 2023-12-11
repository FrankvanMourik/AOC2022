import numpy as np

def read_file():
    data = []
    for x in open("input.txt"):
        data.append(x[:-1])
    return data


def answer1():
    data = read_file()
    total_results = 0
    for line in data:
        line = [int(x) for x in line.split()]
        history = []
        # Build up
        while True:
            history.append(line)
            if line.count(0) == len(line):
                break
            line = [line[i+1]-line[i] for i in range(len(line)-1)]
        history[-1].append(0)
        # Build down
        for i in range(len(history)-1, 0, -1):
            history[i-1].append(history[i-1][-1] + history[i][-1])
        total_results += history[0][-1]
    print(total_results)

def answer2():
    data = read_file()
    total_results = 0
    for line in data:
        line = [int(x) for x in line.split()]
        line.reverse()
        history = []
        # Build up
        while True:
            history.append(line)
            if line.count(0) == len(line):
                break
            line = [line[i+1]-line[i] for i in range(len(line)-1)]
        history[-1].append(0)
        # Build down
        for i in range(len(history)-1, 0, -1):
            history[i-1].append(history[i-1][-1] + history[i][-1])
        total_results += history[0][-1]
    print(total_results)
    

if __name__ == "__main__":
    print("Answer 1:")
    answer1()
    print("Answer 2:")
    answer2()
