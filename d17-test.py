#!/usr/bin/env python

"""Advent of Code 2022, Day 17 (Unit Tests)"""

import unittest

from d17 import parse, tower_height

example1 = ">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"


class TowerHeightTests(unittest.TestCase):
    def test_example1(slf):
        slf.assertEqual(tower_height(parse(example1)), 3068)


if __name__ == "__main__":
    unittest.main()
