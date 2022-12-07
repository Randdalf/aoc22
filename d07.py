#!/usr/bin/env python

"""Advent of Code 2022, Day 7"""

from collections import defaultdict

from aoc import solve


class Directory:
    def __init__(slf):
        slf.files = {}
        slf.dirs = defaultdict(Directory)

    def sub(slf, name):
        return slf.dirs[name]

    def file(slf, name, size):
        slf.files[name] = size

    @property
    def size(slf, max_size=10000):
        return sum(slf.files.values()) + sum(d.size for d in slf.dirs.values())


def parse(data):
    term = [tuple(line.split()) for line in data.splitlines()]
    term.reverse()
    root = Directory()
    path = [root]
    while len(term) > 0:
        cmd = term.pop()
        if cmd[1] == 'cd':
            if cmd[2] == '/':
                path = [root]
            elif cmd[2] == '..':
                path.pop()
            else:
                path.append(path[-1].sub(cmd[2]))
        elif cmd[1] == 'ls':
            while len(term) > 0 and term[-1][0] != '$':
                line = term.pop()
                if line[0] == 'dir':
                    path[-1].sub(line[1])
                else:
                    path[-1].file(line[1], int(line[0]))
    return root


def total_size(tree, max_size=100000):
    total = 0
    for name, dir in tree.dirs.items():
        size = dir.size
        if size <= max_size:
            total += size
        total += total_size(dir, max_size)
    return total


if __name__ == "__main__":
    solve(7, parse, total_size)
