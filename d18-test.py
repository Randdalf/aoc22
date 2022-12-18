#!/usr/bin/env python

"""Advent of Code 2022, Day 18 (Unit Tests)"""

import unittest

from d18 import parse, surface_area

example1 = """2,2,2
1,2,2
3,2,2
2,1,2
2,3,2
2,2,1
2,2,3
2,2,4
2,2,6
1,2,5
3,2,5
2,1,5
2,3,5"""


class SurfaceAreaTests(unittest.TestCase):
    def test_example1(slf):
        slf.assertEqual(surface_area(parse(example1)), 64)


if __name__ == "__main__":
    unittest.main()
