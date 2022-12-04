#!/usr/bin/env python

"""Advent of Code 2022, Day 4"""

from aoc import solve


def parse_range(range):
    return tuple(int(x) for x in range.split('-'))


def parse_pair(pair):
    return tuple(parse_range(range) for range in pair.split(','))


def parse(data):
    return [parse_pair(pair) for pair in data.split('\n')]


def fully_contained(a, b):
    return (a[0] >= b[0] and a[1] <= b[1]) or (b[0] >= a[0] and b[1] <= a[1])


def num_fully_contained(pairs):
    return sum(int(fully_contained(a, b)) for a, b in pairs)


if __name__ == "__main__":
    solve(4, parse, num_fully_contained)
