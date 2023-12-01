from pprint import pprint


def result1(fileName):
    data = []
    for x in open(fileName):
        data.append(x[:-1])
    splitter = data.index('')
    coordinates = data[:splitter]
    instructions = data[splitter + 1:]
    coordinates = [[int(x.split(',')[0]), int(x.split(',')[1])] for x in coordinates]
    max_number_x = max([x[0] for x in coordinates])
    max_number_y = max([x[1] for x in coordinates])
    matrix = []
    for i in range(max_number_y + 1):
        matrix.append([0] * (max_number_x + 1))
    for coordinate in coordinates:
        matrix[coordinate[1]][coordinate[0]] = 1

    first_instruction = instructions[0][11:]
    orientation = first_instruction[0]
    number = int(first_instruction[2:])
    print(orientation, number)
    matrix = x_fold(matrix, number)
    # pprint(new_matrix)
    return sum([x for y in matrix for x in y])


def y_fold(matrix, number):
    new_matrix = matrix[:number]
    remainder = matrix[number + 1:]
    remainder.reverse()
    for i in range(len(remainder)):
        for j in range(len(remainder[0])):
            if new_matrix[i][j] == 0:
                new_matrix[i][j] = remainder[i][j]
    return new_matrix


def x_fold(matrix, number):
    new_matrix = []
    remainder = []
    for i in range(len(matrix)):
        new_matrix.append(matrix[i][:number])
        rem = matrix[i][number + 1:]
        rem.reverse()
        remainder.append(rem)
    for i in range(len(new_matrix)):
        for j in range(len(new_matrix[0])):
            if new_matrix[i][j] == 0:
                new_matrix[i][j] = remainder[i][j]
    return new_matrix


def result2(fileName):
    data = []
    for x in open(fileName):
        data.append(x[:-1])
    splitter = data.index('')
    coordinates = data[:splitter]
    instructions = data[splitter + 1:]
    coordinates = [[int(x.split(',')[0]), int(x.split(',')[1])] for x in coordinates]
    max_number_x = max([x[0] for x in coordinates])
    max_number_y = max([x[1] for x in coordinates])
    max_number_y += 1
    print(max_number_x, max_number_y)
    matrix = []
    for i in range(max_number_y + 1):
        matrix.append([0] * (max_number_x + 1))
    for coordinate in coordinates:
        matrix[coordinate[1]][coordinate[0]] = 1

    for instruction in instructions:
        instruction = instruction[11:]
        orientation = instruction[0]
        number = int(instruction[2:])
        print(orientation, number)
        if orientation == 'x':
            print((len(matrix[0])-1)/number)
            matrix = x_fold(matrix, number)
        else:
            print((len(matrix) - 1) / number)
            matrix = y_fold(matrix, number)
        # pretty(matrix)
    pretty(matrix)
    return 0


def pretty(matrix):
    for row in matrix:
        stri = ""
        for chr in row:
            if chr == 0:
                stri += "-"
            else:
                stri += "#"
        print(stri)


def test():
    return result2("sample.txt")


def result2_golf():
    print("No way")


if __name__ == "__main__":
    # print(test())
    # print(result1("input.txt"))
    print(result2("input.txt"))
