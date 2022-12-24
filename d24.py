#!/usr/bin/env python

"""Advent of Code 2022, Day 24"""

from math import sqrt

from aoc import solve
from pathfind import astar


def moves(x, y):
    yield x, y     # wait
    yield x-1, y   # move left
    yield x, y-1   # move up
    yield x+1, y   # move right
    yield x, y+1   # move down


class Basin:
    def __init__(slf, blizzards, w, h):
        slf.blizzards = [blizzards]
        slf.danger = []
        slf.w = w
        slf.h = h
        slf.start = (1, 0)
        slf.goal = (w-2, h-1)

    def get_blizzards(slf, mins):
        for i in range(len(slf.blizzards), mins+1):
            prev = slf.blizzards[-1]
            new = []
            for x, y, d in prev:
                if d == '>':
                    x = 1 if x == slf.w-2 else x+1
                elif d == '<':
                    x = slf.w-2 if x == 1 else x-1
                elif d == 'v':
                    y = 1 if y == slf.h-2 else y+1
                elif d == '^':
                    y = slf.h-2 if y == 1 else y-1
                new.append((x, y, d))
            slf.blizzards.append(new)
        return slf.blizzards[mins]

    def get_danger(slf, mins):
        for i in range(len(slf.danger), mins+1):
            slf.danger.append({(x, y) for x, y, d in slf.get_blizzards(i)})
        return slf.danger[mins]

    def get_moves(slf, pos, mins):
        danger = slf.get_danger(mins)
        for move in moves(*pos):
            if move == slf.goal:
                yield move, mins
            if move != slf.start:
                mx, my = move
                if mx <= 0 or mx >= slf.w-1:
                    continue
                if my <= 0 or my >= slf.h-1:
                    continue
            if move in danger:
                continue
            yield move, mins


class Node:
    def __init__(slf, basin, pos, mins):
        slf.basin = basin
        slf.pos = pos
        slf.mins = mins

    def __hash__(slf):
        return hash((slf.pos, slf.mins))

    def __eq__(slf, otr):
        return slf.pos == otr.pos and slf.mins == otr.mins

    @property
    def neighbors(slf):
        for move, mins in slf.basin.get_moves(slf.pos, slf.mins+1):
            yield Node(slf.basin, move, mins)

    def dist(slf, neighbor):
        return 1


def parse(data):
    blizzards = []
    rows = data.split('\n')
    for y, row in enumerate(rows):
        for x, tile in enumerate(row):
            if tile != '#' and tile != '.':
                blizzards.append((x, y, tile))
    return Basin(blizzards, len(row), len(rows))


def avoid_blizzards(basin, mins=0):
    def h(node):
        pos = node.pos
        goal = basin.goal
        return abs(goal[0]-pos[0]) + abs(goal[1]-pos[1])

    def goal(node):
        return node.pos == basin.goal

    return len(astar(Node(basin, basin.start, mins), goal, h))-1


def collect_snacks(basin):
    mins = avoid_blizzards(basin)
    basin.start, basin.goal = basin.goal, basin.start
    mins += avoid_blizzards(basin, mins)
    basin.start, basin.goal = basin.goal, basin.start
    return mins + avoid_blizzards(basin, mins)


if __name__ == "__main__":
    solve(24, parse, avoid_blizzards, collect_snacks)
