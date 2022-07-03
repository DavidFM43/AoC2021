def solve(input):
    # keep track of the number of times that each letter appears in the polymer
    rules = {}
    input = input.split("\n\n")
    template = input[0]
    raw_rules = input[1].split("\n")
    steps = 5

    for rule in raw_rules:

        rule = rule.split(" -> ")
        head = rule[0]
        tail = rule[1]
        rules[head] = tail

    for i in range(steps):

        template, counter = step(template + "#", rules)
        print(template)

    items = sorted(list(counter.items()), key=lambda x: x[1])
    big = items[-1][1]
    small = items[0][1]

    return big - small


def step(template, rules):
    polymer = ""
    counter = {}

    for p in range(len(template) - 1):

        char = template[p]
        polymer += char
        counter[char] = counter.get(char, 0) + 1
        lexeme = template[p : p + 2]

        if lexeme in rules.keys():
            char = rules[lexeme]
            polymer += char
            counter[char] = counter.get(char, 0) + 1

    return polymer, counter
