#!/usr/bin/env python

"""Advent of Code 2022, Day 4 (Unit Tests)"""

import unittest

from d04 import parse, num_fully_contained

example1 = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""


class NumFullyContainedTests(unittest.TestCase):
    def test_example1(slf):
        return slf.assertEqual(num_fully_contained(parse(example1)), 2)


if __name__ == "__main__":
    unittest.main()
