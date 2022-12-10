#!/usr/bin/env python

"""Advent of Code 2022, Day 10"""

from aoc import solve


def decycle(instrs):
    for instr in instrs:
        if instr[0] == 'addx':
            yield 0
            yield int(instr[1])
        else:
            yield 0


def parse(data):
    return decycle(tuple(i.split()) for i in data.splitlines())


def signal_strengths(instrs, offset=20, repeat=40):
    sum = 0
    x = 1
    for cycle, dx in enumerate(instrs, 1):
        if (cycle-offset) % repeat == 0:
            sum += cycle * x
        x += dx
    return sum


def crt(instrs, width=40, height=6):
    pixels = []
    x = 1
    for i, dx in enumerate(instrs):
        pixels.append('#' if x-1 <= (i % 40) <= x+1 else '.')
        x += dx
    return '\n'.join((''.join(pixels[y*width:(y+1)*width]) for y in range(6)))


if __name__ == "__main__":
    solve(10, parse, signal_strengths, crt)
