#!/usr/bin/env python

"""Advent of Code 2022, Day 3"""

from aoc import solve


priorities = {}
for item in range(26):
    priorities[item + ord('a')] = 1 + item
    priorities[item + ord('A')] = 27 + item


def parse(data):
    for rucksack in data.split('\n'):
        mid = len(rucksack) // 2
        yield set(rucksack[:mid]), set(rucksack[mid:])


def mispacked(rucksacks):
    return sum(priorities[ord(i)] for c1, c2 in rucksacks for i in (c1 & c2))


if __name__ == "__main__":
    solve(3, parse, mispacked)
