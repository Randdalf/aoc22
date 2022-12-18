#!/usr/bin/env python

"""Advent of Code 2022, Day 18"""

from aoc import solve


def parse(data):
    return {tuple(map(int, cube.split(','))) for cube in data.split('\n')}


def adj(x, y, z):
    yield x-1, y, z
    yield x+1, y, z
    yield x, y-1, z
    yield x, y+1, z
    yield x, y, z-1
    yield x, y, z+1


def surface_area(cubes):
    return sum(6 - sum(int(a in cubes) for a in adj(*c)) for c in cubes)


if __name__ == "__main__":
    solve(18, parse, surface_area)
