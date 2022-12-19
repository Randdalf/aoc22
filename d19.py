#!/usr/bin/env python

"""Advent of Code 2022, Day 19"""

from functools import reduce
from operator import mul
import re

from aoc import solve

blueprint_pattern = re.compile(
    r'Blueprint \d+: Each ore robot costs (\d+) ore. ' +
    r'Each clay robot costs (\d+) ore. ' +
    r'Each obsidian robot costs (\d+) ore and (\d+) clay. ' +
    r'Each geode robot costs (\d+) ore and (\d+) obsidian.')


def parse_blueprint(data):
    return tuple(int(x) for x in blueprint_pattern.match(data).groups())


def parse(data):
    return [parse_blueprint(line) for line in data.split('\n')]


def max_geodes(blueprint, cache=None, mins=24, ore=0, clay=0, obs=0, geodes=0,
               ore_bots=1, clay_bots=0, obs_bots=0, geode_bots=0):
    # Return the number of geodes opened when time is up.
    if mins == 0:
        return geodes

    # Use a cached result if we've already encountered this state.
    if cache is None:
        cache = {}
    key = (mins, ore, clay, obs, geodes, ore_bots, clay_bots, obs_bots,
           geode_bots)
    try:
        return cache[key]
    except KeyError:
        pass

    # Determine which bots can be constructed.
    build_ore = ore >= blueprint[0]
    build_clay = ore >= blueprint[1]
    build_obs = ore >= blueprint[2] and clay >= blueprint[3]
    build_geode = ore >= blueprint[4] and obs >= blueprint[5]

    # Collect resources.
    ore += ore_bots
    clay += clay_bots
    obs += obs_bots
    geodes += geode_bots

    # Consider the outcomes for constructing bots.
    if build_geode:
        opened = max_geodes(blueprint, cache, mins - 1, ore - blueprint[4],
                            clay, obs - blueprint[5], geodes, ore_bots,
                            clay_bots, obs_bots, geode_bots + 1)
    elif build_obs:
        opened = max_geodes(blueprint, cache, mins - 1, ore - blueprint[2],
                            clay - blueprint[3], obs, geodes, ore_bots,
                            clay_bots, obs_bots + 1, geode_bots)
    else:
        opened = []
        opened.append(max_geodes(blueprint, cache, mins - 1, ore, clay, obs,
                                 geodes, ore_bots, clay_bots, obs_bots,
                                 geode_bots))
        if build_ore:
            opened.append(max_geodes(blueprint, cache, mins - 1,
                                     ore - blueprint[0], clay, obs, geodes,
                                     ore_bots + 1, clay_bots, obs_bots,
                                     geode_bots))
        if build_clay:
            opened.append(max_geodes(blueprint, cache, mins - 1,
                                     ore - blueprint[1], clay, obs, geodes,
                                     ore_bots, clay_bots + 1, obs_bots,
                                     geode_bots))
        opened = max(opened)
    cache[key] = opened
    return opened


def quality_levels(blueprints):
    return sum(i*max_geodes(bp) for i, bp in enumerate(blueprints, 1))


def first_three_32(blueprints):
    return reduce(mul, (max_geodes(bp, mins=32) for bp in blueprints[:3]))


if __name__ == "__main__":
    solve(19, parse, quality_levels, first_three_32)
