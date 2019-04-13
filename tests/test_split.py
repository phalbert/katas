import unittest
from code.split_integer import splitInteger

class Test(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(splitInteger(10, 1), [10]) 
        self.assertEqual(splitInteger(2, 2), [1, 1]) 
        self.assertEqual(splitInteger(20, 5), [4, 4, 4, 4, 4]) 
        self.assertEqual(splitInteger(10, 5), [2, 2, 2, 2, 2])

if __name__ == '__main__':
    unittest.main()