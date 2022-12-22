#!/usr/bin/env python

"""Advent of Code 2022, Day 22 (Unit Tests)"""

import unittest

from d22 import parse, final_password

example1 = """        ...#
        .#..
        #...
        ....
...#.......#
........#...
..#....#....
..........#.
        ...#....
        .....#..
        .#......
        ......#.

10R5L5R10L4R5L5"""


class FinalPasswordTests(unittest.TestCase):
    def test_example1(slf):
        slf.assertEqual(final_password(parse(example1)), 6032)


if __name__ == "__main__":
    unittest.main()
