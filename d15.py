#!/usr/bin/env python

"""Advent of Code 2022, Day 15"""

from itertools import pairwise
import re

from aoc import solve


def parse(data):
    pattern = re.compile(r'Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)')
    return [tuple(map(int, m.groups())) for m in re.finditer(pattern, data)]


def no_beacons_row(sensors, y=2000000):
    # Gather sensor range edges and intersecting beacons.
    edges = []
    y_beacons = set()
    for sx, sy, bx, by in sensors:
        if by == y:
            y_beacons.add((bx, by))
        b_dist = abs(sx - bx) + abs(sy - by)
        y_dist = abs(sy - y)
        if y_dist > b_dist:
            continue
        width = b_dist - y_dist
        edges.append((sx - width, -1))
        edges.append((sx + width, +1))

    # Find contiguous chunks of sensor range based on the edges.
    no_beacons = -len(y_beacons)
    start = None
    active = 0
    for i, edge in enumerate(sorted(edges)):
        if start is None:
            start = edge[0]
        active -= edge[1]
        if active == 0:
            no_beacons += 1 + edge[0] - start

    return no_beacons


if __name__ == "__main__":
    solve(15, parse, no_beacons_row)
