from itertools import count


def solve(input):
    p1 = int(input[0][-1])
    p2 = int(input[1][-1])
    return game(p1, p2)


def game(p1, p2):
    score1, score2 = 0, 0
    p1_plays = True
    die = 1
    times = 0
    while True:
        if p1_plays:
            p1, score1, die = turn(p1, score1, die)
            p1_plays = False
        else:
            p2, score2, die = turn(p2, score2, die)
            p1_plays = True
        times += 1
        if score1 >= 1000 or score2 >= 1000:
            losser = score2 if score1 >= 1000 else score1
            return losser * (times * 3)


def turn(pos, score, die):
    sum, die = toss(die)
    pos = ((pos + sum - 1) % 10) + 1
    score += pos
    return pos, score, die


def toss(current):
    """
    return (c+1) + (c+2) + (c+3), and c+4
    """
    val = 0
    die = count(current)
    for _ in range(3):
        num = next(die)
        val += num
    return val, num + 1
