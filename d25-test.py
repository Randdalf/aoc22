#!/usr/bin/env python

"""Advent of Code 2022, Day 25 (Unit Tests)"""

import unittest

from d25 import parse, snafu_sum

example1 = """1=-0-2
12111
2=0=
21
2=01
111
20012
112
1=-1=
1-12
12
1=
122"""


class SnafuSumTests(unittest.TestCase):
    def test_example1(slf):
        slf.assertEqual(snafu_sum(parse(example1)), '2=-1=0')


if __name__ == "__main__":
    unittest.main()
