#!/usr/bin/env python

"""Advent of Code 2022, Day 5"""

import re

from aoc import solve


def parse_stacks(data):
    rows = data.split('\n')
    stacks = [[] for i in range(max(map(int, rows[-1].split())))]
    for row in reversed(rows[:-1]):
        for i, col in enumerate(range(1, len(row), 4)):
            if row[col] != ' ':
                stacks[i].append(row[col])
    return stacks


def parse_proc(data):
    pattern = re.compile(r'move (\d+) from (\d+) to (\d+)')
    return [tuple(int(n) for n in m.groups()) for m in pattern.finditer(data)]


def parse(data):
    parts = data.split('\n\n')
    return parse_stacks(parts[0]), parse_proc(parts[1])


def crate_mover_9000(input):
    stacks, proc = input
    for num, src, target in proc:
        for i in range(num):
            stacks[target-1].append(stacks[src-1].pop())
    return ''.join(stack[-1] for stack in stacks)


def crate_mover_9001(input):
    stacks, proc = input
    for num, src, target in proc:
        src_stack = stacks[src-1]
        stacks[target-1].extend(src_stack[-num:])
        stacks[src-1] = src_stack[:-num]
    return ''.join(stack[-1] for stack in stacks)


if __name__ == "__main__":
    solve(5, parse, crate_mover_9000, crate_mover_9001)
