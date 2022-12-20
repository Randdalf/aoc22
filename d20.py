#!/usr/bin/env python

"""Advent of Code 2022, Day 20"""

from aoc import solve


def parse(data):
    return [int(x) for x in data.split('\n')]


def move(back, fwd, i, n):
    for step in range(n):
        old_back = back[i]
        old_fwd = fwd[i]
        back[i] = old_fwd
        fwd[i] = fwd[old_fwd]
        back[fwd[i]] = i
        fwd[old_back] = old_fwd
        back[old_fwd] = old_back
        fwd[old_fwd] = i


def lookup(file, prev, next, cursor, offset):
    for i in range(offset % len(file)):
        cursor = next[cursor]
    return file[cursor]


def grove_coords(file, offsets=(1000, 2000, 3000)):
    # Initialise circular linked list.
    n = len(file)
    prev = [None for i in range(n)]
    next = [None for i in range(n)]
    for i in range(len(file)):
        prev[i] = (i-1) % n
        next[i] = (i+1) % n

    # Mix the file.
    for i, num in enumerate(file):
        if num < 0:
            move(next, prev, i, -num)
        elif num > 0:
            move(prev, next, i, num)

    # Sum the numbers at each offset.
    zero = file.index(0)
    return sum(lookup(file, prev, next, zero, offset) for offset in offsets)


if __name__ == "__main__":
    solve(20, parse, grove_coords)
