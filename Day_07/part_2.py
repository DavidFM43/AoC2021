def solve(input):
    """ position i in counter array contains the cost of moving the crabs to that horizontal position"""

    positions = [int(x) for x in input[0].split(",")]
    n = max(positions)
    counter = [0 for x in range(n)]
    cost = lambda x: (x*(x+1))//2

    for idx in range(n):
        for position in positions:
            counter[idx] += cost(abs(position - idx))

    return min(counter)
