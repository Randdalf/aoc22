#!/usr/bin/env python

"""Advent of Code 2022, Day 3"""

from aoc import solve

priorities = [0 for i in range(128)]
for i in range(26):
    priorities[i + ord('a')] = 1 + i
    priorities[i + ord('A')] = 27 + i


def parse(data):
    return [[priorities[ord(i)] for i in s] for s in data.split('\n')]


def misplaced(sacks):
    total = 0
    for sack in sacks:
        mid = len(sack) // 2
        total += sum(set(sack[:mid]) & set(sack[mid:]))
    return total


def badges(sacks):
    total = 0
    for i in range(0, len(sacks), 3):
        total += sum(set(sacks[i]) & set(sacks[i+1]) & set(sacks[i+2]))
    return total


if __name__ == "__main__":
    solve(3, parse, misplaced, badges)
