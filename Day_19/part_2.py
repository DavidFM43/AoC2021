import math
from copy import deepcopy


def solve(input):
    scanners = parse(input)

    scan_distances = [0 for x in range(len(scanners))]
    for idx in range(len(scanners)):
        scanner = scanners[idx]
        scan_distances[idx] = compute_distances(scanner)

    s0 = scanners[0]
    positions = compare_against(
        scanners, s0, 0, (0, 0, 0), [s0], scan_distances)
    return max_distance(positions)


def compare_against(scanners: list, s0: set, idx0: int, pos: tuple, processed: set, scan_distances: list):
    # compares s0 against all other scanners
    positions = set()
    for idx1 in range(len(scanners)):
        s1 = scanners[idx1]
        if s1 not in processed:
            new_s1, offset, corrected_beacons = compare_scanners(
                s0, idx0, s1, idx1, pos, scan_distances, scanners)
            if new_s1 != None:
                scan_distances[idx1] = compute_distances(new_s1)
                scanners[idx1] = new_s1

                new_pos = add(pos, offset)
                positions.add(new_pos)
                processed.append(new_s1)

                positions.update(compare_against(
                    scanners, new_s1, idx1, new_pos, processed, scan_distances))
    return positions


def compare_scanners(s0: set, idx0: int, s1: set, idx1: int, pos0, scan_distances: list, scanners: list):
    """
    Returns the position of s2 relative to s1 if they overlap, else returns None
    """
    p = check_overlap(idx0, idx1, scan_distances, scanners)
    if p != None:
        p0 = p[0]
        pivot = p[1]
        for s, new_p in all_scan(s1, pivot):
            offset = substract(p0, new_p)
            ovlap = compare_points(offset, s0, s)
            if len(ovlap) == 12:
                corrected_beacons = {add(add(x, pos0), offset) for x in s}
                return s, offset, corrected_beacons
    return None, -1, -1


def max_distance(positions):
    max = -1
    while len(positions) > 0:
        x = positions.pop()
        for y in positions:
            dis = mahtattan_distance(x, y)
            if max < dis:
                max = dis
    return max


def mahtattan_distance(a, b):
    x1, y1, z1 = a
    x2, y2, z2 = b
    return abs(x1-x2) + abs(y1-y2) + abs(z1-z2)


def check_overlap(idx0: int, idx1: int, scan_distances: list, scanners: list):
    d0 = scan_distances[idx0]
    d1 = scan_distances[idx1]
    s0 = scanners[idx0]
    s1 = scanners[idx1]
    for x in s0:
        for y in s1:
            v = d0[x].intersection(d1[y])
            if len(v) == 11:
                return x, y


def compare_points(offset, s1, s2):
    ovlap = set()
    for p2 in s2:
        p2 = add(p2, offset)
        if p2 in s1:
            ovlap.add(p2)
    return ovlap


def compute_distances(scanner):
    scanner = deepcopy(scanner)
    total_distances = {x: set() for x in scanner}
    while len(scanner) > 0:
        x = scanner.pop()
        for y in scanner:
            dis = distance(x, y)
            total_distances[y].add(dis)
            total_distances[x].add(dis)
    return total_distances


def distance(a, b):
    x1, y1, z1 = a
    x2, y2, z2 = b
    return math.sqrt((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2)


def add(a, b):
    return tuple([sum(x) for x in zip(a, b)])


def substract(a, b):
    x1, y1, z1 = a
    x2, y2, z2 = b
    return(x1-x2, y1-y2, z1-z2)


def turn(p): return (p[0], p[2], -p[1])
def roll(p): return (-p[1], p[0], p[2])


def roll_scan(scanner, pivot=(0, 0, 0)):
    new_scanner = set()
    for p in scanner:
        if p == pivot:
            pivot = roll(p)
        new_scanner.add(roll(p))
    if pivot == (0, 0, 0):
        return new_scanner
    return new_scanner, pivot


def turn_scan(scanner, pivot=(0, 0, 0)):
    new_scanner = set()
    for p in scanner:
        if p == pivot:
            pivot = turn(p)
        new_scanner.add(turn(p))
    if pivot == (0, 0, 0):
        return new_scanner
    return new_scanner, pivot


def all_scan(scanner, pivot):
    for _ in range(2):
        for r in range(3):
            scanner, pivot = roll_scan(scanner, pivot)
            yield (scanner, pivot)
            for t in range(3):
                scanner, pivot = turn_scan(scanner, pivot)
                yield (scanner, pivot)
        scanner = roll_scan(turn_scan(roll_scan(scanner)))
        pivot = roll(turn(roll(pivot)))


def parse(input) -> list:
    scanners = []
    input = [x.split("\n") for x in input.split("\n\n")]
    for chunk in input:
        scanner = set()
        for beacon in chunk[1:]:
            if beacon:
                beacon = tuple(map(int, beacon.split(",")))
                scanner.add(beacon)
        scanners.append(scanner)
    return scanners
