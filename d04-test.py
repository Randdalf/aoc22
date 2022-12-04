#!/usr/bin/env python

"""Advent of Code 2022, Day 4 (Unit Tests)"""

import unittest

from d04 import parse, num_contained, num_overlapped

example1 = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""


class NumContainedTests(unittest.TestCase):
    def test_example1(slf):
        return slf.assertEqual(num_contained(parse(example1)), 2)


class NumOverlapsTests(unittest.TestCase):
    def test_example2(slf):
        return slf.assertEqual(num_overlapped(parse(example1)), 4)


if __name__ == "__main__":
    unittest.main()
