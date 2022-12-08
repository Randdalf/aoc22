#!/usr/bin/env python

"""Advent of Code 2022, Day 8"""

from aoc import solve
from vec2 import Vec2


class Trees:
    def __init__(slf, heights):
        slf.heights = heights
        slf.width = 1 + max(pos.x for pos in heights.keys())
        slf.height = 1 + max(pos.y for pos in heights.keys())

    def visible(slf, pos, dir):
        max_height = -1
        while pos in slf.heights:
            height = slf.heights[pos]
            if height > max_height:
                yield pos
                max_height = height
            pos += dir


def parse(data):
    heights = {}
    for y, row in enumerate(data.splitlines()):
        for x, tile in enumerate(row):
            heights[Vec2(x, y)] = int(tile)
    return Trees(heights)


def visible_outside(trees):
    visible = set()
    for x in range(trees.width):
        visible.update(trees.visible(Vec2(x, 0), Vec2(0, 1)))
        visible.update(trees.visible(Vec2(x, trees.height-1), Vec2(0, -1)))
    for y in range(trees.height):
        visible.update(trees.visible(Vec2(0, y), Vec2(1, 0)))
        visible.update(trees.visible(Vec2(trees.width-1, y), Vec2(-1, 0)))
    return len(visible)


if __name__ == "__main__":
    solve(8, parse, visible_outside)
