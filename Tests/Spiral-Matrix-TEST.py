import unittest
import numpy as np
from Challenges.spiral_matrix_jun_24_25 import spiral

class TestSpiralMatrix(unittest.TestCase):

    def test_square_matrix(self):
        mtx = np.array([[1, 2, 3],
                        [4, 5, 6],
                        [7, 8, 9]])
        expected = [1, 2, 3, 6, 9, 8, 7, 4, 5]
        self.assertEqual(spiral(mtx), expected)

    def test_single_row(self):
        mtx2 = np.array([[1, 2, 3]])
        expected = [1, 2, 3]
        self.assertEqual(spiral(mtx2), expected)

    def test_empty_matrix(self):
        mtx3 = np.array([[]])
        expected = []
        self.assertEqual(spiral(mtx3), expected)

    def test_tall_matrix(self):
        mtx4 = np.array([[1, 2, 3],
                         [4, 5, 6],
                         [7, 8, 9],
                         [10, 11, 12],
                         [13, 14, 15]])
        expected = [1, 2, 3, 6, 9, 12, 15, 14, 13, 10, 7, 4, 5, 8, 11]
        self.assertEqual(spiral(mtx4), expected)

    def test_long_matrix(self):
        mtx4 = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
                         [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]])
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13]
        self.assertEqual(spiral(mtx4), expected)

if __name__ == '__main__':
    unittest.main()