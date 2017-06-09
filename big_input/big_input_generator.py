from matplotlib import pyplot
import numpy as np
import timeit
from functools import partial
import random
import sys

sys.path.append('../')

from algo.dijkstra import dijkstra
from algo.gargalo import gargalo
from engine.normalize import normalize
from engine.wsm import wsm

from engine.matrix import Matrix
from engine.repository import Repository


def criar_matrix(n):
    linhas = n
    colunas = n

    m01 = np.random.randint(1, 100, size=(linhas, colunas))

    for linha in range(linhas):
        for coluna in range(colunas):
            if linha == coluna:
                m01.itemset((linha, coluna), -1)
            elif coluna > linha:
                continue
            elif coluna < linha:
                m01.itemset((coluna, linha), m01.item(linha, coluna))

    nodes = list(range(0, linhas))
    m1 = Matrix(m01, nodes, type="benefit", name="banda", weight=0.3)

    return m1

def salvar_matrix(matrix):
    f = open('big_input_'+str(len(matrix.nodes))+'.txt', 'w')
    string = ''
    for i in range(len(matrix.nodes)):
        for j in range(len(matrix.nodes)):
            string += str(matrix.connections.item(i, j))
            if j != (len(matrix.nodes)-1):
                string += ','
        string += '\n'

    string += '\n'
    string += 'nodes: '
    for i in range(len(matrix.nodes)):
        string += str(i)
        if i != (len(matrix.nodes) -1):
            string += ', '
    string += '\n'
    string += 'type: benefit\n'
    string += 'name: random\n'
    string += 'weight: 0.8'

    f.write(string)
    f.close()

def load_matrix(n):
    matrix = Matrix()
    matrix.build('big_input_'+str(n)+'.txt')
    return matrix

def construir_big_input(n):
    matrix = criar_matrix(n)
    salvar_matrix(matrix)


def small_path(matrix):
    r = Repository([matrix])

    # O(n^2)
    normalize(r)

    # O(n^2)
    result = wsm(r)

    start = 0
    target = 3

    # O(n^2)
    path = dijkstra(result, start, target)[::-1]

def plotTC(fn, nMin, nMax, nInc, nTests):
    """
    Run timer and plot time complexity
    """
    x = []
    y = []
    for tamanho in range(nMin, nMax, nInc):
        matrix = load_matrix(tamanho)
        testNTimer = timeit.Timer(partial(fn, matrix))
        tempo = testNTimer.timeit(number=nTests)
        x.append(tamanho)
        y.append(tempo)
    p1, = pyplot.plot(x, y, 'o')
    return p1


# main() function
def main():
    print('Analyzing Algorithms...')

    p_small = plotTC(small_path, 10, 100, 10, 2)
    # p_gargalo = plotTC(gargalo, 10, 80, 10, 2)
    # pyplot.legend([p_small, p_gargalo,], ['Caminho Mais Curto', 'Gargalos', ])
    pyplot.legend([p_small, ], ['Caminho Mais Curto', ])

    # show plot
    pyplot.show()


# call main
if __name__ == '__main__':
    # for i in range(100, 1100, 100):
    #     construir_big_input(i)
    main()
