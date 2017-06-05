import sys
import numpy as np

sys.path.append('../')

from algo.dijkstra import dijkstra
from algo.gargalo import gargalo

from engine.repository import Repository
from engine.wsm import wsm
from engine.normalize import normalize


def print_matrix(filename, data):
    # Write the array to disk
    with open(filename, 'w') as outfile:
        # I'm writing a header here just for the sake of readability
        # Any line starting with "#" will be ignored by numpy.loadtxt
        outfile.write('# Array shape: {0}\n'.format(data.shape))

        # Iterating through a ndimensional array produces slices along
        # the last axis. This is equivalent to data[i,:,:] in this case
        for data_slice in data:
            # The formatting string indicates that I'm writing out
            # the values in left-justified columns 7 characters in width
            # with 2 decimal places.
            np.savetxt(outfile, data_slice, fmt='%-7.2f')

            # Writing out a break to indicate different slices...
            # outfile.write('# New slice\n')

if __name__ == '__main__':
    while True:
        try:
            escolha = eval(input('Escolha uma ação. Opções disponíveis:\n1. Caminho mínimo\n2. Identificar gargalos\n'))
            r = Repository()
            r.build()
            # dijikstra
            if escolha == 1:
                normalize(r)

                print_matrix('../output/connections.log', r.data[0].connections)
                print_matrix('../output/normalize.log', r.data[0].connections_normalize)

                result = wsm(r)

                print(dijkstra(result, 0, 3))
                break
            # gargalo
            elif escolha == 2:
                try:
                    escolha = eval(input('Escolha um critério a ser analisado. Opções disponíveis:\n1. Banda\n2. '
                                         'Distância\n'))
                    if escolha != 1 and escolha != 2:
                        raise NameError

                    index_matrix = escolha - 1

                    print(gargalo(r.data[index_matrix]))
                    break
                except NameError:
                    raise NameError
            else:
                raise NameError
        except NameError:
            print('Opção inválida!')
