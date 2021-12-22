def get_basin_size(height_map, i, j, memo):
    """ recursively check if the neighbors are part of the basin"""

    if height_map[i][j] >= 9:
        return 0

    memo.append((i, j))
    size = 1

    H = [i+1, i-1, i, i]
    V = [j, j, j-1, j+1]

    for n, m in zip(H, V):
        if (n,m) not in memo:
            size += get_basin_size(height_map,n, m, memo)

    return size 


def solve(input):
    """ finds the lowest points of the map and check the basin size for each point"""
    
    height_map = []
    lower_sizes = []
    inf = float("inf")

    for line in input:
        height_map.append([inf] + [int(x) for x in line] + [inf])

    nrows = len(height_map)
    ncols = len(height_map[0])

    sentinel = [inf for x in range(ncols)]

    height_map.insert(0, sentinel)
    height_map.append(sentinel)

    for i in range(1, nrows+1):
        for j in range(1, ncols-1):

            H = [i+1, i-1, i, i]
            V = [j, j, j-1, j+1]
            failed = False

            for n, m in zip(H, V):

                if height_map[i][j] < height_map[n][m]:
                   pass
                else:
                    failed = True
                    break

            if failed == False:
                lower_sizes.append(get_basin_size(height_map, i, j, []))

    lower_sizes.sort(reverse=True)

    largest_basins = lower_sizes[0]*lower_sizes[1]*lower_sizes[2]

    return largest_basins 