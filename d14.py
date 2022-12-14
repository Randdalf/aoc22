#!/usr/bin/env python

"""Advent of Code 2022, Day 14"""

from itertools import pairwise

from aoc import solve
from vec2 import Vec2


def parse_point(data):
    return Vec2(*map(int, data.split(',')))


def parse_points(data):
    return [parse_point(point) for point in data.split(' -> ')]


def straight_line(start, end):
    return range(min(start, end), max(start, end)+1)


def parse(data):
    state = set()
    for line in data.split('\n'):
        for a, b in pairwise(parse_points(line)):
            if a.x != b.x:
                state.update(Vec2(x, a.y) for x in straight_line(a.x, b.x))
            else:
                state.update(Vec2(a.x, y) for y in straight_line(a.y, b.y))
    return state


def sand_abyss(state):
    rested = 0
    abyss = max(rock.y for rock in state) + 1
    while True:
        sand = Vec2(500, 0)
        while True:
            step = Vec2(sand.x, sand.y + 1)
            if step.y == abyss:
                return rested
            if step in state:
                step.x -= 1
            if step in state:
                step.x += 2
            if step in state:
                rested += 1
                state.add(sand)
                break
            sand = step


def sand_floor(state):
    rested = 0
    floor = max(rock.y for rock in state) + 2

    def blocked(step):
        return step.y == floor or step in state

    while True:
        sand = Vec2(500, 0)
        if sand in state:
            return rested
        while True:
            step = Vec2(sand.x, sand.y + 1)
            if blocked(step):
                step.x -= 1
            if blocked(step):
                step.x += 2
            if blocked(step):
                rested += 1
                state.add(sand)
                break
            sand = step


if __name__ == "__main__":
    solve(14, parse, sand_abyss, sand_floor)
