#!/usr/bin/env python

"""Advent of Code 2022, Day 6"""

from aoc import solve


def parse(data):
    return data


def find_start(buffer, n):
    for i in range(0, len(buffer) - n):
        if len(set(buffer[i:i+n])) == n:
            return i + n


def packet_start(buffer):
    return find_start(buffer, 4)


def message_start(buffer):
    return find_start(buffer, 14)


if __name__ == "__main__":
    solve(6, parse, packet_start, message_start)
