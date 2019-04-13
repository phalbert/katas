import unittest
from code.minimum_swaps import minimum_swaps

class Test(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(minimum_swaps([3, 2, 1]), 0) 
        self.assertEqual(minimum_swaps([3, 1, 2]), 1) 
        self.assertEqual(minimum_swaps([3, 1, 2, 4]), 2)

if __name__ == '__main__':
    unittest.main()