import numpy as np

m = None


def normalize(repository):
    global m
    func = None

    for matrix in repository.data:
        m = matrix
        if matrix.type == 'cost':
            func = cost_normalize
        else:
            func = benefit_normalize

        func = np.vectorize(func)
        matrix.connections_normalize = func(matrix.connections)


def cost_normalize(v):
    if v is 0:
        return 0
    node_max = float(np.max(m.connections[np.nonzero(m.connections)]))
    node_min = float(np.min(m.connections[np.nonzero(m.connections)]))
    return (node_max - v) / (node_max - node_min)


def benefit_normalize(v):
    if v is 0:
        return 0
    node_max = float(np.max(m.connections[np.nonzero(m.connections)]))
    node_min = float(np.min(m.connections[np.nonzero(m.connections)]))
    return 1 - ((node_max - v) / (node_max - node_min))
