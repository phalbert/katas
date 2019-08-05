import unittest
from src.calc import check_string

class Test(unittest.TestCase):

    def test_output_is_correct(self):
        result1 = check_string('arrb6???4xxbl5???eee5')
        result2 = check_string('acc?7??sss?3rr1??????5')
        result3 = check_string('5??aaaaaaaaaaaaaaaaaaa?5?5')
        result4 = check_string('9???1???9???1???9')
        result5 = check_string('aa6?9')

        self.assertIsInstance(result1, bool, msg='Incorrect output type')
        self.assertEqual(result1, True, msg='Incorrect output')

        self.assertIsInstance(result2, bool, msg='Incorrect output type')
        self.assertEqual(result2, True, msg='Incorrect output')

        self.assertIsInstance(result3, bool, msg='Incorrect output type')
        self.assertEqual(result3, False, msg='Incorrect output')

        self.assertIsInstance(result4, bool, msg='Incorrect output type')
        self.assertEqual(result4, True, msg='Incorrect output')

        self.assertIsInstance(result5, bool, msg='Incorrect output type')
        self.assertEqual(result5, False, msg='Incorrect output')

    def test_error_message_if_not_string(self):
        self.assertRaises(TypeError, check_string, 33)
