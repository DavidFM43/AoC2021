import pandas as pd


def solve(input):

    matrix = [list(num) for num in input]
    df = pd.DataFrame(matrix)
    
    for i in range(df.shape[1]):

        max_counts = df.apply(lambda x: x.value_counts()).sort_index(ascending=False).idxmax()
        df = df[df[i] == max_counts[i]]

        if df.shape[0] == 1:
            oxy = int("".join(list(df.iloc[0,:])),2)
            break

    df = pd.DataFrame(matrix)

    for i in range(df.shape[1]):

        min_counts = df.apply(lambda x: x.value_counts()).sort_index().idxmin()
        df = df[df[i] == min_counts[i]]

        if df.shape[0] == 1:
            co2 = int("".join(list(df.iloc[0,:])),2)
            break

    return oxy * co2
