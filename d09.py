#!/usr/bin/env python

"""Advent of Code 2022, Day 9"""

from math import copysign

from aoc import solve
from vec2 import Vec2

dirs = {
    'L': Vec2(-1, 0),
    'R': Vec2(+1, 0),
    'U': Vec2(0, -1),
    'D': Vec2(0, +1)
}


def parse(data):
    for motion in data.split('\n'):
        parts = motion.split()
        for i in range(int(parts[1])):
            yield dirs[parts[0]]


def sign(x):
    return int(copysign(1, x)) if x != 0 else 0


def tail_visits(motions):
    head = Vec2(0, 0)
    tail = Vec2(0, 0)
    visited = {tail}
    for dir in motions:
        head += dir
        dist = head - tail
        if abs(dist.x) > 1 or abs(dist.y) > 1:
            tail += Vec2(sign(dist.x), sign(dist.y))
        visited.add(tail)
    return len(visited)


if __name__ == "__main__":
    solve(9, parse, tail_visits)
