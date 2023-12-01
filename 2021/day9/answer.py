def result1():
    matrix = []
    for x in open("input.txt"):
        matrix.append([b for b in x])
    for i in range(len(matrix)):
        matrix[i] = matrix[i][:-1]
        matrix[i] = [int(x) for x in matrix[i]]
    summ = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if isLocalMinimum(i, j, matrix):
                summ = summ + int(matrix[i][j]) + 1
    return summ


def isLocalMinimum(i, j, matrix):
    if i == 0:
        if j == 0:
            return True if matrix[i][j] < matrix[i + 1][j] and matrix[i][j] < matrix[i][j + 1] else False
        elif j == len(matrix) - 1:
            return True if matrix[i][j] < matrix[i + 1][j] and matrix[i][j] < matrix[i][j - 1] else False
        else:
            return True if matrix[i][j] < matrix[i + 1][j] and matrix[i][j] < matrix[i][j + 1] and matrix[i][j] < \
                           matrix[i][j - 1] else False
    elif i == len(matrix) - 1:
        if j == 0:
            return True if matrix[i][j] < matrix[i][j + 1] and matrix[i][j] < matrix[i - 1][j] else False
        elif j == len(matrix) - 1:
            return True if matrix[i][j] < matrix[i - 1][j] and matrix[i][j] < matrix[i][j - 1] else False
        else:
            return True if matrix[i][j] < matrix[i - 1][j] and matrix[i][j] < matrix[i][j + 1] and matrix[i][j] < \
                           matrix[i][j - 1] else False
    else:
        if j == 0:
            return True if matrix[i][j] < matrix[i + 1][j] and matrix[i][j] < matrix[i - 1][j] and matrix[i][j] < \
                           matrix[i][j + 1] else False
        elif j == len(matrix) - 1:
            return True if matrix[i][j] < matrix[i + 1][j] and matrix[i][j] < matrix[i - 1][j] and matrix[i][j] < \
                           matrix[i][j - 1] else False
        else:
            return True if matrix[i][j] < matrix[i + 1][j] and matrix[i][j] < matrix[i - 1][j] and matrix[i][j] < \
                           matrix[i][j + 1] and matrix[i][j] < matrix[i][j - 1] else False


def result2():
    a = [[*map(int, b)] for *b, c in open('input.txt')];
    b = enumerate
    c = lambda x, y: [(o, p) for o, p in zip([x, x + 1, x, x - 1], [y + 1, y, y - 1, y]) if
                      0 <= o < len(a) and 0 <= p < len(a[o])]
    d = lambda x, y: {(x, y)} | {s for o, p in c(x, y) if 9 > a[o][p] > a[x][y] for s in d(o, p)}
    q = 1
    [q := -q * w for w in sorted(len(d(f, h)) for f, g in b(a) for h, i in b(g))[-3:]]
    print(-q)


def result2_golf():
    print("No way")


if __name__ == "__main__":
    print(result2())
