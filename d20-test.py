#!/usr/bin/env python

"""Advent of Code 2022, Day 20 (Unit Tests)"""

import unittest

from d20 import parse, grove_coords

example1 = """1
2
-3
3
-2
0
4"""


class GroveCoordsTests(unittest.TestCase):
    def test_example1(slf):
        slf.assertEqual(grove_coords(parse(example1)), 3)


if __name__ == "__main__":
    unittest.main()
