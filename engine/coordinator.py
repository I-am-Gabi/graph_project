import sys
import numpy as np

sys.path.append('../')

from algo.dijkstra import dijkstra

from engine.repository import Repository
from engine.wsm import wsm
from engine.normalize import normalize


def print_matrix(data):
    # Write the array to disk
    with open('../output/coordinator.log', 'w') as outfile:
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
    r = Repository()
    r.build()

    normalize(r)

    print_matrix(r.data[0].connections)
    print_matrix(r.data[0].connections_normalize)

    result = wsm(r)

    dijkstra(result, 0, 3)

