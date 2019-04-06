import unittest
from code.numerals import roman_converter

class NumeralTests(unittest.TestCase):
    def test_one(self):
        roman_numeral = roman_converter(1)
        self.assertEqual(roman_numeral, 'I')

    def test_two(self):
        roman = roman_converter(2)
        self.assertEqual(roman, 'II')

if __name__ == '__main__':
    unittest.main()