def solve(input):
    """ gets the lowest point of the map. Sentinels are added to the map to avoid edge cases"""
    
    height_map = []
    lower_heights = []
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
               lower_heights.append(height_map[i][j]+1) 


    return sum(lower_heights)