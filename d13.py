#!/usr/bin/env python

"""Advent of Code 2022, Day 13"""

from functools import cmp_to_key
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
            return -1
        elif left > right:
            return 1
    elif isinstance(left, list) and isinstance(right, list):
        for l, r in zip_longest(left, right):
            if l is None:
                return -1
            elif r is None:
                return 1
            result = compare(l, r)
            if result != 0:
                return result
    elif isinstance(left, int) and isinstance(right, list):
        return compare([left], right)
    elif isinstance(left, list) and isinstance(right, int):
        return compare(left, [right])
    return 0


def right_order(pairs):
    return sum(i for i, (l, r) in enumerate(pairs, 1) if compare(l, r) < 0)


def decoder_key(pairs):
    divider_2 = [[2]]
    divider_6 = [[6]]
    packets = [packet for pair in pairs for packet in pair]
    packets.append(divider_2)
    packets.append(divider_6)
    packets.sort(key=cmp_to_key(compare))
    return (1+packets.index(divider_2)) * (1+packets.index(divider_6))


if __name__ == "__main__":
    solve(13, parse, right_order, decoder_key)
