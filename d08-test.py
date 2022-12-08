#!/usr/bin/env python

"""Advent of Code 2022, Day 8 (Unit Tests)"""

import unittest

from d08 import parse, visible_outside, scenic_score

example1 = """30373
25512
65332
33549
35390"""


class VisibleOutsideTests(unittest.TestCase):
    def test_example1(slf):
        slf.assertEqual(visible_outside(parse(example1)), 21)


class ScenicScoreTests(unittest.TestCase):
    def test_example1(slf):
        slf.assertEqual(scenic_score(parse(example1)), 8)


if __name__ == "__main__":
    unittest.main()
