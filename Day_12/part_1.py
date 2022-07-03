def solve(input):
    """recursively builds each path.
    when a path is completed it is added to the paths list, wich is passed by reference in each recursive call"""
    links = {}
    for link in input:
        link = link.split("-")
        head = link[0]
        tail = link[1]
        links[head] = links.get(head, []) + [tail]
        links[tail] = links.get(tail, []) + [head]
    paths = build_path(["start"], links, [])
    return len(paths)


def build_path(path, links, paths):
    current = path[-1]
    if current == "end":
        paths.append(path)
        return path
    options = links[current]
    for option in options:
        if option.isupper():
            build_path(path + [option], links, paths)
        if option.islower() and option not in path:
            build_path(path + [option], links, paths)
    if current == "start":
        return paths
