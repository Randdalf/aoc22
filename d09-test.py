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

example2 = """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20"""


class TailVisitsTests(unittest.TestCase):
    def test_example1_2(slf):
        slf.assertEqual(tail_visits(parse(example1), 2), 13)

    def test_example1_10(slf):
        slf.assertEqual(tail_visits(parse(example1), 10), 1)

    def test_example2_10(slf):
        slf.assertEqual(tail_visits(parse(example2), 10), 36)


if __name__ == "__main__":
    unittest.main()
