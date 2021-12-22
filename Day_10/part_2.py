import statistics 


def solve(input):
    """ dismisses corrupted sequences and computes error scores"""
    
    open_brackets = "{[(<"
    closing_brackets = "}])>"
    errors_scores = [3, 2, 1, 4]
    scores = []

    for sequence in input:

        local_counter = 0
        open_stack = []
        corrupted = False

        for bracket in sequence:

            if bracket in open_brackets: 
                open_stack.append(bracket)

            else:
                top = open_stack[-1]
                bracket_index = closing_brackets.index(bracket)
                if open_brackets.index(top) == bracket_index:
                    open_stack.pop()

                else:
                    # corrupted sequence
                    corrupted = True
                    break

        if corrupted:
            continue

        if open_stack: 

            n = len(open_stack)

            for idx in range(n-1,-1,-1):

                bracket = open_stack[idx]
                bracket_index = open_brackets.index(bracket)
                local_counter *=5
                local_counter += errors_scores[bracket_index]

            scores.append(local_counter)

    return statistics.median(sorted(scores))