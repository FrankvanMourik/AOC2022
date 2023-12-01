import re

def solve():
    present = {int(line.replace('B', '1').replace('F', '0').replace('R', '1').replace('L', '0'),2) for line in open('exercise9.txt')}
    print(set(range(min(present), max(present)))-set(present))


if __name__ == "__main__":
    solve()
    d = {int(re.sub('B|R', '1', re.sub('F|L', '0', x[:10])), 2) for x in open('exercise9.txt')}
    print(set(range(min(d), max(d))) - d)
