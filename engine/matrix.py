import pandas as pd
import numpy as np


class Matrix:
    def __init__(self):
        self.connections = None
        self.connections_normalize = None
        self.nodes = None
        self.type = None
        self.name = None
        self.weight = None

    def build(self, filename):
        flag_matrix = True
        self.connections = []
        with open(filename, 'r') as f:
            for line in f:
                if line.strip() and flag_matrix:
                    line = [int(x) for x in line.strip().strip('\n').split(',')]
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