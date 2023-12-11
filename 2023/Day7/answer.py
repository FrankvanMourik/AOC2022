

def read_file():
    data = []
    for x in open("sample.txt"):
        data.append(x[:-1])
    return data


def answer1():
    data = read_file()
    processed_hands = []
    for line in data:
        parts = line.split()
        hand = parts[0]
        bid = int(parts[1])
        if len(set(hand)) == 1:
            type = 0
        elif len(set(hand)) == 2:
            four = False
            for char in set(hand):
                if hand.count(char) == 4:
                    four = True
            if four:
                type = 1
            else:
                type = 2
        elif len(set(hand)) == 3:
            three = False
            for char in set(hand):
                if hand.count(char) == 3:
                    three = True
            if three:
                type = 3
            else:
                type = 4
        elif len(set(hand)) == 4:
            type = 5
        else:
            type = 6
        processed_hands.append([hand, type, bid])
    final_list = []
    for i in range(7):
        temp_list = [p for p in processed_hands if p[1] == i]
        final_list.extend(sort(temp_list))
    print(processed_hands)
    print(final_list)
    total_results = 0
    for i in range(len(data)):
        total_results += final_list[i][2] * (len(data)-i)
    print(total_results)

def sort(same_type_array):
    order = 'AKQJT98765432'
    return sorted(same_type_array, key=lambda word: [order.index(c) if c in order else ord(c) for c in word[0]])

def answer2():
    data = read_file()
    processed_hands = []
    for line in data:
        parts = line.split()
        hand = parts[0]
        hand_without_joker = ""
        for char in hand:
            if char != 'J':
                hand_without_joker += char
        bid = int(parts[1])
        if len(set(hand_without_joker)) <= 1:
            type = 0
        elif len(set(hand_without_joker)) == 2:
            four = False
            for char in set(hand):
                if hand.count(char) + hand.count('J') == 4:
                    four = True
            if four:
                type = 1
            else:
                type = 2
        elif len(set(hand_without_joker)) == 3:
            three = False
            for char in set(hand):
                if hand.count(char) + hand.count('J') == 3:
                    three = True
            if three:
                type = 3
            else:
                type = 4
        elif len(set(hand_without_joker)) == 4:
            type = 5
        else:
            type = 6
        processed_hands.append([hand, type, bid])
    final_list = []
    for i in range(7):
        temp_list = [p for p in processed_hands if p[1] == i]
        final_list.extend(sort_2(temp_list))
    print(processed_hands)
    print(final_list)
    total_results = 0
    for i in range(len(data)):
        total_results += final_list[i][2] * (len(data)-i)
    print(total_results)


def sort_2(same_type_array):
    order = 'AKQT98765432J'
    return sorted(same_type_array, key=lambda word: [order.index(c) if c in order else ord(c) for c in word[0]])


if __name__ == "__main__":
    print("Answer 1:")
    answer1()
    print("Answer 2:")
    answer2()
