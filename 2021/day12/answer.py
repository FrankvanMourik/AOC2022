from pprint import pprint


def result1(fileName):
    paths = []
    caves = []
    for x in open(fileName):
        xs = x[:-1].split('-')
        caves.extend(xs)
        paths.append(xs)
    caves = set(caves)
    small_caves = [x for x in caves if not x.isupper()]
    large_caves = [x for x in caves if x.isupper()]
    routes = 0
    visited_small_caves = ['start']
    print(paths)
    routes += visit(caves, paths, visited_small_caves,'start')
    return "The number of paths is: "+ str(routes)


def visit(caves, paths, visited_small_caves, location):
    if location == 'end':
        return 1
    paths_from_location = [x for x in paths if location in x]
    routes = 0
    print(location, paths_from_location, visited_small_caves)
    for path in paths_from_location:
        if path[0] == location:
            if path[1] not in visited_small_caves:
                if not path[1].isupper():
                    visited_small_caves.append(path[1])
                routes += visit(caves, paths, visited_small_caves, path[1])
        else:
            if path[0] not in visited_small_caves:
                if not path[0].isupper():
                    visited_small_caves.append(path[0])
                routes += visit(caves, paths, visited_small_caves, path[0])
    return routes



def result2(fileName):
    paths = []
    caves = []
    for x in open(fileName):
        xs = x[:-1].split('-')
        caves.extend(xs)
        paths.append(xs)
    caves = set(caves)
    small_caves = [x for x in caves if not x.isupper()]
    large_caves = [x for x in caves if x.isupper()]
    routes = 0
    visited_small_caves = ['start']
    print(paths)
    routes += visit(caves, paths, visited_small_caves, 'start')
    return "The number of paths is: " + str(routes)


def test():
    return result1("sample.txt")


def result2_golf():
    print("No way")


if __name__ == "__main__":
    print(test())
    # print(result1("input.txt"))
    # print(result2("input.txt"))
