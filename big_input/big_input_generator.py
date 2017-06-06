import numpy as np
import sys

sys.path.append('../')

from algo.dijkstra import dijkstra
from engine.normalize import normalize
from engine.wsm import wsm


from engine.matrix import Matrix
from engine.repository import Repository

linhas = 5
colunas = 5

m01 = np.random.randint(100, size=(linhas, colunas))
m02 = np.random.randint(100, size=(linhas, colunas))

for linha in range(linhas):
    for coluna in range(colunas):
        if linha == coluna:
            m01.itemset((linha, coluna), 0)
            m02.itemset((linha, coluna), 0)
        elif coluna > linha:
            continue
        elif coluna < linha:
            m01.itemset((coluna, linha), m01.item(linha, coluna))
            m02.itemset((coluna, linha), m02.item(linha, coluna))


print(m01)
"""
m1 = Matrix(m01, range(0, linha))
m2 = Matrix(m02, range(0, linha))

r = Repository([m1, m2])

print(normalize(r))

result = wsm(r)

start = 0
target = 3

# final_result = dijkstra(result, start, target)[::-1]

print(final_result)"""