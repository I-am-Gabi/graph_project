import numpy as np


def normalize(repository):
    func = None

    for matrix in repository.data:
        if matrix.type == 'cost':
            func = matrix.cost_normalize
        else:
            pass

        func = np.vectorize(func)
        matrix.connections_normalize = func(matrix.connections)
        print(matrix.connections_normalize)


def cost_normalize(matrix, v):
    max = float(matrix.connections.max())
    min = float(matrix.connections.min())
    return (max - v) / (max - min)
