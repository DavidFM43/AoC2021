def solve(input):
    
    x = 0
    y = 0

    for instruction in input:

        direction, amount = instruction.split(" ")

        if direction == "forward":
            x += int(amount)
        elif direction == "down":
            y += int(amount)
        elif direction == "up":
            y -= int(amount)

    return x * y 