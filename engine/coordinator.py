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

    #print(r.data[0].connections)
    #print(r.data[0].connections_normalize)

    result = wsm(r)
    #print(result)
    dijkstra(result, 0, 3)


