#!/usr/bin/env python

"""Advent of Code 2022, Day 11 (Unit Tests)"""

import unittest

from d11 import parse, monkey_business_20, monkey_business_10k

example1 = """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1"""


class MonkeyBusiness20Tests(unittest.TestCase):
    def test_example1(slf):
        slf.assertEqual(monkey_business_20(parse(example1)), 10605)


class MonkeyBusiness10kTests(unittest.TestCase):
    def test_example1(slf):
        slf.assertEqual(monkey_business_10k(parse(example1)), 2713310158)


if __name__ == "__main__":
    unittest.main()
