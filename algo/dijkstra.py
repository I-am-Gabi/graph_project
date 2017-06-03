import networkx as nx
import numpy as np
# from engine.graph import Graph


def dijkstra(matrix):
    A = np.array(matrix)
    G = nx.from_numpy_matrix(A, create_using=nx.DiGraph())
    print(nx.dijkstra_path(G, 0, 3))

# grafo = Graph()
# print(grafo.repository.data)
# dijkstra(grafo.repository.data[1])