from itertools import product


def solve(input):
    ins = []
    for line in input:
        line = line.split()
        power = True if line[0] == "on" else False
        coords = process_coords(line[1])
        ins.append((power, coords))
    return run(ins)


def run(ins):
    on = set()
    for power, ranges in ins:
        if not check_ranges(ranges):
            continue
        x_range, y_range, z_range = coords_ranges(ranges)
        if power:
            for coord in product(x_range, y_range, z_range):
                on.add(coord)
        else:
            for coord in product(x_range, y_range, z_range):
                on.discard(coord)
    return len(on)


def check_ranges(ranges):
    def check_bounds(c1, c2):
        if c1 < -50 or c2 > 50:
            return False
        else:
            return True
    for coord in ranges:
        p, q = coord
        if not check_bounds(p, q):
            return False
    return True


def coords_ranges(coords):
    x1, x2 = coords[0]
    y1, y2 = coords[1]
    z1, z2 = coords[2]
    return (range(x1, x2+1), range(y1, y2+1), range(z1, z2+1))


def process_coords(raw):
    coords = []
    raw = raw.split(",")
    for plane in raw:
        plane = tuple(map(int, plane[2:].split("..")))
        coords.append(plane)
    return coords
