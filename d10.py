#!/usr/bin/env python

"""Advent of Code 2022, Day 10"""

from aoc import solve


def parse(data):
    return [tuple(instr.split()) for instr in data.splitlines()]


def decycle(instrs):
    for instr in instrs:
        if instr[0] == 'addx':
            yield ('noop')
        yield instr


def signal_strengths(instrs, offset=20, repeat=40):
    sum = 0
    x = 1
    for i, instr in enumerate(decycle(instrs)):
        cycle = i+1
        if (cycle-offset) % repeat == 0:
            sum += cycle * x
        if instr[0] == 'addx':
            x += int(instr[1])
    return sum


if __name__ == "__main__":
    solve(10, parse, signal_strengths)
