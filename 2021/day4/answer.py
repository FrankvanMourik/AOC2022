def result1():
    data = []
    for b in open('input.txt'):
        data.append(b)
    drawn_numbers = data[0].split(',')
    print(drawn_numbers)
    bingo_cards = []
    begin = 2
    for i in range(len(data)//6):
        cart = []
        [cart.append(data[i*6+begin+x].split()) for x in range(5)]
        cart.extend(list(map(list, zip(*cart))))
        print(cart)
        bingo_cards.append(cart)
    print(len(bingo_cards))
    for nr in drawn_numbers:
        for cart in bingo_cards:
            for row in cart:
                copy = row.copy()
                [row.remove(x) for x in copy if x==nr]
                if len(row)==0:
                    sum = 0
                    for rows in cart[:5]:
                        for nrs in rows:
                            sum += int(nrs)
                    return int(nr)*sum
    return 0


def result2():
    data = []
    for b in open('input.txt'):
        data.append(b)
    drawn_numbers = data[0].split(',')
    print(drawn_numbers)
    bingo_cards = []
    begin = 2
    for i in range(len(data) // 6):
        card = []
        [card.append(data[i * 6 + begin + x].split()) for x in range(5)]
        card.extend(list(map(list, zip(*card))))
        print(card)
        bingo_cards.append(card)
    print(len(bingo_cards))
    for nr in drawn_numbers:
        to_delete = set()
        for i, card in enumerate(bingo_cards):
            for row in card:
                copy = row.copy()
                [row.remove(x) for x in copy if x == nr]
                if len(row) == 0:
                    if len(bingo_cards) == 1:
                        sum = 0
                        for rows in card[:5]:
                            for nrs in rows:
                                sum += int(nrs)
                        return int(nr) * sum
                    to_delete |= {i}
        bingo_cards = [carD for i, carD in enumerate(bingo_cards) if i not in to_delete]
    return 0


def result2_golf():
    print("Nee")


if __name__ == "__main__":
    print(result2())
