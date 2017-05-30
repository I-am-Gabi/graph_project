from os import walk

from engine.matrix import Matrix


class Repository:
    def __init__(self):
        self.data = []

    def build(self):
        files = []
        for (dirpath, dirnames, filenames) in walk('../inputs/'):
            files = filenames
            break

        for file in files:
            m = Matrix()
            m.build('../inputs/' + file)
            self.data.append(m)