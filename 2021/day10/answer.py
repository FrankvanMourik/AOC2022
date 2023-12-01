from pprint import pprint


def result1():
    data = []
    mapping = {
        "[": "]",
        "{": "}",
        "(": ")",
        "<": ">"
    }
    print(mapping["{"])
    for x in open("input.txt"):
        data.append(x[:-1])
    print(data)
    result = ""
    for x in data:
        check = ""
        for char in x:
            if len(check) > 0 and char == mapping[check[-1]]:
                check = check[:-1]
            elif char in "{[(<":
                check += char
            else:
                result += char
                break

    return 3 * result.count(')') + 57 * result.count(']') + 1197 * result.count('}') + 25137 * result.count('>')


def result2(fileName):
    data = []
    mapping = {
        "[": "]",
        "{": "}",
        "(": ")",
        "<": ">"
    }
    score_mapping = {
        "]": 2,
        "}": 3,
        ")": 1,
        ">": 4
    }
    print(mapping["{"])
    for x in open(fileName):
        data.append(x[:-1])
    print(data)
    new_data = []
    for x in data:
        finished = True
        check = ""
        for char in x:
            if len(check) > 0 and char == mapping[check[-1]]:
                check = check[:-1]
            elif char in "{[(<":
                check += char
            else:
                finished = False
                break
        if finished and len(check) > 0:
            complete = [mapping[x] for x in check]
            new_data.append(complete[::-1])
    scores = []
    for complete in new_data:
        result = 0
        for char in complete:
            result *= 5
            result += score_mapping[char]
        scores.append(result)
    scores.sort()
    return scores[len(scores)//2]


def test():
    print(result2("sample.txt"))


def result2_golf():
    print("No way")


if __name__ == "__main__":
    # print(test())
    print(result2("input.txt"))
