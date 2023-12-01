def solve(right):
    nr_trees = 0
    nr_characters = 31
    pos = 0
    with open('exercise5.txt') as my_file:
        for line in my_file:
            pos = pos % nr_characters
            if line[pos] == "#":
                nr_trees += 1
            pos += right
    return nr_trees


def solve2row(right):
    nr_trees = 0
    nr_characters = 31
    pos = 0
    i = 0
    with open('exercise5.txt') as my_file:
        for line in my_file:
            i += 1
            if i % 2 == 0:
                continue
            pos = pos % nr_characters
            if line[pos] == "#":
                nr_trees += 1
            pos += right
    return nr_trees

if __name__ == "__main__":
    solve1 = solve(1)
    solve2 = solve(3)
    solve3 = solve(5)
    solve4 = solve(7)
    solve5 = solve2row(1)
    print(solve1, solve2, solve3, solve4, solve5)
    print(solve1 * solve2 * solve3 * solve4 * solve5)