def solve(input):
    """after the corresponding folds are done, the remaining points are drew on the paper"""

    input = input.split("\n\n")
    dots = set([tuple(map(int, x.split(","))) for x in input[0].split("\n")])
    folds = [x.split()[2].split("=") for x in input[1].split("\n")]

    for ins in folds:
        dots, max_x, max_y = fold(ins, dots)

    paper = []
    for i in range(max_y + 1):
        row = ["_" for x in range(max_x + 1)]
        paper.append(row)

    for dot in dots:
        x = dot[0]
        y = dot[1]
        paper[y][x] = "#"

    code = ""

    for row in paper:
        code += "".join(row) + "\n"

    return code


def fold(ins, dots):

    coord = {"x": 0, "y": 1}
    axis = coord[ins[0]]
    point = int(ins[1])
    new_dots = set()
    max_x = -1
    max_y = -1

    for dot in dots:

        if dot[axis] > point:
            dot = list(dot)
            dot[axis] = 2 * point - dot[axis]
            dot = tuple(dot)
            new_dots.add(dot)
        else:
            new_dots.add(dot)
        if max_x < dot[0]:
            max_x = dot[0]
        if max_y < dot[1]:
            max_y = dot[1]

    return new_dots, max_x, max_y
