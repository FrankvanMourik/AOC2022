def read_file():
    data = []
    for x in open("input.txt"):
        data.append(x[:-1])
    return data


def answer1():
    data = read_file()
    total_score = 0
    for x in data:
        opponent = x[0]
        you = x[2]
        if you == 'X':
            total_score += 1
            if opponent == 'A':
                total_score += 3
            elif opponent == 'C':
                total_score += 6
        elif you == "Y":
            total_score += 2
            if opponent == 'A':
                total_score += 6
            elif opponent == 'B':
                total_score += 3
        else:
            total_score += 3
            if opponent == 'B':
                total_score += 6
            elif opponent == 'C':
                total_score += 3
    print(total_score)


def answer2():
    data = read_file()
    total_score = 0
    for x in data:
        opponent = x[0]
        outcome = x[2]
        if outcome == 'X':  # lose
            if opponent == 'A':
                total_score += 3
            elif opponent == 'B':
                total_score += 1
            else:
                total_score += 2
        elif outcome == "Y":  # draw
            total_score += 3
            if opponent == 'A':
                total_score += 1
            elif opponent == 'B':
                total_score += 2
            else:
                total_score += 3
        else:  # win
            total_score += 6
            if opponent == 'A':
                total_score += 2
            elif opponent == 'B':
                total_score += 3
            else:
                total_score += 1
    print(total_score)


if __name__ == "__main__":
    answer1()
    answer2()
