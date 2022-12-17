#!/usr/bin/env python

"""Advent of Code 2022, Day 17"""

from itertools import cycle

from aoc import solve


rocks = [
    # horizontal line
    [(0, 0), (1, 0), (2, 0), (3, 0)],
    # cross
    [(1, 0), (0, 1), (1, 1), (2, 1), (1, 2)],
    # backwards L
    [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)],
    # vertical line
    [(0, 0), (0, 1), (0, 2), (0, 3)],
    # square
    [(0, 0), (1, 0), (0, 1), (1, 1)]
]


def parse(data):
    return [-1 if jet == '<' else 1 for jet in data]


def collide(rock, tower):
    if any(r[0] < 0 or r[0] > 6 or r[1] < 0 for r in rock):
        return True
    return not tower.isdisjoint(rock)


def simulate(tower, height, rock, jets):
    steps = 0
    rock = [(r[0] + 2, r[1] + height + 3) for r in rock]
    while True:
        steps += 1
        jet = next(jets)
        new_rock = [(r[0] + jet, r[1]) for r in rock]
        if not collide(new_rock, tower):
            rock = new_rock
        new_rock = [(r[0], r[1] - 1) for r in rock]
        if collide(new_rock, tower):
            tower.update(rock)
            return max(height, 1 + max(r[1] for r in rock)), steps
        rock = new_rock


def sign(tower, height):
    open = {(0, 0)}
    closed = set()
    signature = set()
    while len(open) > 0:
        x, y = open.pop()
        if (x, y) in closed:
            continue
        closed.add((x, y))
        if (x, y + height) in tower:
            continue
        signature.add((x, y))
        if x > 0:
            open.add((x-1, y))
        if x < 6:
            open.add((x+1, y))
        if y > -height:
            open.add((x, y-1))
    return tuple(sorted(signature))


def tower_height(jets, n=2022):
    tower = set()
    jet_cycle = cycle(jets)
    rock_cycle = cycle(rocks)
    height = 0
    for i in range(n):
        height, _ = simulate(tower, height, next(rock_cycle), jet_cycle)
    return height


def impress_elephants(jets, n=1000000000000):
    tower = set()
    jet_cycle = cycle(jets)
    rock_cycle = cycle(rocks)
    rock_index = 0
    jet_index = 0
    height = 0
    cache = {}
    deltas = []
    while True:
        prev = height
        height, steps = simulate(tower, height, next(rock_cycle), jet_cycle)
        rock_index = (rock_index + 1) % len(rocks)
        jet_index = (jet_index + steps) % len(jets)
        deltas.append(height - prev)
        key = (rock_index, jet_index, sign(tower, height))
        if key in cache:
            init_steps = cache[key]
            loop_steps = len(deltas) - init_steps
            init_delta = sum(deltas[:init_steps])
            loop_delta = sum(deltas[init_steps:])
            n -= init_steps + loop_steps
            skip_loops = n // loop_steps
            skip_delta = skip_loops * loop_delta
            height += skip_delta
            tower = {(x, y + skip_delta) for x, y, in tower}
            for i in range(n % loop_steps):
                height, _ = simulate(tower, height, next(rock_cycle), jet_cycle)
            return height
        cache[key] = len(deltas)


if __name__ == "__main__":
    solve(17, parse, tower_height, impress_elephants)
