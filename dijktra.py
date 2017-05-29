def dijkstra(graph):
    nodes = len(graph)
    dt = [0]
    rot = [0]
    for n in range(0, nodes - 1):
        dt.append(-1)
        rot.append(0)
    A = [range(0, nodes)]
    F = []
    dt.append(3)

    while True:
        r = min_dist(dt)
        F.append(r)
        A.remove(r)


def min_dist(v):
    min = v[0]
    pos_min = 0
    for i in range(0, len(v)):
        if v[i] < min and v[i] != -1:
            min = v[i]
            pos_min = i
    return pos_min


if __name__ == '__main__':
    graph = [[0, 1, 0, 0, 0, 0],
             [1, 0, 5, 0, 1, 0],
             [0, 5, 0, 1, 0, 1],
             [0, 0, 1, 0, 0, 0],
             [0, 1, 0, 0, 0, 2],
             [0, 0, 1, 0, 2, 0]]

    dijkstra(graph)
