import unittest
import maxProfit

class TestMaxProfit(unittest.TestCase):
    def test_case1(self):
        prices = [7,1,5,3,6,4]
        self.assertEqual(7, maxProfit.maxProfit3(prices))

    def test_case2(self):
        prices = [1,2,3,4,5]
        self.assertEqual(4, maxProfit.maxProfit3(prices))

    def test_case3(self):
        prices = [9]
        self.assertEqual(0, maxProfit.maxProfit3(prices))
    
    def test_case4(self):
        prices = [9, 13]
        self.assertEqual(4, maxProfit.maxProfit3(prices))

    def test_case5(self):
        prices = [7,6,4,3,1]
        self.assertEqual(0, maxProfit.maxProfit3(prices))


if __name__=='__main__':
    unittest.main()