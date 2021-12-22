def solve(input):
    """Array "count" counts the number of fish in each stage from 0-8,
    indexes are shifted by one because the newborn fish appear the next
    day from when it was born"""

    fish = [int(x) for x in input[0].split(",")]
    count = [0 for i in range(10)]
    num_days = 256

    for fish in fish:
        count[fish+1] += 1 

    head = 0

    for i in range(num_days):

        head = (head+1) % 10
        newborn_number = count[head]
        newborn_idx = (head+9) % 10
        mama_idx = (head+7) % 10

        count[newborn_idx] += newborn_number
        count[mama_idx] += newborn_number
        count[head] = 0

    return sum(count)