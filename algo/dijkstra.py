
def dijkstra(matrix, start, target):
    d = []
    rot = []
    A = []
    F = []
    for i in range(0, len(matrix[0])):
        d.append(-1)
        rot.append(0)
        A.append(i)

    d.insert(start, 0)
    rot.insert(start, -1)

    while A:
        min_dist = float("inf")
        r = None

        for node in A:
            if d[node] != -1 and d[node] < min_dist:
                min_dist = d[node]
                r = node

        F.append(r)
        A.remove(r)
        for node in A:
            if matrix[node][r] == -1:
                continue

            if d[node] != -1 and d[node] < (d[r] + matrix[node][r]):
                p = d[node]
            else:
                p = d[r] + matrix[node][r]
            if p < d[node] or d[node] == -1:
                d[node] = p
                rot[node] = r

    path = [target]
    for index in range(0, len(rot)):
        if target == 0: break
        node = rot[target]
        path.append(node)
        target = node

    return path
