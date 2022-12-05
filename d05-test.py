#!/usr/bin/env python

"""Advent of Code 2022, Day 5 (Unit Tests)"""

import unittest

from d05 import parse, crate_mover_9000, crate_mover_9001

example1 = """    [D]
[N] [C]
[Z] [M] [P]
 1   2   3

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""


class CrateMover9000Tests(unittest.TestCase):
    def test_example1(slf):
        slf.assertEqual(crate_mover_9000(parse(example1)), 'CMZ')


class CrateMover9001Tests(unittest.TestCase):
    def test_example1(slf):
        slf.assertEqual(crate_mover_9001(parse(example1)), 'MCD')


if __name__ == "__main__":
    unittest.main()
