import numpy as np

def read_file():
    data = []
    for x in open("input.txt"):
        data.append(x[:-1])
    return data


def answer1():
    data = read_file()
    new_data = []
    for row in data:
        if row.count('.') == len(data[0]):
            new_data.append(row)
        new_data.append(row)
    new_data = list(map(list, zip(*new_data)))
    new_new_data = []
    for row in new_data:
        if row.count('.') == len(new_data[0]):
            new_new_data.append(row)
        new_new_data.append(row)
    data = list(map(list, zip(*new_new_data)))
    [print(x) for x in data]
    pairs = []
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == '#':
                pairs.append((i,j))
    print(pairs)
    total_result = 0
    for i in pairs:
        for j in pairs:
            total_result += abs(i[0]-j[0])+abs(i[1]-j[1])
    print(total_result/2)


def answer2():
    data = read_file()
    expansition_ratio = 1000000

    pairs = []
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == '#':
                pairs.append((i,j))
    
    empty_row_ids = []
    for i in range(len(data)):
        if data[i].count('.') == len(data[i]):
            empty_row_ids.append(i)
    print(empty_row_ids)

    data = list(map(list, zip(*data)))
    empty_col_ids = []
    for i in range(len(data)):
        if data[i].count('.') == len(data[i]):
            empty_col_ids.append(i)
    print(empty_col_ids)
    
    print(pairs)
    total_result = 0
    for i in pairs:
        for j in pairs:
            lower_row = min(i[0],j[0])
            higher_row = max(i[0],j[0])
            steps = set(range(lower_row,higher_row))
            rows_overlap = list(steps & set(empty_row_ids))
            total_result += len(rows_overlap)*expansition_ratio + len(steps) - len(rows_overlap)
            # print(i,j)
            # print(lower_row, higher_row, steps, empty_row_ids, rows_overlap,total_result)
    
    for i in pairs:
        for j in pairs:
            lower_col = min(i[1],j[1])
            higher_col = max(i[1],j[1])
            steps = set(range(lower_col,higher_col))
            cols_overlap = list(steps & set(empty_col_ids))
            total_result += len(cols_overlap)*expansition_ratio + len(steps) - len(cols_overlap)
            # print(i,j)
            # print(lower_col, higher_col, steps, empty_row_ids, rows_overlap,total_result)
    print(total_result/2)
    
    
    

if __name__ == "__main__":
    print("Answer 1:")
    answer1()
    print("Answer 2:")
    answer2()
