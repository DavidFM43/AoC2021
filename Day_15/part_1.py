from heapq import heappop, heappush


def solve(input):
    """
    dijkstra algorithm using priority queue
    """
    matrix = [list(map(int,[num for num in row])) for row in input]
    n_rows = len(matrix)
    n_cols = len(matrix[0])
    # weights dic
    weights = {}
    for y in range(n_rows):
        for x in range(n_cols):
            weights[(x, y)] = matrix[y][x]
    #distances dic
    distances = {}
    inf = float("inf")
    for x, y in weights.keys():
        distances[(x,y)] = inf
    distances[(0, 0)]  = 0 
    # distance priority queue
    pq = [(0, (0, 0))]
    while pq:
        distance, node = heappop(pq)
        if distance > distances[node]:
            continue
        x, y = node 
        H = [x,x,x+1,x-1]
        V = [y+1,y-1,y,y]
        for x_2, y_2 in zip(H,V):
            if 0 <= x_2 < n_cols and 0 <= y_2 < n_rows:
                v = weights[(x_2, y_2)]
                alt = distance + v
                if alt < distances[(x_2, y_2)]:
                    distances[(x_2, y_2)] = alt
                    heappush(pq, (alt, (x_2, y_2)))

    return distances[(n_cols-1, n_rows-1)]
