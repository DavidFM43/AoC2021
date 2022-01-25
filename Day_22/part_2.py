def solve(input):
    ins = parse(input)
    cores = []
    for cuboid in ins:
        # cuboid = (power, [xmin, xmax, ymin, ymax, zmin, zmax])
        to_add = [cuboid] if cuboid[0] else []
        for core in cores:
            inter = inter_cuboid(cuboid, core)
            if inter:
                to_add.append(inter)
        cores.extend(to_add)

    return count_cores(cores)


def inter_cuboid(c1, c2):
    c1_ranges = c1[1]
    c2_ranges = c2[1]
    action = not c2[0]
    inter_ranges = [max, min, max, min, max, min]
    c3 = [inter_ranges[i](c1_ranges[i], c2_ranges[i]) for i in range(6)]
    if c3[0] > c3[1] or c3[2] > c3[3] or c3[4] > c3[5]:
        return None
    return (action, c3)


def count_cores(cores):
    count = 0
    for power, core in cores:
        if power:
            count += (core[1] - core[0]+1) * \
                (core[3] - core[2]+1) * (core[5] - core[4]+1)
        else:
            count -= (core[1] - core[0]+1) * \
                (core[3] - core[2]+1) * (core[5] - core[4]+1)
    return count


def process_coords(raw):
    coords = []
    raw = raw.split(",")
    for plane in raw:
        plane = list(map(int, plane[2:].split("..")))
        coords.extend(plane)
    return coords


def parse(input):
    ins = []
    for line in input:
        line = line.split()
        power = True if line[0] == "on" else False
        cuboid = process_coords(line[1])
        ins.append((power, cuboid))
    return ins
