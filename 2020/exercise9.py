def solve():
    highest = 0
    with open('exercise9.txt') as my_file:
        for line in my_file:
            current = int(line[0:7].replace('B', '1').replace('F', '0'), 2)*8 + int(line[8:10].replace('R', '1').replace('L', '0'),2)
            highest = max(current, highest)
    print(highest)


if __name__ == "__main__":
    solve()
