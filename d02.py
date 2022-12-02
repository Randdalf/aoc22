#!/usr/bin/env python

"""Advent of Code 2022, Day 2"""

from aoc import solve


def parse(data):
    return [(ord(x[0]) - ord('A'), ord(x[2]) - ord('X')) for x in data.split('\n')]


def encrypted_guide(guide):
    return len(guide) + sum(3 * ((r - o + 1) % 3) + r for o, r in guide)


def decrypted_guide(guide):
    return len(guide) + sum(3 * r + (o + r - 1) % 3 for o, r in guide)


if __name__ == "__main__":
    solve(2, parse, encrypted_guide, decrypted_guide)
