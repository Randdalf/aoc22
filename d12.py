#!/usr/bin/env python

"""Advent of Code 2022, Day 12"""

from aoc import solve
from pathfind import dijkstra
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


def fewest_steps(grid):
    def goal(node):
        return node.pos == grid.end
    return len(dijkstra(Node(grid.start, grid), goal))-1


if __name__ == "__main__":
    solve(12, parse, fewest_steps)
