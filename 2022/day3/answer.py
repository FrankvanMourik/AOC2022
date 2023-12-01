def read_file():
    data = []
    for x in open("input.txt"):
        data.append(x[:-1])
    return data


def strIntersection(s1, s2):
  out = ""
  for c in s1:
    if c in s2 and not c in out:
      out += c
  return out


def answer1():
    data = read_file()
    overlap = []
    for x in data:
        half = len(x)//2
        x1 = x[:half]
        x2 = x[half:]
        overlap.append(strIntersection(x1, x2))
    som = 0
    for x in overlap:
        if x < 'a':
            som += ord(x)-38
        else:
            som += ord(x)-96
    print(som)


def answer2():
    data = read_file()
    badges = []
    for x in range(len(data)//3):
        first = data[3*x]
        second = data[3*x+1]
        third = data[3*x+2]
        temp = strIntersection(first, second)
        badges.append(strIntersection(temp, third))
    som = 0
    for x in badges:
        if x < 'a':
            som += ord(x) - 38
        else:
            som += ord(x) - 96
    print(som)


if __name__ == "__main__":
    answer1()
    answer2()
