#!/usr/bin/env python

"""Advent of Code 2022, Day 12"""

from aoc import solve
from pathfind import astar
from vec2 import Vec2

dirs = [
    Vec2(0, -1),
    Vec2(1, 0),
    Vec2(0, 1),
    Vec2(-1, 0)
]


class Grid:
    def __init__(slf, elevation, start, end):
        slf.elevation = elevation
        slf.start = start
        slf.end = end


class Node:
    def __init__(slf, pos, grid):
        slf.pos = pos
        slf.grid = grid

    def __hash__(slf):
        return hash(slf.pos)

    def __eq__(slf, otr):
        return slf.pos == otr.pos

    @property
    def neighbors(slf):
        next_level = slf.grid.elevation[slf.pos] + 1
        for dir in dirs:
            neighbor = slf.pos + dir
            if next_level >= slf.grid.elevation.get(neighbor, 99):
                yield Node(neighbor, slf.grid)

    def dist(slf, neighbor):
        return 1


def parse(data):
    elevation = {}
    for y, row in enumerate(data.splitlines()):
        for x, tile in enumerate(row):
            pos = Vec2(x, y)
            if tile == 'S':
                start = pos
                tile = 'a'
            elif tile == 'E':
                end = pos
                tile = 'z'
            elevation[pos] = ord(tile) - ord('a')
    return Grid(elevation, start, end)


def best_signal(grid):
    def h(node):
        dist = node.pos - grid.end
        return dist.x * dist.x + dist.y * dist.y

    def goal(node):
        return node.pos == grid.end

    return len(astar(Node(grid.start, grid), goal, h))-1


def hiking_trail(grid):
    def h(node):
        dist = node.pos - grid.end
        return dist.x * dist.x + dist.y * dist.y

    def goal(node):
        return node.pos == grid.end

    for pos, elevation in grid.elevation.items():
        if elevation > 0:
            continue
        min_steps = None
        for pos, elevation in grid.elevation.items():
            if elevation > 0:
                continue
            path = astar(Node(pos, grid), goal, h)
            if path is None:
                continue
            steps = len(path)
            min_steps = steps if min_steps is None else min(steps, min_steps)
        return min_steps-1


if __name__ == "__main__":
    solve(12, parse, best_signal, hiking_trail)
