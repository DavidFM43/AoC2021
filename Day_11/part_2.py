def solve(input):
    """ Checks if the number of flashes on a step is equal to the total of positions"""

    steps = 100
    octo_map = []
    flash_count = 0
    inf = float("inf")

    for line in input:
        line = [-inf] + [int(x) for x in line] + [-inf]
        octo_map.append(line)

    sentinel = [-inf for x in range(len(octo_map[0]))]
    octo_map.insert(0, sentinel)
    octo_map.append(sentinel)


    i = 1
    while True:

        flashed = step(octo_map)
        if len(flashed) == 100:
            return i
        i += 1


def step(octo_map):
    """ simulates one step"""

    flashed = []
    nrows = len(octo_map)
    ncols = len(octo_map[0])

    for i in range(1, nrows-1):
        for j in range(1, ncols-1):

            if octo_map[i][j] + 1 > 9:
                flash(octo_map, i, j, flashed)
            else:
                if (i,j) not in flashed:
                    octo_map[i][j] += 1

    return flashed


def flash(octo_map, i, j, flashed):
    """ sets the position to 0, increases the surrounding positions by 1 and does the necessary new flashes"""
    
    octo_map[i][j] = 0
    H = [i-1,i,i+1]
    V = [j-1,j,j+1]
    flashed.append((i, j))

    for h in H:
        for v in V:

            if (h, v) != (i, j) and (h, v) not in flashed:
                if octo_map[h][v] + 1 > 9:
                    flash(octo_map, h, v, flashed)
                else:
                    octo_map[h][v] += 1
