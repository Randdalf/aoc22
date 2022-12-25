#!/usr/bin/env python

"""Advent of Code 2022, Day 25"""

from math import log

from aoc import solve
from pqueue import pqueue

c2v = {'=': -2, '-': -1, '0': 0, '1': 1, '2': 2}
v2c = {v: k for k, v in c2v.items()}


def parse(data):
    return data.split('\n')


def s2d(s):
    n = 0
    k = 1
    for digit in reversed(s):
        n += k * c2v[digit]
        k *= 5
    return n


def d2s(d):
    s = ''
    while d > 0:
        digit = ((d+2) % 5 - 2)
        s = v2c[digit] + s
        d = (d - digit) // 5
    return s


def snafu_sum(numbers):
    return d2s(sum(map(s2d, numbers)))


if __name__ == "__main__":
    solve(25, parse, snafu_sum)
