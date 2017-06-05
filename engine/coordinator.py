import sys

sys.path.append('../')

from algo.dijkstra import dijkstra

from engine.repository import Repository
from engine.wsm import wsm
from engine.normalize import normalize

if __name__ == '__main__':
    r = Repository()
    r.build()

    normalize(r)

    #print(r.data[0].connections_normalize)
    #print(r.data[1].connections_normalize)

    result = wsm(r)

    dijkstra(result, 0, 3)


