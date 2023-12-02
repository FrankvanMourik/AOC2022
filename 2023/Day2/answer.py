def read_file():
    data = []
    for x in open("input.txt"):
        data.append(x[:-1])
    return data


def answer1():
    data = read_file()
    total = 0
    max_red = 12
    max_green = 13
    max_blue = 14
    for line in data:
        possible = True
        parts = line.split(': ')
        game_nr = parts[0].split()
        results = parts[1].split('; ')
        sub_results = []
        for sub in results:
            sub_results.extend(sub.split(', '))
        print(sub_results)
        for colour in sub_results:
            parts = colour.split(' ')
            if parts[1] == 'red':
                if int(parts[0]) > max_red:
                    possible = False
            elif parts[1] == 'blue':
                if int(parts[0]) > max_blue:
                    possible = False
            elif parts[1] == 'green':
                if int(parts[0]) > max_green:
                    possible = False
        if possible:
            total += int(game_nr[1])
    print(total)


def answer2():
    data = read_file()
    total = 0
    for line in data:
        max_red = 0
        max_green = 0
        max_blue = 0
        parts = line.split(': ')
        results = parts[1].split('; ')
        sub_results = []
        for sub in results:
            sub_results.extend(sub.split(', '))
        print(sub_results)
        for colour in sub_results:
            parts = colour.split(' ')
            if parts[1] == 'red':
                if int(parts[0]) > max_red:
                    max_red = int(parts[0])
            elif parts[1] == 'blue':
                if int(parts[0]) > max_blue:
                    max_blue = int(parts[0])
            elif parts[1] == 'green':
                if int(parts[0]) > max_green:
                    max_green = int(parts[0])
        total += (max_green * max_blue * max_red)
    print(total)

if __name__ == "__main__":
    print("Answer 1:")
    answer1()
    print("Answer 2:")
    answer2()
