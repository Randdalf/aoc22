#!/usr/bin/env python

"""Advent of Code 2022, Day 3 (Unit Tests)"""

import unittest

from d03 import parse, misplaced, badges

example1 = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""


class MisplacedTests(unittest.TestCase):
    def test_example1(slf):
        return slf.assertEqual(misplaced(parse(example1)), 157)


class BadgesTests(unittest.TestCase):
    def test_example1(slf):
        return slf.assertEqual(badges(parse(example1)), 70)


if __name__ == "__main__":
    unittest.main()
