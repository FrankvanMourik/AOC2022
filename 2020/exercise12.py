def solve():
    total = 0
    with open('exercise11.txt') as my_file:
        person = ""
        newLine = True
        for line in my_file:
            if line == "\n":
                total += len(person)
                person = ""
                newLine = True
                continue
            res = ""
            if newLine:
                newLine = False
                person = ''.join(set(line.split("\n")[0]))
                print(person)
            else:
                for i in person:
                    if i in line.split("\n")[0] and not i in res:
                        res += i
                person = res
        total += len(person)
        print(total)


if __name__ == "__main__":
    solve()
