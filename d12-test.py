#!/usr/bin/env python

"""Advent of Code 2022, Day 12 (Unit Tests)"""

import unittest

from d12 import parse, best_signal, hiking_trail

example1 = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi"""


class BestSignalTests(unittest.TestCase):
    def test_example1(slf):
        slf.assertEqual(best_signal(parse(example1)), 31)


class HikingTrailTests(unittest.TestCase):
    def test_example1(slf):
        slf.assertEqual(hiking_trail(parse(example1)), 29)


if __name__ == "__main__":
    unittest.main()
