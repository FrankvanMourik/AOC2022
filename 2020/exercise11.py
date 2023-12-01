def solve():
    total = 0
    with open('exercise11.txt') as my_file:
        groups = []
        person = ""
        for line in my_file:
            if line == "\n":
                groups.append(person)
                person = ""
                continue
            person = person + line.split("\n")[0]
        groups.append(person)
        for group in groups:
            total += len(''.join(set(group)))
            print(group)
            print(''.join(set(group)))
        print(total)

if __name__ == "__main__":
    solve()
