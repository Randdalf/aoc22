#!/usr/bin/env python

"""Advent of Code 2022, Day 19 (Unit Tests)"""

import unittest

from d19 import parse, quality_levels

example1 = """Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian.
Blueprint 2: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 8 clay. Each geode robot costs 3 ore and 12 obsidian."""


class QualityLevelsTests(unittest.TestCase):
    def test_example1(slf):
        slf.assertEqual(quality_levels(parse(example1)), 33)


if __name__ == "__main__":
    unittest.main()
