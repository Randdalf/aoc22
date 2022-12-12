#!/usr/bin/env python

"""Advent of Code 2022, Day 12"""

import math

from aoc import solve
from pathfind import astar, bfs
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
    def __init__(slf, pos, grid, check):
        slf.pos = pos
        slf.grid = grid
        slf.check = check

    def __hash__(slf):
        return hash(slf.pos)

    def __eq__(slf, otr):
        return slf.pos == otr.pos

    @property
    def neighbors(slf):
        level = slf.grid.elevation[slf.pos]
        for dir in dirs:
            neighbor = slf.pos + dir
            n_level = slf.grid.elevation.get(neighbor)
            if n_level is None:
                continue
            if slf.check(level, n_level):
                yield Node(neighbor, slf.grid, slf.check)

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


def up_check(from_level, to_level):
    return from_level+1 >= to_level


def down_check(from_level, to_level):
    return from_level-1 <= to_level


def best_signal(grid):
    def h(node):
        dist = node.pos - grid.end
        return dist.x * dist.x + dist.y * dist.y

    def goal(node):
        return node.pos == grid.end

    return len(astar(Node(grid.start, grid, up_check), goal, h))-1


def hiking_trail(grid):
    dist, prev = bfs(Node(grid.end, grid, down_check))
    min_steps = math.inf
    for pos, elevation in grid.elevation.items():
        if elevation == 0:
            min_steps = min(dist[Node(pos, None, None)], min_steps)
    return min_steps


if __name__ == "__main__":
    solve(12, parse, best_signal, hiking_trail)
