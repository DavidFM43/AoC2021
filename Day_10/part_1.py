def solve(input):
    """ uses a stack to match closing brackets with most recent open brackets"""
    
    open_brackets = "{[(<"
    errors_scores = [1197, 57, 3, 25137]
    closing_brackets = "}])>"
    counter = 0

    for sequence in input:

        open_stack = []

        for bracket in sequence:

            if bracket in open_brackets: 
                open_stack.append(bracket)

            else:
                top = open_stack[-1]
                bracket_index = closing_brackets.index(bracket)
                if open_brackets.index(top) == bracket_index:
                    open_stack.pop()

                else:
                    counter += errors_scores[bracket_index]
                    break
                    
    return counter