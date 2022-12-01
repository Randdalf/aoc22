#!/usr/bin/env python

"""Advent of Code 2022, Day 1"""

from aoc import solve


def parse(data):
    return [[int(x) for x in elf.split('\n')] for elf in data.split('\n\n')]


def most_calories(elves):
    return max(sum(elf) for elf in elves)


if __name__ == "__main__":
    solve(1, parse, most_calories)
