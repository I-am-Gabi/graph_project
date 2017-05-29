from normalize import normalize
from repository import Repository

if __name__ == '__main__':
    r = Repository()
    r.build()

    normalize(r)