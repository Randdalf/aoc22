#!/usr/bin/env python

"""Advent of Code 2022, Day 21"""

from operator import add, sub, mul, floordiv as div

from aoc import solve


def rdiv(a, b):
    return b // a


def rsub(a, b):
    return b - a


ops = {'+': add, '-': sub, '*': mul, '/': div}
commute = {add: add, sub: rsub, mul: mul, div: rdiv}
inverse = {add: sub, sub: add, mul: div, div: mul, rsub: rsub}


def parse_job(data):
    try:
        return int(data)
    except ValueError:
        left, op, right = data.split(' ')
        return left, ops[op], right


def parse_monkey(data):
    monkey, job = data.split(': ')
    return monkey, parse_job(job)


def parse(data):
    return dict(parse_monkey(line) for line in data.split('\n'))


def monkey_math(monkeys, monkey='root'):
    job = monkeys[monkey]
    if isinstance(job, int):
        return job
    left = monkey_math(monkeys, job[0])
    right = monkey_math(monkeys, job[2])
    return job[1](left, right)


def sort_monkeys(monkeys, monkey='root'):
    job = monkeys[monkey]
    if isinstance(job, int):
        return monkey == 'humn'
    left = sort_monkeys(monkeys, job[0])
    right = sort_monkeys(monkeys, job[2])
    if right:
        monkeys[monkey] = (job[2], commute[job[1]], job[0])
    else:
        monkeys[monkey] = (job[0], job[1], job[2])
    return left or right


def yell_number(monkeys):
    sort_monkeys(monkeys)
    left, op, right = monkeys['root']
    n = monkey_math(monkeys, right)
    while True:
        job = monkeys[left]
        if isinstance(job, int):
            return n
        left, op, right = job
        right = monkey_math(monkeys, right)
        n = inverse[op](n, right)


if __name__ == "__main__":
    solve(21, parse, monkey_math, yell_number)
