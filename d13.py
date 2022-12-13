#!/usr/bin/env python

"""Advent of Code 2022, Day 13"""

from itertools import zip_longest

from aoc import solve


def parse_item(stack):
    if stack[-1] == '[':
        stack.pop()
        packet = []
        while stack[-1] != ']':
            packet.append(parse_item(stack))
            if stack[-1] == ',':
                stack.pop()
        stack.pop()
        return packet
    else:
        n = stack.pop()
        while stack[-1].isdigit():
            n += stack.pop()
        return int(n)


def parse_packet(packet):
    return parse_item(list(reversed(packet)))


def parse_pair(pair):
    return tuple(parse_packet(packet) for packet in pair.split('\n'))


def parse(data):
    return [parse_pair(pair) for pair in data.split('\n\n')]


def compare(left, right):
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return True
        elif left > right:
            return False
        else:
            return None
    elif isinstance(left, list) and isinstance(right, list):
        for l, r in zip_longest(left, right):
            if l is None:
                return True
            elif r is None:
                return False
            result = compare(l, r)
            if result is not None:
                return result
    elif isinstance(left, int) and isinstance(right, list):
        return compare([left], right)
    elif isinstance(left, list) and isinstance(right, int):
        return compare(left, [right])


def right_order(pairs):
    return sum(i for i, (l, r) in enumerate(pairs, 1) if compare(l, r))


if __name__ == "__main__":
    solve(13, parse, right_order)
