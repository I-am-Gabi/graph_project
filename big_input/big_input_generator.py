from scipy.sparse import *
from scipy import *
import numpy as np


def read_file():
    with open("USA-road-d.NY.gr", "r") as ins:
        for line in ins:
            if "p sp " in line:
                n_nodes = int(line.split()[2])
                m = -1 * np.ones((2, 5))
            if "a " in line:
                data = line.split()
                i = int(data[1]) - 1
                j = int(data[2]) - 1
                m.itemset((i, j), int(data[3]))


m = np.random.rand(2000, 2000)
print(m)
