#!/usr/bin/env python

"""Advent of Code 2022, Day 21"""

from operator import add, sub, mul, floordiv

from aoc import solve

ops = {'+': add, '-': sub, '*': mul, '/': floordiv}


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


if __name__ == "__main__":
    solve(21, parse, monkey_math)
