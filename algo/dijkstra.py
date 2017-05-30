import networkx as nx
import numpy as np


def dijkstra(matrix):
    A = np.array(matrix)
    G = nx.from_numpy_matrix(A, create_using=nx.DiGraph())
    print(nx.dijkstra_path(G, 0, 3))