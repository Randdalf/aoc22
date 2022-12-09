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


def tail_visits(motions, knots):
    rope = [Vec2(0, 0) for knot in range(knots)]
    visited = {rope[-1]}
    for dir in motions:
        rope[0] += dir
        for i in range(1, len(rope)):
            dist = rope[i-1] - rope[i]
            if abs(dist.x) > 1 or abs(dist.y) > 1:
                rope[i] += Vec2(sign(dist.x), sign(dist.y))
        visited.add(rope[-1])
    return len(visited)


if __name__ == "__main__":
    solve(9, parse, lambda x: tail_visits(x, 2), lambda x: tail_visits(x, 10))
