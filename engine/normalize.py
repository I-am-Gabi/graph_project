import numpy as np

m = None


def normalize(repository):
    global m

    for matrix in repository.data:
        m = matrix
        node_max = float(np.max(m.connections[m.connections > 0]))
        node_min = float(np.min(m.connections[m.connections > 0]))

        if matrix.type == 'cost':
            func = benefit_normalize
        else:
            func = cost_normalize

        func = np.vectorize(func)
        matrix.connections_normalize = func(matrix.connections, node_max, node_min)


def cost_normalize(v, node_max, node_min):
    if v is -1:
        return -1
    return (node_max - v) / (node_max - node_min)


def benefit_normalize(v, node_max, node_min):
    if v is -1:
        return -1
    return 1 - ((node_max - v) / (node_max - node_min))
