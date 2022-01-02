from ast import literal_eval, walk


class Node:
    def __init__(self, parent) :
        self.height = -1 
        self.parent = parent 
        self.children = None

def solve(input):
    x = [[[[[9,8],1],2],3],4]
    return 0

def set_height(num):
    if type(num) == list:
        h1 = set_height(num[0]) + 1
        h2 = set_height(num[1]) + 1
        height = max(h1, h2)
        return height
    else:
        return -1

def build_tree(num, parent):
    node = Node(parent)

    if type(num) == list:
        h1 = build_tree(num[0], node)
        h2 = build_tree(num[1], node)
    else:
        return -1

def add(n1, n2):
    sum = [n1, n2]
    return sum

def reduce(pair):
    return pair   
