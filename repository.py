from os import walk

from matrix import Matrix


class Repository:
    def __init__(self):
        self.data = []

    def build(self):
        files = []
        for (dirpath, dirnames, filenames) in walk('./input/'):
            files = filenames
            break

        for file in files:
            m = Matrix()
            m.build('input/' + file)
            self.data.append(m)