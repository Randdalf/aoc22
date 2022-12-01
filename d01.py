#!/usr/bin/env python

"""Advent of Code 2022, Day 1"""

from aoc import solve


def parse(data):
    return [[int(x) for x in elf.split('\n')] for elf in data.split('\n\n')]


def most_calories(elves, n):
    calories = [sum(elf) for elf in elves]
    calories.sort(reverse=True)
    return sum(calories[:n])


if __name__ == "__main__":
    solve(1, parse, lambda x: most_calories(x, 1), lambda x: most_calories(x, 3))
