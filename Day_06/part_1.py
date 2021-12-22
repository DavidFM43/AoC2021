def solve(input):
    """fish array contains all fish. 
    Decreases by 1 each day and replaces -1 positions with 6 and adds 8 to the array"""
    
    fishes = [int(x) for x in input[0].split(",")]
    days = 80

    for day in range(days):

        for idx in range(len(fishes)):
            fishes[idx] -= 1

            if fishes[idx] == -1:
                fishes[idx] = 6
                fishes.append(8)

    return len(fishes)