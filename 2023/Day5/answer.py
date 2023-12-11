def read_file():
    data = []
    for x in open("input.txt"):
        data.append(x[:-1])
    return data


def answer1():
    data = read_file()
    stages = ['seed', 'soil','fert','wate','ligh','temp','humi','loca']
    print()
    seeds = data[0].split(':')
    seeds = seeds[1].split()
    print(seeds)
    results = []
    for s in range(len(seeds)):
        seed = int(seeds[s])
        or_seed = seed
        print(f"Starting with seed: {seed}")
        current_stage = 0
        count_empty = 0
        for i in range(2,len(data)):
            if i == len(data)-1:
                results.append(seed)
                continue
            if data[i] == '':
                count_empty += 1
                if current_stage != count_empty:
                    current_stage += 1
                    print(f"Not found! Update seed: from {stages[current_stage]}{seed} to {stages[current_stage+1]}{seed} via line {data[i]}")
                    if current_stage >= 7:
                        print(f"End of seed: {or_seed}, results: {seed}")
                        results.append(seed)
                        break
                continue
            if current_stage >= 7:
                print(f"End of seed: {or_seed}, results: {seed}")
                results.append(seed)
                break
            if current_stage == count_empty and data[i][0] in '0123456789':
                dest, source, steps = data[i].split()
                if seed in range(int(source), int(source)+int(steps)):
                    old_seed = seed
                    seed = int(dest) + seed - int(source)
                    print(f"Found! Update seed: from {stages[current_stage]}{old_seed} to {stages[current_stage+1]}{seed} via line {data[i]}")
                    current_stage += 1

    results.append(seed)
    print(results)
    print(min(results))



def answer2():
    data = read_file()
    stages = ['seed', 'soil','fert','wate','ligh','temp','humi','loca']
    print()
    seeds_numbers = data[0].split(':')
    seeds_numbers = seeds_numbers[1].split()
    min_res = -1
    for i in range(0,len(seeds_numbers),2):
        print('Started with new range')
        for seed in range(int(seeds_numbers[i]),int(seeds_numbers[i])+int(seeds_numbers[i+1])):
            # print(f"Starting with seed: {seed}")
            current_stage = 0
            count_empty = 0
            for i in range(2,len(data)):
                if i == len(data)-1:
                    if min_res == -1 or int(seed) < min_res:
                        min_res = seed
                    continue
                if data[i] == '':
                    count_empty += 1
                    if current_stage != count_empty:
                        current_stage += 1
                        # print(f"Not found! Update seed: from {stages[current_stage]}{seed} to {stages[current_stage+1]}{seed} via line {data[i]}")
                        if current_stage >= 7:
                            # print(f"End of seed: {or_seed}, results: {seed}")
                            if min_res == -1 or int(seed) < min_res:
                                min_res = seed
                            break
                    continue
                if current_stage >= 7:
                    # print(f"End of seed: {or_seed}, results: {seed}")
                    if min_res == -1 or int(seed) < min_res:
                        min_res = seed
                    break
                if current_stage == count_empty and data[i][0] in '0123456789':
                    dest, source, steps = data[i].split()
                    if seed in range(int(source), int(source)+int(steps)):
                        old_seed = seed
                        seed = int(dest) + seed - int(source)
                        # print(f"Found! Update seed: from {stages[current_stage]}{old_seed} to {stages[current_stage+1]}{seed} via line {data[i]}")
                        current_stage += 1
    if min_res == -1 or int(seed) < min_res:
        min_res = seed    # print(results)
    print(min_res)


if __name__ == "__main__":
    # print("Answer 1:")
    # answer1()
    print("Answer 2:")
    answer2()
