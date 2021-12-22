def solve(input):
    """ unique_digits picks up the number of unique digits by checking the length of the signal"""
    
    counter = 0
    for line in input:
        instruction = line.split(" | ")
        signal = instruction[0].split(" ")
        output = instruction[1].split(" ")
        unique_digits = sum([len(x) in [2,4,3,7] for x in output]) 

        counter += unique_digits

    return counter