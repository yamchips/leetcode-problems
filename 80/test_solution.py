import unittest
import solution

class TestSolution(unittest.TestCase):
    def test_case1(self):
        nums = [1,1,1,2,2,3]
        self.assertEqual(5, solution.removeDuplicates(nums))

    def test_case2(self):
        nums = [0,0,1,1,1,1,2,3,3]
        self.assertEqual(7, solution.removeDuplicates(nums))

   
if __name__=='__main__':
    unittest.main()