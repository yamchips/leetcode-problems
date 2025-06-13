import unittest
import solution

class TestSolution(unittest.TestCase):
    def test_case1(self):
        nums = [1,1,2]
        self.assertEqual(2, solution.removeDuplicates(nums))

    def test_case2(self):
        nums = [0,0,1,1,1,2,2,3,3,4]
        self.assertEqual(5, solution.removeDuplicates(nums))

    def test_case3(self):
        nums = [0,0,0,1,2,2]
        self.assertEqual(3, solution.removeDuplicates(nums))

   
if __name__=='__main__':
    unittest.main()