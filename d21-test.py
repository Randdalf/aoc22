#!/usr/bin/env python

"""Advent of Code 2022, Day 21 (Unit Tests)"""

import unittest

from d21 import parse, monkey_math

example1 = """root: pppw + sjmn
dbpl: 5
cczh: sllz + lgvd
zczc: 2
ptdq: humn - dvpt
dvpt: 3
lfqf: 4
humn: 5
ljgn: 2
sjmn: drzm * dbpl
sllz: 4
pppw: cczh / lfqf
lgvd: ljgn * ptdq
drzm: hmdt - zczc
hmdt: 32"""


class MonkeyMathTests(unittest.TestCase):
    def test_example1(slf):
        slf.assertEqual(monkey_math(parse(example1)), 152)


if __name__ == "__main__":
    unittest.main()
