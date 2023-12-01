from pprint import pprint


def result1(fileName):
    data = []
    for x in open(fileName):
        data.append(x[:-1])
    result = data[0]
    mapping = data[2:]
    map_dict = {}
    for x in mapping:
        items =x.split(" -> ")
        map_dict[items[0]] = items[1]
    NR_DAYS = 10
    for i in range(NR_DAYS):
        result_after_day = ""
        for j in range(len(result)-1):
            result_after_day = result_after_day + result[j] + map_dict[result[j:j+2]]
        result = result_after_day + result[-1]
        print(i, len(result))
    letters = set(result)
    occur = [result.count(x) for x in letters]
    print(max(occur)-min(occur))

def result2(fileName):
    data = []
    for x in open(fileName):
        data.append(x[:-1])
    result = data[0]
    mapping = data[2:]
    map_dict = {}
    for x in mapping:
        items = x.split(" -> ")
        map_dict[items[0]] = items[1]
    NR_DAYS = 40
    count_mapping = {}

    # processing initial result
    for i in range(len(result)-1):
        if result[i:i+2] in count_mapping:
            count_mapping[result[i:i+2]] += 1
        else:
            count_mapping[result[i:i+2]] = 1

    first_char = result[0]
    last_char = result[-1]
    print(count_mapping)
    for i in range(NR_DAYS):
        new_count_mapping = count_mapping.copy()
        for key in new_count_mapping.keys():
            new_pair1 = key[0]+map_dict[key]
            new_pair2 = map_dict[key]+key[1]
            if new_pair1 in count_mapping:
                count_mapping[new_pair1] += new_count_mapping[key]
            else:
                count_mapping[new_pair1] = new_count_mapping[key]
            if new_pair2 in count_mapping:
                count_mapping[new_pair2] += new_count_mapping[key]
            else:
                count_mapping[new_pair2] = new_count_mapping[key]
    print(count_mapping)
    letters = [x for y in count_mapping.keys() for x in y]
    print(letters)
    unique_letters = set(letters)
    final_count = {}
    for x in unique_letters:
        final_count[x] = 0
    for key in count_mapping.keys():
        for letter in key:
            final_count[letter] += count_mapping[key]
    for key in final_count:
        final_count[key] *= 2
    final_count[first_char] -= 1
    final_count[last_char] -= 1
    occur = [final_count[x] for x in final_count.keys()]
    print(max(occur)-min(occur))



def test():
    return result1("sample.txt")


def result2_golf():
    print("No way")


if __name__ == "__main__":
    # print(test())
    # print(result1("input.txt"))
    print(result2("input.txt"))
