#!/usr/bin/env python

"""Advent of Code 2022, Day 11"""

import re

from aoc import solve


class Monkey:
    def __init__(slf, items, operation, test):
        slf.items = items
        slf.operation = operation
        slf.test = test
        slf.inspections = 0


operation_pattern = re.compile(r'  Operation: new = old ([*+]) (\d+|old)')


def parse_items(items):
    return [int(item) for item in items[18:].split(', ')]


def parse_operation(operation):
    op, n = operation_pattern.match(operation).groups()
    if n != 'old':
        n = int(n)
    if op == '*':
        return (lambda x: x * x) if n == 'old' else (lambda x: x * n)
    else:
        return (lambda x: x + x) if n == 'old' else (lambda x: x + n)


def parse_test(test, if_true, if_false):
    n = int(test[21:])
    t = int(if_true[29:])
    f = int(if_false[30:])
    return lambda x: t if x % n == 0 else f


def parse_monkey(monkey):
    lines = monkey.splitlines()
    items = parse_items(lines[1])
    operation = parse_operation(lines[2])
    test = parse_test(lines[3], lines[4], lines[5])
    return Monkey(items, operation, test)


def parse(data):
    return [parse_monkey(monkey) for monkey in data.split('\n\n')]


def monkey_business(monkeys, rounds=20, verbose=False):
    for round in range(rounds):
        for monkey in monkeys:
            for item in monkey.items:
                monkey.inspections += 1
                item = monkey.operation(item)
                item //= 3
                monkeys[monkey.test(item)].items.append(item)
            monkey.items.clear()
        if verbose:
            print(f'After round {round+1}, the monkeys are holding items with these worry levels:')
            for i, monkey in enumerate(monkeys):
                print(f'Monkey {i}: {", ".join(map(str, monkey.items))}')
    activity = [monkey.inspections for monkey in monkeys]
    activity.sort()
    return activity[-1] * activity[-2]


if __name__ == "__main__":
    solve(11, parse, monkey_business)
