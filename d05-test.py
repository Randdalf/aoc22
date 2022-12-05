#!/usr/bin/env python

"""Advent of Code 2022, Day 5 (Unit Tests)"""

import unittest

from d05 import parse, rearrange

example1 = """    [D]
[N] [C]
[Z] [M] [P]
 1   2   3

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""


class RearrangeTests(unittest.TestCase):
    def test_example1(slf):
        slf.assertEqual(rearrange(parse(example1)), 'CMZ')


if __name__ == "__main__":
    unittest.main()
