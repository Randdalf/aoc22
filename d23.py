#!/usr/bin/env python

"""Advent of Code 2022, Day 23"""

from collections import Counter

from aoc import solve


def parse(data):
    elves = set()
    for y, row in enumerate(data.split('\n')):
        for x, tile in enumerate(row):
            if tile == '#':
                elves.add((x, y))
    return elves


def north(x, y):
    return x, y-1


def south(x, y):
    return x, y+1


def west(x, y):
    return x-1, y


def east(x, y):
    return x+1, y


def adjacencies(x, y):
    yield x-1, y-1      # NW
    yield north(x, y)   # N
    yield x+1, y-1      # NE
    yield east(x, y)    # E
    yield x+1, y+1      # SE
    yield south(x, y)   # S
    yield x-1, y+1      # SW
    yield west(x, y)    # W


def any_north(hood):
    return not (hood[0] or hood[1] or hood[2])


def any_south(hood):
    return not (hood[4] or hood[5] or hood[6])


def any_west(hood):
    return not (hood[6] or hood[7] or hood[0])


def any_east(hood):
    return not (hood[2] or hood[3] or hood[4])


def ground_tiles(elves, rounds=10):
    dirs = [
        (any_north, north),
        (any_south, south),
        (any_west, west),
        (any_east, east)
    ]
    for round in range(rounds):
        # First half: propose movement.
        proposals = {}
        for elf in elves:
            x, y = elf
            neighborhood = [adj in elves for adj in adjacencies(x, y)]
            if not any(neighborhood):
                continue
            for cond, step in dirs:
                if cond(neighborhood):
                    proposals[elf] = step(x, y)
                    break

        # Second half: enact movement.
        moved = set()
        counter = Counter(proposals.values())
        for elf in elves:
            proposal = proposals.get(elf)
            if proposal is None or counter[proposal] > 1:
                moved.add(elf)
            else:
                moved.add(proposal)
        elves = moved

        # End of round: cycle direction checks.
        dirs = dirs[1:] + dirs[:1]

    # Find the smallest rectangle containing all the elves.
    min_x = min(x for x, y in elves)
    min_y = min(y for x, y in elves)
    max_x = max(x for x, y in elves)
    max_y = max(y for x, y in elves)
    area = (max_x - min_x + 1) * (max_y - min_y + 1)

    # Calculate the number of empty ground tiles.
    return area - len(elves)


if __name__ == "__main__":
    solve(23, parse, ground_tiles)
