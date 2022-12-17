#!/usr/bin/env python

"""Advent of Code 2022, Day 17"""

from itertools import cycle

from aoc import solve
from vec2 import Vec2


rocks = [
    # horizontal line
    [Vec2(0, 0), Vec2(1, 0), Vec2(2, 0), Vec2(3, 0)],

    # cross
    [Vec2(1, 0), Vec2(0, 1), Vec2(1, 1), Vec2(2, 1), Vec2(1, 2)],

    # backwards L
    [Vec2(0, 0), Vec2(1, 0), Vec2(2, 0), Vec2(2, 1), Vec2(2, 2)],

    # vertical line
    [Vec2(0, 0), Vec2(0, 1), Vec2(0, 2), Vec2(0, 3)],

    # square
    [Vec2(0, 0), Vec2(1, 0), Vec2(0, 1), Vec2(1, 1)]
]


def parse(data):
    return cycle([Vec2(-1, 0) if jet == '<' else Vec2(1, 0) for jet in data])


def collide(rock, pos, tower):
    rock = [r + pos for r in rock]
    if any(r.x < 0 or r.x > 6 or r.y < 0 for r in rock):
        return True
    if any(r in tower for r in rock):
        return True
    return False


def simulate(tower, rock, jets):
    pos = Vec2(2, 4 + max((t.y for t in tower), default=-1))
    while True:
        pos_j = pos + next(jets)
        if not collide(rock, pos_j, tower):
            pos = pos_j
        pos_g = pos + Vec2(0, -1)
        if collide(rock, pos_g, tower):
            return tower.update(r + pos for r in rock)
        pos = pos_g


def tower_height(jets, n=2022):
    tower = set()
    jet_cycle = cycle(jets)
    rock_cycle = cycle(rocks)
    for i in range(n):
        simulate(tower, next(rock_cycle), jet_cycle)
    return 1 + max(t.y for t in tower)


if __name__ == "__main__":
    solve(17, parse, tower_height)
