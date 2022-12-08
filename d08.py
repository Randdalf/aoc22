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

    def viewable(slf, pos, dir, from_height):
        count = 0
        pos += dir
        while pos in slf.heights:
            height = slf.heights[pos]
            count += 1
            if height >= from_height:
                break
            pos += dir
        return count


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


def scenic_score(trees):
    max_score = 0
    for pos, height in trees.heights.items():
        score = 1
        score *= trees.viewable(pos, Vec2(+1, 0), height)
        score *= trees.viewable(pos, Vec2(-1, 0), height)
        score *= trees.viewable(pos, Vec2(0, +1), height)
        score *= trees.viewable(pos, Vec2(0, -1), height)
        max_score = max(score, max_score)
    return max_score


if __name__ == "__main__":
    solve(8, parse, visible_outside, scenic_score)
