def solve(input):
    """ keeps track of the pairs and their count on each iteration, at the end count the first letter of
    the pairs so that there's no double count"""

    rules = {}
    input = input.split("\n\n")
    polymer = input[0] 
    raw_rules = input[1].split("\n")
    steps = 40

    for rule in raw_rules:

        rule = rule.split(" -> ")
        head = rule[0]
        tail = rule[1]
        rules[head] = tail

    pairs = get_pairs(polymer)

    for _ in range(steps):
        pairs = step(pairs, rules)

    count = chars_count(pairs)

    return count[-1][1] - count[0][1] + 1


def get_pairs(polymer):

    n = len(polymer) - 1
    pairs = {}
    for p in range(n):
        pair = polymer[p:p+2]
        pairs[pair] = pairs.get(pair, 0) + 1
    return pairs


def chars_count(pairs):
    char_count = {}

    for pair, value in pairs.items():
        char_count[pair[0]] = char_count.get(pair[0], 0) + value
    counts = sorted(list(char_count.items()), key=lambda x: x[1])
    return counts


def step(pairs, rules):    

    new_pairs = {}
    for pair, value in pairs.items():
        char = rules[pair] 
        pair1 = pair[0] + char
        pair2 = char + pair[1]

        new_pairs[pair1] = new_pairs.get(pair1, 0) + value
        new_pairs[pair2] = new_pairs.get(pair2, 0) + value

    return new_pairs

