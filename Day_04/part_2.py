import pandas as pd

def solve(input):

    input = input.split("\n\n")

    nums = input[0]
    raw_cards = input[1:]
    cards = []
    winners = []
    for card in raw_cards:
        cards.append(pd.DataFrame(x.replace("  "," ")
                                   .strip()
                                   .split(" ") for x in card.split("\n")).astype(int))


    for num in nums.split(','):
        num = int(num)
        num_cards = len(cards)

        for idx in range(num_cards):
            if len(cards[idx]) == 0:
                pass
            else:
                cards[idx].replace(num, 'X', inplace=True)
                card = cards[idx] 

                try:
                    row_Xs = card.apply(lambda x: x.value_counts(), axis=0).loc["X",:].max()
                    col_Xs = card.apply(lambda x: x.value_counts(), axis=1).loc[:,"X"].max()
                except:
                    pass        

                if row_Xs == card.shape[0] or col_Xs == card.shape[1]:

                    winners.append((card, num))
                    cards[idx] = []
                



    last_winner, num = winners[-1]
    leftover_sum = last_winner.replace('X', 0).sum().sum()

    return num*leftover_sum 