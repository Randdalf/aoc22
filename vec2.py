#!/usr/bin/env python

"""Advent of Code 2022, 2d Vector"""


class Vec2:
    def __init__(slf, x, y):
        slf.x = x
        slf.y = y

    def __add__(slf, otr):
        return Vec2(slf.x + otr.x, slf.y + otr.y)

    def __sub__(slf, otr):
        return Vec2(slf.x - otr.x, slf.y - otr.y)

    def __mul__(slf, k):
        return Vec2(k * slf.x, k * slf.y)

    def __rmul__(slf, k):
        return Vec2(k * slf.x, k * slf.y)

    def __hash__(slf):
        return hash((slf.x, slf.y))

    def __eq__(slf, otr):
        return slf.x == otr.x and slf.y == otr.y

    def __str__(slf):
        return f'({slf.x}, {slf.y})'

    def __repr__(slf):
        return f'Vec2({slf.x}, {slf.y})'

    def sqlength(slf):
        return slf.x * slf.x + slf.y * slf.y

    def rot90left(slf):
        return Vec2(slf.y, -slf.x)

    def rot90right(slf):
        return Vec2(-slf.y, slf.x)


def manhattan(a, b):
    return abs(a.x - b.x) + abs(a.y - b.y)
