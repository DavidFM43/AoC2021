from ast import literal_eval
from math import ceil, floor


def solve(input) -> int:
    max_count = -1
    idx = 0
    while idx < len(input):
        n1 = literal_eval(input[idx])
        for n2 in input[idx:]:
            n2 = literal_eval(n2)
            s1 = magnitude(add(n1, n2))
            s2 = magnitude(add(n2, n1))
            max_count = max(max(s1, s2), max_count)
        idx += 1
    return max_count


class Pair:
    def __init__(self, parent, pair) -> None:
        self.parent = parent
        if type(pair[0]) == list:
            self.l = Pair(self, pair[0])
        else:
            self.l = pair[0]
        if type(pair[1]) == list:
            self.r = Pair(self, pair[1])
        else:
            self.r = pair[1]


def get_children(pair) -> list:
    if type(pair) == int:
        return pair
    return [get_children(pair.l), get_children(pair.r)]


def get_height(tree):
    if type(tree) == Pair:
        h1 = get_height(tree.l) + 1
        h2 = get_height(tree.r) + 1
        return max(h1, h2)
    else:
        return -1


def magnitude(pair) -> int:
    if type(pair) == int:
        return pair
    return 3*magnitude(pair.l) + magnitude(pair.r)*2


def add(p1, p2):
    sum = Pair(None, [p1, p2])
    sum.l.parent = sum
    sum.r.parent = sum
    reduce(sum)
    return sum


def reduce(pair):
    while True:
        if get_height(pair) >= 4:
            nested = find_nested(pair)
            explode(nested)
            continue
        big_num = find_bignum(pair)
        if big_num != None:
            parent, index = big_num
            split(parent, index)
        else:
            break


def find_nested(pair):
    h = get_height(pair)
    if h == 0:
        return pair
    if get_height(pair.l) == h - 1:
        return find_nested(pair.l)
    else:
        return find_nested(pair.r)


def find_bignum(pair, parent=None):
    if type(pair) == int:
        if pair >= 10:
            if pair == parent.l:
                idx = 0
            else:
                idx = 1
            return parent, idx
        else:
            return None
    left = find_bignum(pair.l, pair)
    if left != None:
        return left
    right = find_bignum(pair.r, pair)
    if right != None:
        return right
    else:
        return None


def get_childref(y, l_ref):
    if l_ref:
        return y.l
    else:
        return y.r


def set_childref(y, val, l_ref):
    if l_ref:
        y.l = val
    else:
        y.r = val


def change_adj(pair, change_pred):
    """
    change_pred=True changes the predecessor and change_pred=False changes successor
    """
    dir_pointer = change_pred
    x = pair
    y = pair.parent
    parent_ref = get_childref(pair, dir_pointer)

    while y != None and get_childref(y, dir_pointer) == x:
        x = y
        y = y.parent
    if y != None:
        if type(get_childref(y, dir_pointer)) != int:
            y = get_childref(y, dir_pointer)
            while type(get_childref(y, not dir_pointer)) != int:
                y = get_childref(y, not dir_pointer)
            set_childref(y, get_childref(y, not dir_pointer) +
                         parent_ref, not dir_pointer)
        else:
            set_childref(y, get_childref(y, dir_pointer) +
                         parent_ref, dir_pointer)


def explode(pair):
    change_adj(pair, True)
    change_adj(pair, False)
    if pair == get_childref(pair.parent, True):
        set_childref(pair.parent, 0, True)
    else:
        set_childref(pair.parent, 0, False)


def split(parent, index):
    is_left = not bool(index)
    num = get_childref(parent, is_left)
    x = floor(num/2)
    y = ceil(num/2)
    pair = Pair(parent, [x, y])
    set_childref(parent, pair, is_left)
