def result1():
    data = []
    for line in open("input.txt"):
        tuple_from_line = line.split(" -> ")
        tuple_from_line[1] = tuple_from_line[1][:-1]
        tuple = [x.split(",") for x in tuple_from_line]
        tuple = [[int(y[0]), int(y[1])] for y in tuple]
        data.append(tuple)
    vertical_lines = []
    horizontal_lines = []
    for line in data:
        if line[0][0] == line[1][0]:
            vertical_lines.append(line)
        elif line[0][1] == line[1][1]:
            horizontal_lines.append(line)
    matrix = []
    for x in range(1000):
        matrix.append([0] * 1000)
    print("Example vertical line: " + str(vertical_lines[0]))
    print("Example horizontal line: " + str(horizontal_lines[0]))
    for line in vertical_lines:
        if line[0][1] < line[1][1]:
            for x in range(line[0][1], line[1][1] + 1):
                matrix[x][line[0][0]] += 1
        else:
            for x in range(line[1][1], line[0][1] + 1):
                matrix[x][line[0][0]] += 1
    for line in horizontal_lines:
        if line[0][0] < line[1][0]:
            for x in range(line[0][0], line[1][0] + 1):
                matrix[line[1][1]][x] += 1
        else:
            for x in range(line[1][0], line[0][0] + 1):
                matrix[line[1][1]][x] += 1
    som = 0
    for line in matrix:
        for cell in line:
            if cell > 1:
                som += 1
    return som



def result2():
    data = []
    for line in open("input.txt"):
        tuple_from_line = line.split(" -> ")
        tuple_from_line[1] = tuple_from_line[1][:-1]
        tuple = [x.split(",") for x in tuple_from_line]
        tuple = [[int(y[0]), int(y[1])] for y in tuple]
        data.append(tuple)
    vertical_lines = []
    horizontal_lines = []
    diagonal_lines = []
    for line in data:
        if line[0][0] == line[1][0]:
            vertical_lines.append(line)
        elif line[0][1] == line[1][1]:
            horizontal_lines.append(line)
        else:
            diagonal_lines.append(line)
    print(len(data))
    print(len(diagonal_lines))
    print(len(horizontal_lines))
    print(len(vertical_lines))
    matrix = []
    for x in range(1000):
        matrix.append([0] * 1000)
    print("Example vertical line: " + str(vertical_lines[0]))
    print("Example horizontal line: " + str(horizontal_lines[0]))
    print("Example diagonal line: " + str(diagonal_lines[0]))
    for line in vertical_lines:
        if line[0][1] < line[1][1]:
            for x in range(line[0][1], line[1][1] + 1):
                matrix[x][line[0][0]] += 1
        else:
            for x in range(line[1][1], line[0][1] + 1):
                matrix[x][line[0][0]] += 1
    for line in horizontal_lines:
        if line[0][0] < line[1][0]:
            for x in range(line[0][0], line[1][0] + 1):
                matrix[line[1][1]][x] += 1
        else:
            for x in range(line[1][0], line[0][0] + 1):
                matrix[line[1][1]][x] += 1
    for line in diagonal_lines:
        if line[0][0] < line[1][0] and line[0][1] < line[1][1]:
            for x in range(line[1][0] - line[0][0] + 1):
                matrix[line[0][1] + x][line[0][0] + x] += 1
        elif line[0][0] < line[1][0] and line[0][1] >= line[1][1]:
            for x in range(line[1][0] - line[0][0] + 1):
                matrix[line[0][1] - x][line[0][0] + x] += 1
        elif line[0][0] >= line[1][0] and line[0][1] < line[1][1]:
            for x in range(line[0][0] - line[1][0] + 1):
                matrix[line[0][1] + x][line[0][0] - x] += 1
        elif line[0][0] >= line[1][0] and line[0][1] >= line[1][1]:
            for x in range(line[0][0] - line[1][0] + 1):
                matrix[line[0][1] - x][line[0][0] - x] += 1
                print(x)
    som = 0
    for line in matrix:
        for cell in line:
            if cell > 1:
                som += 1
    [print(x) for x in matrix]
    return som


def result2_golf():
    print("Nee")


if __name__ == "__main__":
    print(result2())
