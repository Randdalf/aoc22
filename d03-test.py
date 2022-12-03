#!/usr/bin/env python

"""Advent of Code 2022, Day 3 (Unit Tests)"""

import unittest

from d03 import parse, mispacked

example1 = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""


class MispackedTests(unittest.TestCase):
    def test_example1(slf):
        return slf.assertEqual(mispacked(parse(example1)), 157)


if __name__ == "__main__":
    unittest.main()
