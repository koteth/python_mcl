import unittest
import numpy as np
from mcl_clustering import *
import logging

#TODO: improveme
class TestMcl(unittest.TestCase):

    def setUp(self):
        pass

    def test_normalize(self):
        A = np.ones((4, 4))
        A[2,0] = 2
        A_n = normalize(A)
        self.assertEqual(0.4, A_n[2, 0])

    def test_inflate(self):
        A = np.ones((4, 4))
        A[3,0] = 2
        A[1,0] = 3
        A_i = inflate(A, 2)
        self.assertTrue( A[3, 0] >  A_i[3, 0])

    def test_expand(self):
        A = np.ones((4, 4))
        A[3,0] = 2
        A[2,0] = 3
        A = normalize(A)
        A_i = expand(A, 2)
        self.assertTrue(A[2, 0] > A_i[2, 0])

if __name__ == '__main__':
    unittest.main()

