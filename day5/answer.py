def read_file():
    data = []
    for x in open("input.txt"):
        data.append(x[:-1])
    return data


def create_array_per_pile(piles):
    new_piles = []
    [new_piles.append([]) for _ in range(9)]
    for pile_id in range(len(piles)):
        piles[pile_id] += "    "
    for line in piles:
        for x in range(len(line) // 4):
            character = line[4 * x + 1]
            if character == ' ': continue
            new_piles[x].append(character)
    return new_piles


def translate_instructions(instructions):
    new_instructions = []
    for line in instructions:
        line = line.split(' ')
        new_instructions.append([int(line[1]), int(line[3]), int(line[5])])
    return new_instructions


def answer1():
    data = read_file()
    piles = data[:8]
    instructions = data[10:]
    piles.reverse()
    piles = create_array_per_pile(piles)
    instructions = translate_instructions(instructions)
    for instruction in instructions:
        from_pile_index = instruction[1] - 1
        to_pile_index = instruction[2] - 1
        for _ in range(instruction[0]):
            piles[to_pile_index].append(piles[from_pile_index][len(piles[from_pile_index])-1])
            piles[from_pile_index].pop(len(piles[from_pile_index])-1)
    for pile in piles:
        print(pile[len(pile)-1])


def answer2():
    data = read_file()
    piles = data[:8]
    instructions = data[10:]
    piles.reverse()
    piles = create_array_per_pile(piles)
    instructions = translate_instructions(instructions)
    for instruction in instructions:
        from_pile_index = instruction[1] - 1
        to_pile_index = instruction[2] - 1
        start_range = len(piles[from_pile_index]) - instruction[0]
        end = len(piles[from_pile_index])
        piles[to_pile_index].extend(piles[from_pile_index][start_range:end])
        for _ in range(instruction[0]):
            piles[from_pile_index].pop(len(piles[from_pile_index]) - 1)
    for pile in piles:
        print(pile[len(pile) - 1])


if __name__ == "__main__":
    # answer1()
    answer2()
