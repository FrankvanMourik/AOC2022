def solve():
    accepted = 0
    with open('exercise7.txt') as my_file:
        passports = []
        passport = []
        for line in my_file:
            if line == "\n":
                passports.append(passport)
                passport = []
                continue
            items = line.split()
            passport.extend(items)
        for passport in passports:
            cidfound = False
            if len(passport) == 8:
                accepted += 1
            elif len(passport) == 7:
                for item in passport:
                    if item[0:3] == "cid":
                        cidfound = True
                        break
                if not(cidfound):
                    accepted += 1
    print(len(passports))
    print(accepted)





if __name__ == "__main__":
    solve()