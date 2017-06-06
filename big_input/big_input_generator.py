from matplotlib import pyplot
import numpy as np
import timeit
from functools import partial
import random
import sys

sys.path.append('../')

from algo.dijkstra import dijkstra
from engine.normalize import normalize
from engine.wsm import wsm


from engine.matrix import Matrix
from engine.repository import Repository

def small_path(n):
    linhas = n
    colunas = n

    m01 = np.random.randint(1, 100, size=(linhas, colunas))
    m02 = np.random.randint(1, 100, size=(linhas, colunas))

    for linha in range(linhas):
        for coluna in range(colunas):
            if linha == coluna:
                m01.itemset((linha, coluna), -1)
                m02.itemset((linha, coluna), -1)
            elif coluna > linha:
                continue
            elif coluna < linha:
                m01.itemset((coluna, linha), m01.item(linha, coluna))
                m02.itemset((coluna, linha), m02.item(linha, coluna))


    nodes = list(range(0, linhas))
    m1 = Matrix(m01, nodes, type="cost", name="cost", weight=0.3)
    m2 = Matrix(m02, nodes, type="cost", name="distance", weight=0.5)

    r = Repository([m1])

    # O(n^2)
    normalize(r)

    # O(n^2)
    result = wsm(r)

    start = 0
    target = 3

    final_result = dijkstra(result, start, target)[::-1]

    #print(final_result)

def fconst(N):
    """
    O(1) function
    """
    x = 1

def plotTC(fn, nMin, nMax, nInc, nTests):
    """
    Run timer and plot time complexity
    """
    x = []
    y = []
    for i in range(nMin, nMax, nInc):
        N = i
        testNTimer = timeit.Timer(partial(fn, N))
        t = testNTimer.timeit(number=nTests)
        x.append(i)
        y.append(t)
    p1 = pyplot.plot(x, y, 'o')
    #pyplot.legend([p1,], [fn.__name__, ])


# main() function
def main():
    print('Analyzing Algorithms...')

    plotTC(fconst, 10, 10000, 100, 100)

    # enable this in case you want to set y axis limits
    # pyplot.ylim((-0.1, 0.5))

    # show plot
    pyplot.show()


# call main
if __name__ == '__main__':
    main()