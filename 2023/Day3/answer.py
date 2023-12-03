def read_file():
    data = []
    for x in open("input.txt"):
        data.append(x[:-1])
    return data


def answer1():
    data = read_file()
    sum = 0
    total_rows = len(data)
    total_columns = len(data[0])
    for i in range(len(data)):
        nr_to_skip = 0
        for j in range(len(data[0])):
            number_found = False
            if nr_to_skip > 0:
                nr_to_skip -= 1
                continue
            k = j
            if data[i][j] in '0123456789':
                number = 0
                while True:
                    if k < total_columns and data[i][k] in '0123456789':
                        k += 1
                    else:
                        k -= 1
                        number = data[i][j:k+1]
                        print(number)
                        break
                number_found = True
            # Check
            if number_found:
                neighbours = []
                if i > 0:
                    neighbours.extend(data[i-1][j:k+1])
                if i < total_rows - 1:
                    neighbours.extend(data[i+1][j:k+1])
                if j > 0:
                    neighbours.extend(data[i][j-1])
                if k < total_columns - 1:
                    neighbours.extend(data[i][k+1])
                if i > 0 and j > 0:
                    neighbours.extend(data[i-1][j-1])
                if i > 0 and k < total_columns - 1:
                    neighbours.extend(data[i-1][k+1])
                if i < total_rows - 1 and j > 0:
                    neighbours.extend(data[i+1][j-1])
                if i < total_rows - 1 and k < total_columns - 1:
                    neighbours.extend(data[i+1][k+1])
                print(neighbours)
                add_to_sum = False
                for char in neighbours:
                    if char not in '0123456789.':
                        add_to_sum = True
                if add_to_sum:
                    sum += int(number)
                print(add_to_sum)
                print()
                nr_to_skip = k-j
    print('Total sum: ', sum)


def answer2():
    data = read_file()
    sum = 0
    total_rows = len(data)
    total_columns = len(data[0])
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == '*':
                neighbours = []
                # Top left
                if data[i-1][j-1] in '0123456789':
                    start = j-1
                    end = j-1
                    while True:
                        if start >= 0 and data[i-1][start] in '0123456789':
                            start -= 1
                        else:
                            start += 1
                            break
                    while True:
                        if end < total_columns - 1 and data[i-1][end] in '0123456789':
                            end += 1
                        else:
                            end -= 1
                            break
                    neighbours.append(data[i-1][start:end+1])
                # Top right
                if data[i-1][j+1] in '0123456789':
                    start = j+1
                    end = j+1
                    while True:
                        if start >= 0 and data[i-1][start] in '0123456789':
                            start -= 1
                        else:
                            start += 1
                            break
                    while True:
                        if end < total_columns - 1 and data[i-1][end] in '0123456789':
                            end += 1
                        else:
                            end -= 1
                            break
                    neighbours.append(data[i-1][start:end+1])
                # Bottom left
                if data[i+1][j-1] in '0123456789':
                    start = j-1
                    end = j-1
                    while True:
                        if start >= 0 and data[i+1][start] in '0123456789':
                            start -= 1
                        else:
                            start += 1
                            break
                    while True:
                        if end < total_columns - 1 and data[i+1][end] in '0123456789':
                            end += 1
                        else:
                            end -= 1
                            break
                    neighbours.append(data[i+1][start:end+1])
                # Bottom right
                if data[i+1][j+1] in '0123456789':
                    start = j+1
                    end = j+1
                    while True:
                        if start >= 0 and data[i+1][start] in '0123456789':
                            start -= 1
                        else:
                            start += 1
                            break
                    while True:
                        if end < total_columns - 1 and data[i+1][end] in '0123456789':
                            end += 1
                        else:
                            end -= 1
                            break
                    neighbours.append(data[i+1][start:end+1])
                # Left
                if data[i][j-1] in '0123456789':
                    start = j-1
                    end = j-1
                    while True:
                        if start >= 0 and data[i][start] in '0123456789':
                            start -= 1
                        else:
                            start += 1
                            break
                    while True:
                        if end < total_columns - 1 and data[i][end] in '0123456789':
                            end += 1
                        else:
                            end -= 1
                            break
                    neighbours.append(data[i][start:end+1])
                # Right
                if data[i][j+1] in '0123456789':
                    start = j+1
                    end = j+1
                    while True:
                        if start >= 0 and data[i][start] in '0123456789':
                            start -= 1
                        else:
                            start += 1
                            break
                    while True:
                        if end < total_columns - 1 and data[i][end] in '0123456789':
                            end += 1
                        else:
                            end -= 1
                            break
                    neighbours.append(data[i][start:end+1])
                # Top
                if data[i-1][j] in '0123456789':
                    start = j
                    end = j
                    while True:
                        if start >= 0 and data[i-1][start] in '0123456789':
                            start -= 1
                        else:
                            start += 1
                            break
                    while True:
                        if end < total_columns - 1 and data[i-1][end] in '0123456789':
                            end += 1
                        else:
                            end -= 1
                            break
                    neighbours.append(data[i-1][start:end+1])
                # Bottom
                if data[i+1][j] in '0123456789':
                    start = j
                    end = j
                    while True:
                        if start >= 0 and data[i+1][start] in '0123456789':
                            start -= 1
                        else:
                            start += 1
                            break
                    while True:
                        if end < total_columns - 1 and data[i+1][end] in '0123456789':
                            end += 1
                        else:
                            end -= 1
                            break
                    neighbours.append(data[i+1][start:end+1])
                
                unique_neighbours = unique(neighbours)
                if len(unique_neighbours) != len(neighbours):
                    print("Not unique: Gear at position (",i,',',j,') with neighbour numbers: ',neighbours)
                if len(unique_neighbours) == 2:
                    sum += (int(unique_neighbours[0]) * int(unique_neighbours[1]))
                    # print("Added: Gear at position (",i,',',j,') with neighbour numbers: ',neighbours)
                # else:
                    # print("Rejected: Gear at position (",i,',',j,') with neighbour numbers: ',unique_neighbours)
                
    print('Total sum: ', sum)


def unique(list1):
    unique_list = []
    for x in list1:
        if x not in unique_list:
            unique_list.append(x)
    return unique_list


if __name__ == "__main__":
    print("Answer 1:")
    answer1()
    print("Answer 2:")
    answer2()
