def read_file():
    data = []
    for x in open("input.txt"):
        data.append(x[:-1])
    return data


def answer1():
    dict = {}
    root_dir = "./"
    current_dir = "./"
    data = read_file()
    i = 0
    while i < len(data):
        print("Current dir: " + current_dir)
        print('Line:' + str(i) + ": " + data[i])
        if '$' in data[i]:
            if "ls" == data[i][2:4]:
                i += 1
                continue
            else:
                if data[i] == "$ cd /":
                    current_dir = root_dir
                    i += 1
                    continue
                elif "$ cd .." == data[i]:
                    current_dir = current_dir.split('/')
                    if len(current_dir) <= 3:
                        current_dir = root_dir
                    else:
                        current_dir = '/'.join(current_dir[:-2]) + '/'
                else:
                    line = data[i].split()
                    current_dir = current_dir + line[len(line)-1] + "/"
        else:
            line = data[i].split()
            if line[0] == "dir":
                i += 1
                continue
            else:
                size = int(line[0])
                if dict.keys().__contains__(current_dir):
                    dict[current_dir] += size
                else:
                    dict[current_dir] = size
        i += 1
    dict_keys_sorted = list(dict.keys())
    print(dict_keys_sorted[0:10])
    dict_keys_sorted.sort(key=len, reverse=True)
    print(dict_keys_sorted[0:10])

    for key in dict_keys_sorted:
        for other_key in dict_keys_sorted:
            if key == other_key:
                continue
            if key in other_key:
                dict[key] += dict[other_key]
    for key in dict.keys():
        print(str(dict[key]) + "\t" + key)
    print([dict[root_dir]])
    small = [x for x in dict.values() if x <= 100000]
    print("Answer: " + str(sum([x for x in dict.values() if x <= 100000])))


def answer2():
    dict = {}
    root_dir = "./"
    current_dir = "./"
    data = read_file()
    i = 0
    while i < len(data):
        print("Current dir: " + current_dir)
        print('Line:' + str(i) + ": " + data[i])
        if '$' in data[i]:
            if "ls" == data[i][2:4]:
                i += 1
                continue
            else:
                if data[i] == "$ cd /":
                    current_dir = root_dir
                    i += 1
                    continue
                elif "$ cd .." == data[i]:
                    current_dir = current_dir.split('/')
                    if len(current_dir) <= 3:
                        current_dir = root_dir
                    else:
                        current_dir = '/'.join(current_dir[:-2]) + '/'
                else:
                    line = data[i].split()
                    current_dir = current_dir + line[len(line) - 1] + "/"
        else:
            line = data[i].split()
            if line[0] == "dir":
                i += 1
                continue
            else:
                size = int(line[0])
                if dict.keys().__contains__(current_dir):
                    dict[current_dir] += size
                else:
                    dict[current_dir] = size
        i += 1
    dict_keys_sorted = list(dict.keys())
    print(dict_keys_sorted[0:10])
    dict_keys_sorted.sort(key=len, reverse=True)
    print(dict_keys_sorted[0:10])

    for key in dict_keys_sorted:
        for other_key in dict_keys_sorted:
            if key == other_key:
                continue
            if key in other_key:
                dict[key] += dict[other_key]
    for key in dict.keys():
        print(str(dict[key]) + "\t" + key)
    print([dict[root_dir]])
    small = [x for x in dict.values() if x <= 100000]
    print("Answer: " + str(sum([x for x in dict.values() if x <= 100000])))


if __name__ == "__main__":
    print("Answer 1:")
    answer1()
    print("Answer 2:")
    answer2()
