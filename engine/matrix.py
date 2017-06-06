import numpy as np


class Matrix(object):
    def __init__(self, connections=None, nodes=None, type=None, name=None, weight=None):
        self.connections = connections
        self.connections_normalize = None
        self.nodes = nodes
        self.type = type
        self.name = name
        self.weight = weight

    def build(self, filename):
        flag_matrix = True
        self.connections = []
        with open(filename, 'r') as f:
            for line in f:
                if line.strip() and flag_matrix:
                    line = [int(x) for x in line.strip().strip('\n').split(',')]
                    line = [x if x != 0 else -1 for x in line]
                    self.connections.append(line)
                elif not line.strip() or not flag_matrix:
                    flag_matrix = False
                    label = line.split(':')
                    if label[0] == "nodes":
                        line = line.split(':')[1]
                        self.nodes = [x.strip(' ') for x in line.strip('\n').split(',')]
                    elif label[0] == "type":
                        self.type = label[1].strip().strip('\n')
                    elif label[0] == "name":
                        self.name = label[1].strip().strip('\n')
                    elif label[0] == "weight":
                        self.weight = float(label[1].strip().strip('\n'))
        self.connections = np.matrix(self.connections)

    def get_adjs(self, index):
        adjs = []

        # Roda node vezes =  vertice vezes
        for node in range(len(self.nodes)):
            if node == index:
                continue
            if self.connections.item(index, node) != -1:
                adjs.append(node)

        return adjs