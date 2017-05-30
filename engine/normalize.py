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
            pass

        func = np.vectorize(func)
        matrix.connections_normalize = func(matrix.connections)


def cost_normalize(v):
    max = float(m.connections.max())
    min = float(m.connections.min())
    return (max - v) / (max - min)
