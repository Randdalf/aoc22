#!/usr/bin/env python

"""Advent of Code 2022, Day 16 (Unit Tests)"""

import unittest

from d16 import parse, solo_pressure, pair_pressure

example1 = """Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II"""


class SoloPressureTests(unittest.TestCase):
    def test_example1(slf):
        slf.assertEqual(solo_pressure(parse(example1)), 1651)


class PairPressureTests(unittest.TestCase):
    def test_example1(slf):
        slf.assertEqual(pair_pressure(parse(example1)), 1707)


if __name__ == "__main__":
    unittest.main()
