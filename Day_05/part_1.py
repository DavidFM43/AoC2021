def solve(input):

    map_count = dict()

    for line in input:

        line = [[int(i) for i in x.split(",")] for x in line.split(" -> ")]

        # same x coordinate
        if line[0][0] == line[1][0]:

            x = line[0][0]
            y_1 = min(line[0][1], line[1][1])
            y_2 = max(line[0][1], line[1][1])

            for y in range(y_1, y_2 + 1):

                coordinates = "{},{}".format(x, y)
                map_count[coordinates] = map_count.get(coordinates, 0) + 1

        # same y coordinate
        elif line[0][1] == line[1][1]:

            y = line[0][1]
            x_1 = min(line[0][0], line[1][0])
            x_2 = max(line[0][0], line[1][0])

            for x in range(x_1, x_2 + 1):

                coordinates = "{},{}".format(x, y)
                map_count[coordinates] = map_count.get(coordinates, 0) + 1

    count = 0
    # count the number of recurrent coordinates
    for coor in map_count.values():
        if coor > 1:
            count += 1

    return count
