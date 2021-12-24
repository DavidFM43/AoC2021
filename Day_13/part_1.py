def solve(input):
    """ fold() function keeps track of the points in a set so that there's no duplicate points"""

    input = input.split("\n\n")
    dots = set([tuple(map(int, x.split(","))) for x in input[0].split("\n")])
    folds = [x.split()[2].split("=") for x in input[1].split("\n")]

    for ins in folds:
        # first fold only
        dots = fold(ins,dots)
        break

    return len(dots)


def fold(ins, dots):

    coord = {"x" : 0,
             "y" : 1} 
    axis = coord[ins[0]]
    point = int(ins[1])
    new_dots = set()

    for dot in dots:

        if dot[axis] > point:

            dot = list(dot)
            dot[axis] = 2*point - dot[axis]
            dot = tuple(dot)
            new_dots.add(dot)

        else:
            new_dots.add(dot)

    return new_dots
