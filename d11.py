#!/usr/bin/env python

"""Advent of Code 2022, Day 11"""

from functools import reduce
from operator import mul, add
import re

from aoc import solve


class Monkey:
    def __init__(slf, items, operation, test, divisor):
        slf.items = items
        slf.operation = operation
        slf.test = test
        slf.divisor = divisor
        slf.inspections = 0


operation_pattern = re.compile(r'  Operation: new = old ([*+]) (\d+|old)')


def parse_items(items):
    return [int(item) for item in items[18:].split(', ')]


def parse_operation(operation):
    op, n = operation_pattern.match(operation).groups()
    n = n if n == 'old' else int(n)
    op = mul if op == '*' else add
    return (lambda x: op(x, x)) if n == 'old' else (lambda x: op(x, n))


def parse_test(test, if_true, if_false):
    divisor = int(test[21:])
    t = int(if_true[29:])
    f = int(if_false[30:])
    return (lambda x: t if x % divisor == 0 else f), divisor


def parse_monkey(monkey):
    lines = monkey.splitlines()
    items = parse_items(lines[1])
    operation = parse_operation(lines[2])
    test, divisor = parse_test(lines[3], lines[4], lines[5])
    return Monkey(items, operation, test, divisor)


def parse(data):
    return [parse_monkey(monkey) for monkey in data.split('\n\n')]


def simulate(monkeys, rounds, limit):
    for round in range(rounds):
        for monkey in monkeys:
            for item in monkey.items:
                monkey.inspections += 1
                item = monkey.operation(item)
                item = limit(item)
                monkeys[monkey.test(item)].items.append(item)
            monkey.items.clear()
    activity = [monkey.inspections for monkey in monkeys]
    activity.sort()
    return activity[-1] * activity[-2]


def monkey_business(monkeys, rounds=20):
    return simulate(monkeys, rounds, lambda item: item // 3)


def funky_business(monkeys, rounds=10000):
    limiter = reduce(mul, (monkey.divisor for monkey in monkeys), 1)
    return simulate(monkeys, rounds, lambda item: item % limiter)


if __name__ == "__main__":
    solve(11, parse, monkey_business, funky_business)
