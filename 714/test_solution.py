import unittest
import solution
import numpy as np
import os

class TestSolution(unittest.TestCase):
    def test_case1(self):
        prices = [1,3,2,8,4,9]
        fee = 2
        self.assertEqual(8, solution.maxProfit3(prices,fee))

    def test_case2(self):
        prices = [1,3,7,5,10,3]
        fee = 3
        self.assertEqual(6, solution.maxProfit3(prices,fee))

    def test_case3(self):
        prices = [9]
        fee = 2
        self.assertEqual(0, solution.maxProfit3(prices,fee))
    
    def test_case4(self):
        prices = [9, 13]
        fee = 2
        self.assertEqual(2, solution.maxProfit3(prices,fee))

    def test_case5(self):
        prices = [7,6,4,3,1]
        fee = 2
        self.assertEqual(0, solution.maxProfit3(prices,fee))

    def test_case5(self):
        current_dir = os.path.dirname(__file__)
        filepath = os.path.join(current_dir, "prices.npy")
        prices = np.load(filepath).tolist()
        fee = 6806
        self.assertEqual(309432285, solution.maxProfit3(prices,fee))

if __name__=='__main__':
    unittest.main()