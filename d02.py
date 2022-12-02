#!/usr/bin/env python

"""Advent of Code 2022, Day 2"""

from aoc import solve


def parse(data):
    return [(ord(x[0]) - ord('A'), ord(x[2]) - ord('X')) for x in data.split('\n')]


def follow_guide(guide):
    score = len(guide)
    for oppo, resp in guide:
        score += resp
        if resp == oppo:
            score += 3
        elif (oppo + 1) % 3 == resp:
            score += 6
    return score


if __name__ == "__main__":
    solve(2, parse, follow_guide)
