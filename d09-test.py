#!/usr/bin/env python

"""Advent of Code 2022, Day 9 (Unit Tests)"""

import unittest

from d09 import parse, tail_visits

example1 = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""


class TailVisitsTests(unittest.TestCase):
    def test_example1(slf):
        slf.assertEqual(tail_visits(parse(example1)), 13)


if __name__ == "__main__":
    unittest.main()
