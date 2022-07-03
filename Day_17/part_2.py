def solve(input):
    global target
    target = input.strip().split()
    for par in range(50, 200, 10):
        counter = 0
        for x in range(1, par):
            for y in range(-par, par):
                vel = [x, y]
                missed, positions = sim(vel)
                if not missed:
                    counter += 1
    return counter


def sim(vel):
    x0, x1 = tuple(map(int, target[2][2:-1].split("..")))
    y0, y1 = tuple(map(int, target[3][2:].split("..")))
    pos = [0, 0]
    positions = [pos]
    while True:
        vel, pos = step(vel, pos)
        positions.append(pos)
        if pos[0] > x1 or pos[1] < y0:
            missed = True
            break
        elif x0 <= pos[0] <= x1 and y0 <= pos[1] <= y1:
            missed = False
            break
    return missed, positions


def step(vel, pos):
    x, y = pos
    new_pos = [x + vel[0], y + vel[1]]
    # drag(since it's always moving right, drag decreases x)
    if vel[0] > 0:
        vel[0] -= 1
    # gravity
    vel[1] -= 1
    return vel, new_pos
