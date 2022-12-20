#!/usr/bin/env python

"""Advent of Code 2022, Day 20"""

from aoc import solve


def parse(data):
    return [int(x) for x in data.split('\n')]


def move(back, fwd, i, steps):
    for step in range(steps):
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


def grove_coords(file, key=1, mixes=1, offsets=(1000, 2000, 3000)):
    n = len(file)

    # Apply the decryption key.
    file = [num * key for num in file]
    stepss = [num % (n-1) for num in file]

    # Initialise circular linked list.
    prev = [(i-1) % n for i in range(n)]
    next = [(i+1) % n for i in range(n)]

    # Mix the file.
    for mix in range(mixes):
        for i, steps in enumerate(stepss):
            move(prev, next, i, steps)

    # Sum the numbers at each offset.
    zero = file.index(0)
    return sum(lookup(file, prev, next, zero, offset) for offset in offsets)


def decrypt(file):
    return grove_coords(file, key=811589153, mixes=10)


if __name__ == "__main__":
    solve(20, parse, grove_coords, decrypt)
