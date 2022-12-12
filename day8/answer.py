def read_file():
    data = []
    for x in open("dummy.txt"):
        data.append(x[:-1])
    return data


def create_forest(data):
    forest = []
    for _ in range(len(data)):
        forest.append([0] * len(data[0]))
    for i, row in enumerate(data):
        for j, height in enumerate(row):
            forest[i][j] = int(height)
    return forest


def is_visible(i, j, forest):
    left, top, right, bottom = True, True, True, True
    if i == 0 or j == 0 or i == len(forest) - 1 or j == len(forest[0]) - 1:
        return True
    else:
        for x in range(0, i):
            if forest[x][j] >= forest[i][j]:
                left = False
        for x in range(i + 1, len(forest)):
            if forest[x][j] >= forest[i][j]:
                right = False
        for y in range(0, j):
            if forest[i][y] >= forest[i][j]:
                top = False
        for y in range(j + 1, len(forest[0])):
            if forest[i][y] >= forest[i][j]:
                bottom = False
    return left or right or top or bottom


def calculate_scenic_score(i, j, forest):
    left, top, right, bottom = 1, 1, 1, 1
    for x in reversed(range(i - 1,-1,-1)):
        if forest[x][j] >= forest[i][j] or x == 0:
            top = abs(x - i)
            print(x, i)
            break
    for x in range(i + 1, len(forest)):
        if forest[x][j] >= forest[i][j] or x == len(forest):
            bottom = abs(x - i)
            break
    for y in reversed(range(j - 1, -1, -1)):
        if forest[i][y] >= forest[i][j] or y == 0:
            left = abs(y - j)
            break
    for y in range(j + 1, len(forest[0])):
        if forest[i][y] >= forest[i][j] or y == len(forest[0]):
            right = abs(y - j)
            break
    if i==3 and j==2:
        print(left, top, right, bottom)

    return left * top * right * bottom


def answer1():
    data = read_file()
    forest = create_forest(data)
    visible_trees = 0
    for i in range(len(data)):
        for j in range(len(data[0])):
            if is_visible(i, j, forest):
                visible_trees += 1
    print(visible_trees)


def answer2():
    data = read_file()
    forest = create_forest(data)
    max_scenic_score = 0
    max_i, max_j = 0, 0
    for i in range(1, len(data) - 1):
        for j in range(1, len(data[0]) - 1):
            if calculate_scenic_score(i, j, forest) > max_scenic_score:
                print("New best: [" + str(i) + "," + str(j) + "]")
                max_scenic_score = calculate_scenic_score(i, j, forest)
                print("With score: " + str(max_scenic_score))
                max_i = i
                max_j = j
    print(max_scenic_score)
    print(str(max_i) + ", " + str(max_j))


if __name__ == "__main__":
    print("Answer 1:")
    answer1()
    print("Answer 2:")
    answer2()
