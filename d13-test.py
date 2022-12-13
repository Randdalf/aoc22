#!/usr/bin/env python

"""Advent of Code 2022, Day 13 (Unit Tests)"""

import unittest

from d13 import parse, right_order

example1 = """[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]"""


class RightOrderTests(unittest.TestCase):
    def test_example1(slf):
        slf.assertEqual(right_order(parse(example1)), 13)


if __name__ == "__main__":
    unittest.main()
