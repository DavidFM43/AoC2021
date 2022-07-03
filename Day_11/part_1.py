def solve(input):
    """for every step the number of flashes is collected by taking the lenght of the flashed list"""

    steps = 100
    octo_map = []
    inf = float("inf")
    flash_count = 0

    for line in input:
        line = [-inf] + [int(x) for x in line] + [-inf]
        octo_map.append(line)

    sentinel = [-inf for x in range(len(octo_map[0]))]
    octo_map.insert(0, sentinel)
    octo_map.append(sentinel)

    for i in range(steps):
        flashed = step(octo_map)
        flash_count += len(flashed)

    return flash_count


def step(octo_map):
    """flashed keeps track of the positions that have alredy flashed"""

    flashed = []
    nrows = len(octo_map)
    ncols = len(octo_map[0])

    for i in range(1, nrows - 1):
        for j in range(1, ncols - 1):

            if octo_map[i][j] + 1 > 9:
                flash(octo_map, i, j, flashed)
            else:
                if (i, j) not in flashed:
                    octo_map[i][j] += 1

    return flashed


def flash(octo_map, i, j, flashed):
    """sets the position to 0, flashes the surroundings and does the necessary flashes"""

    octo_map[i][j] = 0
    H = [i - 1, i, i + 1]
    V = [j - 1, j, j + 1]
    flashed.append((i, j))

    for h in H:
        for v in V:

            if (h, v) != (i, j) and (h, v) not in flashed:
                if octo_map[h][v] + 1 > 9:
                    flash(octo_map, h, v, flashed)
                else:
                    octo_map[h][v] += 1
