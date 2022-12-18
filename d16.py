#!/usr/bin/env python

"""Advent of Code 2022, Day 16"""

from itertools import combinations, product
import re

from aoc import solve
from pathfind import dijkstra, path_length


class PrepassNode:
    def __init__(slf, valve):
        slf.valve = valve

    def __hash__(slf):
        return hash(slf.valve)

    def __eq__(slf, otr):
        return slf.valve == otr.valve

    @property
    def neighbors(slf):
        for valve in tunnels[slf.valve]:
            yield PrepassNode(valve)

    def dist(slf, neighbor):
        return 1


class SoloNode:
    def __init__(slf, valve='AA', open=frozenset(), mins=0, released=0):
        slf.valve = valve
        slf.open = open
        slf.mins = mins
        slf.released = released

    def __hash__(slf):
        return hash((slf.valve, slf.open, slf.mins))

    def __eq__(slf, otr):
        return (slf.valve == otr.valve and slf.open == otr.open and
                slf.mins == otr.mins)

    @property
    def neighbors(slf):
        for valve in tunnels[slf.valve]:
            yield SoloNode(valve, slf.open, slf.mins + 1, slf.released)
        if slf.valve not in slf.open and flows[slf.valve] > 0:
            yield SoloNode(slf.valve, slf.open | frozenset({slf.valve}), slf.mins + 1, slf.released + flows[slf.valve])

    def dist(slf, neighbor):
        return max_pressure - slf.released


class PairNode:
    def __init__(slf, valve_0='AA', valve_1='AA', open=frozenset(), mins=0, released=0):
        slf.valve_0 = valve_0
        slf.valve_1 = valve_1
        slf.open = open
        slf.mins = mins
        slf.released = released

    def __hash__(slf):
        return hash((slf.valve_0, slf.valve_1, slf.open, slf.mins))

    def __eq__(slf, otr):
        return (slf.valve_0 == otr.valve_0 and slf.valve_1 == otr.valve_1 and
                slf.open == otr.open and slf.mins == otr.mins)

    @property
    def neighbors(slf):
        options_0 = tunnels[slf.valve_0]
        options_1 = tunnels[slf.valve_1]
        if slf.valve_0 not in slf.open and flows[slf.valve_0] > 0:
            options_0 = options_0 + ['open']
        if slf.valve_1 not in slf.open and flows[slf.valve_1] > 0 and slf.valve_0 != slf.valve_1:
            options_1 = options_1 + ['open']
        for action_0, action_1 in product(options_0, options_1):
            released = slf.released
            open = slf.open
            if action_0 == 'open':
                action_0 = slf.valve_0
                open = open | frozenset({action_0})
                released += flows[action_0]
            if action_1 == 'open':
                action_1 = slf.valve_1
                open = open | frozenset({action_1})
                released += flows[action_1]
            yield PairNode(action_0, action_1, open, slf.mins + 1, released)

    def dist(slf, neighbor):
        return max_pressure - slf.released


def parse(data):
    pattern = re.compile('^Valve ([A-Z]+) has flow rate=(\d+); tunnels? leads? to valves? ((?:[A-Z]+(?:, )?)+)')
    flows = {}
    tunnels = {}
    for line in data.splitlines():
        valve, flow, neighbors = re.match(pattern, line).groups()
        flows[valve] = int(flow)
        tunnels[valve] = neighbors.split(', ')
    return flows, tunnels


def pressure(valves, time_limit, node_type):
    global flows, tunnels, max_pressure
    flows = valves[0]
    tunnels = valves[1]

    # Compute an upper bound on pressure so we can use negative flow rates as
    # the edges of a graph.
    max_pressure = sum(flows.values())

    # Run Dijkstra's algorithm to find the optimal order to open the valve.
    def goal(node):
        return node.mins == time_limit

    return max_pressure * time_limit - path_length(dijkstra(node_type(), goal))


def solo_pressure(valves):
    return pressure(valves, 30, SoloNode)


def pair_pressure(valves):
    return pressure(valves, 26, PairNode)


if __name__ == "__main__":
    solve(16, parse, pair_pressure)
