#!/usr/bin/env python

"""Advent of Code 2022, Day 15"""

from itertools import pairwise
import re

from aoc import solve


def parse(data):
    pattern = re.compile(r'Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)')
    return [tuple(map(int, m.groups())) for m in re.finditer(pattern, data)]


def manhattan(ax, ay, bx, by):
    return abs(ax - bx) + abs(ay - by)


def no_beacons(sensors, y=2000000):
    # Gather sensor range edges and intersecting beacons.
    edges = []
    y_beacons = set()
    for sx, sy, bx, by in sensors:
        if by == y:
            y_beacons.add((bx, by))
        b_dist = manhattan(sx, sy, bx, by)
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


def tuning_frequency(sensors, size=4000000):
    tuned = []
    for i, (sx, sy, bx, by) in enumerate(sensors):
        tuned.append((i, sx, sy, manhattan(sx, sy, bx, by)))
    for i, sx0, sy0, dist0 in tuned:
        e_dist_y = dist0 + 1
        for dy in range(sy0 - e_dist_y, sy0 + e_dist_y + 1):
            if dy < 0 or dy > size:
                continue
            e_dist_x = e_dist_y - abs(dy - sy0)
            for dx in [sx0 - e_dist_x, sx0 + e_dist_x]:
                if dx < 0 or dx > size:
                    continue
                found = True
                for j, sx1, sy1, dist1 in tuned:
                    if i == j:
                        continue
                    if manhattan(dx, dy, sx1, sy1) <= dist1:
                        found = False
                        break
                if found:
                    return dx * 4000000 + dy


if __name__ == "__main__":
    solve(15, parse, no_beacons, tuning_frequency)
