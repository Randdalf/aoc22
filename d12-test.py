#!/usr/bin/env python

"""Advent of Code 2022, Day 12 (Unit Tests)"""

import unittest

from d12 import parse, fewest_steps

example1 = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi"""


class FewestStepsTests(unittest.TestCase):
    def test_example1(slf):
        slf.assertEqual(fewest_steps(parse(example1)), 31)


if __name__ == "__main__":
    unittest.main()
