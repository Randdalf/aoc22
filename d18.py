#!/usr/bin/env python

"""Advent of Code 2022, Day 18"""

from aoc import solve


def parse(data):
    return {tuple(map(int, cube.split(','))) for cube in data.split('\n')}


def adjacencies(x, y, z):
    yield x-1, y, z
    yield x+1, y, z
    yield x, y-1, z
    yield x, y+1, z
    yield x, y, z-1
    yield x, y, z+1


def compute(droplet, cond):
    return sum(6 - sum(cond(a) for a in adjacencies(*c)) for c in droplet)


def surface_area(droplet):
    return compute(droplet, lambda x: x in droplet)


def exterior_area(droplet):
    lo = tuple(min(c[i] - 1 for c in droplet) for i in range(3))
    hi = tuple(max(c[i] + 1 for c in droplet) for i in range(3))

    open = {(lo)}
    exterior = set()
    while len(open) > 0:
        pos = open.pop()
        exterior.add(pos)
        for adj in adjacencies(*pos):
            if any(a < l for a, l in zip(adj, lo)):
                continue
            if any(a > h for a, h in zip(adj, hi)):
                continue
            if adj in droplet:
                continue
            if adj in exterior:
                continue
            open.add(adj)

    return compute(droplet, lambda x: x not in exterior)


if __name__ == "__main__":
    solve(18, parse, surface_area, exterior_area)
