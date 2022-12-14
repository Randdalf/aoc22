#!/usr/bin/env python

"""Advent of Code 2022, Day 14 (Unit Tests)"""

import unittest

from d14 import parse, sand_flow

example1 = """498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9"""


class SandFlowTests(unittest.TestCase):
    def test_example1(slf):
        slf.assertEqual(sand_flow(parse(example1)), 24)


if __name__ == "__main__":
    unittest.main()
