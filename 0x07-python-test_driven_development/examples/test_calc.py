#!/usr/bin/python3

import unittest
from calc import *

class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(4,2), 4 + 2)
        self.assertEqual(add(-4,-2), -6)
        self.assertEqual(add(-4,2), -2)

    def test_subtract(self):
        self.assertEqual(subtract(4,2), 2)
        self.assertEqual(subtract(-4,-2), -2)
        self.assertEqual(subtract(-4,2), -6)

    def test_divide(self):
        self.assertRaises(ValueError, divide, 10, 0)

if __name__=='__main__':
    unittest.main()
