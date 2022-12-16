#!/usr/bin/env python

"""Advent of Code 2022, Day 16"""

import re

from aoc import solve
from pathfind import dijkstra, path_length


class Volcano:
    def __init__(slf, flow_rates, tunnels):
        slf.flow_rates = flow_rates
        slf.tunnels = tunnels


class Node:
    def __init__(slf, volcano, valve, open, mins):
        slf.volcano = volcano
        slf.valve = valve
        slf.open = open
        slf.mins = mins

    def __hash__(slf):
        return hash((slf.valve, slf.open, slf.mins))

    def __eq__(slf, otr):
        return slf.valve == otr.valve and slf.open == otr.open and slf.mins == otr.mins

    @property
    def neighbors(slf):
        for valve in slf.volcano.tunnels[slf.valve]:
            yield Node(slf.volcano, valve, slf.open, slf.mins + 1)
        if slf.valve not in slf.open and slf.volcano.flow_rates[slf.valve] > 0:
            yield Node(slf.volcano, slf.valve, slf.open | frozenset({slf.valve}), slf.mins + 1)

    def dist(slf, neighbor):
        return slf.volcano.bound - sum(slf.volcano.flow_rates[valve] for valve in slf.open)


def parse(data):
    pattern = re.compile('^Valve ([A-Z]+) has flow rate=(\d+); tunnels? leads? to valves? ((?:[A-Z]+(?:, )?)+)')
    flow_rates = {}
    tunnels = {}
    for line in data.splitlines():
        valve, flow_rate, neighbors = re.match(pattern, line).groups()
        flow_rates[valve] = int(flow_rate)
        tunnels[valve] = neighbors.split(', ')
    return Volcano(flow_rates, tunnels)


def most_pressure(volcano, time_limit=30):
    def goal(node):
        return node.mins == time_limit

    volcano.bound = sum(volcano.flow_rates.values()) * time_limit
    path = dijkstra(Node(volcano, 'AA', frozenset(), 0), goal)
    return volcano.bound * time_limit - path_length(path)


if __name__ == "__main__":
    solve(16, parse, most_pressure)
