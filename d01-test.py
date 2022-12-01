#!/usr/bin/env python

"""Advent of Code 2022, Day 1 (Unit Tests)"""

import unittest

from d01 import parse, most_calories

example1 = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""


class MostCaloriesTests(unittest.TestCase):
    def test_example1(slf):
        slf.assertEqual(most_calories(parse(example1)), 24000)


if __name__ == "__main__":
    unittest.main()
