import unittest
import solution

class TestSolution(unittest.TestCase):
    def test_case1(self):
        nums = [1,2,3,4,5,6,7]
        k = 3
        solution.rotate3(nums,k)
        self.assertEqual(nums, [5,6,7,1,2,3,4])

    def test_case2(self):
        nums = [-1, -100, 3, 99]
        k = 2
        solution.rotate3(nums, k)
        self.assertEqual(nums, [3, 99, -1, -100])
    
    def test_case3(self):
        nums = [1,2,3,4,5,6,7]
        k = 10
        solution.rotate3(nums,k)
        self.assertEqual(nums, [5,6,7,1,2,3,4])

    def test_case4(self):
        nums = [1,2,3,4,5,6,7]
        k = 0
        solution.rotate3(nums,k)
        self.assertEqual(nums, [1,2,3,4,5,6,7])

    def test_case5(self):
        nums = [-1]
        k = 3
        solution.rotate3(nums, k)
        self.assertEqual(nums, [-1])
    

if __name__=='__main__':
    unittest.main()