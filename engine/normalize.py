import numpy as np

m = None


def normalize(repository):
    global m

    for matrix in repository.data:
        m = matrix
        node_max = None
        node_min = None
        for a in matrix.connections:
            v = []
            for index in range(0, a.size):
                if a.item(index) != float("inf"):
                    v.append(a.item(index))
            temp_max = float(np.nanmax(v))
            temp_min = float(np.nanmin(v))
            if node_max is None or node_max < temp_max:
                node_max = temp_max
            if node_min is None or node_min > temp_min:
                node_min = temp_min

        if matrix.type == 'cost':
            func = benefit_normalize
        else:
            func = cost_normalize

        func = np.vectorize(func)
        matrix.connections_normalize = func(matrix.connections, node_max, node_min)


def cost_normalize(v, node_max, node_min):
    if v is float('-inf'):
        return 0
    return (node_max - v) / (node_max - node_min)


def benefit_normalize(v, node_max, node_min):
    if v is float('-inf'):
        return 0
    return 1 - ((node_max - v) / (node_max - node_min))
