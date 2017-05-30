import unittest
import sys

sys.path.append('../')

from engine.matrix import Matrix, np


class TestMatrixMethods(unittest.TestCase):
    def test_build(self):
        m = Matrix()
        m.build('input_test.txt')
        self.assertEqual(m.type, 'cost')
        self.assertEqual(m.name, 'cost')
        self.assertEqual(m.weight, 0.3)
        self.assertEqual(m.nodes, ['a', 'b', 'c'])
        matrix = np.matrix([[0, 1, 1], [1, 0, 0], [1, 0, 0]])
        self.assertTrue(np.allclose(m.connections, matrix))


if __name__ == '__main__':
    unittest.main()
