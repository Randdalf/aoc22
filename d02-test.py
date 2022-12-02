#!/usr/bin/env python

"""Advent of Code 2022, Day 2 (Unit Tests)"""

import unittest

from d02 import parse, follow_guide

example1 = """A Y
B X
C Z"""


class FollowGuideTests(unittest.TestCase):
    def test_example1(slf):
        slf.assertEqual(follow_guide(parse(example1)), 15)


if __name__ == "__main__":
    unittest.main()
