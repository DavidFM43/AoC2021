import pandas as pd


def solve(input):

    matrix = [list(num) for num in input]
    df = pd.DataFrame(matrix)
    max_counts = df.apply(lambda x: x.value_counts().idxmax())
     
    gamma = "".join(list(max_counts))
    gamma = int(gamma, 2)

    epsilon = "".join([str(int(not bool(int(x)))) for x in max_counts])
    epsilon = int(epsilon, 2)

    return gamma * epsilon
    