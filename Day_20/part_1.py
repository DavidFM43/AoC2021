import sys
sys.setrecursionlimit(5000)


def solve(input):
    input = input.split("\n\n")
    algo = input[0]
    image = input[1].split("\n")[:-1]
    lited = get_lited(image)
    runs = 2
    for it in range(1, runs + 1):
        bg_char = '#' if it % 2 == 0 else '.'
        lited = run_algo(lited, algo, it, bg_char)

    return len(lited)


def run_algo(lited, algo, limit, bg_char):
    nw_lited = set()
    visited = set()
    for lit in lited:
        transform(lit, lited, visited, nw_lited, algo, limit, bg_char)
    return nw_lited


def transform(point, lited, visited, nw_lited, algo, limit, bg_char):
    if point in visited:
        return

    visited.add(point)
    code = get_code(point, lited, limit, bg_char)
    idx = int(decode(code), 2)

    if algo[idx] == '#':
        nw_lited.add(point)

    if check_bounds(point, limit):
        return

    for adj in get_adj(point):
        if adj not in lited and adj not in visited:
            transform(adj, lited, visited, nw_lited, algo, limit, bg_char)


def check_bounds(point, limit):
    x, y = point
    if x <= -limit or x >= 99 + limit:
        return True
    if y <= -limit or y >= 99 + limit:
        return True
    return False


def get_code(point, lited, limit, bg_char):
    code = ""
    for nx, ny in get_adj(point):
        if (nx, ny) in lited:
            code += '#'
        elif check_bounds((nx, ny), limit):
            code += bg_char
        else:
            code += '.'
    return code


def get_adj(point):
    # returns adjacent coordinates
    x, y = point
    adjacency = [(i, j) for j in (-1, 0, 1) for i in (-1, 0, 1)]
    for dx, dy in adjacency:
        nx = x + dx
        ny = y + dy
        yield nx, ny


def decode(string):
    def decode_char(char):
        if char == '#':
            return '1'
        else:
            return '0'

    return "".join(list(map(decode_char, string)))


def get_lited(image):
    lited = set()
    for y in range(len(image)):
        for x in range(len(image[0])):
            pix = image[y][x]
            if pix == '#':
                coord = (x, y)
                lited.add(coord)
    return lited
