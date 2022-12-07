#!/usr/bin/env python

"""Advent of Code 2022, Day 7"""

from collections import defaultdict

from aoc import solve


class Directory:
    def __init__(slf):
        slf.files = {}
        slf.dirs = defaultdict(Directory)
        slf._size = None

    def sub(slf, name):
        return slf.dirs[name]

    def file(slf, name, size):
        slf.files[name] = size

    @property
    def size(slf, max_size=10000):
        if slf._size is None:
            slf._size = sum(slf.files.values()) + sum(d.size for d in slf.dirs.values())
        return slf._size


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
        if dir.size <= max_size:
            total += dir.size
        total += total_size(dir, max_size)
    return total


def free_space(tree, total_space=70000000, target_space=30000000):
    min_size = target_space - total_space + tree.size
    to_delete = None
    stack = [tree]
    while len(stack) > 0:
        dir = stack.pop()
        if dir.size >= min_size and (to_delete is None or dir.size < to_delete.size):
            to_delete = dir
        stack.extend(dir.dirs.values())
    return to_delete.size


if __name__ == "__main__":
    solve(7, parse, total_size, free_space)
