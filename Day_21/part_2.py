from itertools import product
from functools import lru_cache 


def solve(input):
    p1 = int(input[0][-1])
    p2 = int(input[1][-1])
    return max(game(0, p1, p2, 0, 0))


def turn(pos, score, roll):
    new_pos = ((pos + sum(roll) - 1) % 10) + 1
    new_score = score + new_pos
    return new_pos, new_score


# @cache = @lru_cache(maxzise=None) available in 3.9 onwards
@lru_cache(maxsize=None)
def game(player, pos1, pos2, score1, score2):

    if score1 >= 21:
        return 1, 0
    elif score2 >= 21:
        return 0, 1

    game_info = {0: (pos1, score1),
                 1: (pos2, score2)}

    other_player = int(not bool(player))

    pos, score = game_info[player]
    others_info = game_info[other_player]
    wins = [0, 0]

    for roll in product(range(1, 4), repeat=3):
        new_pos, new_score = turn(pos, score, roll)
        if player == 0:
            pos1, score1 = (new_pos, new_score)
            pos2, score2 = others_info
        else:
            pos1, score1 = others_info
            pos2, score2 = (new_pos, new_score)

        wins0, wins1 = game(other_player, pos1, pos2, score1, score2)

        wins[0] += wins0
        wins[1] += wins1

    return wins
