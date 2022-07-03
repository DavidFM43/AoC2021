def solve(input):

    x = 0
    y = 0
    aim = 0

    for instruction in input:

        direction, amount = instruction.split(" ")

        if direction == "forward":
            x += int(amount)
            y += aim * int(amount)
        elif direction == "down":
            aim += int(amount)
        elif direction == "up":
            aim -= int(amount)

    return x * y
