#!/usr/bin/env python

"""Advent of Code 2022, Day 24 (Unit Tests)"""

import unittest

from d24 import parse, avoid_blizzards

example1 = """#.######
#>>.<^<#
#.<..<<#
#>v.><>#
#<^v^^>#
######.#"""


class AvoidBlizzardsTests(unittest.TestCase):
    def test_example1(slf):
        slf.assertEqual(avoid_blizzards(parse(example1)), 18)


if __name__ == "__main__":
    unittest.main()
